import React, { useEffect, useState } from "react"
import { api, setToken } from "./api"
export default function Cars() {
  const [cars, setCars] = useState([])
  useEffect(() => {
    const t = localStorage.getItem("jwt")
    setToken(t)
    api.get("/api/cars").then(r => setCars(r.data))
  }, [])
  return (
    <table>
      <thead>
        <tr>
          <th>Brand</th><th>Model</th><th>Year</th><th>Price</th><th>Color</th>
        </tr>
      </thead>
      <tbody>
        {cars.map(c => (
          <tr key={c.url}>
            <td>{c.brand}</td>
            <td>{c.model}</td>
            <td>{c.year}</td>
            <td>{c.price}</td>
            <td>{c.color}</td>
          </tr>
        ))}
      </tbody>
    </table>
  )
}
