import { createContext, useState, useContext } from 'react'

const SearchContext = createContext()

export function SearchProvider({ children }) {
  const [search, setSearch] = useState('')
  const [genero, setGenero] = useState('')
  const [artista, setArtista] = useState('')
  const [formato, setFormato] = useState('')

  return (
    <SearchContext.Provider value={{ 
      search, setSearch,
      genero, setGenero,
      artista, setArtista,
      formato, setFormato
    }}>
      {children}
    </SearchContext.Provider>
  )
}

export function useSearch() {
  return useContext(SearchContext)
}