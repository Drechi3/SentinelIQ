import React, { useState } from "react";
import EliteGraph from "./EliteGraph";

export default function App() {
  const [path, setPath] = useState("");
  const [data, setData] = useState(null);

  const runScan = async () => {
    const res = await fetch("http://127.0.0.1:8000/scan-code", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ path }),
    });

    const json = await res.json();

    console.log("BACKEND RESPONSE:", json);

    setData(json);
  };

  return (
    <div style={{ padding: 20, background: "#0b0f1c", minHeight: "100vh", color: "#fff" }}>
      <h2>SentinelIQ SOC v4 ELITE</h2>

      <input
        value={path}
        onChange={(e) => setPath(e.target.value)}
        placeholder="Enter project path..."
        style={{ padding: 10, width: "60%" }}
      />

      <button onClick={runScan} style={{ marginLeft: 10, padding: 10 }}>
        RUN SCAN
      </button>

      {/* 🔥 CRITICAL FIX */}
      <EliteGraph data={data} />

      <pre style={{ marginTop: 20, color: "#888" }}>
        {data ? JSON.stringify(data.summary, null, 2) : "No graph data yet — run scan"}
      </pre>
    </div>
  );
}