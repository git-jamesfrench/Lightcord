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
import threading
import json
from lightcord.heartbeats import Heartbeats
from lightcord.handlers import Handlers

class Gateway():
    def __init__(self, token: str, intents: int, handlers: Handlers):
        self.token = token
        self.ws = None
        self.intents = intents
        self.loop = asyncio.new_event_loop()
        self.session = None
        self.heartbeats = Heartbeats()
        self.handlers = handlers
        
    def run_loop(self):
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()
        
    async def generate_session(self):
        self.session = aiohttp.ClientSession()
        
    async def start(self):
        threading.Thread(target=self.run_loop, daemon=True).start()
        await self.generate_session()
        
        try:
            async with self.session.ws_connect('wss://gateway.discord.gg/?v=10&encoding=json') as ws:
                self.ws = ws
                await self.opcodes()
                
                if ws.closed:
                    message = await ws.receive()
                    # ws.close_code, message.data
        finally:
            await self.ws.close()
            if self.heartbeats.running:
                self.heartbeats.stop()
            
    async def stop(self):
        if self.ws and not self.ws.closed:
            await self.ws.close()
            
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
            
    async def opcodes(self):
        async for msg in self.ws:
            d = json.loads(msg.data)
            
            if d['op'] == 0: # Event
                await self.handlers.call_handlers(d['t'], d['d'])
            elif d['op'] == 10: # After connecting
                self.heartbeats.run(self.ws, d['d']['heartbeat_interval'] / 1000)
                await self.identify()
            elif d['op'] == 11: # Heartbeat acknowledgement
                pass