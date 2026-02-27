import React, { useState } from "react"
import { api, setToken } from "./api"
export default function Login({ onLogin }) {
  const [u, setU] = useState("")
  const [p, setP] = useState("")
  async function submit() {
    const r = await api.post("/api/login", { username: u, password: p })
    localStorage.setItem("jwt", r.data.access_token)
    setToken(r.data.access_token)
    onLogin(r.data.access_token)
  }
  return (
    <div>
      <input placeholder="user" onChange={e => setU(e.target.value)} />
      <input placeholder="pass" type="password" onChange={e => setP(e.target.value)} />
      <button onClick={submit}>Login</button>
    </div>
  )
}
