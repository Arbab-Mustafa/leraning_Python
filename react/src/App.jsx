import { useEffect, useState } from "react";

import "./App.css";

const API_URL = "http://localhost:8000/";

function App() {
  const [data, setData] = useState(null);
  const [items, setItems] = useState([]);

  useEffect(() => {
    const fetchRes = async () => {
      try {
        const res = await fetch(API_URL);
        const json = await res.json(); // Convert response to JSON
        setData(json.Hello);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchRes();
  }, []);

  useEffect(() => {
    const fetchRes = async () => {
      try {
        const res = await fetch(`${API_URL}items`);
        const json = await res.json();

        setItems(json.items);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };
    fetchRes();
  }, []);

  return (
    <>
      <h2>Response:</h2>

      <pre>{data}</pre>

      <h2>Items:</h2>
      {items?.map((item) => (
        <div key={item.id || item.name}>
          <h3>{item.name}</h3>
        </div>
      ))}
    </>
  );
}

export default App;
