import os
import sys
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture
def rabbitmq_config():
    return {"AMQP_URI": "amqp://guest:guest@rabbitmq"}
