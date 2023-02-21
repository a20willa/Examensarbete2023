const mysql = require('mysql')
const express = require('express')
const cors = require('cors');
const app = express()
const port = 3000

// Create MySQL connection
const connection = mysql.createConnection({
  host: '127.0.0.1',
  user: 'someuser',
  password: 'somepass',
  database: 'testing_db',
  port: '3306'
})
connection.connect()

// Use CORS to fetch via javascript
app.use(cors());

// Send the results
function getRows(req, res) {
  // Make some MySQL queries
  connection.query('SELECT 1 + 1 AS solution', (err, result) => {
    if (err) throw err;
    res.send(`The solution is: ${result[0].solution}`);
  });
}

// Dummy endpoint
app.get('/getAll', getRows)

// Listen to port 3000
app.listen(port, () => {
  console.log("Server started")
})