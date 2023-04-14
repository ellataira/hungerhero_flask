drop database hungerhero;

create database hungerhero ;

use hungerhero;

create table Users(
    phone        varchar(20) not null ,
    language     text not null ,
    first_name   text not null ,
    last_name    text not null ,
    total_orders int not null ,
    username     varchar(20) primary key,
    total_spent  float not null ,
    pronouns     text,
    card_number varchar(20) not null unique ,
    address_street text not null ,
    address_zip int not null ,
    address_city text not null ,
    address_state text not null ,
    address_country text not null
);

create table PaymentMethod (
    username varchar(20),
    card_number varchar(20) not null,
    cvv int not null ,
    expiration varchar(20) not null ,
    primary key (card_number, cvv, expiration),
    foreign key (username) references Users (username)
);

CREATE TABLE Driver
(
    employeeid       int          NOT NULL PRIMARY KEY,
    phone_number     varchar(50)  NOT NULL,
    radius           float        NOT NULL,
    drivers_license  float        NOT NULL,
    rating           int          NOT NULL,
    current_location varchar(100) NOT NULL,
    jobs_completed   int          NOT NULL,
    transportation   varchar(50)  NOT NULL,
    date_joined      datetime     default   current_timestamp,
    total_earned     float        NOT NULL
);


CREATE TABLE Orders
(
    orderid                varchar(50)   UNIQUE NOT NULL PRIMARY KEY,
    driver                 int  UNIQUE NOT NULL,
    items                  varchar(100) NOT NULL,
    total_amount           float        NOT NULL,
    items_amount           int          NOT NULL,
    dropoff_instructions   varchar(100) NOT NULL,
    ready_in               int     NOT NULL,
    time_delivered         varchar(100)     NOT NULL,
    estimated_deliverytime varchar(100)          NOT NULL,
    time_placed            datetime     default current_timestamp,
    restaurant_name        varchar(50)  NOT NULL,
    CONSTRAINT fk_1 FOREIGN KEY (driver) REFERENCES Driver (employeeid)
);



create table Restaurant(
    phone_number varchar(50) not null ,
    name varchar(50) primary key ,
    address_street text not null ,
    address_state text not null ,
    address_city text not null ,
    address_zip int not null ,
    address_country text not null ,
    date_joined datetime default current_timestamp
);

create table DriverRating(
    driver_id int,
    restaurant varchar(50),
    rating float not null ,
    review text,
    foreign key (driver_id) references Driver (employeeid),
    foreign key (restaurant) references Restaurant (name),
    primary key (driver_id, rating)
);

create table UserRating(
    username varchar(20),
    restaurant varchar(50),
    rating float not null ,
    review text,
    foreign key (username) references Users (username),
    foreign key (restaurant) references Restaurant (name),
    primary key (username, rating)
);

create table Menu
(
    menuID     int         not null,
    name       varchar(50) not null,
    promotions text,
    primary key (menuID, name),
    foreign key (name) references Restaurant (name)
);


create table MenuItem(
    name varchar(50) primary key ,
    price float,
    menuID int,
    foreign key (menuID) references Menu (menuID)
);


insert into Users values (7086388402, "English", "Ella", "Taira", 1, "ellataira",
                          30.50, "she/her", 39239199393, "144 Hemenway", 00000, "Boston", "MA", "USA" ),
                      (3145669906, "English", "Ben", "Weiss", 1, "bweiss",
                          30.50, "he/him", 4813923949, "700 columbus", 00000, "Boston", "MA", "USA" );

select * from Users;

insert into PaymentMethod values("ellataira", 39239199393, 123, "2009-11-11"), ("bweiss", 4813923949, 123, "2026-09-07");

select * from PaymentMethod;

insert into Driver
    (employeeid, phone_number, radius, drivers_license, rating, current_location, jobs_completed, transportation, total_earned)
values (6969, 3456789903, 5, 0990, 1, "Brookline", 1, "E-Scooter",67.32),
                          (420, 3236777923, 6.2, 5432, 2, "Compton", 104, "Car", 601.54);

select *
from Driver;

insert into Orders (orderid, driver, items, total_amount, items_amount, dropoff_instructions, ready_in, time_delivered, estimated_deliverytime, restaurant_name)
values (09393, 6969, "Cheese Pizza, Garlic Bread", 25.62, 2, "on my porch", 2, "2008-11-11 11:12:01", "2", "New York Pizza");

insert into Orders (orderid, driver, items, total_amount, items_amount, dropoff_instructions, ready_in, time_delivered, estimated_deliverytime, restaurant_name) VALUES
(89243, 420, "Blueberry Muffin, Hot Coffee, Biscuit", 10.24, 3, "hand to me", 20, "2008-12-11 11:12:01", "5", "Tatte");

select  * from Orders;

insert into Restaurant (phone_number, name, address_street, address_state, address_city, address_zip, address_country)
values (2, "Pavement", "708 Boylston Ave", "New York", "Queens", 67098, "USA");
insert into Restaurant (phone_number, name, address_street, address_state, address_city, address_zip, address_country)
values (12345, "Dave's", "908 Main Street", "Missouri", "St. Louis", 63017, "USA"),
       (987652, "Sofie's", "900 Park Avenue", "California", "Oakland", 94602, "USA");

insert into DriverRating values (6969, "Sofie's", 4.2, "solid");
insert into DriverRating values (6969, "Pavement", 5.0, "fantastic!!! :)"),
                                (420, "Dave's", 2.3, "nowhere to park car");

insert into UserRating values ("bweiss", "Sofie's", 4.2, "solid soups"),
                              ("ellataira", "Pavement", 5.0, "incredible!"),
                              ("bweiss", "Dave's", 3.8, "food was cold");

Insert into Menu values (738, "Pavement", "You win a prize");
insert into Menu values (383, "Dave's", "Come to Dave’s to get a free appetizer");

select * from Menu;

insert into MenuItem
values ("Mozzerella Sticks", 7.49, 383), ("Cheese Pizza", 17.99, 738), ("Chocolate Cake", 5.24, 738);

