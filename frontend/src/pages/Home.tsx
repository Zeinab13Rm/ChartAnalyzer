import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { appService } from '../services/api';
// import { authService } from '../services/api';
import '../styles/home.css';

export const Home = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [serverStatus, setServerStatus] = useState<'loading' | 'online' | 'offline'>('loading');
  const [userData, setUserData] = useState<{ username: string } | null>(null);
  const [featureCards] = useState([
    {
      title: "Chart Analysis",
      description: "Upload and analyze your charts with our powerful tools",
      path: "/charts/analyze",
    },
    {
      title: "Ask Questions",
      description: "Get insights about your data by asking natural language questions",
      path: "/charts/ask", 
    },
  ]);

  useEffect(() => {
    // Check if user is authenticated
    const token = localStorage.getItem('token');
    setIsAuthenticated(!!token);

    // Fetch server status
    const checkServerStatus = async () => {
      try {
        await appService.getRoot();
        setServerStatus('online');
      } catch (error) {
        setServerStatus('offline');
      }
    };

    checkServerStatus();

    // If authenticated, fetch user data
    if (token) {
      const fetchUserData = async () => {
        try {
          // Assuming you have an endpoint to get current user
          // const response = await authService.getCurrentUser();
          // setUserData(response.data);
          // For now, just get username from token or local storage
          setUserData({ username: localStorage.getItem('username') || 'User' });
        } catch (error) {
          console.error('Failed to fetch user data:', error);
        }
      };

      fetchUserData();
    }
  }, []);

  const handleLogout = async () => {
    try {
      // Optional: Call logout endpoint if you have one
      // await authService.logout();
      localStorage.removeItem('token');
      localStorage.removeItem('username');
      setIsAuthenticated(false);
      setUserData(null);
    } catch (error) {
      console.error('Logout failed:', error);
    }
  };

  return (
    <div className="home-container">
      <header className="home-header">
        <div className="server-status">
          Server Status: 
          <span className={`status-indicator ${serverStatus}`}>
            {serverStatus.toUpperCase()}
          </span>
        </div>
        
        <nav className="auth-nav">
          {isAuthenticated ? (
            <div className="user-section">
              <span>Welcome, {userData?.username}</span>
              <button onClick={handleLogout} className="logout-button">
                Logout
              </button>
            </div>
          ) : (
            <>
              <Link to="/auth/login" className="auth-link">
                Login
              </Link>
              <Link to="/auth/register" className="auth-link">
                Register
              </Link>
            </>
          )}
        </nav>
      </header>

      <main className="home-main">
        <section className="hero-section">
          <h1>Data Visualization & Analysis Platform</h1>
          <p>
            Transform your data into insights with our powerful chart analysis tools
            and AI-powered question answering system.
          </p>
        </section>

        <section className="features-section">
          <h2>Key Features</h2>
          <div className="feature-cards">
            {featureCards.map((feature, index) => (
              <div key={index} className="feature-card">
                <h3>{feature.title}</h3>
                <p>{feature.description}</p>
                <Link to={feature.path} className="feature-link">
                  Try it out →
                </Link>
              </div>
            ))}
          </div>
        </section>

        {!isAuthenticated && (
          <section className="cta-section">
            <h2>Ready to get started?</h2>
            <div className="cta-buttons">
              <Link to="/auth/register" className="cta-button primary">
                Create Account
              </Link>
              <Link to="/auth/login" className="cta-button secondary">
                Login
              </Link>
            </div>
          </section>
        )}
      </main>

      <footer className="home-footer">
        <p>© {new Date().getFullYear()} Data Analysis Platform. All rights reserved.</p>
      </footer>
    </div>
  );
};