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
@users.route('/users', methods=['GET'])
def get_users():
    cursor = db.get_db().cursor()
    cursor.execute('select phone, language,\
        first_name, last_name, total_orders, username, total_spent, pronouns, address_street,\
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

@users.route('/mostSpentCustomer', methods=['GET'])
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
@users.route('/mostOrdersPlaced', methods=['GET'])
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

@users.route('/users/pronouns', methods=['PUT'])
def update_pronouns(new_pronouns):
    query = '''
        UPDATE USER SET pronouns = new_pronouns
    '''

    data = request.json

    new_pronouns = data['Pronouns']
    
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


# deletes a given user from Users
@users.route('/u/delete', methods=['DELETE'])
def delete_customer():
    cursor = db.get_db().cursor()

    data = request.json 

    userID = data["userID"]

    query = 'DELETE FROM Users WHERE Users.UserID = {}'.format(userID)
    cursor.execute(query)

    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# creates a new User given their personal information input 
@users.route('/u/user', methods=['POST'])
def create_new_user():
    cursor = db.get_db().cursor()

    data = request.json

    phone, lang, fname, lname, username, pronouns, street, zipcode, city, state, country = data["phone"], data["lang"], data["fname"], data["lname"], data["username"], data["pronouns"], data["street"], data["zipcode"], data["city"], data["state"], data["country"]

    query = 'INSERT INTO Users VALUES ({},{},{},{},{},{},{},{},{},{},{},{})'.format(phone, lang, fname, lname, 0, username, "0", 
                                                                                    pronouns, street, zipcode,city,state, country )
    cursor.execute(query)

    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# updates a PaymentMethod's CVV and expiration date 
@users.route('/u/payment', methods=['PUT'])
def change_payment(cardno, oldcvv, oldexp, newcvv, newexp):
    cursor = db.get_db().cursor()

    data = request.json 

    cardno, oldcvv, oldexp, newcvv, newexp  = data["cardno"], data["oldcvv"], data["oldexp"], data["newcvv"], data["newexp"]

    query = '''update PaymentMethod 
                set cvv = {}, expiration = {} 
                where cvv = {} and expiration = {} and card_number = {};'''.format(newcvv, newexp, oldcvv, oldexp, cardno)

    cursor.execute(query)

    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# updates a User's address 
@users.route('/address', methods=['PUT'])
def update_address():
    cursor = db.get_db().cursor()

    data = request.json 

    street, zipcode, city, state, country, username = data["street"], data["zipcode"], data["city"], data["state"], data["country"], data["username"]

    query = '''
    update Users
    set address_street={}, address_zip={} , address_city={} , address_state={} , address_country={}
    where username={}
    '''.format(street, zipcode, city, state, country, username)

    cursor.execute(query)

    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response