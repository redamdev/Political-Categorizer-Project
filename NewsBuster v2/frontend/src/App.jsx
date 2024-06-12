import React from "react";
import LoadingScreen from "./pages/LoadingScreen";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import Article from "./pages/Article";
import Navbar from "./components/Navbar";
import PreviousArticles from "./pages/PreviousArticles";

function App() {
  return (
    <>
      <Navbar />
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/loadingscreen" element={<LoadingScreen />} />
          <Route path="/article" element={<Article />} />
          <Route path="/previousarticles" element={<PreviousArticles />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
