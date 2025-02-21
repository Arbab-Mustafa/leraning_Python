import { useEffect, useState } from "react";

const API_URL = "http://localhost:8000/";

function App() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [items, setItems] = useState([]);

  const fetchRes = async () => {
    try {
      const res = await fetch(`${API_URL}getusers`);
      const json = await res.json();
      console.log("Data fetched:", json);

      setItems(json.data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };
  useEffect(() => {
    fetchRes();
  }, []);
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch(`${API_URL}adduser`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ name, email }),
      });
      const json = await res.json();
      console.log("Data posted:", json);
      fetchRes();
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  const handleDelete = async (id) => {
    try {
      const res = await fetch(`${API_URL}deleteUser/${id}`, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ id }),
      });

      const json = await res.json();
      console.log("Data deleted:", json);
      fetchRes();
    } catch (error) {
      console.error("Error deleting data:", error);
    }
  };

  return (
    <>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={name}
          placeholder="Name"
          onChange={(e) => setName(e.target.value)}
        />
        <input
          type="email"
          value={email}
          placeholder="Email"
          onChange={(e) => setEmail(e.target.value)}
        />
        <button type="submit">Submit</button>
      </form>

      <h2>Items:</h2>
      {items?.map((item) => (
        <div key={item._id}>
          <h3>{item.name}</h3>
          <h3>{item.email}</h3>
          <button onClick={() => handleDelete(item._id)}>*</button>
        </div>
      ))}
    </>
  );
}

export default App;
