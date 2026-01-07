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

from typing import Callable, Any
from lightcord.events import find_event
from lightcord.typedata import TypeData
import asyncio
from inspect import signature, _empty

import logging
logger = logging.getLogger(__name__)

class Handlers:
    def __init__(self):
        self.handlers = {}
        
    def add_handler(self, event: str, fn: Callable, once: bool):
        arguments = find_event(event)
        fn_arguments = signature(fn).parameters.keys()

        if arguments[1]:
            if not fn_arguments == arguments[1].keys():
                expected_arguments = []
                for key, type in arguments[1].items():
                    expected_arguments.append(f"{key}: lightcord.types.{type.__name__}")

                raise TypeError(f"{fn.__name__}() arguments are invalid for event {event}, please follow this format (types are not enforced but recommended):\n\n{fn.__name__}({", ".join(expected_arguments)})")
        else:
            if not fn_arguments == {"event": None}.keys():
                raise TypeError(f"{fn.__name__}() arguments are invalid for event {event}, lightcord doesn't recognize this event, please follow this format:\n\n{fn.__name__}(event)")

        self.handlers.setdefault(event.upper(), [])
        self.handlers[event.upper()].append({
            "fn": fn,
            "data": arguments[0], 
            "once": once
        })
        logger.debug(f"Successfully defined {fn} as an handler for {event.upper()} (once: {once}).")
        
    async def call_handlers(self, event: str, data: dict):
        logger.debug(f"{event} was dispatched.")

        for handler in self.handlers.get(event, []):
            if handler["data"]: arguments = handler["data"](data)
            else: arguments = {"event": TypeData(data)}

            asyncio.create_task(self.dispatch(handler["fn"], arguments))

    async def dispatch(self, fn, arguments):
        try:
            await fn(**arguments)
        except Exception as e:
            logger.exception(f"An error occured in the handler {fn.__name__}(): {e}")