import { connection_strings_mysql } from "../mongodb/connection_strings"
import mysql from 'mysql'
import express_mysql from 'express'
import cors_mysql from 'cors'
const app_mysql = express_mysql()
const port_mysql = 3000;
const data_mysql: connection_strings_mysql = {
  host: "127.0.0.1",
  user: "a20willa",
  user_password: "mysql123",
  database: "mysql_database",
  port: 3306,
  table_name: "spatial_data_testing",
}

// Create MySQL connection
const connection = mysql.createConnection({
  host: data_mysql.host,
  user: data_mysql.user,
  password: data_mysql.user_password,
  database: data_mysql.database,
  port: data_mysql.port
})
connection.connect()

// Use CORS to fetch via javascript
app_mysql.use(cors_mysql());

// Add static folder location
app_mysql.use(express_mysql.static('src/page'))

// Get all rows
function getRows(req: any, res: any) {
  // Run get query
  connection.query(`SELECT * from ${data_mysql.table_name}`, (err: Error, result: any) => {
    if (err) throw err;
    if(result.length != 0) {
      res.send(`Response ${result[0].solution}`);
    } else {
      res.send([])
    }
  });
}

// Dummy endpoint
app_mysql.get('/getAllMysql', getRows)

// Listen to port 3000
app_mysql.listen(port_mysql, () => {
  console.log("Server started at http://localhost:3000")
})