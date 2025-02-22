import { useState } from "react";
import { useNavigate } from "react-router-dom";

const API_URL = "http://localhost:8000/";

const Login = () => {
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch(`${API_URL}login`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username: name, password }),
      });

      const data = await res.json();

      if (res.status !== 200) {
        window.alert(data.error);
        console.log("Login error:", data.error);
      } else {
        localStorage.setItem("token", data.access_token); // Store token correctly
        window.alert("Login successful");
        navigate("/dashboard");
        console.log("Login success:", data);
      }
    } catch (error) {
      console.log("Request failed:", error);
    }
  };

  return (
    <>
      <h1>Login</h1>
      <form onSubmit={handleSubmit}>
        <label>Name</label>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <label>Password</label>
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit">Login</button>
        <a href="/">Register</a>
      </form>
    </>
  );
};

export default Login;
