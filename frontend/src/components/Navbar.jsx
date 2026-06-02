import { Link } from 'react-router-dom'

function Navbar() {
  return (
    <nav>
      <Link to="/">Inicio</Link>
      <Link to="/catalogo">Catálogo</Link>
      <Link to="/login">IniciarSecion</Link>
      <Link to="/register">Registro</Link>
    </nav>
  )
}

export default Navbar