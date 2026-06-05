import sys
import os

backend_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "backend")
)

sys.path.insert(0, backend_path)

from main import app

from fastapi.testclient import TestClient
import pytest


@pytest.fixture
def client():
    return TestClient(app)