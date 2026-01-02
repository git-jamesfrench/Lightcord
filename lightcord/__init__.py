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

"""Lightcord is a python library for interacting with the discord API and Gateway.

* **Github Page:** https://github.com/lightcord-py/Lightcord
* **License:** [GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.fr.html)"""

from lightcord.gateway import Gateway
from lightcord.handlers import Handlers
from lightcord.literals import Events
from typing import Callable
import asyncio

class Client():
    def __init__(self, token: str = None, intents: int | str = 0):
        """Define a discord client.
        
        :param token: Your private token. You can get it on your Developer Portal.
        :type token: `str`
        :param intents: The intents to send over to discord, this is optional because Lightcord already generate an intents.
        :type intents: Optional `int | str`"""
        self.intents = int(intents)

        self.handlers = Handlers()
        self.gateway = Gateway(token, intents)
        
    async def start_async(self):
        await self.gateway.start()
    
    def start(self, token: str = None, intents: int | str = 0):
        """Start your client, making it online and able to receive events from discord.
        
        :param token: Your private token. You can get it on your Developer Portal.
        :type token: `str`"""
        if token: self.gateway.token = token
        if intents: self.gateway.intents = intents
        self.gateway.handlers = self.handlers
        
        try:
            asyncio.get_event_loop()
            return self.start_async()
        except RuntimeError:
            asyncio.run(self.gateway.start())
        
    async def stop(self) -> None:
        """Stop your client gracefully, making it offline and unable to receive events from discord."""
        await self.gateway.stop()
        
    def on(self, event: Events = None, function: Callable = None, *, once: bool = False):
        """
        Will call `function` when `event` happen. Will automatically add needed intents if intents are not defined by the user.
        
        Can be used as a decorator: 
        ```
        @bot.on("READY")
        async def on_ready():
            print("READY!")
        ```
        :param event: The event that will trigger the defined `function`.
        :type event: `str`
        :param function: The function that will be called when the defined `event` happen.
        :type function: `Callable`
        :param once: Will make the function be triggered once when `event` happens, making others occurrences be ignored.
        :type once: `bool`
        """
        def decorator(fn):
            self.handlers.add_handler(
                event,
                fn,
                once
            )
        if function is not None: return decorator(function)
        else: return decorator
        
    def once(self, event: Events = None, function: Callable = None):
        """
        Will call `function` once when `event` happen. Will automatically add needed intents if intents are not defined by the user. 
        
        The `function` will be called once, others occurrences of the `event` will be ignored.
        
        Can be used as a decorator: 
        ```
        @bot.once("READY")
        async def on_ready():
            print("READY!")
        ```
        :param event: The event that will trigger the defined `function`.
        :type event: `str`
        :param function: The function that will be called when the defined `event` happen.
        :type function: `Callable`
        """
        def decorator(fn):
            self.on(event = event, function = fn, once = True)
        if function is not None: return decorator(function)
        else: return decorator