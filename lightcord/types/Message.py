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

from lightcord.variables import Snowflake, Timestamp
from lightcord.types.User import User
from lightcord.types.Guild import Member
from lightcord.types.Role import Role, RoleSubscriptionData
from lightcord.types.Channel import Channel, ChannelMention
from lightcord.types.Sticker import Sticker, StickerItem
from lightcord.types.Reaction import Reaction
from lightcord.types.Attachment import Attachment
from lightcord.types.Embed import Embed
from lightcord.types.Application import Application
from lightcord.types.Component import Component
from lightcord.types.Poll import Poll

class MessageActivity(TypeData):
    type: int
    party_id: str

class MessageReference(TypeData):
    type: int
    message_id: Snowflake
    channel_id: Snowflake
    guild_id: Snowflake
    fail_if_not_exists: bool

class MessageSnapshot(TypeData):
    message: 'Message'

class MessageInteractionMetadata(TypeData):
    id: Snowflake
    type: int
    name: str
    user: User
    authorizing_integration_owners: Dict[Any,Any]
    original_response_message_id: Snowflake
    target_user: User
    target_message_id: Snowflake
    command_type: int

class MessageInteraction(TypeData):
    id: Snowflake
    type: int
    name: str
    user: User
    member: Member

class ResolvedData(TypeData):
    users: List[User]
    members: List[Member]
    roles: List[Role]
    channels: List[Channel]
    messages: List["Message"]
    attachments: List[Attachment]

class MessageCall(TypeData):
    participants: List[Snowflake]
    ended_timestamp: Timestamp

class Message(TypeData):
    id: Snowflake
    channel_id: Snowflake
    author: User
    content: str
    timestamp: Timestamp
    edited_timestamp: Timestamp
    tts: bool
    mention_everyone: bool
    mentions: List[User]
    mention_roles: List[Role]
    mention_channels: List[ChannelMention]
    attachments: List[Attachment]
    embeds: List[Embed]
    reactions: List[Reaction]
    nonce: bool | int
    pinned: bool
    webhook_id: Snowflake
    type: int
    activity: MessageActivity
    application: Application
    application_id: Snowflake
    channel_type: int
    member: Member
    guild_id: Snowflake
    flags: int
    message_reference: MessageReference
    message_snapshots: List[MessageSnapshot]
    referenced_message: 'Message'
    interaction_metadata: MessageInteractionMetadata
    interaction: MessageInteraction
    thread: Channel
    components: List[Component]
    sticker_items: List[StickerItem]
    stickers: List[Sticker]
    position: int
    role_subscription_data: RoleSubscriptionData
    resolved: ResolvedData
    poll: Poll
    call: MessageCall