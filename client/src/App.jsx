import { useState, useEffect } from "react";

const API_URL = "http://localhost:8000"; // Your Python backend URL

function App() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await fetch(`${API_URL}/api/users`);
        const result = await res.json();
        console.log("API Response:", result);
        setUsers(result);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };
    fetchData();
  }, []);

  return (
    <div>
      <h1>User List</h1>
      <ul>
        {users.map((user, index) => (
          <li key={user._id}>
            <strong>Name:</strong> {user.name} <br />
            <strong>Email:</strong> {user.email} <br />
            <strong>Course ID:</strong> {user.course}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
