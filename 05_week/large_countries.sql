-- Data Modeling -- how to structure the tabless 

-- How to create a database?


-- How to run the script?

-- psql -U posgresql -d country -f large_countries.sql

-- How do we create a table?
CREATE DATABASE country;

DROP TABLE IF EXISTS countries;
CREATE TABLE countries(
    -- column_name, datatype, constraint
    country_id SERIAL PRIMARY KEY,
    country VARCHAR(40) NOT NULL,
    population NUMERIC NOT NULL,
    fertility NUMERIC,
    continent VARCHAR(40)
);

COPY countries FROM '/Users/oguzhanbekar/OneDrive/Spiced/euclidean-eukalyptus-encounter-notes/05_week/Data_Modeling/large_countries_2015.csv' DELIMITER ',' CSV HEADER;