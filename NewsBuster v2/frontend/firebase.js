import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyC893euNJkE01PP5r4GbUGZ2UUUKihkjHM",
  authDomain: "newsbustr.firebaseapp.com",
  projectId: "newsbustr",
  storageBucket: "newsbustr.appspot.com",
  messagingSenderId: "968689701636",
  appId: "1:968689701636:web:417fac247403f544ae3651",
  measurementId: "G-3HYNMEJEH3",
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

export { db };
