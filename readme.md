# Thesis Project 2023
This is my thesis project where MongoDB and MySQL query times will be compared using geospatial data. 

This README file will explain how to setup the project and start testing.

## NodeJS
This project uses NodeJS as the server to host the application and the databases. Therefore, it will need to be installed. After installing NodeJS, open a terminal and cd to the root folder of this respotory, then install dependencies using:
```
> npm i
```

Then, build the application using:
```
> npm run build
```

You are now ready to start the servers. You can either start MySQL or MongoDB using the follwing commands:

```
MySQL

> npm run start:mysql

MongoDB

> npm run start:mongodb
```