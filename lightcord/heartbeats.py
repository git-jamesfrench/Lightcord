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

import asyncio
import threading

class Heartbeats:
    def __init__(self):
        self.ws = None
        self.interval = None
        self.running = False
        self.loop = asyncio.new_event_loop()
        self.thread = threading.Thread(target=self.run_loop, daemon=True)
        self.thread.start()

    def run_loop(self):
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()

    async def heartbeat(self):
        while self.running:
            await asyncio.sleep(self.interval)
            if self.running:
                await self.ws.send_json({"op": 1, "d": 'null'})

    def run(self, ws, interval):
        self.ws = ws
        self.interval = interval
        self.running = True
        asyncio.run_coroutine_threadsafe(self.heartbeat(), self.loop)

    def stop(self):
        self.running = False
        self.loop.call_soon_threadsafe(self.loop.stop)