import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./login";
import Reg from "./resister";
import Dasjboard from "./Dasjboard";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Reg />} />
        <Route path="/login" element={<Login />} />
        <Route path="/dashboard" element={<Dasjboard />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
