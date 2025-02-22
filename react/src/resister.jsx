import { useState } from "react";
import { useNavigate } from "react-router-dom";

const API_URL = "http://localhost:8000/";

const Reg = () => {
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch(`${API_URL}register`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: name,
          password: password,
        }),
      });

      const data = await res.json();

      if (res.ok) {
        window.alert("Register success");
        console.log("Success:", data);
        navigate("/login");
      } else {
        window.alert(data.error || "Unknown error");
        console.error("Error:", data.error || "Unknown error");
      }
    } catch (error) {
      console.error("Request failed:", error);
    }
  };

  return (
    <>
      <h1>Register</h1>
      <form onSubmit={handleSubmit}>
        <label>Name</label>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <label>password</label>
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit">Register</button>
        <a href="/login">Login</a>
      </form>
    </>
  );
};

export default Reg;
