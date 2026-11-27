-- Creates the table unique_id where id is unique with the default value 1.
-- Create the table only if it is missing
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
