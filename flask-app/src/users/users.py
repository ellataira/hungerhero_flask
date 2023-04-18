from flask import Blueprint, request, jsonify, make_response, current_app
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

@users.route('/pronouns', methods=['PUT'])
def update_pronouns():

    # get a cursor object from the database
    cursor = db.get_db().cursor()
        
    data = request.json
    
    username1, pronouns1 = data["username1"], data["pronouns1"]

    #maybe?
    query = '''
        UPDATE Users SET pronouns = '{}'

        WHERE username = '{}'
    '''.format(pronouns1, username1)

    # use cursor to query the database for a list of products
    cursor.execute(query)

    query = "select * from Users where username = '{}'".format(username) 
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


# deletes a given user from Users
@users.route('/delete', methods=['DELETE'])
def delete_user():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    data = request.json
    username2 = data["username2"]


    # this might not be right
    query = '''
        DELETE FROM Users
        WHERE username = '{}'
    '''.format(username2)

    # use cursor to query the database for a list of products
    cursor.execute(query)

    return "Fired {}".format(username2)


# creates a new User given their personal information input 
@users.route('/user', methods=['POST'])
def create_new_user():
    cursor = db.get_db().cursor()

    data = request.json
    current_app.logger.info(data)

    phone, lang, fname, lname, username, pronouns, street, zipcode, city, state, country = data["phone"], data["lang"], data["fname"], data["lname"], data["username"], data["pronouns"], data["street"], data["zipcode"], data["city"], data["state"], data["country"]

    # query = "INSERT INTO Users VALUES ('{}','{}','{}','{}',{},'{}','{}','{}','{}','{}','{}','{}')".format(phone, lang, fname, lname, 0, username, 0, 
    #                                                                                 pronouns, street, zipcode,city,state, country )
    query = """INSERT INTO Users (phone, language, first_name, last_name, total_orders, username, total_spent, pronouns, address_street, address_zip, address_city, address_state, address_country) VALUES 
    ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')
""".format(phone, lang, fname, lname, 0, username, 0, pronouns, street, zipcode, city, state, country)
    
    cursor.execute(query)

    query = "select * from Users where username = '{}'".format(username) 
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


# updates a PaymentMethod's CVV and expiration date 
@users.route('/payment', methods=['PUT'])
def change_payment():
    cursor = db.get_db().cursor()

    data = request.json 

    cardno, oldcvv, oldexp, newcvv, newexp, username3 = data["cardno"], data["oldcvv"], data["oldexp"], data["newcvv"], data["newexp"], data["username3"]

    query = '''update PaymentMethod 
                set cvv = '{}', expiration = '{}'
                where cvv = '{}' and expiration = '{}'and card_number = '{}';'''.format(newcvv, newexp, oldcvv, oldexp, cardno)

     # use cursor to query the database for a list of products
    cursor.execute(query)

    # a user may have multiple payment methods, but only return the one that is updated 
    query = "select * from PaymentMethod where username = '{}' and card_number = '{}'".format(username3, cardno) 
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

# updates a User's address 
@users.route('/address', methods=['PUT'])
def update_address():
    cursor = db.get_db().cursor()

    data = request.json 

    street1, zipcode1, city1, state1, country1, username4 = data["street1"], data["zipcode1"], data["city1"], data["state1"], data["country1"], data["username4"]

    query = '''
    update Users
    set address_street='{}', address_zip='{}' , address_city='{}' , address_state='{}' , address_country='{}'
    where username='{}'
    '''.format(street1, zipcode1, city1, state1, country1, username4)

    cursor.execute(query)
    
    query = "select * from Users where username = '{}' ".format(username4) 
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
