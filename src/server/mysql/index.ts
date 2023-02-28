const {MongoClient} = require('mongodb');
const express = require('express')
const cors = require('cors');
const app = express()

// Create MongoDB client
const client = new MongoClient(uri)

// Use CORS to fetch via javascript
app.use(cors());
// Add static folder location
app.use(express.static('src/page'))

// Dummy endpoint
app.get('/getAllMysql', async (req: any, res: any) => {
  try {
    // Connect the client to the server (optional starting in v4.7)
    await client.connect();
    // Establish and verify connection
    await client.db("admin").command({ ping: 1 });
    res.send({
      "response": "Ping Successfull"
    })

  } finally {
    // Ensures that the client will close when you finish/error
    await client.close();
  }
})

// Listen to port 3000
app.listen(port, () => {
  console.log("Server started")
})