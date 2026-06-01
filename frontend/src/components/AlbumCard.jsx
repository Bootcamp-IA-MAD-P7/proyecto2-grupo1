function AlbumCard({ title, artist, price, image_url }) {
  return (
    <div>
      <img src={image_url} alt={title} width="100" />
      <h2>{title}</h2>
      <p>{artist}</p>
      <p>{price} €</p>
    </div>
  )
}

export default AlbumCard