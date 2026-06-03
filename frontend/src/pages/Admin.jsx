import { useState, useEffect } from 'react'
import { useAuth } from '../context/AuthContext'
import { useNavigate } from 'react-router-dom'
import { getAlbumes, deleteAlbum, updateAlbum } from '../services/api'

function Admin() {
  const { token, rol } = useAuth()
  const navigate = useNavigate()
  const [albums, setAlbums] = useState([])
  const [loading, setLoading] = useState(true)
  const [editando, setEditando] = useState(null)

  useEffect(() => {
    // if (!token || rol !== 'admin') {
    //   navigate('/login')
    //   return
    // }
    async function loadAlbums() {
      try {
        const data = await getAlbumes()
        setAlbums(data)
      } finally {
        setLoading(false)
      }
    }
    loadAlbums()
  }, [token, rol])

  async function handleDelete(id) {
    if (!window.confirm('Delete this album?')) return
    await deleteAlbum(id)
    setAlbums(albums.filter(a => a.id !== id))
  }

  function handleEditStart(album) {
    setEditando({ ...album })
  }

  async function handleEditSave() {
    await updateAlbum(editando.id, {
      title: editando.title,
      artist_id: editando.artist_id,
      genre_id: editando.genre_id,
      format_type_id: editando.format_type_id,
      price: editando.price,
      stock: editando.stock,
      year: editando.year,
      image_url: editando.image_url
    })
    setAlbums(albums.map(a => a.id === editando.id ? editando : a))
    setEditando(null)
  }

  if (loading) return <p>Loading...</p>

  return (
    <div>
      <h1>Admin Panel</h1>
      {editando && (
        <div>
          <h2>Editing: {editando.title}</h2>
          <input
            type="text"
            minLength={1}
            maxLength={100}
            value={editando.title}
            onChange={(e) => setEditando({ ...editando, title: e.target.value })}
            placeholder="Title"
          />
          <input
            type="number"
            min="1"
            value={editando.artist_id}
            onChange={(e) => setEditando({ ...editando, artist_id: Number(e.target.value) })}
            placeholder="Artist ID"
          />
          <input
            type="number"
            min="1"
            value={editando.genre_id}
            onChange={(e) => setEditando({ ...editando, genre_id: Number(e.target.value) })}
            placeholder="Genre ID"
          />
          <input
            type="number"
            min="1"
            value={editando.format_type_id}
            onChange={(e) => setEditando({ ...editando, format_type_id: Number(e.target.value) })}
            placeholder="Format ID"
          />
          <input
            type="number"
            min="0"
            step="0.01"
            value={editando.price}
            onChange={(e) => setEditando({ ...editando, price: Number(e.target.value) })}
            placeholder="Price"
          />
          <input
            type="number"
            min="0"
            step="1"
            value={editando.stock}
            onChange={(e) => setEditando({ ...editando, stock: Number(e.target.value) })}
            placeholder="Stock"
          />
          <input
            type="number"
            min="1900"
            max={new Date().getFullYear()}
            value={editando.year}
            onChange={(e) => setEditando({ ...editando, year: Number(e.target.value) })}
            placeholder="Year"
          />
          <input
            type="url"
            value={editando.image_url}
            onChange={(e) => setEditando({ ...editando, image_url: e.target.value })}
            placeholder="Image URL"
          />
          <button onClick={handleEditSave}>Save</button>
          <button onClick={() => setEditando(null)}>Cancel</button>
        </div>
      )}
      <table>
        <thead>
          <tr>
            <th>Title</th>
            <th>Artist</th>
            <th>Price</th>
            <th>Stock</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {albums.map(album => (
            <tr key={album.id}>
              <td>{album.title}</td>
              <td>{album.artist.name}</td>
              <td>{album.price} €</td>
              <td>{album.stock}</td>
              <td>
                <button onClick={() => handleEditStart(album)}>Edit</button>
                <button onClick={() => handleDelete(album.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default Admin