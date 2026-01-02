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

from typing import Callable
import asyncio

class Handlers:
    def __init__(self):
        self.handlers = {}
        
    def add_handler(self, event: str, fn: Callable, once: bool):
        self.handlers.setdefault(event.upper(), [])
        self.handlers[event.upper()].append({
            "fn": fn,
            "once": once
        })
        
    async def call_handlers(self, event: str, data: dict):
        for handler in self.handlers.get(event, []):
            asyncio.create_task(handler["fn"]())