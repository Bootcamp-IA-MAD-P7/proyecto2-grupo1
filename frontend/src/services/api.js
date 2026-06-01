const BASE_URL = 'http://localhost:8000'

export async function getAlbumes() {
  const response = await fetch(`${BASE_URL}/albumes`)
  const data = await response.json()
  return data
}