"use client"

import { useState, useRef, useEffect } from "react"
import { ChatMessage } from "./ChatMessage"
import { ChatInput } from "./ChatInput"
import type { MessageType } from "../types"
import { chartService } from "../services/api"
import "../styles/chat.css"

export const ChatInterface = () => {
  const [messages, setMessages] = useState<MessageType[]>([])
  const [isProcessing, setIsProcessing] = useState(false)
  const messagesEndRef = useRef<HTMLDivElement>(null)

  // Auto-scroll to bottom
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" })
  }, [messages])

  const handleSendMessage = async (text: string) => {
    const userMessage: MessageType = {
      id: Date.now().toString(),
      content: text,
      sender: "user",
      type: "text",
      timestamp: new Date(),
    }

    setMessages((prev) => [...prev, userMessage])
    setIsProcessing(true)

    try {
      // Find the last uploaded image in the chat
      const lastImageMessage = [...messages].reverse().find((msg) => msg.type === "image" && msg.sender === "user")

      if (!lastImageMessage) {
        setMessages((prev) => [
          ...prev,
          {
            id: Date.now().toString(),
            content: "Please upload a chart image first before asking questions.",
            sender: "bot",
            type: "text",
            timestamp: new Date(),
          },
        ])
        return
      }

      const formData = new FormData()
      // You might need to convert the image URL back to a file if needed
      // Or modify your backend to accept image URLs
      formData.append("question", text)
      formData.append("image", await fetch(lastImageMessage.content).then((r) => r.blob()))

      const response = await chartService.AskQuestion(formData)

      const botMessage: MessageType = {
        id: Date.now().toString(),
        content: response.data.answer || response.data,
        sender: "bot",
        type: "text",
        timestamp: new Date(),
      }

      setMessages((prev) => [...prev, botMessage])
    } catch (error) {
      const errorMessage: MessageType = {
        id: Date.now().toString(),
        content: "Sorry, I encountered an error processing your question. Please try again.",
        sender: "bot",
        type: "text",
        timestamp: new Date(),
      }
      setMessages((prev) => [...prev, errorMessage])
    } finally {
      setIsProcessing(false)
    }
  }

  const handleUploadImage = (file: File) => {
    const reader = new FileReader()
    reader.onloadend = () => {
      const imageMessage: MessageType = {
        id: Date.now().toString(),
        content: reader.result as string,
        sender: "user",
        type: "image",
        timestamp: new Date(),
      }
      setMessages((prev) => [...prev, imageMessage])
    }
    reader.readAsDataURL(file)
  }

  return (
    <div className="chat-interface">
      <div className="chat-container">
        <div className="chat-header">
          <h1>Chart Chat Assistant</h1>
          <p>Upload a chart and ask questions about it</p>
        </div>

        <div className="chat-messages">
          {messages.length === 0 ? (
            <div className="chat-empty-state">
              <div className="empty-icon">💬</div>
              <h3>Start a conversation</h3>
              <p>Upload a chart image and ask me anything about it!</p>
            </div>
          ) : (
            messages.map((message) => <ChatMessage key={message.id} message={message} />)
          )}
          <div ref={messagesEndRef} />
        </div>

        <ChatInput onSendMessage={handleSendMessage} onUploadImage={handleUploadImage} isProcessing={isProcessing} />
      </div>
    </div>
  )
}
