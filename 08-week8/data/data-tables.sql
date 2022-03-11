CREATE TABLE monday (
    timestamp TIMESTAMP,
    customer_no INT,
    location_1 VARCHAR (255)
);

COPY monday FROM '/Users/ckarlsen/Documents/Spiced/euclidean-eukalyptus/work/08-week-8/Project/data/monday.csv' DELIMITER ';' CSV HEADER;

CREATE TABLE tuesday (
    timestamp TIMESTAMP,
    customer_no INT,
    location_1 VARCHAR (255)
);

COPY tuesday FROM '/Users/ckarlsen/Documents/Spiced/euclidean-eukalyptus/work/08-week-8/Project/data/tuesday.csv' DELIMITER ';' CSV HEADER;

CREATE TABLE wednesday (
    timestamp TIMESTAMP,
    customer_no INT,
    location_1 VARCHAR (255)
);

COPY wednesday FROM '/Users/ckarlsen/Documents/Spiced/euclidean-eukalyptus/work/08-week-8/Project/data/wednesday.csv' DELIMITER ';' CSV HEADER;

CREATE TABLE thursday (
    timestamp TIMESTAMP,
    customer_no INT,
    location_1 VARCHAR (255)
);

COPY thursday FROM '/Users/ckarlsen/Documents/Spiced/euclidean-eukalyptus/work/08-week-8/Project/data/thursday.csv' DELIMITER ';' CSV HEADER;

CREATE TABLE friday (
    timestamp TIMESTAMP,
    customer_no INT,
    location_1 VARCHAR (255)
);

COPY friday FROM '/Users/ckarlsen/Documents/Spiced/euclidean-eukalyptus/work/08-week-8/Project/data/friday.csv' DELIMITER ';' CSV HEADER;