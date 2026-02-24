CREATE DATABASE library;
USE library;

CREATE TABLE books (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100),
    author VARCHAR(100),
    year INT,
    copies INT
);
