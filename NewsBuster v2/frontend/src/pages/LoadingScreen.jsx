import React, { useEffect, useRef, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import axios from "axios";
import styles from "./modules/LoadingScreen.module.css";
import "ldrs/ring";

const LoadingScreen = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const hasFetched = useRef(false);

  useEffect(() => {
    console.log("Location state:", location.state); // Debug log

    if (!location.state || hasFetched.current) return;
    hasFetched.current = true;

    const fetchData = async () => {
      try {
        const response = await axios.post(
          "http://localhost:8080/api/link",
          { link: location.state.link },
          {
            headers: {
              "Content-Type": "application/json",
            },
          },
        );

        if (response.data.status === "success") {
          navigate("/article", { state: response.data });
        } else {
          setError(response.data.message || "Failed to fetch article");
          setLoading(false);
        }
      } catch (error) {
        console.error("Error fetching the article:", error);
        setError("Error fetching the article");
        setLoading(false);
      }
    };

    fetchData();
  }, [location.state, navigate]);

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
