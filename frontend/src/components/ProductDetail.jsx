
import React from 'react'

export default function ProductDetail({product, onClose}){
  return (
    <div style={{position:'fixed', inset:0, background:'rgba(0,0,0,0.6)', display:'flex', alignItems:'center', justifyContent:'center'}}>
      <div style={{background:'#071026', padding:20, borderRadius:12, width:'90%', maxWidth:900, color:'#fff'}}>
        <div style={{display:'flex', justifyContent:'space-between', alignItems:'center'}}>
          <h2>{product.name}</h2>
          <button onClick={onClose}>Cerrar</button>
        </div>
        <div style={{marginTop:12}}>
          <img src={product.image} style={{width:'100%', height:260, objectFit:'cover', borderRadius:8}}/>
        </div>
        <div style={{marginTop:12}}>
          <pre style={{whiteSpace:'pre-wrap', color:'#cfe'}}>{JSON.stringify(product.prices, null, 2)}</pre>
        </div>
      </div>
    </div>
  )
}
