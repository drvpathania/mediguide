import { useEffect, useState } from "react";
import axios from "axios";

const API = "https://mediguide-wgwx.onrender.com";

function App() {
  const [result, setResult] = useState("");

  const login = async () => {
    try {
      const res = await axios.post(`${API}/login`, {
        username: "test",
        password: "1234",
      });
      setResult(res.data.message || JSON.stringify(res.data));
    } catch (err) {
      console.error(err);
      setResult("Error connecting to backend");
    }
  };

  useEffect(() => {
    login();
  }, []);

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>Mediguide App Running ✅</h1>
      <p>{result}</p>
      <button onClick={login}>Test Login</button>
    </div>
  );
}

export default App;