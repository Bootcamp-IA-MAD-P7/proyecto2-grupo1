import { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'

const datosFalsos = {
  1: { id: 1, title: 'Thriller', artist: 'Michael Jackson', price: 19.99, image_url: 'https://upload.wikimedia.org/wikipedia/en/5/55/Michael_Jackson_-_Thriller.png' },
  2: { id: 2, title: 'Back in Black', artist: 'AC/DC', price: 17.99, image_url: 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Backinblack.png/220px-Backinblack.png' },
  3: { id: 3, title: 'Rumours', artist: 'Fleetwood Mac', price: 21.99, image_url: 'https://upload.wikimedia.org/wikipedia/en/f/f3/Fleetwood_Mac_-_Rumours.png' },
}

function DetalleAlbum() {
  const { id } = useParams()
  const [album, setAlbum] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    async function cargarAlbum() {
      try {
        const response = await fetch(`http://localhost:8000/albumes/${id}`)
        const data = await response.json()
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
      <p>{album.artist}</p>
      <p>{album.price} €</p>
    </div>
  )
}

export default DetalleAlbum