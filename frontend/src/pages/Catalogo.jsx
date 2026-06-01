import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import AlbumCard from '../components/AlbumCard'
import { getAlbumes } from '../services/api'

const datosFalsos = [
  { id: 1, title: 'Thriller', artist: { name: 'Michael Jackson' }, genre: { name: 'Pop' }, format_type: { name: 'Vinilo' }, price: 19.99, stock: 5, year: 1982, image_url: 'https://upload.wikimedia.org/wikipedia/en/5/55/Michael_Jackson_-_Thriller.png' },
  { id: 2, title: 'Back in Black', artist: { name: 'AC/DC' }, genre: { name: 'Rock' }, format_type: { name: 'CD' }, price: 17.99, stock: 3, year: 1980, image_url: 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Backinblack.png/220px-Backinblack.png' },
  { id: 3, title: 'Rumours', artist: { name: 'Fleetwood Mac' }, genre: { name: 'Rock' }, format_type: { name: 'Cassette' }, price: 21.99, stock: 8, year: 1977, image_url: 'https://upload.wikimedia.org/wikipedia/en/f/f3/Fleetwood_Mac_-_Rumours.png' },
]

function Catalogo() {
  const [albumes, setAlbumes] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [search, setSearch] = useState('')

  useEffect(() => {
    async function cargarAlbumes() {
      try {
        const data = await getAlbumes()
        setAlbumes(data)
      } catch (err) {
        console.warn('Backend no disponible, usando datos falsos')
        setAlbumes(datosFalsos)
        setError('Backend no disponible')
      } finally {
        setLoading(false)
      }
    }
    cargarAlbumes()
  }, [])

  const albumesFiltrados = albumes.filter(album =>
    album.title.toLowerCase().includes(search.toLowerCase())
  )

  if (loading) return <p>Cargando...</p>

  return (
    <div>
      <h1>Catálogo</h1>
      {error && <p>{error} — mostrando datos de prueba</p>}
      <input
        type="text"
        placeholder="Buscar álbum..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />
      {albumesFiltrados.length === 0 && <p>No se encontraron resultados</p>}
      <div>
        {albumesFiltrados.map(album => (
          <Link key={album.id} to={`/albumes/${album.id}`}>
            <AlbumCard
              title={album.title}
              artist={album.artist}
              genre={album.genre}
              format_type={album.format_type}
              price={album.price}
              stock={album.stock}
              year={album.year}
              image_url={album.image_url}
            />
          </Link>
        ))}
      </div>
    </div>
  )
}

export default Catalogo