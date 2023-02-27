"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
const { MongoClient } = require('mongodb');
const express = require('express');
const cors = require('cors');
const app = express();
const port = 3000;
const uri = "mongodb://127.0.0.1:27017";
// Create MongoDB client
const client = new MongoClient(uri);
// Use CORS to fetch via javascript
app.use(cors());
// Add static folder location
app.use(express.static('src/page'));
// Dummy endpoint
app.get('/getAll', (req, res) => __awaiter(void 0, void 0, void 0, function* () {
    try {
        // Connect the client to the server (optional starting in v4.7)
        yield client.connect();
        // Establish and verify connection
        yield client.db("admin").command({ ping: 1 });
        res.send({
            "response": "Ping Successfull"
        });
    }
    finally {
        // Ensures that the client will close when you finish/error
        yield client.close();
    }
}));
// Listen to port 3000
app.listen(port, () => {
    console.log("Server started");
});
//# sourceMappingURL=server.js.map