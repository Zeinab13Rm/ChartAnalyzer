"use client"

import type React from "react"

import { useState } from "react"
import { authService } from "../../services/api"
import { useNavigate } from "react-router-dom"
import { Link } from "react-router-dom"
import "../../styles/auth.css"

export const Register = () => {
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
    confirmPassword: "",
  })
  const [error, setError] = useState("")
  const [success, setSuccess] = useState(false)
  const navigate = useNavigate()

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()

    // Basic validation
    if (formData.password !== formData.confirmPassword) {
      setError("Passwords do not match")
      return
    }

    try {
      setError("")
      await authService.register({
        username: formData.username,
        email: formData.email,
        password: formData.password,
      })
      setSuccess(true)
      // Auto-redirect after 2 seconds
      setTimeout(() => navigate("/auth/login"), 2000)
    } catch (err: any) {
      setError(err.response?.data?.detail || "Registration failed")
    }
  }

  if (success) {
    return (
      <div className="success-message">
        <div className="success-icon">✅</div>
        <h2>Registration Successful!</h2>
        <p>You will be redirected to login page shortly...</p>
      </div>
    )
  }

  return (
    <div className="auth-container">
      <div className="auth-card">
        <div className="auth-header">
          <h2>Create Account</h2>
          <p>Join us to start analyzing your charts</p>
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
                minLength={3}
                placeholder="Enter your username"
              />
            </div>

            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input
                id="email"
                type="email"
                value={formData.email}
                onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                required
                placeholder="Enter your email"
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
                minLength={6}
                placeholder="Enter your password"
              />
            </div>

            <div className="form-group">
              <label htmlFor="confirmPassword">Confirm Password</label>
              <input
                id="confirmPassword"
                type="password"
                value={formData.confirmPassword}
                onChange={(e) => setFormData({ ...formData, confirmPassword: e.target.value })}
                required
                minLength={6}
                placeholder="Confirm your password"
              />
            </div>

            <button type="submit" className="submit-button">
              Create Account
            </button>
          </form>
        </div>

        <div className="auth-footer">
          <p>Already have an account?</p>
          <Link to="/auth/login">Sign in here</Link>
        </div>
      </div>
    </div>
  )
}
