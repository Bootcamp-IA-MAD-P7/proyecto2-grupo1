import { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import { getAlbumById } from '../services/api'

const datosFalsos = {
  1: { id: 1, title: 'Thriller', artist: { name: 'Michael Jackson' }, genre: { name: 'Pop' }, format_type: { name: 'Vinilo' }, price: 19.99, stock: 5, year: 1982, image_url: 'https://upload.wikimedia.org/wikipedia/en/5/55/Michael_Jackson_-_Thriller.png' },
  2: { id: 2, title: 'Back in Black', artist: { name: 'AC/DC' }, genre: { name: 'Rock' }, format_type: { name: 'CD' }, price: 17.99, stock: 3, year: 1980, image_url: 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Backinblack.png/220px-Backinblack.png' },
  3: { id: 3, title: 'Rumours', artist: { name: 'Fleetwood Mac' }, genre: { name: 'Rock' }, format_type: { name: 'Cassette' }, price: 21.99, stock: 8, year: 1977, image_url: 'https://upload.wikimedia.org/wikipedia/en/f/f3/Fleetwood_Mac_-_Rumours.png' },
}

function DetalleAlbum() {
  const { id } = useParams()
  const [album, setAlbum] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    async function cargarAlbum() {
      try {
        const data = await getAlbumById(id)
        setAlbum(data)
      } catch (err) {
        console.warn('Backend no disponible, usando datos falsos')
        setAlbum(datosFalsos[Number(id)])
      } finally {
        setLoading(false)
      }
    }
    cargarAlbum()
  }, [id])

  if (loading) return <p>Cargando...</p>
  if (!album) return <p>Álbum no encontrado</p>

  return (
    <div>
      <img src={album.image_url} alt={album.title} width="200" />
      <h1>{album.title}</h1>
      <p>{album.artist.name}</p>
      <p>{album.genre.name}</p>
      <p>{album.format_type.name}</p>
      <p>{album.year}</p>
      <p>{album.price} €</p>
      <p>Stock: {album.stock}</p>
    </div>
  )
}

export default DetalleAlbum