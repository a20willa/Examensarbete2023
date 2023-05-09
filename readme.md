# Thesis Project 2023
This is my thesis project where MongoDB and MySQL query times will be compared using geospatial data. 

This README file will explain how to setup the project and start testing.

## Databases
You need to have both a MongoDB and MySQL database up and running. You also need to configure the `.env` file to use the correct values to connect to your databases. The values are by default configured for local databases, as the testing will be on the same computer in this thesis. If you follow the instruction in the markdown file in the installation folder you should not have to change anything. 

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
-s, --seed INTEGER: The seed used when generating (default: 420)
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
python3 src/generator/mysql/main.py --amount 100 --type linestring --points 20 --instances 5 --seed 200
```

With 100 datapoints and 3 repeats.

The following datatypes will be used in the pilot study:
* Point
* Linestring
* Multilinestring

#### Final Study
The final study uses the following query:
```
python3 src/generator/mysql/main.py --amount 1000 --type linestring --points 20 --instances 5 --seed 200
```

With 1000 datapoints and 3 repeats.

All datatypes will be used in the final study.

## NodeJS
This project uses NodeJS as the server to host the application and the databases. Therefore, it will need to be installed, which can be done with `sudo apt install nodejs`. You also need to have npm, so install it using `sudo apt install npm`. After installing NodeJS and npm, open a terminal and cd to the root folder of this respotory, then install dependencies using:
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

### Running meassurments
The meassurments can now be started by going to [localhost](localhost:3000) in your browser. From there, pick the database which you started the server for (so if you ran `npm run start:mysql`, pick mysql). After that, you can choose how many "itterations" you want to run. This basically means that you run the test `x` amount of times. 

After that, you can get the data using the "Get HAR" Firefox addon, which is explain below. 

## Getting the result data
A custom addon called "Get HAR" has been created to get the fetched data using the developer tools API in firefox. Use this after runnning the tests.

### Installing the "Get HAR" addon

1. Open Firefox and type `about:debugging` in the address bar.

2. On the "about:debugging" page, click on the "This Firefox" menu on the left side of the page.

3. Click on the "Load Temporary Add-on" button. This will open a file dialog.

4. Navigate to the "getHAR" folder in the root folder of this project.

5. Select the `manifest.json` file and click "Open".

## Using the "Get HAR" Add-on

The "Get HAR" add-on adds a button to the developer tools panel in Firefox that allows you to capture the network activity and export it as a HAR file in JSON format. To use the add-on, follow these steps:

1. Open the Firefox developer tools by pressing F12 or by selecting "Web Developer" > "Developer Tools" from the Firefox menu.

2. In the developer tools panel, select the "Get HAR" panel.

3. Click the "Get Network HAR" button to capture the network activity.

4. The HAR file will be downloaded to your computer with the filename "geospatial_test_data.json".

Note that the "Get HAR" add-on is a temporary add-on and will be unloaded when you close Firefox. 
