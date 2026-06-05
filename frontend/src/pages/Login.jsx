import { useState } from 'react'
import { useNavigate, Link} from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import { login as loginApi } from '../services/api'

function Login() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState(null)
  const navigate = useNavigate()
  const { login } = useAuth()

  async function handleLogin() {
    try {
      const data = await login(email, password)
      localStorage.setItem('token', data.token)
      navigate('/catalogo')
    } catch (err) {
      setError('Email o contraseña incorrectos')
    }
  }

  return (
  <div className="form-page">
    <div className="form-box">
      <h1 className="form-title">Iniciar <span>sesión</span></h1>
      {error && <p className="form-error">{error}</p>}
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
      <button className="form-btn" onClick={handleLogin}>Entrar</button>
      <p className="form-link">¿No tienes cuenta? <Link to="/register">Regístrate</Link></p>
    </div>
  </div>
)
}

export default Login
