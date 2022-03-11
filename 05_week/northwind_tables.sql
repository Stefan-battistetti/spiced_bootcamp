DROP DATABASE IF EXISTS northwind;
CREATE DATABASE northwind;

DROP TABLE IF EXISTS categories;
CREATE TABLE categories(
    categoryID INT PRIMARY KEY, 
    categoryName VARCHAR(40),
    description TEXT,
    picture TEXT
);

COPY categories FROM '/Users/oguzhanbekar/OneDrive/Spiced/euclidean-eukalyptus-encounter-notes/05_week/northwind/categories.csv' DELIMITER ',' CSV HEADER;

DROP TABLE IF EXISTS products;
CREATE TABLE products(
    productID INT PRIMARY KEY,
	productName VARCHAR(50),
	supplierID INT, 
    categoryID INT,
    quantityPerUnit VARCHAR(50),
    unitPrice NUMERIC,
    unitsInStock INT,
    unitsOnOrder INT,
    reorderLevel INT,
    discontinued INT
);

ALTER TABLE products
    ADD FOREIGN KEY (categoryID) REFERENCES categories(categoryID) ON DELETE CASCADE,
    ADD FOREIGN KEY (supplierID) REFERENCES suppliers(supplierID) ON DELETE CASCADE;

COPY products FROM '/Users/oguzhanbekar/OneDrive/Spiced/euclidean-eukalyptus-encounter-notes/05_week/northwind/products.csv' DELIMITER ',' CSV HEADER;

DROP TABLE IF EXISTS shippers;
CREATE TABLE shippers(
    shipperid INT PRIMARY KEY,
	companyname VARCHAR(50),
	phone VARCHAR(50)
);

COPY shippers FROM '/Users/oguzhanbekar/OneDrive/Spiced/euclidean-eukalyptus-encounter-notes/05_week/northwind/shippers.csv' DELIMITER ',' CSV HEADER;

DROP TABLE IF EXISTS suppliers;
CREATE TABLE suppliers(
    supplierID INT PRIMARY KEY,
    companyName VARCHAR(50),
    contactName VARCHAR(50),
    contactTitle VARCHAR(50),
    address VARCHAR(50),
    city VARCHAR(50),
    region VARCHAR(50),
    postalCode VARCHAR(50),
    country VARCHAR(50),
    phone VARCHAR(50),
    fax VARCHAR(50),
    homePage TEXT
);

COPY suppliers FROM '/Users/oguzhanbekar/OneDrive/Spiced/euclidean-eukalyptus-encounter-notes/05_week/northwind/suppliers.csv' DELIMITER ',' CSV HEADER;

DROP TABLE IF EXISTS orders;
CREATE TABLE orders(
    orderID INT PRIMARY KEY,
    customerID VARCHAR(50),
    employeeID INT,
    orderDate DATE,
    requiredDate DATE,
    shippedDate DATE,
    shipVia INT,
    freight NUMERIC,
    shipName VARCHAR(50),
    shipAddress VARCHAR(100),
    shipCity VARCHAR(50),
    shipRegion VARCHAR(50),
    shipPostalCode VARCHAR(50),
    shipCountry VARCHAR(50)
);

ALTER TABLE orders
    ADD FOREIGN KEY (shipVia) REFERENCES shippers(shipperid) ON DELETE CASCADE,
    ADD FOREIGN KEY (customerID) REFERENCES customers(customerID) ON DELETE CASCADE,
    ADD FOREIGN KEY (employeeID) REFERENCES employees(employeeID) ON DELETE CASCADE;

COPY orders FROM '/Users/oguzhanbekar/OneDrive/Spiced/euclidean-eukalyptus-encounter-notes/05_week/northwind/orders.csv' DELIMITER ',' CSV HEADER NULL 'NULL';

DROP TABLE IF EXISTS employee_territories;
CREATE TABLE employee_territories(
    employeeID INT,
    territoryID INT
);

ALTER TABLE employee_territories
    ADD FOREIGN KEY (territoryID) REFERENCES territories(territoryID) ON DELETE CASCADE,
    ADD FOREIGN KEY (employeeID) REFERENCES employees(employeeID) ON DELETE CASCADE;


COPY employee_territories FROM '/Users/oguzhanbekar/OneDrive/Spiced/euclidean-eukalyptus-encounter-notes/05_week/northwind/employee_territories.csv' DELIMITER ',' CSV HEADER;

DROP TABLE IF EXISTS order_details;
CREATE TABLE order_details(
    orderID	INT,
    productID INT,
    unitPrice NUMERIC,
    quantity NUMERIC,
    discount NUMERIC
);

ALTER TABLE order_details
    ADD FOREIGN KEY (productID) REFERENCES products(productID) ON DELETE CASCADE,
    ADD FOREIGN KEY (orderID) REFERENCES orders(orderID) ON DELETE CASCADE;


COPY order_details FROM '/Users/oguzhanbekar/OneDrive/Spiced/euclidean-eukalyptus-encounter-notes/05_week/northwind/order_details.csv' DELIMITER ',' CSV HEADER;

DROP TABLE IF EXISTS customers;
CREATE TABLE customers(
    customerID VARCHAR(50) PRIMARY KEY,
    companyName VARCHAR(50),
    contactName VARCHAR(50),
    contactTitle VARCHAR(50),
    address VARCHAR(100),
    city VARCHAR(50),
    region VARCHAR(50),
    postalCode VARCHAR(50),
    country VARCHAR(50),
    phone VARCHAR(50),
    fax VARCHAR(50)
);

COPY customers FROM '/Users/oguzhanbekar/OneDrive/Spiced/euclidean-eukalyptus-encounter-notes/05_week/northwind/customers.csv' DELIMITER ',' CSV HEADER;


DROP TABLE IF EXISTS regions;
CREATE TABLE regions(
    regionID INT PRIMARY KEY,
    regionDescription VARCHAR(255)
);

COPY regions FROM '/Users/oguzhanbekar/OneDrive/Spiced/euclidean-eukalyptus-encounter-notes/05_week/northwind/regions.csv' DELIMITER ',' CSV HEADER;

DROP TABLE IF EXISTS territories;
CREATE TABLE territories(
    territoryID	INT PRIMARY KEY,
    territoryDescription VARCHAR(50),
    regionID INT
);
ALTER TABLE territories
    ADD FOREIGN KEY (regionID) REFERENCES regions(regionID) ON DELETE CASCADE;

COPY territories FROM '/Users/oguzhanbekar/OneDrive/Spiced/euclidean-eukalyptus-encounter-notes/05_week/northwind/territories.csv' DELIMITER ',' CSV HEADER;

DROP TABLE IF EXISTS employees;
CREATE TABLE employees(
    employeeID INT PRIMARY KEY,
    lastName VARCHAR(50),
    firstName VARCHAR(50),
    title VARCHAR(50),
    titleOfCourtesy VARCHAR(50),
    birthDate DATE,
    hireDate DATE,
    address VARCHAR(100),
    city VARCHAR(50),
    region VARCHAR(50),
    postalCode VARCHAR(50),
    country VARCHAR(50),
    homePhone VARCHAR(50),
    extension INT,
    photo TEXT,
    notes TEXT,
    reportsTo INT,
    photoPath TEXT
);

COPY employees FROM '/Users/oguzhanbekar/OneDrive/Spiced/euclidean-eukalyptus-encounter-notes/05_week/northwind/employees.csv' DELIMITER ',' CSV HEADER NULL 'NULL';

