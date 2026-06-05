function AlbumCard({ title, artist, genre, format_type, price, year, image_url }) {
  return (
  <div className="card">
    <div className="cover-wrap">
      <img src={image_url} alt={title} />
      <span className="fmt-pill">{format_type.name}</span>
    </div>
    <div className="card-title">{title}</div>
    <div className="card-artist">{artist.name}</div>
    <div className="card-meta">{genre.name} · {year}</div>
    <div className="card-price">{price} €</div>
  </div>
)
}

export default AlbumCard