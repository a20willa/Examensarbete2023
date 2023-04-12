import { connection_strings_mongodb } from '../connection_strings';
import * as dotenv from 'dotenv'
dotenv.config()
import { MongoClient } from 'mongodb';
import express_mongodb from 'express';
import cors_mongodb from 'cors';
const app_mongodb = express_mongodb()
const data_mongodb: connection_strings_mongodb = {
  host: process.env.mongodb_host as string ?? "mongodb://localhost:27017",
  database: process.env.mongodb_database! as string ?? "mongodb_database",
  collection_name: process.env.mongodb_collection_name as string ?? "spatial_data_testing"
}

// Global variables for MongoDB
let db: any;
let dbo: any;

// Create MongoDB client
const client = new MongoClient(data_mongodb.host, {})

// Use CORS to fetch via javascript
app_mongodb.use(cors_mongodb());

// Add static folder location
app_mongodb.use(express_mongodb.static('src/page'))

async function connectToDatabase() {
  // Connect the client to the server (optional starting in v4.7)
  db = await client.connect();
  dbo = db.db(String(data_mongodb.database));
}

// Dummy endpoint
app_mongodb.get('/getAllMongodb', (req: any, res: any) => {
  // Establish and verify connection
  const cursor = dbo.collection(String(data_mongodb.collection_name)).find({
    loc: {
      $near: {
        $geometry: {
          type: "Point",
          coordinates: [-83.5163830345708, 50.646429997753756]
        },
      }
    }
  });

  cursor.toArray((err: any, result: any) => {
    if (err) {
      console.error(err);
      return res.send({ response: "err" });
    }
    res.send({ response: result });
  });
});

app_mongodb.get('/closeConnection', (req: any, res: any) => {
    client.close();
    res.send({ response: "Connection closed" });
})


// Listen to port 3000
app_mongodb.listen("3000", () => {
  console.log("Server started at http://localhost:3000")
})

connectToDatabase()