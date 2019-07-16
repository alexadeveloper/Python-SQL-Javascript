-- create database and table
-- database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- table id and name
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, name VARCHAR(256) NOT NULL);
