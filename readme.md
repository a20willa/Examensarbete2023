# Thesis Project 2023
This is my thesis project where MongoDB and MySQL query times will be compared using geospatial data. 

This README file will explain how to setup the project and start testing.

## Databases
You need to have both a MongoDB and MySQL database up and running. You also need to configure the `.env` file to use the correct values to connect to your databases. The values are by default configured for local databases, as the testing will be on the same computer in this thesis. 

## Generating data
Firstly, install all dependencies:
```
pip install -r requirements.txt
```

Data can thne be generated using the python scripts inside the `generator` folder. Inside there is a folder for MongoDB and MySQL seperately, which each conatins a `main.py` script. This script uses command line arguments to control how the outputed data is generated:

```
Usage: python src/generator/<mysql | mongodb>/main.py [OPTIONS]

Options:
-a, --amount INTEGER: Number of geometries to generate (default: 1)
-t, --type TEXT: Type of geometry to generate, must be one of 'point', 'multipoint', 'linestring', 'multilinestring', 'polygon' or 'multipolygon' (default: 'point')
-p, --points INTEGER: The amount of points to generate for a linestring or polygon (default: 4, minimum: 4)
-i, --instances INTEGER: The amount of instances of geometries to add in a collection type (default: 1)
-s, --seed INTEGER: The seed used when generating
-h, --help: Displays this text

Example usage:
python src/generator/mysql/main.py --amount 10 --type linestring --points 10 --seed 200
python src/generator/mongodb/main.py --amount 10 --type multilinestring --points 10 --instances 10 --seed 200
```

### Values for testing
These are the values which will be used to generate and insert data into both MySQL and MongoDB. Note that the `--type` parameter will be changed between tests.

#### Pilot Study
The pilot study uses the following query:
```
python3 src/generator/mysql/main.py --amount 100 --type linestring --points 20 --seed 200
```
#### Real Tests
The real tests uses the following query:
```
python3 src/generator/mysql/main.py --amount 1000 --type linestring --points 20 --seed 200
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