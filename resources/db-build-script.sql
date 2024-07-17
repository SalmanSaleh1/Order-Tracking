CREATE DATABASE IF NOT EXISTS order_tracking;
USE order_tracking;

CREATE USER 'dbuser'@'%' IDENTIFIED BY 'changeme';
GRANT ALL PRIVILEGES ON order_tracking.* TO 'dbuser'@'%';
FLUSH PRIVILEGES;

-- TABLES

CREATE TABLE IF NOT EXISTS addOrders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    order_name VARCHAR(255) NOT NULL,
    order_description VARCHAR(255),
    department_name VARCHAR(255) NOT NULL,
    order_state VARCHAR(255) DEFAULT 'waiting',
    order_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Orders (
    order_id INT NOT NULL,
    department_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (order_id, department_name),
    FOREIGN KEY (order_id) REFERENCES addOrders(order_id)
);
