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
from typing import Any, List

from lightcord.variables import Timestamp

class EmbedField(TypeData):
    name: str
    value: str
    inline: bool

class EmbedAuthor(TypeData):
    name: str
    url: str
    icon_url: str
    proxy_icon_url: str

class EmbedProvider(TypeData):
    name: str
    url: str

class EmbedFooter(TypeData):
    text: str
    icon_url: str
    proxy_icon_url: str

class Embed(TypeData):
    title: str
    type: str
    description: str
    url: str
    timestamp: Timestamp
    color: int
    footer: EmbedFooter
    image: Any
    thumbnail: Any
    video: Any
    provider: EmbedProvider
    author: EmbedAuthor
    fields: List[EmbedField]
