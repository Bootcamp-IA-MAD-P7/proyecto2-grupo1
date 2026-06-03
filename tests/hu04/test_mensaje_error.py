def test_get_album_not_found_message(client):

    response = client.get("/api/v1/albums/999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Álbum no encontrado"