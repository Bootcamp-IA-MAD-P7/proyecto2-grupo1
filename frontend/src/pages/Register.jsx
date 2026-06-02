import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
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
    <div>
      <h1>Registro</h1>
      {error && <p>{error}</p>}
      <input
        type="text"
        placeholder="Nombre"
        value={nombre}
        onChange={(e) => setNombre(e.target.value)}
      />
      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <input
        type="password"
        placeholder="Contraseña"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button onClick={handleRegister}>Registrarse</button>
    </div>
  )
}

export default Register
