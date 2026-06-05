from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    original = deepcopy(activities)
    yield
    activities.clear()
    activities.update(deepcopy(original))


@pytest.fixture
def existing_activity_name():
    return "Chess Club"


@pytest.fixture
def missing_activity_name():
    return "Nonexistent Activity"


@pytest.fixture
def new_email():
    return "new.student@mergington.edu"


@pytest.fixture
def existing_email():
    return "michael@mergington.edu"
