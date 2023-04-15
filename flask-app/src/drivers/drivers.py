from flask import Blueprint, request, jsonify, make_response
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

    employee_id = data['employeeid']

    # this might not be right
    query = '''
        DELETE FROM Driver
        WHERE employeeid = {}
    '''.format(employee_id)

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
@drivers.route('/hireDriver', methods=['POST'])
def hire_driver():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    data = request.json

    employeeid, phone_number, radius, drivers_license, current_location, transportation = data['employeeid'], data['phone_number'], data['radius'], data['drivers_license'], data['current_location'], data['transportation']

    # use cursor to query the database for a list of products
    # cursor.execute("INSERT INTO Driver VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
    # (employeeid, phone_number, radius, drivers_license, "0", current_location, "0", transportation, "0"))

    cursor.execute("INSERT INTO Driver (employeeid, phone_number, radius, drivers_license, current_location, jobs_completed, transportation, total_earned, rating) VALUES ({}, {},{},{},{},{},{},{},{})".format(employeeid, phone_number, radius, drivers_license, "0", current_location, "0", transportation, "0"))

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
@drivers.route('/updateRadius', methods=['PUT'])
def update_radius(new_radius, employee_id):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    #maybe?
    query = '''
        UPDATE Driver SET radius = new_radius
        WHERE employeeid = employee_id
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

# Allows a driver to update their current location
@drivers.route('/updateLocation', methods=['PUT'])
def update_location(new_location, employee_id):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    #maybe?
    query = '''
        UPDATE Driver SET current_location = new_location

        WHERE employeeid = employee_id
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

# Adds a completed delivery to a driver and updates amount earned
@drivers.route('/newOrderCompleted', methods=['PUT'])
def new_order_completed(employee_id):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    updated_earned = '''
        SELECT SUM(total_amount)
        FROM Orders
        WHERE driver = employee_id
    '''

    #maybe?
    query = '''
        UPDATE Driver SET total_earned = updated_earned,
        jobs_completed = jobs_completed + 1
        WHERE employeeid = employee_id
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

# Get top 20 worst rated drivers
@drivers.route('/worstDrivers', methods=['GET'])
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
@drivers.route('/highestRated', methods=['GET'])
def get_highest_rated():
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
@drivers.route('/mostEarned', methods=['GET'])
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