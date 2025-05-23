import styles from "./modules/Home.module.css";
import SearchBar from "../components/SearchBar";

function Home() {
  return (
    <div className={styles.Home}>
      <div className={styles.overlay}></div>
      <div className={styles.content}>
        <h1>NewsBustr</h1>
        <p>Check leading news articles for bias!</p>
        <SearchBar />
      </div>
    </div>
  );
}

export default Home;
