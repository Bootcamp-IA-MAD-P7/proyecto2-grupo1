def test_create_album_empty_title(client):

    album = {
        "title": "",
        "price": 10,
        "stock": 5,
        "artist_id": 1,
        "format_type_id": 1
    }

    response = client.post(
        "/api/v1/albums",
        json=album
    )

    assert response.status_code == 422