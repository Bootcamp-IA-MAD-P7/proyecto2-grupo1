import { Outlet } from 'react-router-dom'
import Navbar from './Navbar'
import Footer from './Footer'

function Layout() {
  return (
    <div>
      <Navbar />
      <main style={{ paddingTop: '60px' }}>
        <Outlet />
      </main>
      <Footer />
    </div>
  )
}

export default Layout