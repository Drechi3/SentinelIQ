import React from "react";

export default function GraphView({ edges }) {
  console.log("GRAPH EDGES:", edges);

  if (!edges || edges.length === 0) {
    return (
      <div style={{ color: "#aaa", marginTop: 20 }}>
        No graph data yet — run scan
      </div>
    );
  }

  return (
    <div style={{ marginTop: 20, padding: 20, background: "#111827", borderRadius: 10 }}>
      <h3>Attack Graph</h3>

      {edges.map((e, i) => (
        <div key={i} style={{ marginBottom: 8 }}>
          <span style={{ color: "#00ffd5" }}>{e.source}</span>
          {" → "}
          <span style={{ color: "#ff9500" }}>{e.target}</span>
          {"  | risk: " + e.risk}
        </div>
      ))}
    </div>
  );
}