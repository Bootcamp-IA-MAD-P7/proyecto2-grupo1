import { createContext, useState, useContext } from 'react'

const AuthContext = createContext()

export function AuthProvider({ children }) {
  const [token, setToken] = useState(localStorage.getItem('token') || null)
  const [rol, setRol] = useState(localStorage.getItem('rol') || null)

  function login(nuevoToken, nuevoRol) {
    localStorage.setItem('token', nuevoToken)
    localStorage.setItem('rol', nuevoRol)
    setToken(nuevoToken)
    setRol(nuevoRol)
  }

  function logout() {
    localStorage.removeItem('token')
    localStorage.removeItem('rol')
    setToken(null)
    setRol(null)
  }

  return (
    <AuthContext.Provider value={{ token, rol, login, logout }}>
      {children}
    </AuthContext.Provider>
  )
}

export function useAuth() {
  return useContext(AuthContext)
}