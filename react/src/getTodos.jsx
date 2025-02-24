import { useEffect, useState } from "react";

const API_URL = "http://localhost:8000/gettodos";

const GetTodos = () => {
  const [todos, setTodos] = useState([]);
  useEffect(() => {
    const fetchTodos = async () => {
      const token = localStorage.getItem("token");

      try {
        const response = await fetch(API_URL, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
          },
        });

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json(); // Parse JSON response
        console.log(data);
        setTodos(data);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchTodos(); // Call the async function inside useEffect
  }, []);

  return (
    <div>
      <h2>All Todos</h2>
      <div>
        {todos.map((todo, i) => (
          <div key={todo.id}>
            <span>{1 + i}</span>
            <h3>{todo.title}</h3>
            <span>{todo.description}</span>
            <span>{todo.completed ? "Completed" : "Not Completed"}</span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default GetTodos;
