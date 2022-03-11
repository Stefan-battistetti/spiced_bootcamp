-- northwind.sql

-- To automatize
-- psql -U postgres -p 5432  -d northwind -f '/Users/kashi/Documents/euclidean-eukalyptus/student-code/euclidean-eukalyptus-student-code/week05/northwind.sql' 

-- DROP DATABASE [ IF EXISTS ] northwind;
DROP DATABASE IF EXISTS northwind;
CREATE DATABASE northwind;

DROP TABLE IF EXISTS categories;

CREATE TABLE categories (
    categoryID SERIAL primary key NOT NULL,
    categoryName VARCHAR(40) NOT NULL,
    description	TEXT NOT NULL,
    picture TEXT NOT NULL
);

-- To see the table content
-- TABLE categories;

DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customerID VARCHAR(40) primary key ,
    companyName  TEXT,
    contactName TEXT,
    contactTitle TEXT,
    address TEXT, 
    city VARCHAR(40),
    region VARCHAR(40),
    postalCode VARCHAR(40),
    country	VARCHAR(40),
    phone VARCHAR(40),
    fax VARCHAR(40)
);




DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    employeeID SERIAL primary key,
    lastName VARCHAR(40),
    firstName VARCHAR(40),
    title	TEXT,
    titleOfCourtesy	VARCHAR(40),
    birthDate	TIMESTAMP,
    hireDate	TEXT,
    address	TEXT,
    city	VARCHAR(40),
    region	TEXT,
    postalCode	VARCHAR(40),
    country	VARCHAR(40),
    homePhone	VARCHAR(40),
    extension	INT,
    photo	TEXT,
    notes	TEXT,
    reportsTo	INT,
    photoPath TEXT
);


DROP TABLE IF EXISTS order_details;

CREATE TABLE order_details(
      orderID INT,
      productID	INT,
      unitPrice	NUMERIC,
      quantity	INT,
      discount NUMERIC
);
  
DROP TABLE IF EXISTS orders;  

CREATE TABLE orders(
    orderID	INT primary key,
    customerID VARCHAR(40),
    employeeID	INT,
    orderDate TIMESTAMP, 
    requiredDate TIMESTAMP, 
    shippedDate	TIMESTAMP, 
    shipVia	INT,
    freight	NUMERIC,
    shipName TEXT,
    shipAddress	TEXT,
    shipCity VARCHAR(40),
    shipRegion	VARCHAR(40),
    shipPostalCode	VARCHAR(40),
    shipCountry VARCHAR(40),
    FOREIGN KEY(customerID)  
    REFERENCES customers(customerID) ON DELETE CASCADE,
    FOREIGN KEY(employeeID)  
    REFERENCES employees(employeeID) ON DELETE CASCADE
);  


DROP TABLE IF EXISTS products; 

CREATE TABLE products(
    productID	INT primary key,
    productName	VARCHAR(40),
    supplierID	INT,
    categoryID	INT,
    quantityPerUnit	VARCHAR(40),
    unitPrice		NUMERIC,
    unitsInStock	INT,
    unitsOnOrder	INT,
    reorderLevel	INT,
    discontinued    INT,
    FOREIGN KEY(categoryID)  
    REFERENCES categories(categoryID) ON DELETE CASCADE

);


DROP TABLE IF EXISTS regions; 

CREATE TABLE regions(
    regionID	INT primary key,
    regionDescription VARCHAR(40)
);

DROP TABLE IF EXISTS shippers; 

CREATE TABLE shippers(
    shipperID	INT primary key,
    companyName	VARCHAR(40),
    phone VARCHAR(40)

);

DROP TABLE IF EXISTS suppliers; 

CREATE TABLE suppliers (
    supplierID	TEXT,
    companyName		TEXT,
    contactName		TEXT,
    contactTitle		TEXT,
    address		TEXT,
    city	VARCHAR(40),
    region	VARCHAR(40),
    postalCode	VARCHAR(40),
    country	VARCHAR(40),
    phone	VARCHAR(40),
    fax	VARCHAR(40),
    homePage TEXT
);

DROP TABLE IF EXISTS territories; 

CREATE TABLE territories(
    territoryID	INT,
    territoryDescription	VARCHAR(40),
    regionID INT, 
    FOREIGN KEY(regionID)  
    REFERENCES regions(regionID) ON DELETE CASCADE
);


DROP TABLE IF EXISTS employee_territories;

CREATE TABLE employee_territories (
    employeeID INT,
    territoryID INT,
    FOREIGN KEY(employeeID)  
    REFERENCES employees(employeeID) ON DELETE CASCADE
);




\copy categories FROM '/Users/kashi/Documents/euclidean-eukalyptus/encounter-notes/euclidean-eukalyptus-encounter-notes/05_week/northwind/categories.csv' DELIMITER ',' CSV HEADER;
\copy customers FROM '/Users/kashi/Documents/euclidean-eukalyptus/encounter-notes/euclidean-eukalyptus-encounter-notes/05_week/northwind/customers.csv' DELIMITER ',' CSV HEADER;
\copy employees FROM '/Users/kashi/Documents/euclidean-eukalyptus/encounter-notes/euclidean-eukalyptus-encounter-notes/05_week/northwind/employees.csv' DELIMITER ',' CSV HEADER NULL 'NULL' ;
\copy order_details FROM '/Users/kashi/Documents/euclidean-eukalyptus/encounter-notes/euclidean-eukalyptus-encounter-notes/05_week/northwind/order_details.csv' DELIMITER ',' CSV HEADER NULL 'NULL' ;
\copy orders FROM '/Users/kashi/Documents/euclidean-eukalyptus/encounter-notes/euclidean-eukalyptus-encounter-notes/05_week/northwind/orders.csv' DELIMITER ',' CSV HEADER NULL 'NULL' ;
\copy products FROM '/Users/kashi/Documents/euclidean-eukalyptus/encounter-notes/euclidean-eukalyptus-encounter-notes/05_week/northwind/products.csv' DELIMITER ',' CSV HEADER NULL 'NULL' ;
\copy regions FROM '/Users/kashi/Documents/euclidean-eukalyptus/encounter-notes/euclidean-eukalyptus-encounter-notes/05_week/northwind/regions.csv' DELIMITER ',' CSV HEADER NULL 'NULL' ;
\copy shippers FROM '/Users/kashi/Documents/euclidean-eukalyptus/encounter-notes/euclidean-eukalyptus-encounter-notes/05_week/northwind/shippers.csv' DELIMITER ',' CSV HEADER NULL 'NULL' ;
\copy suppliers FROM '/Users/kashi/Documents/euclidean-eukalyptus/encounter-notes/euclidean-eukalyptus-encounter-notes/05_week/northwind/suppliers.csv' DELIMITER ',' CSV HEADER NULL 'NULL' ;
\copy territories FROM '/Users/kashi/Documents/euclidean-eukalyptus/encounter-notes/euclidean-eukalyptus-encounter-notes/05_week/northwind/territories.csv' DELIMITER ',' CSV HEADER NULL 'NULL' ;
\copy employee_territories FROM '/Users/kashi/Documents/euclidean-eukalyptus/encounter-notes/euclidean-eukalyptus-encounter-notes/05_week/northwind/employee_territories.csv' DELIMITER ',' CSV HEADER NULL 'NULL';
