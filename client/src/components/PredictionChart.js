import React, { useEffect, useRef } from "react";
import {
  Chart,
  BarElement,
  CategoryScale,
  LinearScale,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

Chart.register(BarElement, CategoryScale, LinearScale, Title, Tooltip, Legend);

const PredictionChart = ({ data }) => {
  const chartRef = useRef(null);
  const chartInstanceRef = useRef(null);

  useEffect(() => {
    if (chartInstanceRef.current) {
      chartInstanceRef.current.destroy(); // Destroy previous chart instance before re-rendering
    }

    const ctx = chartRef.current.getContext("2d");
    chartInstanceRef.current = new Chart(ctx, {
      type: "bar",
      data: {
        labels: ["Temperature", "Pressure", "Humidity"],
        datasets: [
          {
            label: "Failure Contribution (%)",
            data: data,
            backgroundColor: ["red", "yellow", "green"],
            borderColor: ["darkred", "goldenrod", "darkgreen"],
            borderWidth: 1,
          },
        ],
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            display: true,
          },
          title: {
            display: true,
            text: "Sensor Contribution to Machine Failure",
          },
        },
        scales: {
          y: {
            beginAtZero: true,
            max: 100,
          },
        },
      },
    });

    return () => {
      chartInstanceRef.current.destroy();
    };
  }, [data]);

  return <canvas ref={chartRef} />;
};

export default PredictionChart;
