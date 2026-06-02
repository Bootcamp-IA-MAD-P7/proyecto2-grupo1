import { Link } from 'react-router-dom'
import logoImg from '../assets/logo_musintage.png' // <-- Cambiamos .jpg por .png
import { useSearch } from '../context/SearchContext'

function Navbar() {
  const { search, setSearch } = useSearch()
  return (
    <nav>
      <Link to="/">
        <img src={logoImg} alt="Musvintage" />
      </Link>
      <Link to="/catalogo">Catálogo</Link>
      <Link to="/login">IniciarSecion</Link>
      <Link to="/register">Registro</Link>
      <input
        type="text"
        placeholder="Buscar álbum..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />
    </nav>
  )
}

export default Navbar