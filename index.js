
import React, { useState } from "react";
import ReactDOM from "react-dom/client";

function App() {
  const [cars, setCars] = useState([]);

  const fetchCars = async () => {
    const res = await fetch("http://localhost:8000/api/cars", {
      headers: { Authorization: "Bearer test" }
    });
    const data = await res.json();
    setCars(data);
  };

  return (
    <div>
      <h1>Auto Ads</h1>
      <button onClick={fetchCars}>Load Cars</button>
      <ul>
        {cars.map((c, i) => (
          <li key={i}>
            {c.brand} {c.model} {c.year} — {c.price}
          </li>
        ))}
      </ul>
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
