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
from typing import Any

from lightcord.types.User import User
from lightcord.types.Guild import Guild
from lightcord.types.Application import Application

class Ready(TypeData):
    v: int
    user_settings: dict
    user: User
    session_type: str
    session_id: str
    resume_gateway_url: str
    relationships: list
    private_channels: list
    presences: list
    guilds: list[Guild]
    guild_join_requests: list
    geo_ordered_rtc_regions: list[str]
    game_relationships: list
    auth: dict
    application: Application