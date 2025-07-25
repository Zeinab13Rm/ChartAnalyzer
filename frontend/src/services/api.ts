import axios from 'axios';


const api = axios.create({
  baseURL: 'http://localhost:8000', // Your FastAPI URL
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  },
  withCredentials: true, // If you need to send cookies
});



export default api;

// Auth services
export const authService = {
  register: (data: { username: string; password: string; email: string }) =>
    api.post('/auth/register', data),
  login: (data: { username: string; password: string }) =>
    api.post('/auth/login', data),
};

// Chart services
export const chartService = {
  AskQuestion: (formData: FormData) => 
    api.post('/charts/ask', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
        'accept': 'application/json',
      },
    }),
  analyzeChart: (formData: FormData) => 
    api.post('/charts/analyze', formData, {
      headers: {
        'accept': 'application/json',
        'Content-Type': 'multipart/form-data',
      },
    }),
};

// General services
export const appService = {
  getRoot: () => api.get('/'),
};