import { useState } from 'react'
import { createAlbum } from '../services/api'

function FormAlbum() {
  const [titulo, setTitulo] = useState('')
  const [artistaId, setArtistaId] = useState('')
  const [generoId, setGeneroId] = useState('')
  const [formatoId, setFormatoId] = useState('')
  const [precio, setPrecio] = useState('')
  const [stock, setStock] = useState('')
  const [year, setYear] = useState('')
  const [imageUrl, setImageUrl] = useState('')
  const [mensaje, setMensaje] = useState(null)
  const [error, setError] = useState(null)

  async function handleSubmit() {
    try {
      const nuevoAlbum = {
        title: titulo,
        artist_id: Number(artistaId),
        genre_id: Number(generoId),
        format_type_id: Number(formatoId),
        price: Number(precio),
        stock: Number(stock),
        year: Number(year),
        image_url: imageUrl
      }
      await createAlbum(nuevoAlbum)
      setMensaje('Álbum creado correctamente')
      setError(null)
    } catch (err) {
      setError('Error al crear el álbum')
      setMensaje(null)
    }
  }

  return (
    <div>
      <h1>Añadir álbum</h1>
      {mensaje && <p>{mensaje}</p>}
      {error && <p>{error}</p>}
      <input placeholder="Título" value={titulo} onChange={(e) => setTitulo(e.target.value)} />
      <input placeholder="ID artista" value={artistaId} onChange={(e) => setArtistaId(e.target.value)} />
      <input placeholder="ID género" value={generoId} onChange={(e) => setGeneroId(e.target.value)} />
      <input placeholder="ID formato" value={formatoId} onChange={(e) => setFormatoId(e.target.value)} />
      <input placeholder="Precio" value={precio} onChange={(e) => setPrecio(e.target.value)} />
      <input placeholder="Stock" value={stock} onChange={(e) => setStock(e.target.value)} />
      <input placeholder="Año" value={year} onChange={(e) => setYear(e.target.value)} />
      <input placeholder="URL imagen" value={imageUrl} onChange={(e) => setImageUrl(e.target.value)} />
      <button onClick={handleSubmit}>Guardar</button>
    </div>
  )
}

export default FormAlbum