import { Link } from 'react-router-dom'
import logoImg from '../assets/logo_musintage.png' // <-- Cambiamos .jpg por .png

function Navbar() {
  return (
    <nav>
      <Link to="/">
        <img src={logoImg} alt="Musvintage" />
      </Link>
      <Link to="/catalogo">Catálogo</Link>
      <Link to="/login">IniciarSecion</Link>
      <Link to="/register">Registro</Link>
    </nav>
  )
}

export default Navbar