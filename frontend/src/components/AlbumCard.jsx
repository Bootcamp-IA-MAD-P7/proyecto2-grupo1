function AlbumCard({ title, artist, genre, format_type, price, year, image_url }) {
  return (
    <div className="card">
      <div className="cover-wrap">
        <img src={image_url} alt={title} width="100" />
      </div>

      <h2>{title}</h2>
      <p>{artist.name}</p>
      <p>{genre.name}</p>
      <p>{format_type.name}</p>
      <p>{year}</p>
      <p>{price} €</p>
    </div>
  )
}

export default AlbumCard