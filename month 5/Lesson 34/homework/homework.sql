CREATE TABLE db.Ingridients (
    id INTEGER PRIMARY KEY,
    name varchar unique,
	type varchar,
	expiration TIMESTAMP
);

CREATE TABLE db.Recipees (
    id INTEGER PRIMARY KEY,
    name varchar unique,
	description varchar,
	cook_time serial
);

CREATE TABLE db.Calculations (
    id INTEGER PRIMARY KEY,
    recipee_id SERIAL,
    ingredient_id SERIAL,
    amount SERIAL,
    order serial,
    FOREIGN KEY (recipee_id) REFERENCES db.Recipees(id)
	FOREIGN KEY (ingredient_id) REFERENCES db.Ingredients(id)
);

CREATE TABLE db.Rooms (
    id INTEGER PRIMARY KEY,
    capacity SERIAL,
	price SERIAL,
	current_state BOOLEAN
);

CREATE TABLE db.Clients (
    id INTEGER PRIMARY KEY,
    name varchar,
	surname varchar,
	age: serial
);

CREATE TABLE db.Reservations (
    id INTEGER PRIMARY KEY,
    room_id SERIAL,
    client_id SERIAL,
    date_of_entry TIMESTAMP,
    date_of_leave TIMESTAMP,
    FOREIGN KEY (room_id) REFERENCES db.Rooms(id)
	FOREIGN KEY (client_id) REFERENCES db.Clients(id)
);


CREATE TABLE db.Products (
    id INTEGER PRIMARY KEY,
    Name varchar unique,
    price SERIAL,
	amount SERIAL
);

CREATE TABLE db.Price_changes (
    id INTEGER PRIMARY KEY,
    product_id SERIAL,
    old_price SERIAL,
    new_price SERIAL,
    date_of_change TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES db.Products(id)
);