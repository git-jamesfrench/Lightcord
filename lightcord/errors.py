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

close_codes = {
    4000: "Unknown error",
    4001: "Unknown opcode",
    4002: "Decode error",
    4003: "Not authenticated",
    4004: "Authentication failed",
    4005: "Already authenticated",
    4007: "Invalid seq",
    4008: "Rate limited",
    4009: "Session timed out",
    4010: "Invalid shard",
    4011: "Sharding required",
    4012: "Invalid API version",
    4013: "Invalid intent(s)",
    4014: "Disallowed intent(s)"
}