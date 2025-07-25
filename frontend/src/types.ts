export type MessageType = {
  id: string;
  content: string;
  sender: 'user' | 'bot';
  type: 'text' | 'image';
  timestamp: Date;
};