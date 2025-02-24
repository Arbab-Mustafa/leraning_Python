//
import { useState } from "react";
import GetTodos from "./getTodos";
const API_URL = "http://127.0.0.1:8000/addtodo";
const TodoForm = () => {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [completed, setCompleted] = useState(false);
  const token = localStorage.getItem("token");

  const handleSubmit = (e) => {
    e.preventDefault();

    try {
      const response = fetch(API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          title,
          description,
          completed,
        }),
      }).then((res) => {
        console.log(res);
        console.log("Todo Added Successfully");
      });

      setTitle("");
      setDescription("");
      setCompleted(false);
      console.log(response);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h2>Todo Form</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Title</label>
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
        </div>
        <div>
          <label>Description</label>
          <input
            type="text"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          />
        </div>
        <div>
          <lable>Completed</lable>
          <input
            type="checkbox"
            value={completed}
            onChange={(e) => setCompleted(e.target.value)}
          />
        </div>
        <div>
          <button type="submit">Add</button>
        </div>
      </form>

      <GetTodos />
    </div>
  );
};

export default TodoForm;
