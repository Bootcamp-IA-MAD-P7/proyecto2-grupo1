import { Routes, Route } from 'react-router-dom'
import Layout from './components/Layout'
import Catalogo from './pages/Catalogo'
import DetalleAlbum from './pages/DetalleAlbum'

function App() {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Catalogo />} />
        <Route path="catalogo" element={<Catalogo />} />
        <Route path="albumes/:id" element={<DetalleAlbum />} />
      </Route>
    </Routes>
  )
}

export default App