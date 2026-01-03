# Lightcord - A lightweight, modern and optimized Discord API wrapper for Python. 
# Copyright (C) 2025  Jamesfrench_
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import aiohttp
import asyncio
import json
from lightcord.handlers import Handlers
from contextlib import suppress
from random import random

class Gateway():
    def __init__(self, token: str = None, intents: int = None):
        self.token = token
        self.intents = intents
        self.handlers: Handlers = None

        self.websocket_task: asyncio.Task = None
        self.heartbeats_task: asyncio.Task = None
        self.session: aiohttp.ClientSession = None
        self.ws: aiohttp.ClientWebSocketResponse = None

        self.heartbeats_interval: float = None
        self.s_number_of_events: int = None
        self.waiting_for_heartbeat_ack: bool = False

    async def start(self):
        if self.token is None:
            raise ValueError('No token provided.')
        
        self.session = aiohttp.ClientSession()
        self.websocket_task = asyncio.create_task(self.websocket())

        try:
            await self.websocket_task
        except asyncio.CancelledError:
            pass

    async def stop(self):
        await self.close(1000)
        if self.websocket_task:
            self.websocket_task.cancel()
            with suppress(asyncio.CancelledError):
                await self.websocket_task
        
    async def websocket(self):
        try:
            async with self.session.ws_connect('wss://gateway.discord.gg/?v=10&encoding=json') as ws:
                self.ws = ws
                await self.opcodes()

                if ws.closed:
                    message = await ws.receive()
                    #print(ws.close_code, message.data)
        except asyncio.CancelledError:
            raise
        finally:
            await self.close(1000)
    
    async def close(self, code):
        if self.ws and not self.ws.closed: 
            await self.ws.close(code = code)
        if self.session and not self.session.closed: await self.session.close()
        await self.stop_heartbeats()

    async def stop_heartbeats(self):
        if self.heartbeats_task:
            self.heartbeats_task.cancel()
            with suppress(asyncio.CancelledError):
                await self.heartbeats_task
            
    async def identify(self):
        payload = {
            'op': 2,
            'd': {
                'token': self.token,
                'intents': self.intents,
                'properties': {
                    'os': 'linux',
                    'browser': 'lightcord',
                    'device': 'lightcord'
                }
            }
        }
        await self.ws.send_json(payload)

    async def heartbeats(self, skip = False):
        first = True
        try:
            while True:
                # The random is just a jitter asked by discord, only for the first heartbeat.
                if not skip or not first:
                    await asyncio.sleep(self.heartbeats_interval * random() if first else self.heartbeats_interval)
                if self.waiting_for_heartbeat_ack: # Closes connection if it is "zombified"
                    await self.close(1006)
                    break
                await self.ws.send_json({"op": 1, "d": self.s_number_of_events})
                self.waiting_for_heartbeat_ack = True
                first = False
        except asyncio.CancelledError:
            raise

    async def opcodes(self):
        async for msg in self.ws:
            d = json.loads(msg.data)

            if d['s']: 
                self.s_number_of_events = d['s']
            
            if d['op'] == 0: # Event
                await self.handlers.call_handlers(d['t'], d['d'])

            elif d['op'] == 1: # Heartbeat request
                self.waiting_for_heartbeat_ack = False
                await self.stop_heartbeats()
                self.heartbeats_task = asyncio.create_task(self.heartbeats(True))

            elif d['op'] == 10: # After connecting
                self.heartbeats_interval = d['d']['heartbeat_interval'] / 1000
                self.heartbeats_task = asyncio.create_task(self.heartbeats(False))
                await self.identify()

            elif d['op'] == 11: # Heartbeat acknowledgement
                self.waiting_for_heartbeat_ack = False
