import React, { useMemo } from "react";

export default function EliteGraph({ data }) {
  const graph = useMemo(() => {
    const edges = data?.attack_graph || [];

    if (!edges.length) return null;

    const nodes = new Map();

    edges.forEach((e) => {
      nodes.set(e.source, true);
      nodes.set(e.target, true);
    });

    const nodeList = Array.from(nodes.keys());

    return { edges, nodeList };
  }, [data]);

  if (!graph) {
    return (
      <div style={{ marginTop: 20, color: "#aaa" }}>
        No graph data yet — run scan
      </div>
    );
  }

  return (
    <div style={{ marginTop: 20 }}>
      <h3>Attack Graph</h3>

      <div style={{ display: "flex", gap: 20 }}>
        {/* NODES */}
        <div style={{ flex: 1 }}>
          <h4>Nodes</h4>
          {graph.nodeList.map((n, i) => (
            <div key={i} style={{ padding: 5, background: "#111", margin: 5 }}>
              {n}
            </div>
          ))}
        </div>

        {/* EDGES */}
        <div style={{ flex: 2 }}>
          <h4>Attack Paths</h4>
          {graph.edges.map((e, i) => (
            <div key={i} style={{ padding: 5, background: "#1a1a2e", margin: 5 }}>
              {e.source} → {e.target} (risk: {e.risk})
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}