const {MongoClient} = require('mongodb');
const express = require('express')
const cors = require('cors');
const app = express()
const port = 3000
const uri = "mongodb://127.0.0.1:27017";

// Create MongoDB client
const client = new MongoClient(uri)

// Use CORS to fetch via javascript
app.use(cors());

// Dummy endpoint
app.get('/getAll', async (req, res) => {
  try {
    // Connect the client to the server (optional starting in v4.7)
    await client.connect();
    // Establish and verify connection
    await client.db("admin").command({ ping: 1 });
    console.log("Connected successfully to server");
  } finally {
    // Ensures that the client will close when you finish/error
    await client.close();
  }
})

// Listen to port 3000
app.listen(port, () => {
  console.log("Server started")
})