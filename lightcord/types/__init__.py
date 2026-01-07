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

"""
Types given by discord.

You can import types like this:
```
import lightcord.types as types

types.Message
```
(This is still optimized with lazy imports)
"""

# Magnificient Lazy Importing, yes this was vibecoded, may get back to it but I understand how it works and it's great

from typing import TYPE_CHECKING
import importlib

_module_map = { # Where is located a function
    "Message": "lightcord.types.Message",
    "User": "lightcord.types.User"
}

if TYPE_CHECKING: # The IDE thinks were importing it, but when executing, it does SHIT, NOTHING, THIS SHIT IS FUCKING CONFUSING
    from lightcord.types.Message import Message
    from lightcord.types.User import User

__all__ = list(_module_map.keys())

def __getattr__(name: str):
    if name in _module_map:
        module = importlib.import_module(_module_map[name])
        value = getattr(module, name)
        globals()[name] = value # Honestly, it was chatgpt that said this was important, so we don't go though __getattr__ everytime we want something, but i don't know how it works! i'm learning
        return value
    raise AttributeError(f"module 'types' doesn't have the attribute {name}.")