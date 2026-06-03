import { useState, useEffect } from 'react'
import { useAuth } from '../context/AuthContext'
import { useNavigate } from 'react-router-dom'
import { getAlbumes, deleteAlbum, updateAlbum, createAlbum, getArtists, getGenres, getFormats } from '../services/api'

function Admin() {
  const { token, rol } = useAuth()
  const navigate = useNavigate()
  const [albums, setAlbums] = useState([])
  const [artists, setArtists] = useState([])
  const [genres, setGenres] = useState([])
  const [formats, setFormats] = useState([])
  const [loading, setLoading] = useState(true)
  const [editing, setEditing] = useState(null)
  const [creating, setCreating] = useState(false)
  const [newAlbum, setNewAlbum] = useState({
    title: '', artist_id: '', genre_id: '', format_type_id: '',
    price: '', stock: '', year: '', image_url: ''
  })

  useEffect(() => {
    // if (!token || rol !== 'admin') {
    //   navigate('/login')
    //   return
    // }
    async function loadData() {
      try {
        const [albumsData, artistsData, genresData, formatsData] = await Promise.all([
          getAlbumes(), getArtists(), getGenres(), getFormats()
        ])
        setAlbums(albumsData)
        setArtists(artistsData)
        setGenres(genresData)
        setFormats(formatsData)
      } finally {
        setLoading(false)
      }
    }
    loadData()
  }, [token, rol])

  async function handleDelete(id) {
    if (!window.confirm('Delete this album?')) return
    await deleteAlbum(id)
    setAlbums(albums.filter(a => a.id !== id))
  }

  function handleEditStart(album) {
    setEditing({ ...album, artist_id: album.artist?.id, genre_id: album.genre?.id, format_type_id: album.format_type?.id })
  }

  async function handleEditSave() {
    await updateAlbum(editing.id, {
      title: editing.title,
      artist_id: Number(editing.artist_id),
      genre_id: Number(editing.genre_id),
      format_type_id: Number(editing.format_type_id),
      price: Number(editing.price),
      stock: Number(editing.stock),
      year: Number(editing.year),
      image_url: editing.image_url
    })
    setAlbums(albums.map(a => a.id === editing.id ? editing : a))
    setEditing(null)
  }

  async function handleCreate() {
    const created = await createAlbum({
      title: newAlbum.title,
      artist_id: Number(newAlbum.artist_id),
      genre_id: Number(newAlbum.genre_id),
      format_type_id: Number(newAlbum.format_type_id),
      price: Number(newAlbum.price),
      stock: Number(newAlbum.stock),
      year: Number(newAlbum.year),
      image_url: newAlbum.image_url
    })
    setAlbums([...albums, created])
    setCreating(false)
    setNewAlbum({ title: '', artist_id: '', genre_id: '', format_type_id: '', price: '', stock: '', year: '', image_url: '' })
  }

  if (loading) return <p>Loading...</p>

  return (
    <div>
      <h1>Admin Panel</h1>

      <div>
        <button onClick={() => setCreating(!creating)}>+ New Album</button>
        <button onClick={() => alert('Coming soon')}>+ New Artist</button>
        <button onClick={() => alert('Coming soon')}>+ New Genre</button>
        <button onClick={() => alert('Coming soon')}>+ New Format</button>
      </div>

      {creating && (
        <div>
          <h2>New Album</h2>
          <input type="text" placeholder="Title" value={newAlbum.title}
            onChange={(e) => setNewAlbum({ ...newAlbum, title: e.target.value })} />
          <select value={newAlbum.artist_id} onChange={(e) => setNewAlbum({ ...newAlbum, artist_id: e.target.value })}>
            <option value="">Select artist</option>
            {artists.map(a => <option key={a.id} value={a.id}>{a.name}</option>)}
          </select>
          <select value={newAlbum.genre_id} onChange={(e) => setNewAlbum({ ...newAlbum, genre_id: e.target.value })}>
            <option value="">Select genre</option>
            {genres.map(g => <option key={g.id} value={g.id}>{g.name}</option>)}
          </select>
          <select value={newAlbum.format_type_id} onChange={(e) => setNewAlbum({ ...newAlbum, format_type_id: e.target.value })}>
            <option value="">Select format</option>
            {formats.map(f => <option key={f.id} value={f.id}>{f.name}</option>)}
          </select>
          <input type="number" min="0" step="0.01" placeholder="Price" value={newAlbum.price}
            onChange={(e) => setNewAlbum({ ...newAlbum, price: e.target.value })} />
          <input type="number" min="0" step="1" placeholder="Stock" value={newAlbum.stock}
            onChange={(e) => setNewAlbum({ ...newAlbum, stock: e.target.value })} />
          <input type="number" min="1900" max={new Date().getFullYear()} placeholder="Year" value={newAlbum.year}
            onChange={(e) => setNewAlbum({ ...newAlbum, year: e.target.value })} />
          <input type="url" placeholder="Image URL" value={newAlbum.image_url}
            onChange={(e) => setNewAlbum({ ...newAlbum, image_url: e.target.value })} />
          <button onClick={handleCreate}>Save</button>
          <button onClick={() => setCreating(false)}>Cancel</button>
        </div>
      )}

      {editing && (
        <div>
          <h2>Editing: {editing.title}</h2>
          <input type="text" minLength={1} maxLength={100} placeholder="Title" value={editing.title}
            onChange={(e) => setEditing({ ...editing, title: e.target.value })} />
          <select value={editing.artist_id} onChange={(e) => setEditing({ ...editing, artist_id: e.target.value })}>
            <option value="">Select artist</option>
            {artists.map(a => <option key={a.id} value={a.id}>{a.name}</option>)}
          </select>
          <select value={editing.genre_id} onChange={(e) => setEditing({ ...editing, genre_id: e.target.value })}>
            <option value="">Select genre</option>
            {genres.map(g => <option key={g.id} value={g.id}>{g.name}</option>)}
          </select>
          <select value={editing.format_type_id} onChange={(e) => setEditing({ ...editing, format_type_id: e.target.value })}>
            <option value="">Select format</option>
            {formats.map(f => <option key={f.id} value={f.id}>{f.name}</option>)}
          </select>
          <input type="number" min="0" step="0.01" placeholder="Price" value={editing.price}
            onChange={(e) => setEditing({ ...editing, price: e.target.value })} />
          <input type="number" min="0" step="1" placeholder="Stock" value={editing.stock}
            onChange={(e) => setEditing({ ...editing, stock: e.target.value })} />
          <input type="number" min="1900" max={new Date().getFullYear()} placeholder="Year" value={editing.year}
            onChange={(e) => setEditing({ ...editing, year: e.target.value })} />
          <input type="url" placeholder="Image URL" value={editing.image_url}
            onChange={(e) => setEditing({ ...editing, image_url: e.target.value })} />
          <button onClick={handleEditSave}>Save</button>
          <button onClick={() => setEditing(null)}>Cancel</button>
        </div>
      )}

      <table>
        <thead>
          <tr>
            <th>Title</th>
            <th>Artist</th>
            <th>Genre</th>
            <th>Format</th>
            <th>Price</th>
            <th>Stock</th>
            <th>Year</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {albums.map(album => (
            <tr key={album.id}>
              <td>{album.title}</td>
              <td>{album.artist?.name}</td>
              <td>{album.genre?.name}</td>
              <td>{album.format_type?.name}</td>
              <td>{album.price} €</td>
              <td>{album.stock}</td>
              <td>{album.year}</td>
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