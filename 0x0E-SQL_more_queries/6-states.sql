-- Create database `hbtn_0d_usa`
-- Create table `states` in `hbtn_0d_usa`
-- Make id field unique, auto generated, not NULL, and a primary key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL
	);
