import { useState } from "react";
import { useNavigate } from "react-router-dom";

const API_URL = "http://localhost:8000/";

const Login = () => {
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");
  const navigation = useNavigate();

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
      if (data.error) {
        window.alert(data.error.message);
        console.log(data.error + "error");
      } else {
        localStorage.setItem("token", data.token);
        window.alert("Login success");
        navigation("/dashboard");
        console.log(data + "success");
      }
    } catch (error) {
      console.log(error);
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
        <button type="submit">Login</button>
        <a href="/">Register</a>
      </form>
    </>
  );
};

export default Login;
