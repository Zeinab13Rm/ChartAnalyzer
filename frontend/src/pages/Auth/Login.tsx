"use client"

import type React from "react"

import { useState } from "react"
import { authService } from "../../services/api"
import { useNavigate, Link } from "react-router-dom"
import "../../styles/auth.css"

export const Login = () => {
  const [formData, setFormData] = useState({
    username: "",
    password: "",
  })
  const [error, setError] = useState("")
  const [isLoading, setIsLoading] = useState(false)
  const navigate = useNavigate()

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsLoading(true)

    try {
      setError("")
      const response = await authService.login(formData)
      localStorage.setItem("token", response.data.token)
      localStorage.setItem("username", formData.username)
      navigate("/")
    } catch (err: any) {
      setError(err.response?.data?.detail || "Invalid credentials")
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="auth-container">
      <div className="auth-card">
        <div className="auth-header">
          <h2>Welcome Back</h2>
          <p>Sign in to your account to continue</p>
        </div>

        <div className="auth-content">
          {error && <div className="error-message">{error}</div>}

          <form onSubmit={handleSubmit} className="auth-form">
            <div className="form-group">
              <label htmlFor="username">Username</label>
              <input
                id="username"
                type="text"
                value={formData.username}
                onChange={(e) => setFormData({ ...formData, username: e.target.value })}
                required
                placeholder="Enter your username"
              />
            </div>

            <div className="form-group">
              <label htmlFor="password">Password</label>
              <input
                id="password"
                type="password"
                value={formData.password}
                onChange={(e) => setFormData({ ...formData, password: e.target.value })}
                required
                placeholder="Enter your password"
              />
            </div>

            <button type="submit" className="submit-button" disabled={isLoading}>
              {isLoading ? "Signing in..." : "Sign In"}
            </button>
          </form>
        </div>

        <div className="auth-footer">
          <p>Don't have an account?</p>
          <Link to="/auth/register">Create one here</Link>
        </div>
      </div>
    </div>
  )
}
