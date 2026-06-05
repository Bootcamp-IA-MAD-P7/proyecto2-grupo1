def test_get_albums(client):
    response = client.get("/api/v1/albums")

    assert response.status_code == 200