import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";

// Firebase Config Here
// const firebaseConfig = {};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

export { db };
