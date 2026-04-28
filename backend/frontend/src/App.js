import React, { useState } from "react";
import axios from "axios";

function App() {
  const [name, setName] = useState("");
  const [age, setAge] = useState("");
  const [symptoms, setSymptoms] = useState("");
  const [result, setResult] = useState(null);

  const BACKEND_URL = "https://mediguide-wgwx.onrender.com";

  const analyze = async () => {
    try {
      const res = await axios.post(`${BACKEND_URL}/analyze`, {
        name,
        age: parseInt(age),
        symptoms
      });

      setResult(res.data);
    } catch (err) {
      setResult({ error: "Error connecting to backend" });
    }
  };

  return (
    <div style={{ textAlign: "center", marginTop: "40px" }}>
      <h1>ENT AI Clinic Assistant 🏥</h1>

      <input
        placeholder="Name"
        onChange={(e) => setName(e.target.value)}
      /><br /><br />

      <input
        placeholder="Age"
        onChange={(e) => setAge(e.target.value)}
      /><br /><br />

      <textarea
        placeholder="Enter symptoms (e.g. ear pain, snoring)"
        onChange={(e) => setSymptoms(e.target.value)}
      /><br /><br />

      <button onClick={analyze}>Analyze Symptoms</button>

      {result && (
        <div style={{ marginTop: "20px" }}>
          {result.error ? (
            <p>{result.error}</p>
          ) : (
            <>
              <h3>Diagnosis: {result.diagnosis}</h3>
              <p><b>Advice:</b> {result.advice}</p>
              <p><b>Urgency:</b> {result.urgency}</p>

              <a
                href="https://wa.me/919811387746"
                target="_blank"
                rel="noreferrer"
              >
                <button>📲 Book via WhatsApp</button>
              </a>
            </>
          )}
        </div>
      )}
    </div>
  );
}

export default App;