CREATE DATABASE imports;

\c imports;
CREATE TABLE upload_dates(
    upload_id SERIAL PRIMARY KEY,
    upload_date TIMESTAMP NOT NULL 
);