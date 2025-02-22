import { useEffect } from "react";
import { useState } from "react";

const API_URL = "http://localhost:8000/";

const Dasjboard = () => {
  const [name, setName] = useState([]);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const res = await fetch(`${API_URL}`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        });

        const data = await res.json();
        console.log(data);
        setName(data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchUsers();
  }, []);

  return (
    <div>
      <h1>Dasjboard</h1>
      <ul>
        {name.map((item) => (
          <li key={item._id}>
            <h2>{item.username}</h2>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Dasjboard;
