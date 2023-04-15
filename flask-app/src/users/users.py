from flask import Blueprint, request, jsonify, make_response
import json
from src import db

# DELETE will get rid of an account

# POST will be creating an account

# PUT will be changing payment method
# PUT can also be updating orders placed
# PUT can also change total amount spent

# GET top 10 highest spending customers
# GET top 10 customers with most orders place
# GET top 3 highest rated customers
# GET top 3 lowest rated customers


users = Blueprint('users', __name__)

# Get all customers from the DB
@users.route('/users', methods=['GET'])
def get_uers():
    cursor = db.get_db().cursor()
    cursor.execute('select company, last_name,\
        first_name, job_title, business_phone from customers')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get customer detail for customer with particular userID
@users.route('/users/<userID>', methods=['GET'])
def get_customer(userID):
    cursor = db.get_db().cursor()
    cursor.execute('select * from users where id = {0}'.format(userID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Gets the top 10 highest spending customers 

@users.route('/mostSpentCustomer', method=['GET'])
def get_top_10_spending_customer():
    query = '''
        SELECT totaL_spent, first_name, last_name
        FROM Users
        ORDER BY total_spent DESC
        LIMIT 10
    '''
    cursor = db.get_db().cursor()
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

# GET top 10 customers with most orders place
@users.route('/mostOrdersPlaced', method=['GET'])
def get_top_10_orders_placed():
    query = '''
        SELECT total_orders, first_name, last_name
        FROM Users
        ORDER BY total_orders DESC
        LIMIT 10
    '''
    cursor = db.get_db().cursor()
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
