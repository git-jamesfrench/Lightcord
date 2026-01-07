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
from typing import Any, Dict, List

from lightcord.variables import Snowflake
from lightcord.types.User import User
from lightcord.types.Guild import Guild
from lightcord.types.Team import Team

class InstallParams(TypeData):
    scopes: List[str]
    permissions: str

class Application(TypeData):
    id: Snowflake
    name: str
    icon: str
    description: str
    rpc_origins: List[str]
    bot_public: bool
    bot_require_code_grant: bool
    bot: User
    terms_of_service_url: str
    privacy_policy_url: str
    owner: User
    verify_key: str
    team: Team
    guild_id: Snowflake
    guild: Guild
    primary_sku_id: Snowflake
    slug: str
    cover_image: str
    flags: int
    approximate_guild_count: int
    approximate_user_install_count: int
    redirect_uris: List[str]
    interactions_endpoint_url: str
    role_connections_verification_url: str
    event_webhooks_url: str
    event_webhooks_status: int
    event_webhooks_types: List[str]
    tags: List[str]
    install_params: InstallParams
    integration_types_config: Dict[Any, Any]
    custom_install_url: str