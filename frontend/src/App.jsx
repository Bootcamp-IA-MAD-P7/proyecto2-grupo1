import { Routes, Route } from 'react-router-dom'
import Layout from './components/Layout'
import Catalogo from './pages/Catalogo'
function App() {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Catalogo />} />
      </Route>
    </Routes>
  )
}

export default App