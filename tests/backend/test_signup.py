def test_signup_success_returns_200_and_message(client, existing_activity_name, new_email):
    response = client.post(
        f"/activities/{existing_activity_name}/signup", params={"email": new_email}
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": f"Signed up {new_email} for {existing_activity_name}"
    }


def test_signup_adds_email_to_participants(client, existing_activity_name, new_email):
    client.post(f"/activities/{existing_activity_name}/signup", params={"email": new_email})

    activities_response = client.get("/activities")
    participants = activities_response.json()[existing_activity_name]["participants"]

    assert new_email in participants


def test_signup_duplicate_email_returns_400(client, existing_activity_name, existing_email):
    response = client.post(
        f"/activities/{existing_activity_name}/signup", params={"email": existing_email}
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"


def test_signup_nonexistent_activity_returns_404(client, missing_activity_name, new_email):
    response = client.post(
        f"/activities/{missing_activity_name}/signup", params={"email": new_email}
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_missing_email_returns_422(client, existing_activity_name):
    response = client.post(f"/activities/{existing_activity_name}/signup")

    assert response.status_code == 422


def test_unregister_success_returns_200_and_message(client, existing_activity_name, existing_email):
    response = client.delete(
        f"/activities/{existing_activity_name}/signup", params={"email": existing_email}
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": f"Unregistered {existing_email} from {existing_activity_name}"
    }


def test_unregister_removes_email_from_participants(client, existing_activity_name, existing_email):
    client.delete(f"/activities/{existing_activity_name}/signup", params={"email": existing_email})

    activities_response = client.get("/activities")
    participants = activities_response.json()[existing_activity_name]["participants"]

    assert existing_email not in participants


def test_unregister_nonexistent_activity_returns_404(client, missing_activity_name, new_email):
    response = client.delete(
        f"/activities/{missing_activity_name}/signup", params={"email": new_email}
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_not_signed_up_returns_404(client, existing_activity_name, new_email):
    response = client.delete(
        f"/activities/{existing_activity_name}/signup", params={"email": new_email}
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not signed up for this activity"


def test_unregister_missing_email_returns_422(client, existing_activity_name):
    response = client.delete(f"/activities/{existing_activity_name}/signup")

    assert response.status_code == 422
