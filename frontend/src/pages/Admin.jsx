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

  if (loading) return <p className="loading">Cargando...</p>

  return (
  <div className="admin-page">
    <h1 className="admin-title">Panel Admin</h1>

    <div className="admin-actions">
      <button className="admin-btn-primary" onClick={() => setCreating(!creating)}>+ Nuevo álbum</button>
      <button className="admin-btn" onClick={() => alert('Coming soon')}>+ Artista</button>
      <button className="admin-btn" onClick={() => alert('Coming soon')}>+ Género</button>
      <button className="admin-btn" onClick={() => alert('Coming soon')}>+ Formato</button>
    </div>

    {creating && (
      <div className="admin-form-box">
        <h2>Nuevo álbum</h2>
        <input className="admin-input" type="text" placeholder="Título" value={newAlbum.title}
          onChange={(e) => setNewAlbum({ ...newAlbum, title: e.target.value })} />
        <select className="admin-select" value={newAlbum.artist_id} onChange={(e) => setNewAlbum({ ...newAlbum, artist_id: e.target.value })}>
          <option value="">Artista</option>
          {artists.map(a => <option key={a.id} value={a.id}>{a.name}</option>)}
        </select>
        <select className="admin-select" value={newAlbum.genre_id} onChange={(e) => setNewAlbum({ ...newAlbum, genre_id: e.target.value })}>
          <option value="">Género</option>
          {genres.map(g => <option key={g.id} value={g.id}>{g.name}</option>)}
        </select>
        <select className="admin-select" value={newAlbum.format_type_id} onChange={(e) => setNewAlbum({ ...newAlbum, format_type_id: e.target.value })}>
          <option value="">Formato</option>
          {formats.map(f => <option key={f.id} value={f.id}>{f.name}</option>)}
        </select>
        <input className="admin-input" type="number" placeholder="Precio" value={newAlbum.price}
          onChange={(e) => setNewAlbum({ ...newAlbum, price: e.target.value })} />
        <input className="admin-input" type="number" placeholder="Stock" value={newAlbum.stock}
          onChange={(e) => setNewAlbum({ ...newAlbum, stock: e.target.value })} />
        <input className="admin-input" type="number" placeholder="Año" value={newAlbum.year}
          onChange={(e) => setNewAlbum({ ...newAlbum, year: e.target.value })} />
        <input className="admin-input" type="url" placeholder="URL imagen" value={newAlbum.image_url}
          onChange={(e) => setNewAlbum({ ...newAlbum, image_url: e.target.value })} />
        <div style={{ marginTop: '16px', display: 'flex', gap: '8px' }}>
          <button className="admin-btn-primary" onClick={handleCreate}>Guardar</button>
          <button className="admin-btn" onClick={() => setCreating(false)}>Cancelar</button>
        </div>
      </div>
    )}

    {editing && (
      <div className="admin-form-box">
        <h2>Editando: {editing.title}</h2>
        <input className="admin-input" type="text" placeholder="Título" value={editing.title}
          onChange={(e) => setEditing({ ...editing, title: e.target.value })} />
        <select className="admin-select" value={editing.artist_id} onChange={(e) => setEditing({ ...editing, artist_id: e.target.value })}>
          <option value="">Artista</option>
          {artists.map(a => <option key={a.id} value={a.id}>{a.name}</option>)}
        </select>
        <select className="admin-select" value={editing.genre_id} onChange={(e) => setEditing({ ...editing, genre_id: e.target.value })}>
          <option value="">Género</option>
          {genres.map(g => <option key={g.id} value={g.id}>{g.name}</option>)}
        </select>
        <select className="admin-select" value={editing.format_type_id} onChange={(e) => setEditing({ ...editing, format_type_id: e.target.value })}>
          <option value="">Formato</option>
          {formats.map(f => <option key={f.id} value={f.id}>{f.name}</option>)}
        </select>
        <input className="admin-input" type="number" placeholder="Precio" value={editing.price}
          onChange={(e) => setEditing({ ...editing, price: e.target.value })} />
        <input className="admin-input" type="number" placeholder="Stock" value={editing.stock}
          onChange={(e) => setEditing({ ...editing, stock: e.target.value })} />
        <input className="admin-input" type="number" placeholder="Año" value={editing.year}
          onChange={(e) => setEditing({ ...editing, year: e.target.value })} />
        <input className="admin-input" type="url" placeholder="URL imagen" value={editing.image_url}
          onChange={(e) => setEditing({ ...editing, image_url: e.target.value })} />
        <div style={{ marginTop: '16px', display: 'flex', gap: '8px' }}>
          <button className="admin-btn-primary" onClick={handleEditSave}>Guardar</button>
          <button className="admin-btn" onClick={() => setEditing(null)}>Cancelar</button>
        </div>
      </div>
    )}

    <table className="admin-table">
      <thead>
        <tr>
          <th>Título</th>
          <th>Artista</th>
          <th>Género</th>
          <th>Formato</th>
          <th>Precio</th>
          <th>Stock</th>
          <th>Año</th>
          <th>Acciones</th>
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
              <button className="admin-btn" onClick={() => handleEditStart(album)}>Editar</button>
              <button className="admin-btn" onClick={() => handleDelete(album.id)}>Eliminar</button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  </div>
)
}

export default Admin