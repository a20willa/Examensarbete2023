const {MongoClient} = require('mongodb');
const express_mongodb = require('express')
const cors_mongodb = require('cors');
const app_mongodb = express_mongodb()
const port_mongodb = 3000
const uri_mongodb = "mongodb://127.0.0.1:27017";

// Create MongoDB client
const client = new MongoClient(uri_mongodb)

// Use CORS to fetch via javascript
app_mongodb.use(cors_mongodb());
// Add static folder location
app_mongodb.use(express_mongodb.static('src/page'))

// Dummy endpoint
app_mongodb.get('/getAllMongodb', async (req: any, res: any) => {
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
app_mongodb.listen(port_mongodb, () => {
  console.log("Server started")
})