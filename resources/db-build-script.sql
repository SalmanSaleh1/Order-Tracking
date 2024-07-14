CREATE DATABASE IF NOT EXISTS Order_tracking;
USE Order_tracking;

-- TABLES

CREATE TABLE IF NOT EXISTS department (
    department_id INT NOT NULL AUTO_INCREMENT,
    department_name VARCHAR(255),
    PRIMARY KEY (department_id)
);

CREATE TABLE IF NOT EXISTS users (
    user_id INT NOT NULL AUTO_INCREMENT,
    user_name VARCHAR(255),
    password VARCHAR(255),
    department_id INT NOT NULL,
    PRIMARY KEY (user_id),
    FOREIGN KEY (department_id) REFERENCES department(department_id)
);

CREATE TABLE IF NOT EXISTS addOrders (
    order_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    order_name VARCHAR(255),
    order_description VARCHAR(255),
    order_state VARCHAR(255),
    order_date DATETIME,
    department_id INT NOT NULL,
    PRIMARY KEY (order_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (department_id) REFERENCES department(department_id)
);

CREATE TABLE IF NOT EXISTS Orders (
    order_id INT NOT NULL,
    department_id INT NOT NULL,
    PRIMARY KEY (order_id, department_id),
    FOREIGN KEY (order_id) REFERENCES addOrders(order_id),
    FOREIGN KEY (department_id) REFERENCES department(department_id)
);
