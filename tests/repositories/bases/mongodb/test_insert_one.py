# Standard Library
from unittest.mock import patch, MagicMock

# Third-Party Library
import pytest

# IRango
from src.repositories.bases.mongodb.repository import BaseMongoDBRepository
from tests.repositories.bases.mongodb.stub_mongodb_operations import (
    StubMongoDBOperations,
)


@pytest.mark.asyncio
@patch.object(BaseMongoDBRepository, "_get_mongodb_base_collection")
async def test_insert_one(_get_mongodb_base_collection_patch: MagicMock):
    _get_mongodb_base_collection_patch.return_value = StubMongoDBOperations()

    data = {
        "name": "IRango",
    }
    result = await BaseMongoDBRepository.insert_one(data)
    assert result is None