import { useEffect } from "react";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import Me from "./Me";

const API_URL = "http://localhost:8000/";

const Dasjboard = () => {
  const [name, setName] = useState([]);
  const navigation = useNavigate();

  useEffect(() => {
    try {
      const fetchUsers = async () => {
        const res = await fetch(`${API_URL}`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        });

        if (!res.ok) {
          throw new Error("Error fetching users");
        }

        const data = await res.json();
        console.log(data);
        setName(data);
      };

      fetchUsers();
    } catch (error) {
      console.error("Error fetching users:", error);
    }
  }, []);

  useEffect(() => {
    const fetchUsers = async () => {
      const token = localStorage.getItem("token"); // Get token from localStorage

      if (!token) {
        console.log("No token found, redirecting to login...");
        navigation("/login");
        return;
      }

      try {
        const res = await fetch(`${API_URL}me`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`, // ✅ Include Token
          },
        });

        if (!res.ok) {
          const errorData = await res.json();
          throw new Error(errorData.detail || "Unauthorized");
        }

        const data = await res.json();
        console.log(data);
      } catch (error) {
        console.error("Error fetching users:", error);
        localStorage.removeItem("token"); // Remove invalid token
        navigation("/login"); // Redirect to login page
      }
    };

    fetchUsers();
  }, [navigation]);

  const handleLogout = () => {
    localStorage.removeItem("token");
    navigation("/login");

    window.alert("Logout success");
  };

  return (
    <div>
      <h1>Dasjboard</h1>
      <Me />
      <button onClick={handleLogout}>Logout</button>
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
