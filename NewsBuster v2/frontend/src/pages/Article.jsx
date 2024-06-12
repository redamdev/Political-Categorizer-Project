import React, { useEffect, useRef } from "react";
import { useLocation } from "react-router-dom";
import styles from "./modules/Article.module.css";
import { db } from "../firebase";
import { addDoc, collection, query, where, getDocs } from "firebase/firestore";

function Article() {
  const location = useLocation();
  const { title, date, publisher, body, label } = location.state || {};
  const hasSaved = useRef(false);
  const styleLabel = label === "left" ? styles.leftLabel : styles.rightLabel;
  const logoUrl = `https://logo.clearbit.com/${new URL(publisher).hostname}`;

  useEffect(() => {
    if (!location.state || hasSaved.current) return;

    const saveToDatabase = async (state) => {
      try {
        const q = query(
          collection(db, "articles"),
          where("title", "==", state.title),
          where("date", "==", state.date),
        );
        const querySnapshot = await getDocs(q);

        if (querySnapshot.empty) {
          const docRef = await addDoc(collection(db, "articles"), state);
          console.log("Document written with ID: ", docRef.id);
          hasSaved.current = true; // Mark as saved to prevent re-saving
        } else {
          console.log("Document already exists, not adding to the database.");
        }
      } catch (e) {
        console.error("Error adding document: ", e);
      }
    };

    saveToDatabase(location.state);
  }, [location.state]);

  return (
    <div className={styleLabel}>
      <div className={styles.Article}>
        <img src={logoUrl} alt={`${publisher} logo`} className={styles.logo} />
        <h2 className={styles.label}>
          <strong>{label} LEANING BIAS</strong>
        </h2>

        <h1 className={styles.title}>{title}</h1>

        <p className={styles.date}>{date}</p>
        <div
          className={styles.body}
          dangerouslySetInnerHTML={{ __html: body }}
        />
      </div>
    </div>
  );
}

export default Article;
