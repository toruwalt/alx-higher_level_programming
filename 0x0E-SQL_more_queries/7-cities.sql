-- creates the database hbtn_0d_usa and the table cities.
-- cities description:
--	id INT unique, auto gen, not null and is a primary key
--	state_id INT, not null and must be a FOREIGN KEY that references to id of the states table
-- 	name VARCHAR(256) not null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(state_id) REFERENCES states(id)
);
