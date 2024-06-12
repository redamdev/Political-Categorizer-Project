import React from "react";
import styles from "./modules/PreviewCard.module.css";

function PreviewCard({ article, onReadMore }) {
  const logoUrl = `https://logo.clearbit.com/${new URL(article.publisher).hostname}`;
  const styleCard =
    article.label === "left" ? styles.leftCard : styles.rightCard;
  return (
    <div className={styles.card}>
      <div className={styleCard}>
        <h2 className={styles.title}>{article.title}</h2>
        <p className={styles.label}>
          <strong>{article.label} LEANING BIAS</strong>
        </p>
        <p className={styles.date}>
          <strong>Date:</strong> {article.date}
        </p>
        <div className={styles.publisher}>
          <img
            src={logoUrl}
            alt={`${article.publisher} logo`}
            className={styles.logo}
          />
          <a href={article.publisher} target="_blank" rel="noopener noreferrer">
            {article.publisher}
          </a>
        </div>
        <p className={styles.body}>{article.body.substring(0, 100)}...</p>
        <button className={styles.button} onClick={() => onReadMore(article)}>
          Read more
        </button>
      </div>
    </div>
  );
}

export default PreviewCard;
