import React, { useEffect, useState } from "react";
import { collection, getDocs } from "firebase/firestore";
import { db } from "../firebase";
import styles from "./modules/PreviousArticles.module.css";
import { useNavigate } from "react-router-dom";
import PreviewCard from "../components/PreviewCard";

function PreviousArticles() {
  const [articles, setArticles] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchArticles = async () => {
      try {
        const querySnapshot = await getDocs(collection(db, "articles"));
        const articlesData = querySnapshot.docs.map((doc) => ({
          id: doc.id,
          ...doc.data(),
        }));

        const uniqueArticlesMap = new Map();
        articlesData.forEach((article) => {
          if (!uniqueArticlesMap.has(article.title)) {
            uniqueArticlesMap.set(article.title, article);
          }
        });

        const uniqueArticles = Array.from(uniqueArticlesMap.values());
        setArticles(uniqueArticles);
      } catch (error) {
        console.error("Error fetching articles:", error);
      }
    };

    fetchArticles();
  }, []);

  const handleReadMore = (article) => {
    navigate("/article", { state: article });
  };

  return (
    <div className={styles.container}>
      <h1 className={styles.header}>Previous Articles</h1>
      <div className={styles.articleList}>
        {articles.map((article) => (
          <PreviewCard
            key={article.id}
            article={article}
            onReadMore={handleReadMore}
          />
        ))}
      </div>
    </div>
  );
}

export default PreviousArticles;
