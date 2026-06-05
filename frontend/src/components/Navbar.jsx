import { Link, useNavigate } from 'react-router-dom'
import logoImg from '../assets/logo_musintage.png'
import { useSearch } from '../context/SearchContext'
import { useAuth } from '../context/AuthContext'

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
      <input
      className="nav-search"
      type="text"
      placeholder="Buscar álbum..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />
      <div className="nav-links">
      {rol === 'admin' && <Link to="/admin">Panel Admin</Link>}
      {token ? (
        <>
          <span>{rol === 'admin' ? 'Admin' : 'Mi cuenta'}</span>
          <button onClick={handleLogout}>Cerrar sesión</button>
        </>
      ) : (
        <>
          <Link to="/login">Iniciar sesión</Link>
          <Link to="/register">Registro</Link>
        </>
      )}
      </div>
    </nav>
  )
}

export default Navbar
