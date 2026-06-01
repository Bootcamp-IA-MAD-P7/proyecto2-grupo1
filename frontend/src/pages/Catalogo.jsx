import { useState, useEffect } from 'react'

const datosFalsos = [
  { id: 1, title: 'Thriller', artist: 'Michael Jackson', price: 19.99, image_url: 'https://upload.wikimedia.org/wikipedia/en/5/55/Michael_Jackson_-_Thriller.png' },
  { id: 2, title: 'Back in Black', artist: 'AC/DC', price: 17.99, image_url: 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Backinblack.png/220px-Backinblack.png' },
  { id: 3, title: 'Rumours', artist: 'Fleetwood Mac', price: 21.99, image_url: 'https://upload.wikimedia.org/wikipedia/en/f/f3/Fleetwood_Mac_-_Rumours.png' },
]

function Catalogo() {
  const [albumes, setAlbumes] = useState([])

  useEffect(() => {
    setAlbumes(datosFalsos)
  }, [])

  return (
    <div>
      <h1>Catálogo</h1>
      <div>
        {albumes.map(album => (
          <div key={album.id}>
            <img src={album.image_url} alt={album.title} width="100" />
            <h2>{album.title}</h2>
            <p>{album.artist}</p>
            <p>{album.price} €</p>
          </div>
        ))}
      </div>
    </div>
  )
}

export default Catalogo