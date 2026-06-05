import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import AlbumCard from '../components/AlbumCard'
import { getAlbumes } from '../services/api'
import { useSearch } from '../context/SearchContext'

const fakeData = [
  { id: 1, title: 'Thriller', artist: { name: 'Michael Jackson' }, genre: { name: 'Pop' }, format_type: { name: 'Vinilo' }, price: 19.99, stock: 5, year: 1982, image_url: 'https://upload.wikimedia.org/wikipedia/en/5/55/Michael_Jackson_-_Thriller.png' },
  { id: 2, title: 'Back in Black', artist: { name: 'AC/DC' }, genre: { name: 'Rock' }, format_type: { name: 'CD' }, price: 17.99, stock: 3, year: 1980, image_url: 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Backinblack.png/220px-Backinblack.png' },
  { id: 3, title: 'Rumours', artist: { name: 'Fleetwood Mac' }, genre: { name: 'Rock' }, format_type: { name: 'Cassette' }, price: 21.99, stock: 8, year: 1977, image_url: 'https://upload.wikimedia.org/wikipedia/en/f/f3/Fleetwood_Mac_-_Rumours.png' },
]

function Catalog() {
  const [albums, setAlbums] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const { search, genero, setGenero, artista, setArtista, formato, setFormato } = useSearch()

  useEffect(() => {
    async function loadAlbums() {
      try {
        const data = await getAlbumes()
        setAlbums(data)
      } catch (err) {
        console.warn('Backend unavailable, using fake data')
        setAlbums(fakeData)
        setError('Backend unavailable')
      } finally {
        setLoading(false)
      }
    }
    loadAlbums()
  }, [])

  const filteredAlbums = albums.filter(album => {
    const matchSearch = album.title.toLowerCase().includes(search.toLowerCase())
    const matchGenre = genero === '' || album.genre.name === genero
    const matchArtist = artista === '' || album.artist.name === artista
    const matchFormat = formato === '' || album.format_type.name === formato
    return matchSearch && matchGenre && matchArtist && matchFormat
  })

  if (loading) return <p>Loading...</p>

  return (
    <div>
      {error && <p>{error} — showing test data</p>}
      <select value={genero} onChange={(e) => setGenero(e.target.value)}>
        <option value="">All genres</option>
        <option value="Pop">Pop</option>
        <option value="Rock">Rock</option>
      </select>
      <select value={artista} onChange={(e) => setArtista(e.target.value)}>
        <option value="">All artists</option>
        <option value="Michael Jackson">Michael Jackson</option>
        <option value="AC/DC">AC/DC</option>
        <option value="Fleetwood Mac">Fleetwood Mac</option>
      </select>
      <select value={formato} onChange={(e) => setFormato(e.target.value)}>
        <option value="">All formats</option>
        <option value="Vinilo">Vinilo</option>
        <option value="CD">CD</option>
        <option value="Cassette">Cassette</option>
      </select>
      {filteredAlbums.length === 0 && <p>No results found</p>}
      <div className="album-grid">
        {filteredAlbums.map(album => (
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

export default Catalog