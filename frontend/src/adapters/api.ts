import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Auth services
export const authService = {
  register: (data: { username: string; password: string; email: string }) =>
    api.post('/auth/register', data),
  login: (data: { username: string; password: string }) =>
    api.post('/auth/login', data),
};

// Chart services
export const chartService = {
  askAboutChart: (data: { chartId: string; question: string }) =>
    api.post('/charts/ask', data),
  analyzeChart: (data: { chartData: any }) =>
    api.post('/charts/analyze', data),
};

// General services
export const appService = {
  getRoot: () => api.get('/'),
};