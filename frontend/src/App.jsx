import { Routes, Route } from 'react-router-dom'
import Layout from './components/Layout'
import Catalogo from './pages/Catalogo'
import DetalleAlbum from './pages/DetalleAlbum'
import FormAlbum from './pages/FormAlbum'

function App() {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Catalogo />} />
        <Route path="catalogo" element={<Catalogo />} />
        <Route path="albumes/:id" element={<DetalleAlbum />} />
        <Route path="admin/albumes/nuevo" element={<FormAlbum />} />
      </Route>
    </Routes>
  )
}

export default App