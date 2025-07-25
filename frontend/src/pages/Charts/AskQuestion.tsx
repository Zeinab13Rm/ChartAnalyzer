"use client"

import type React from "react"

import { useState, useRef } from "react"
import { chartService } from "../../services/api"
import "../../styles/charts.css"

export const AskQuestion = () => {
  const [image, setImage] = useState<File | null>(null)
  const [preview, setPreview] = useState<string | null>(null)
  const [question, setQuestion] = useState("")
  const [answer, setAnswer] = useState("")
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState("")
  const fileInputRef = useRef<HTMLInputElement>(null)

  const handleImageChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      const file = e.target.files[0]
      setImage(file)

      // Create preview URL
      const reader = new FileReader()
      reader.onloadend = () => {
        setPreview(reader.result as string)
      }
      reader.readAsDataURL(file)
    }
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()

    if (!image) {
      setError("Please upload an image first")
      return
    }

    if (!question.trim()) {
      setError("Please enter your question")
      return
    }

    try {
      setIsLoading(true)
      setError("")
      setAnswer("")

      // Create FormData matching your curl example exactly
      const formData = new FormData()
      formData.append("image", image) // Matches your -F 'image=@...'
      formData.append("question", question) // Matches your -F 'question=...'

      const response = await chartService.AskQuestion(formData)
      setAnswer(response.data.answer) // Adjust based on your API response structure
    } catch (err: any) {
      setError(err.response?.data?.detail || "Analysis failed")
      console.error("Error analyzing chart:", err)
    } finally {
      setIsLoading(false)
    }
  }

  const triggerFileInput = () => {
    fileInputRef.current?.click()
  }

  return (
    <div className="analyze-chart-container">
      <div className="analyze-content">
        <h1 className="analyze-title">Ask About Your Chart</h1>

        <div className="upload-section">
          <input type="file" ref={fileInputRef} onChange={handleImageChange} accept="image/*" className="file-input" />

          {preview ? (
            <div className="image-preview-container">
              <img src={preview || "/placeholder.svg"} alt="Chart preview" className="image-preview" />
              <button onClick={triggerFileInput} className="change-image-button">
                Change Image
              </button>
            </div>
          ) : (
            <div className="upload-area" onClick={triggerFileInput}>
              <div className="upload-icon">📊</div>
              <p>Click to upload chart image</p>
              <p className="upload-hint">Supports PNG, JPG, SVG files</p>
            </div>
          )}
        </div>

        <form onSubmit={handleSubmit} className="analysis-form">
          <div className="form-group">
            <label htmlFor="question" className="question-label">
              What would you like to know about this chart?
            </label>
            <textarea
              id="question"
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              rows={4}
              placeholder="Example: What is the highest value shown in this chart? What trends can you identify?"
              disabled={isLoading}
              className="question-input"
            />
          </div>

          {error && <div className="error-message">{error}</div>}

          <div className="button-group">
            <button type="submit" className="analyze-button" disabled={isLoading || !image || !question.trim()}>
              {isLoading ? (
                <>
                  <span className="spinner"></span>
                  Getting Answer...
                </>
              ) : (
                <>
                  <span>❓</span>
                  Ask Question
                </>
              )}
            </button>
          </div>
        </form>

        {answer && (
          <div className="answer-section">
            <h3 className="answer-title">Answer</h3>
            <div className="answer-content">
              {typeof answer === "string" ? answer : JSON.stringify(answer, null, 2)}
            </div>
          </div>
        )}
      </div>
    </div>
  )
}
