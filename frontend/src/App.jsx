import React, { useState } from "react"
import Login from "./Login"
import Cars from "./Cars"
export default function App() {
  const [token, setToken] = useState(localStorage.getItem("jwt"))
  if (!token) return <Login onLogin={setToken} />
  return <Cars />
}
