import { useRef, useState } from 'react';

export const ChatInput = ({
  onSendMessage,
  onUploadImage,
  isProcessing,
}: {
  onSendMessage: (text: string) => void;
  onUploadImage: (file: File) => void;
  isProcessing: boolean;
}) => {
  const [message, setMessage] = useState('');
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (message.trim() && !isProcessing) {
      onSendMessage(message);
      setMessage('');
    }
  };

  const handleImageUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      onUploadImage(e.target.files[0]);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="chat-input-container">
      <button
        type="button"
        onClick={() => fileInputRef.current?.click()}
        className="upload-button"
        disabled={isProcessing}
      >
        📎
      </button>
      <input
        type="file"
        ref={fileInputRef}
        onChange={handleImageUpload}
        accept="image/*"
        className="file-input"
      />
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Ask about the chart..."
        className="message-input"
        disabled={isProcessing}
      />
      <button type="submit" className="send-button" disabled={!message.trim() || isProcessing}>
        {isProcessing ? '⏳' : '➤'}
      </button>
    </form>
  );
};