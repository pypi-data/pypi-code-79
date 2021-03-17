"""
    Copyright 2017 Inmanta

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Contact: code@inmanta.com
"""
import logging
import uuid

import pytest

LOGGER = logging.getLogger(__name__)


@pytest.mark.asyncio(timeout=60)
async def test_param(client, environment):
    """
    Test creating and updating forms
    """
    fake_uuid = uuid.uuid4()
    result = await client.list_params(tid=fake_uuid)
    assert result.code == 404

    result = await client.list_params(tid=environment)
    assert result.code == 200
