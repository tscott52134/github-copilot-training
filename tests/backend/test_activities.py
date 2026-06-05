def test_get_activities_status_code_200(client):
    response = client.get("/activities")

    assert response.status_code == 200


def test_get_activities_returns_dictionary(client):
    response = client.get("/activities")

    assert isinstance(response.json(), dict)


def test_get_activities_includes_seeded_entries(client):
    response = client.get("/activities")
    payload = response.json()

    assert "Chess Club" in payload
    assert "Programming Class" in payload
    assert "Gym Class" in payload


def test_activity_payload_contains_expected_fields(client):
    response = client.get("/activities")
    payload = response.json()

    chess_club = payload["Chess Club"]

    assert set(chess_club.keys()) == {
        "description",
        "schedule",
        "max_participants",
        "participants",
    }
    assert isinstance(chess_club["description"], str)
    assert isinstance(chess_club["schedule"], str)
    assert isinstance(chess_club["max_participants"], int)
    assert isinstance(chess_club["participants"], list)
