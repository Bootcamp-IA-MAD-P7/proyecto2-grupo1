def test_album_contains_required_fields(client):
    response = client.get("/api/v1/albums")

    albums = response.json()

    if albums:

        album = albums[0]

        assert "id" in album
        assert "title" in album
        assert "price" in album
        assert "stock" in album
        assert "artist_id" in album
        assert "format_type_id" in album