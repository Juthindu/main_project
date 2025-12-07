import React from "react";

export default function Sidebar() {
  return (
    <div style={{
      width: "220px",
      height: "100vh",
      background: "#222",
      color: "#fff",
      padding: "20px",
      position: "fixed",
      left: 0,
      top: 0
    }}>
      <h2>Menu</h2>
      <ul>
        <li>Dashboard</li>
        <li>Users</li>
        <li>Reports</li>
      </ul>
    </div>
  );
}
