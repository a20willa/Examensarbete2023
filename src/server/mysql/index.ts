const mysql = require('mysql')
const express_mysql = require('express')
const cors_mysql = require('cors');
const app_mysql = express_mysql()

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
app_mongodb.use(cors_mongodb());

// Send the results
function getRows(res: any) {
  // Make some MySQL queries
  connection.query('SELECT 1 + 1 AS solution', (err: Error, result: any) => {
    if (err) throw err;
    res.send(`The solution is: ${result[0].solution}`);
  });
}

// Dummy endpoint
app_mongodb.get('/getAllMysql', getRows)

// Listen to port 3000
app_mongodb.listen(port_mongodb, () => {
  console.log("Server started")
})