import type { MessageType } from '../types';

export const ChatMessage = ({ message }: { message: MessageType }) => {
  return (
    <div className={`chat-message ${message.sender}`}>
      <div className="message-content">
        {message.type === 'text' && (
          <p>{message.content}</p>
        )}
        {message.type === 'image' && (
          <img src={message.content} alt="Uploaded chart" className="chat-image" />
        )}
      </div>
      <div className="message-time">
        {new Date(message.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
      </div>
    </div>
  );
};