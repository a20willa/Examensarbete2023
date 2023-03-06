const fs_mongodb = require('fs')
const data_mongodb = JSON.parse(fs_mongodb.readFileSync("src/server/connection_strings.json", "utf8"))
const { MongoClient } = require('mongodb');
const express_mongodb = require('express')
const cors_mongodb = require('cors');
const app_mongodb = express_mongodb()
const mongodb_host = "mongodb://127.0.0.1:27017";
const port_mongodb = 3000

// Create MongoDB client
const client = new MongoClient(mongodb_host)

// Use CORS to fetch via javascript
app_mongodb.use(cors_mongodb());
// Add static folder location
app_mongodb.use(express_mongodb.static('src/page'))

// Dummy endpoint
app_mongodb.get('/getAllMongodb', async (req: any, res: any) => {
  try {
    // Connect the client to the server (optional starting in v4.7)
    const db = await client.connect();
    var dbo = db.db(String(data_mongodb.mongodb_database));
    // Establish and verify connection
    const cursor = dbo.collection(String(data_mongodb.mongodb_collection_name)).find()
    res.send({
      "response": await cursor.toArray()
    })
  } catch (e) {
    console.log(e)
  } finally {
    // Ensures that the client will close when you finish/error
    await client.close();
  }
})

// Listen to port 3000
app_mongodb.listen("3000", () => {
  console.log("Server started")
})