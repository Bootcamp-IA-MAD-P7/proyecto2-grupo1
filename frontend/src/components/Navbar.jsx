import { Link } from 'react-router-dom'
import logoImg from '../assets/logo_musintage.png' // <-- Cambiamos .jpg por .png
import { useSearch } from '../context/SearchContext'
import { useAuth } from '../context/AuthContext'
import { useNavigate } from 'react-router-dom'

function Navbar() {
  const { search, setSearch } = useSearch()
  const { token, rol, logout } = useAuth()
  const navigate = useNavigate()

  function handleLogout() {
    logout()
    navigate('/')
  }

  return (
    <nav>
      <Link to="/">
        <img src={logoImg} alt="Musvintage" />
      </Link>
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