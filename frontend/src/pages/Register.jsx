import { useState } from 'react'
import { useNavigate, Link  } from 'react-router-dom'
import { register } from '../services/api'

function Register() {
  const [nombre, setNombre] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState(null)
  const navigate = useNavigate()

  async function handleRegister() {
    try {
      const data = await register(nombre, email, password)
      localStorage.setItem('token', data.token)
      navigate('/catalogo')
    } catch (err) {
      setError('Error al registrarse. El email puede estar en uso.')
    }
  }

  return (
  <div className="form-page">
    <div className="form-box">
      <h1 className="form-title">Crear <span>cuenta</span></h1>
      {error && <p className="form-error">{error}</p>}
      <input
        className="form-input"
        type="text"
        placeholder="Nombre"
        value={nombre}
        onChange={(e) => setNombre(e.target.value)}
      />
      <input
        className="form-input"
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <input
        className="form-input"
        type="password"
        placeholder="Contraseña"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button className="form-btn" onClick={handleRegister}>Registrarse</button>
      <p className="form-link">¿Ya tienes cuenta? <Link to="/login">Inicia sesión</Link></p>
    </div>
  </div>
)
}

export default Register
