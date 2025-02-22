import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

const API_URL = "http://localhost:8000/";

const Me = () => {
  const [user, setUser] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchUser = async () => {
      const token = localStorage.getItem("token");
      if (!token) {
        console.log("No token found, redirecting to login...");
        navigate("/login");
        return;
      }

      try {
        const res = await fetch(`${API_URL}me`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`, // ✅ Include Token in Header
          },
        });

        if (!res.ok) {
          throw new Error(`HTTP error! Status: ${res.status}`);
        }

        const data = await res.json();
        setUser(data);
      } catch (error) {
        console.error("Error fetching user:", error);
        localStorage.removeItem("token"); // Clear invalid token
        // Redirect to login
      }
    };

    fetchUser();
  }, [navigate]);

  return (
    <div>
      {user ? <h2>Welcome, {user.username}!</h2> : <p>Loading user data...</p>}
    </div>
  );
};

export default Me;
