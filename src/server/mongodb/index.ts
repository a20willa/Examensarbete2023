import { connection_strings_mongodb } from '../connection_strings';
import * as dotenv from 'dotenv'
dotenv.config()
import { MongoClient } from 'mongodb';
import express_mongodb from 'express';
import cors_mongodb from 'cors';
const app_mongodb = express_mongodb()
const data_mongodb: connection_strings_mongodb = {
  host: process.env.mongodb_host! as string,
  database: process.env.mongodb_database! as string,
  collection_name: process.env.mongodb_collection_name! as string
}

// Create MongoDB client
const client = new MongoClient(data_mongodb.host)

// Use CORS to fetch via javascript
app_mongodb.use(cors_mongodb());

// Add static folder location
app_mongodb.use(express_mongodb.static('src/page'))

// Dummy endpoint
app_mongodb.get('/getAllMongodb', async (req: any, res: any) => {
  try {
    // Connect the client to the server (optional starting in v4.7)
    const db = await client.connect();
    var dbo = db.db(String(data_mongodb.database));
    
    // Establish and verify connection
    const cursor = dbo.collection(String(data_mongodb.collection_name)).find()
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