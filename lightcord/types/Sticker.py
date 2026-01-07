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

from lightcord.typedata import TypeData

from lightcord.variables import Snowflake
from lightcord.types.User import User

class StickerItem(TypeData):
    id: Snowflake
    name: str
    format_type: int


class Sticker(TypeData):
    id: Snowflake
    pack_id: Snowflake
    name: str
    description: str
    tags: str
    type: int
    format_type: int
    available: bool
    guild_id: Snowflake
    user: User
    sort_value: int