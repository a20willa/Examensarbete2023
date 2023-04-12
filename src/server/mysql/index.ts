import { connection_strings_mysql } from "../connection_strings"
import * as dotenv from 'dotenv'
dotenv.config()
import mysql from 'mysql'
import express_mysql from 'express'
import cors_mysql from 'cors'
const app_mysql = express_mysql()
const data_mysql: connection_strings_mysql = {
  host: process.env.mysql_host as string ?? "127.0.0.1",
  user: process.env.mysql_user as string ?? "a20willa",
  user_password: process.env.mysql_user_password as string ?? "mysql123",
  database: process.env.mysql_database as string ?? "mysql_database",
  port: process.env.mysql_port! as unknown as number ?? 3306,
  table_name: process.env.mysql_table_name as string ?? "spatial_data_testing",
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
  connection.query(`SELECT * from ${data_mysql.table_name} WHERE ST_Distance(g, ST_GeomFromText('POINT(-83.5163830345708 50.646429997753756)', 4326))`, (err: Error, result: any) => {
    if (err) throw err;
    if (result.length != 0) {
      res.send({ response: result });
    } else {
      res.send({ response: "err" })
    }
  });
}

// Close connection
function closeConnection(req: any, res: any) {
  connection.end();
  res.send({ response: "Connection closed" });
}

// Dummy endpoint
app_mysql.get('/getAllMysql', getRows)
app_mysql.get('/closeConnection', closeConnection)

// Listen to port 3000
app_mysql.listen("3000", () => {
  console.log("Server started at http://localhost:3000")
})