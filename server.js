const express = require("express");

const app = express();
const PORT = 3000;

const FLASK_BACKEND = "http://54.236.51.146:5000";

app.get("/", (req, res) => {
  res.send(`
    <h1>Express Frontend</h1>
    <p>Frontend is successfully running on AWS ECS!</p>
    <a href="${FLASK_BACKEND}">Open Flask Backend</a>
  `);
});

app.listen(PORT, "0.0.0.0", () => {
  console.log(`Express frontend running on port ${PORT}`);
});
