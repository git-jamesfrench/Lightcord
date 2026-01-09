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

import aiohttp
import asyncio

#    __ _       _     _                    _ 
#   / /(_) __ _| |__ | |_ ___ ___  _ __ __| |
#  / / | |/ _` | '_ \| __/ __/ _ \| '__/ _` |
# / /__| | (_| | | | | || (_| (_) | | | (_| |
# \____/_|\__, |_| |_|\__\___\___/|_|  \__,_|
#         |___/                              

import logging
logger = logging.getLogger(__name__)

class RestAPI:
    def __init__(self, token):
        self.token = token

        self.session: aiohttp.ClientSession = None
        self.session_lock = asyncio.Lock()
        
        self.base_url = "https://discord.com/api/v10/"
        
    async def request(self, method: str, url: str, data: dict) -> dict | None:
        session = await self.get_session()
        try:
            async with session.request(method, f'{self.base_url}{url}', json=data) as resp:
                if resp.status in [200, 201]: # 200: Ok, 201: Created
                    return await resp.json()
                elif resp.status in [204, 304]: # 204: No content, 304: Not modified
                    return None
                elif resp.status in [400, 401, 403, 404, 405]: # 400: Bad request, 401: Unauthorized, 403: Forbidden, 404: Not found, 405: Method not allowed
                    error = f"An user error ({resp.status}) occured when requesting ({method} {url}): {await resp.text()}"
                    raise aiohttp.ClientError(error)
                elif resp.status == 429: # 429: Rate limited
                    error = f"The request ({method} {url}) was rate limited: {await resp.text()}"
                    raise aiohttp.ClientError(error)
                elif resp.status == 502: # 502: Gateway unavailable
                    # TODO: Retry after 1 seconds or more
                    error = f"An error (502) occured when requesting ({method} {url}), no gateway available to accept this request: {await resp.text()}"
                    raise aiohttp.ClientError(error)
                elif str(resp.status).startswith('5'):
                    # TODO: Retry after 1 seconds or more, but only 1 try
                    error = f"An server error ({resp.status}) occured when requesting ({method} {url}): {await resp.text()}"
                    raise aiohttp.ClientError(error)
                else:
                    error = f"An unknown error ({resp.status}) occured when requesting ({method} {url}): {await resp.text()}"
                    raise aiohttp.ClientError(error)
        except aiohttp.ClientError as e:
            logging.error(e)
            raise e

    async def get_session(self) -> aiohttp.ClientSession:
        async with self.session_lock: # Just to prevent race condition
            if not self.session or self.session.closed:
                timeout = aiohttp.ClientTimeout( # Closes connection after 5 seconds if not connected, closes after 20 seconds if no response, closes after 30 seconds if not done yey
                    total = 30,
                    connect = 5,
                    sock_read= 20
                )

                self.session = aiohttp.ClientSession(
                    headers = {
                        'authorization': f'Bot {self.token}',
                        'content-type': 'application/json'
                    },
                    timeout=timeout
                )
                logging.info("Created session for Rest API.")
        return self.session
    
    async def close(self):
        if self.session or not self.session.closed:
            await self.session.close()