import React from 'react';
import { useLocation } from 'react-router-dom';
import styles from './modules/Article.module.css';
import { Link } from 'react-router-dom';

function Article() {
  const location = useLocation();
  const { title, date, publisher, body } = location.state;

  return (
    <div className={styles.Article}>
      <h1>{title}</h1>
      <p><strong>Date:</strong> {date}</p>
      <p><strong>Publisher:</strong> {publisher}</p>
      <p>{body}</p>
    </div>
  );
};

export default Article;
