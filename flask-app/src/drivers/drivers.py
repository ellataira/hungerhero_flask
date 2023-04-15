from flask import Blueprint, request, jsonify, make_response
import json
from src import db

# -- DELETE will be firing a driver  done potentially

# -- POST will be new driver joining the app joining app  done potentially

# PUT when driver changes desired radius
# PUT for driver to change current location
# PUT for updating jobs completed and amount earned

# -- GET to find top 10 highest rated drivers done
# -- GET to find bottom 20 rated drivers done
# -- GET to find 5 highest earning drivers done

drivers = Blueprint('drivers', __name__)

# Removes a driver from the database drivers
@drivers.route('/drivers/fireDriver', methods=['DELETE'])
def get_drivers():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # this might not be right
    query = '''
        DELETE FROM Driver
        WHERE employeeid = employeeid
    '''

    # use cursor to query the database for a list of products
    cursor.execute(query)

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# Adds a driver to the database of drivers
@drivers.route('/drivers/hireDriver', methods=['POST'])
def get_drivers(employeeid, phone_number, radius, drivers_license,
current_location, transportation):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute("INSERT INTO Driver VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
    (employeeid, phone_number, radius, drivers_license, 0, current_location, 0, transportation, 0))

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# get the top 5 products from the database
@drivers.route('/mostExpensive')
def get_most_pop_products():
    cursor = db.get_db().cursor()
    query = '''
        SELECT product_code, product_name, list_price, reorder_level
        FROM products
        ORDER BY list_price DESC
        LIMIT 5
    '''
    cursor.execute(query)
       # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# Get top 20 worst rated drivers
@drivers.route('/drivers/worstDrivers', methods=['GET'])
def get_lowest():
    cursor = db.get_db().cursor()
    query = '''
        SELECT employeeid
        FROM Driver
        ORDER BY rating
        LIMIT 20
    '''
    cursor.execute(query)
       # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# Get 10 highest rated drivers
@drivers.route('/drivers/mostEarned', methods=['GET'])
def get_most_earned():
    cursor = db.get_db().cursor()
    query = '''
        SELECT employeeid
        FROM Driver
        ORDER BY rating DESC
        LIMIT 10
    '''
    cursor.execute(query)
       # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# get 5 highest earning drivers
@drivers.route('/drivers/mostEarned', methods=['GET'])
def get_most_earned():
    cursor = db.get_db().cursor()
    query = '''
        SELECT employeeid
        FROM Driver
        ORDER BY total_earned DESC
        LIMIT 5
    '''
    cursor.execute(query)
       # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)