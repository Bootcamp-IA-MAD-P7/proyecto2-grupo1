const BASE_URL = 'http://localhost:8000/api/v1'
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

export async function login(email, password) {
  const response = await fetch(`${BASE_URL}/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password })
  })
  if (!response.ok) throw new Error('Login failed')
  const data = await response.json()
  return data
}

export async function register(nombre, email, password) {
  const response = await fetch(`${BASE_URL}/auth/register`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name: nombre, email, password })
  })
  if (!response.ok) throw new Error('Register failed')
  const data = await response.json()
  return data
}