
import React, {useEffect, useState} from 'react'
import ProductCard from './components/ProductCard'
import ProductDetail from './components/ProductDetail'

export default function App(){
  const [products, setProducts] = useState([])
  const [query, setQuery] = useState('')
  const [selected, setSelected] = useState(null)

  useEffect(() => {
    fetch('/api/products')
      .then(r=>r.json())
      .then(data=>setProducts(data))
      .catch(()=>setProducts([]))
  },[])

  const filtered = products.filter(p => p.name.toLowerCase().includes(query.toLowerCase()))

  return (
    <div style={{padding:20, fontFamily:'Arial, sans-serif', background:'#0b1220', minHeight:'100vh', color:'#fff'}}>
      <h1 style={{fontSize:28}}>THE RAM CRYSIS ANALYZER</h1>

      <div style={{marginTop:12, marginBottom:12, display:'flex', gap:8}}>
        <input placeholder="Buscar RAM..." value={query} onChange={e=>setQuery(e.target.value)} style={{flex:1,padding:8,borderRadius:8}}/>
      </div>

      <div style={{display:'grid', gridTemplateColumns:'repeat(auto-fill,minmax(240px,1fr))', gap:12}}>
        {filtered.map(p => (
          <ProductCard key={p.id} product={p} onSelect={()=>setSelected(p)} />
        ))}
      </div>

      {selected && <ProductDetail product={selected} onClose={()=>setSelected(null)} />}
    </div>
  )
}
