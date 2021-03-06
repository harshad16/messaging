#!/usr/bin/env python3
# thoth-messaging
# Copyright(C) 2020 Sai Sankar Gochhayat
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


"""This is Thoth Messaging module for KebechetRunUrlTriggerMessage."""

import logging
from typing import Optional

from pydantic import BaseModel, Field

from .message_base import MessageBase, BaseMessageContents

_LOGGER = logging.getLogger(__name__)

base_name = "thoth.kebechet-run-url-trigger"


class Metadata(BaseModel):
    """Metadata for kebechet-run-url message type."""

    message_justification: Optional[int]
    package_name: Optional[str]
    package_version: Optional[str]
    package_index: Optional[str]


class MessageContents(BaseMessageContents):
    """Class used to represent contents of a message Kafka topic."""

    url: Optional[str]
    service_name: Optional[str]
    installation_id: Optional[str]
    job_id: Optional[str]
    metadata: Metadata = Field(default_factory=Metadata)
    version: str = "v2"


kebechet_run_url_trigger_message = MessageBase(base_name=base_name, model=MessageContents)
