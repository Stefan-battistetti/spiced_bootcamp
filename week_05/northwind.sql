-- CREATE TABLE countries(
-- -- column__name, datatype, constraint
-- country_id SERIAL PRIMARY KEY,
-- country VARCHAR(40) NOT NULL,
-- population VARCHAR(60),
-- fertility NUMERIC,
-- continent VARCHAR(40)
-- );

-- \copy countries FROM '/Data_Modeling/large_countries_2015.csv' DELIMITER ',' CSV HEADER;

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
photoPath TEXT,
FOREIGN KEY(reportsTo) REFERENCES employees(employeeID) ON DELETE CASCADE
);

\copy employees FROM 'northwind/employees.csv' DELIMITER ',' CSV HEADER NULL 'NULL' ;

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

\copy customers FROM 'northwind/customers.csv' DELIMITER ',' CSV HEADER NULL 'NULL' ;

CREATE TABLE categories(
categoryID INT PRIMARY KEY,
categoryName VARCHAR(50),
description TEXT,
picture TEXT
);

\copy categories FROM 'northwind/categories.csv' DELIMITER ',' CSV HEADER NULL 'NULL' ;


CREATE TABLE regions(
regionID INT PRIMARY KEY,
regionDescription VARCHAR(9)
);

\copy regions FROM 'northwind/regions.csv' DELIMITER ',' CSV HEADER NULL 'NULL' ;


CREATE TABLE territories(
territoryID INT PRIMARY KEY,
territoryDescription VARCHAR(20) NOT NULL,
regionID INT,
FOREIGN KEY(regionID) REFERENCES regions(regionid) ON DELETE CASCADE
);

\copy territories FROM 'northwind/territories.csv' DELIMITER ',' CSV HEADER NULL 'NULL';

CREATE TABLE employee_territories(
employeeID INT,
territoryID INT,
FOREIGN KEY(employeeID) REFERENCES employees(employeeID) ON DELETE CASCADE,
FOREIGN KEY(territoryID) REFERENCES territories(territoryID) ON DELETE CASCADE
);

\copy employee_territories FROM 'northwind/employee_territories.csv' DELIMITER ',' CSV HEADER NULL 'NULL' ;

CREATE TABLE suppliers(
supplierID INT PRIMARY KEY,
companyName VARCHAR(50),
contactName VARCHAR(50),
contactTitle VARCHAR(50),
address VARCHAR(100),
city VARCHAR(50),
region VARCHAR(50),
postalCode VARCHAR(50),
country VARCHAR(50),
phone VARCHAR(50),
fax VARCHAR(50),
homePage TEXT
);

\copy suppliers FROM 'northwind/suppliers.csv' DELIMITER ',' CSV HEADER NULL 'NULL' ;

CREATE TABLE shippers(
shipperID INT PRIMARY KEY,
companyName VARCHAR(50),
phone VARCHAR(50)
);

\copy shippers FROM 'northwind/shippers.csv' DELIMITER ',' CSV HEADER NULL 'NULL' ;


CREATE TABLE products(
productID INT PRIMARY KEY,
productName VARCHAR(50),
supplierID INT,
categoryID INT,
quantityPerUnit VARCHAR(50),
unitPrice NUMERIC,
unitInStock INT,
unitsOnOrder INT,
reorderLevel INT,
discontinued INT,
FOREIGN KEY(supplierID) REFERENCES suppliers(supplierid) ON DELETE CASCADE,
FOREIGN KEY(categoryID) REFERENCES categories(categoryID) ON DELETE CASCADE
);

\copy products FROM 'northwind/products.csv' DELIMITER ',' CSV HEADER NULL 'NULL' ;

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
shipAddress VARCHAR(50),
shipCity VARCHAR(50),
shipRegion VARCHAR(50),
shipPostalCode VARCHAR(50),
shipCountry VARCHAR(50),
FOREIGN KEY(customerID) REFERENCES customers(customerID) ON DELETE CASCADE,
FOREIGN KEY(employeeID) REFERENCES employees(employeeID) ON DELETE CASCADE,
FOREIGN KEY(shipVia) REFERENCES shippers(shipperID) ON DELETE CASCADE
);

\copy orders FROM 'northwind/orders.csv' DELIMITER ',' CSV HEADER NULL 'NULL' ; 

CREATE TABLE order_details(
orderID INT,
productID INT,
unitPrice NUMERIC,
quantity INT,
discount NUMERIC,
FOREIGN KEY(orderID) REFERENCES orders(orderID) ON DELETE CASCADE,
FOREIGN KEY(productID) REFERENCES products(productID) ON DELETE CASCADE
);

\copy order_details FROM 'northwind/order_details.csv' DELIMITER ',' CSV HEADER NULL 'NULL' ;
