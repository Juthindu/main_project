import { useState } from "react";

function App() {
  const [username, setU] = useState("");
  const [password, setP] = useState("");

  // -----------------------------
  // STEP 1: LOGIN -> get tokens
  // -----------------------------
  const handleLogin = async (e) => {
    e.preventDefault();

    const res = await fetch("http://127.0.0.1:8000/api/token/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password }),
    });

    const data = await res.json();
    console.log("Login Response:", data);

    if (!res.ok) {
      alert("Invalid login");
      return;
    }

    // Save tokens
    localStorage.setItem("access", data.access);
    localStorage.setItem("refresh", data.refresh);

    // Save initial role + username from token
    localStorage.setItem("username", data.username);
    localStorage.setItem("role", data.role);

    // Now load full user profile + permissions
    await loadUserData();

    alert("Login success!");
  };

  // ----------------------------------------
  // STEP 2: FETCH USER / PERMISSIONS ( /api/me/ )
  // ----------------------------------------
  const loadUserData = async () => {
    const access = localStorage.getItem("access");

    const res = await fetch("http://127.0.0.1:8000/api/me/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${access}`,
      },
    });

    const data = await res.json();
    console.log("Me Response:", data);

    if (res.ok) {
      // Save updated data
      localStorage.setItem("username", data.username);
      localStorage.setItem("role", data.role);
      localStorage.setItem("permissions", JSON.stringify(data.permissions));
    } else {
      alert("Failed to load user info");
    }
  };

  return (
    <form onSubmit={handleLogin}>
      <input
        value={username}
        onChange={(e) => setU(e.target.value)}
        placeholder="Username"
      />
      <input
        type="password"
        value={password}
        onChange={(e) => setP(e.target.value)}
        placeholder="Password"
      />
      <button type="submit">Login</button>
    </form>
  );
}

export default App;
