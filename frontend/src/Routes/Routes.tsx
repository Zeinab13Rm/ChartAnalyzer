import { createBrowserRouter } from 'react-router-dom';
import { Login } from '../pages/Auth/Login';
import { Register } from '../pages/Auth/Register';
import { AskQuestion } from '../pages/Charts/AskQuestion';
import { AnalyzeChart } from '../pages/Charts/AnalyzeChart';
import { Home } from '../pages/Home';
import { ChatInterface } from '../components/ChatInteface';

export const router = createBrowserRouter([
  {
    path: '/',
    element: <Home />,
  },
  {
    path: '/auth/login',
    element: <Login />,
  },
  {
    path: '/auth/register',
    element: <Register />,
  },
  {
    path: '/charts/ask',
    element: <AskQuestion />,
  },
  {
    path: '/charts/analyze',
    element: <AnalyzeChart />,
  },
  {
  path: '/charts/chat',
  element: <ChatInterface />,
  },
]);