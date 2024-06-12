import React from "react";
import styles from "./modules/Navbar.module.css";

function Navbar() {
  return (
    <nav className={styles.Navbar}>
      <ul>
        <li>
          <a href="/">Submit Articles</a>
        </li>
        <li>
          <a href="/previousarticles">Previous Articles</a>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;
