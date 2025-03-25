import logo from './logo.svg';
import './App.css';
import React, { useState, useEffect } from "react";
import PredictionChart from "./components/PredictionChart";

const App = () => {
  // Simulated failure contribution percentages
  const [failureData, setFailureData] = useState([60, 25, 15]);

  useEffect(() => {
    // Simulate real-time updates every 5 seconds
    const interval = setInterval(() => {
      setFailureData([
        Math.floor(Math.random() * 100),
        Math.floor(Math.random() * 100),
        Math.floor(Math.random() * 100),
      ]);
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ width: "500px", margin: "50px auto", textAlign: "center" }}>
      <h1>Machine Failure Prediction</h1>
      <PredictionChart data={failureData} />
    </div>
  );
};

export default App;
