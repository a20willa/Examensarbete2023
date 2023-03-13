# Thesis Project 2023
This is my thesis project where MongoDB and MySQL query times will be compared using geospatial data. 

This README file will explain how to setup the project and start testing.

## Databases
You need to have both a MongoDB and MySQL database up and running. 

## Generating data
Data can be generated using the python scripts inside the `generator` folder. Inside there is a folder for MongoDB and MySQL seperately, which each conatins a `main.py` script. This script uses command line arguments to control how the outputed data is generated:

```
Usage: python main.py [OPTIONS]

Options:
-a, --amount INTEGER: Number of geometries to generate (default: 1)
-t, --type TEXT [REQUIRED]: Type of geometry to generate, must be one of 'point', 'linestring', or 'polygon'
-h, --help: Displays this text
-p, --points INTEGER: The amount of points to generate for a linestring or polygon (default: 4, minimum: 4)

Example usage:
python main.py --amount 10 --type linestring --points 10
```



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