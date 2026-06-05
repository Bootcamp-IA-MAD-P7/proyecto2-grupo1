def test_create_album_without_data(client):
    response = client.post(
        "/api/v1/albums",
        json={}
    )

    assert response.status_code in [400, 422]