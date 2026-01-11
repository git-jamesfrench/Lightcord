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
from typing import List, TYPE_CHECKING

from lightcord.variables import Snowflake, Timestamp
from lightcord.types.User import User
from lightcord.types.Thread import ThreadMetadata, ThreadMember, ForumTag, DefaultReaction
from lightcord.types.Permissions import Overwrite
from lightcord.types.Embed import Embed

if TYPE_CHECKING:
    from lightcord.types.Message import Message

class IconEmoji(TypeData):
    name: str
    id: Snowflake

class ChannelMention(TypeData):
    id: Snowflake
    guild_id: Snowflake
    type: int
    name: str

class Channel(TypeData):
    id: Snowflake
    type: int
    guild_id: Snowflake
    position: int
    permission_overwrites: List[Overwrite]
    name: str
    topic: str
    nsfw: bool
    last_message_id: Snowflake
    bitrate: int
    user_limit: int
    rate_limit_per_user: int
    recipients: List[User]
    theme_color: str
    icon: str
    owner_id: Snowflake
    application_id: Snowflake
    icon_emoji: IconEmoji
    managed: bool
    parent_id: Snowflake
    last_pin_timestamp: Timestamp
    rtc_region: str
    video_quality_mode: int
    message_count: int
    member_count: int
    thread_metadata: ThreadMetadata
    member: ThreadMember
    default_auto_archive_duration: int
    permissions: str
    flags: int
    total_message_sent: int
    available_tags: List[ForumTag]
    applied_tags: List[Snowflake]
    default_reaction_emoji: DefaultReaction
    default_thread_rate_limit_per_user: int
    default_sort_order: int
    default_forum_layout: int

    async def send(
        self,
        content: str,
        *,
        embeds: Embed | List[Embed] = None
    ) -> Message:
        from lightcord.types.Message import Message

        """
        Send a message in the channel.
        
        :param content: Content of the message.
        :type content: str
        :param embeds: Embed(s) of the message.
        :type embeds: Embed | List[Embed]
        :return: Message object.
        :rtype: Message
        """

        payload = {}
        payload.setdefault('content', str(content))
        
        return Message(await self.api.request('post', f'channels/{self.id}/messages', payload), self.api)