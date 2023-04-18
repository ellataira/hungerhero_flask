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
    db.get_db().commit()

    return "Fired {}".format(employee_id)

# Adds a driver to the database of drivers
@drivers.route('/hireDriver', methods=['POST', 'GET'])
def hire_driver():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    data = request.json
    current_app.logger.info(data)

    employeeid1, phone_number1, radius1, drivers_license1, current_location1, transportation1 = data["employeeid1"], data["phone_number1"], data["radius1"], data["drivers_license1"], data["current_location1"], data["transportation1"]

    # use cursor to query the database for a list of products
    query = """INSERT INTO Driver (employeeid, phone_number, radius, drivers_license, current_location, jobs_completed, transportation, total_earned, rating)
                 VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(employeeid1, phone_number1, radius1, drivers_license1, current_location1, 0, transportation1, 0, 0)

    cursor.execute(query)

    query = "select * from Driver where employeeid = '{}'".format(employeeid1) 
    cursor.execute(query)
    db.get_db().commit()

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
    
    new_radius, employeesid = data["new_radius"], data["employeesid"]

    query = '''
        UPDATE Driver SET radius = '{}'
        WHERE employeeid = '{}'
    '''.format(new_radius, employeesid)

    # use cursor to query the database for a list of products
    cursor.execute(query)

    query = "select * from Driver where employeeid = '{}'".format(employeesid) 
    cursor.execute(query)
    db.get_db().commit()

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
    
    new_location, employeees_id = data["new_location"], data["employeees_id"]

    #maybe?
    query = '''
        UPDATE Driver SET current_location = '{}'

        WHERE employeeid = '{}'
    '''.format(new_location, employeees_id)

    # use cursor to query the database for a list of products
    cursor.execute(query)

    query = "select * from Driver where employeeid = '{}'".format(employeees_id) 
    cursor.execute(query)
    db.get_db().commit()

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
    
    new_phone, employees_id = data["new_phone"], data["employees_id"]

    #maybe?
    query = '''
        UPDATE Driver SET phone_number = '{}'
        WHERE employeeid = '{}'
    '''.format(new_phone, employees_id)

    # use cursor to query the database for a list of products
    cursor.execute(query)

    query = "select * from Driver where employeeid = '{}'".format(employees_id) 
    cursor.execute(query)
    db.get_db().commit()

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
