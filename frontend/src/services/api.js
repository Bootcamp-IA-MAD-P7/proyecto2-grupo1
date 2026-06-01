const BASE_URL = 'http://localhost:8000'

export async function getAlbumes() {
  const response = await fetch(`${BASE_URL}/albums`)
  const data = await response.json()
  return data
}

export async function getAlbumById(id) {
  const response = await fetch(`${BASE_URL}/albums/${id}`)
  const data = await response.json()
  return data
}

export async function createAlbum(albumData) {
  const response = await fetch(`${BASE_URL}/albums`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(albumData)
  })
  const data = await response.json()
  return data
}