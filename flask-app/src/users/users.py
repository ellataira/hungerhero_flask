from flask import Blueprint, request, jsonify, make_response
import json
from src import db

# DELETE will get rid of an account

# POST will be creating an account

# PUT will be changing payment method

# PUT change address 

# PUT can also change total amount spent

# GET top 10 highest spending customers
# GET top 10 customers with most orders place
# PUT will update the pronouns 


users = Blueprint('users', __name__)

# Get all customers from the DB
@users.route('u/users', methods=['GET'])
def get_uers():
    cursor = db.get_db().cursor()
    cursor.execute('phone, language,\
        first_name, last_name, total_orders, username, total_spent, pronouns, card_number, address_street,\
                   address_zip, address_city, address_state, address_country from Users')
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

    return jsonify(json_data)


# PUT will update the pronouns 

@users.route('/users/pronouns', method=['PUT'])
def update_pronouns(new_pronouns):
    query = '''
        UPDATE USER SET pronouns = new_pronouns
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

# Get customer detail for customer with particular userID
@users.route('/users/<userID>', methods=['GET'])
def get_customer(userID):
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
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response