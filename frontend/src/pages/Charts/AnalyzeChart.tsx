"use client"

import type React from "react"

import { useState, useRef } from "react"
import { chartService } from "../../services/api"
import "../../styles/charts.css"

export const AnalyzeChart = () => {
  const [image, setImage] = useState<File | null>(null)
  const [preview, setPreview] = useState<string | null>(null)
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState("")
  const [analysisResult, setAnalysisResult] = useState("")
  const fileInputRef = useRef<HTMLInputElement>(null)

  const handleImageChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      const file = e.target.files[0]
      setImage(file)
      setAnalysisResult("") // Clear previous result when new image is selected

      // Create preview URL
      const reader = new FileReader()
      reader.onloadend = () => {
        setPreview(reader.result as string)
      }
      reader.readAsDataURL(file)
    }
  }

  const handleAnalyze = async (e: React.FormEvent) => {
    e.preventDefault()

    if (!image) {
      setError("Please upload an image first")
      return
    }

    try {
      setIsLoading(true)
      setError("")
      setAnalysisResult("")

      // Create FormData as your API expects
      const formData = new FormData()
      formData.append("image", image) // Matches your -F 'image=@file.png'

      const response = await chartService.analyzeChart(formData)
      setAnalysisResult(response.data.analysis || response.data.result || "Analysis complete")
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
        <h1 className="analyze-title">Chart Analysis</h1>

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

        {error && <div className="error-message">{error}</div>}

        <div className="action-section">
          <button onClick={handleAnalyze} className="analyze-button" disabled={isLoading || !image}>
            {isLoading ? (
              <>
                <span className="spinner"></span>
                Analyzing Chart...
              </>
            ) : (
              <>
                <span>🔍</span>
                Analyze Chart
              </>
            )}
          </button>
        </div>

        {analysisResult && (
          <div className="result-section">
            <h3 className="result-title">Analysis Result</h3>
            <div className="result-content">{analysisResult}</div>
          </div>
        )}
      </div>
    </div>
  )
}
