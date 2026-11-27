-- Creates the database hbtn_0d_usa and the table cities in it.
-- Create the database only if it is missing
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Create the table only if it is missing, with a foreign key to states
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);
