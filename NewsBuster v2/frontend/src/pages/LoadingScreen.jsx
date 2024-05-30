import React, { useEffect, useState } from 'react';
import { useLocation, useNavigate, Link } from 'react-router-dom';  // Make sure Link is imported
import axios from 'axios';
import styles from './modules/LoadingScreen.module.css';
import 'ldrs/ring';




const LoadingScreen = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {

        // Simulate an API call with a delay
        await new Promise((resolve) => setTimeout(resolve, 3000));

        // Send the link to the backend
        const response = await axios.post('http://localhost:8080/api/link', { link: location.state.link }, {
          headers: {
            'Content-Type': 'application/json'
          }
        });

        if (response.data.status === 'success') {
          // Navigate to the article page with the article data
          navigate('/article', { state: response.data });
        } else {
          // Handle failure response
          setError(response.data.message || 'Failed to fetch article');
          setLoading(false);
        }
      } catch (error) {
        console.error('Error fetching the article:', error);
        setError('Error fetching the article');
        setLoading(false); // Set loading to false if there's an error
      }
    };

    fetchData();
  }, [location.state.link, navigate]);

  return (
    <div className={styles.LoadingScreen}>
      {loading ? (
        <div>
          <p>Loading...</p>
          <l-ring
            size="80"
            stroke="5"
            bg-opacity="0"
            speed="2"
            color="black"
          ></l-ring>
        </div>
      ) : error ? (
        <div className={styles.Error}>
          <p>Error: {error}</p>
        </div>
      ) : (
        <p>Redirecting...</p>
      )}
    </div>
  );
};

export default LoadingScreen;
