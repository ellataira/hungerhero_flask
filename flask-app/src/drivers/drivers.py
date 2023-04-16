from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

# -- DELETE will be firing a driver  done potentially

# -- POST will be new driver joining the app joining app  done potentially

# -- PUT when driver changes desired radius maybe done
# -- PUT for driver to change current location  maybe done
# PUT for updating jobs completed and amount earned

# -- GET to find top 10 highest rated drivers done
# -- GET to find bottom 20 rated drivers done
# -- GET to find 5 highest earning drivers done

drivers = Blueprint('drivers', __name__)

# Removes a driver from the database drivers
@drivers.route('/fireDriver', methods=['DELETE'])
def remove_driver():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    data = request.json
    employee_id = data["employee_id"]


    # this might not be right
    query = '''
        DELETE FROM Driver
        WHERE employeeid = '{}'
    '''.format(employee_id)

    # use cursor to query the database for a list of products
    cursor.execute(query)

    return "Fired {}".format(employee_id)

# Adds a driver to the database of drivers
@drivers.route('/hireDriver', methods=['POST', 'GET'])
def hire_driver():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    data = request.json
    current_app.logger.info(data)

    employeeid, phone_number, radius, drivers_license, current_location, transportation = data["employeeid"], data["phone_number"], data["radius"], data["drivers_license"], data["current_location"], data["transportation"]

    # use cursor to query the database for a list of products
    query = """INSERT INTO Driver (employeeid, phone_number, radius, drivers_license, current_location, jobs_completed, transportation, total_earned, rating)
                 VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(employeeid, phone_number, radius, drivers_license, current_location, 0, transportation, 0, 0)

    cursor.execute(query)

    query = "select * from Driver where employeeid = '{}'".format(employeeid) 
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

# Allows a driver to update their desired working radius
@drivers.route('/updateRadius', methods=['PUT', 'GET'])
def update_radius():
    # get a cursor object from the database
    cursor = db.get_db().cursor()
    
    data = request.json
    
    new_radius, employeeid = data["new_radius"], data["employeeid"]

    query = '''
        UPDATE Driver SET radius = '{}'
        WHERE employeeid = '{}'
    '''.format(new_radius, employeeid)

    # use cursor to query the database for a list of products
    cursor.execute(query)

    query = "select * from Driver where employeeid = '{}'".format(employeeid) 
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

# Allows a driver to update their current location
@drivers.route('/updateLocation', methods=['PUT'])
def update_location():
    # get a cursor object from the database
    cursor = db.get_db().cursor()
        
    data = request.json
    
    new_location, employee_id = data["new_location"], data["employee_id"]

    #maybe?
    query = '''
        UPDATE Driver SET current_location = '{}'

        WHERE employeeid = '{}'
    '''.format(new_location, employee_id)

    # use cursor to query the database for a list of products
    cursor.execute(query)

    query = "select * from Driver where employeeid = '{}'".format(employee_id) 
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

# updates a driver's phone number 
@drivers.route('/phone', methods=['PUT'])
def update_phone():
# get a cursor object from the database
    cursor = db.get_db().cursor()
        
    data = request.json
    
    newphone, employee_id = data["phone"], data["employee_id"]

    #maybe?
    query = '''
        UPDATE Driver SET phone_number = '{}'
        WHERE employeeid = '{}'
    '''.format(newphone, employee_id)

    # use cursor to query the database for a list of products
    cursor.execute(query)

    query = "select * from Driver where employeeid = '{}'".format(employee_id) 
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
@drivers.route('/worstDrivers', methods=['GET'])
def get_lowest():
    cursor = db.get_db().cursor()
    query = '''
        SELECT employeeid, rating
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
@drivers.route('/highestRated', methods=['GET'])
def get_highest_rated():
    cursor = db.get_db().cursor()
    query = '''
        SELECT employeeid, rating
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
@drivers.route('/mostEarned', methods=['GET'])
def get_most_earned():
    cursor = db.get_db().cursor()
    query = '''
        SELECT employeeid, total_earned
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