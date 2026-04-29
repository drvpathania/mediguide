import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./Home";
import AI from "./AI";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/ai" element={<AI />} />
      </Routes>
    </Router>
  );
}

export default App;