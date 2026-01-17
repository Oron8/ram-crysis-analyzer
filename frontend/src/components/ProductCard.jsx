
import React from 'react'

export default function ProductCard({product, onSelect}){
  return (
    <div onClick={onSelect} style={{background:'#0f1724', padding:12, borderRadius:12, cursor:'pointer'}}>
      <img src={product.image} alt={product.name} style={{width:'100%', height:140, objectFit:'cover', borderRadius:8}}/>
      <h3 style={{margin:'8px 0 4px'}}>{product.name}</h3>
      <p style={{color:'#9aa'}}> {product.brand} · {product.size} · {product.type}</p>
    </div>
  )
}
