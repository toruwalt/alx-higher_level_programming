-- creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa)
-- states description:
--	id INT unique, auto gen, not null and is a primary key
--	name VARCHAR(256) can’t be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
use hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE PRIMARY KEY AUTO_INCREMENT NOT NULL, name VARCHAR(256) NOT NULL);
