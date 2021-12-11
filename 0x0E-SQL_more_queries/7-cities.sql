-- Create database `hbtn_0d_usa`
-- Create table `cities` in `hbtn_0d_usa`
-- Make id field unique, auto generated, not NULL, and a primary key
-- Make state_id field not NULL, foreign key, references id
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id)
);
