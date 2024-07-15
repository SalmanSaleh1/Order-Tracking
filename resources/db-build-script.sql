CREATE DATABASE IF NOT EXISTS Order_tracking;
USE Order_tracking;

-- TABLES

CREATE TABLE IF NOT EXISTS addOrders (
    order_id INT NOT NULL AUTO_INCREMENT,
    order_name VARCHAR(255),
    order_description VARCHAR(255),
    order_state VARCHAR(255),
    order_date DATETIME,
    department_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (order_id)
);

CREATE TABLE IF NOT EXISTS Orders (
    order_id INT NOT NULL,
    department_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (order_id, department_name),
    FOREIGN KEY (order_id) REFERENCES addOrders(order_id)
);
