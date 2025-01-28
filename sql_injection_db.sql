CREATE DATABASE sql_injection_db;

USE sql_injection_db;

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE passwords (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    password VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
