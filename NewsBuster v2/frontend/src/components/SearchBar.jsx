import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import styles from '../pages/modules/Home.module.css';

function SearchBar() {
  const [link, setLink] = useState('');
  const navigate = useNavigate();

  const handleSubmit = (event) => {
    event.preventDefault();
    navigate('/loadingscreen', { state: { link } });
  };

  return (
    <div className={styles.SearchBar}>
      <form onSubmit={handleSubmit}>
        <label>
          Enter an article:
          <input 
            type="text" 
            value={link} 
            onChange={(e) => setLink(e.target.value)} 
          />
        </label>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default SearchBar;
