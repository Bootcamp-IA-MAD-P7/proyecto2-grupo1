def test_get_albums_returns_list(client):
    response = client.get("/api/v1/albums")

    assert response.status_code == 200
    assert isinstance(response.json(), list)