DROP TABLE IF EXISTS customers;

CREATE TABLE customers(
customerID VARCHAR(50) PRIMARY KEY NOT NULL, 
   companyName VARCHAR(50) NOT NULL,
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

\copy customers FROM '/Users/shoheisuzuki/workspace/euclidean-eukalyptus/work/05_week/northwind/customers.csv' DELIMITER ',' CSV HEADER NULL 'NULL';



DROP TABLE IF EXISTS orders;

CREATE TABLE orders(
orderID INT PRIMARY KEY NOT NULL,
   customerID VARCHAR(50) REFERENCES customers(customerID),
   employeeID INT,
   orderDate DATE,
   requiredDate DATE,
   shippedDate DATE,
   shipVia INT,
   freight DOUBLE PRECISION,
   shipName VARCHAR(50),
   shipAddress VARCHAR(100),
   shipCity VARCHAR(50),
   shipRegion VARCHAR(50),
   shipPostalCode VARCHAR(50),
   shipCountry VARCHAR(50)
);

\copy orders FROM '/Users/shoheisuzuki/workspace/euclidean-eukalyptus/work/05_week/northwind/orders.csv' DELIMITER ',' CSV HEADER NULL 'NULL';



DROP TABLE IF EXISTS territories;

CREATE TABLE territories(
territoryID INT PRIMARY KEY,
    territoryDescription VARCHAR(50),
    regionID INT
);

\copy territories FROM '/Users/shoheisuzuki/workspace/euclidean-eukalyptus/work/05_week/northwind/territories.csv' DELIMITER ',' CSV HEADER NULL 'NULL';



DROP TABLE IF EXISTS employee_territories;

CREATE TABLE employee_territories(
employeeID INT,
   territoryID INT REFERENCES territories(territoryID)
);

\copy employee_territories FROM '/Users/shoheisuzuki/workspace/euclidean-eukalyptus/work/05_week/northwind/employee_territories.csv' DELIMITER ',' CSV HEADER NULL 'NULL';



DROP TABLE IF EXISTS regions;

CREATE TABLE regions(
regionID INT PRIMARY KEY,
    regionDescription VARCHAR(225)
);

\copy regions FROM '/Users/shoheisuzuki/workspace/euclidean-eukalyptus/work/05_week/northwind/regions.csv' DELIMITER ',' CSV HEADER NULL 'NULL';



DROP TABLE IF EXISTS shippers;

CREATE TABLE shippers(
shipperID INT PRIMARY KEY,
   companyName VARCHAR(50),
   phone VARCHAR(50)
);

\copy shippers FROM '/Users/shoheisuzuki/workspace/euclidean-eukalyptus/work/05_week/northwind/shippers.csv' DELIMITER ',' CSV HEADER NULL 'NULL';



ALTER TABLE territories ADD FOREIGN KEY (regionID)
REFERENCES regions(regionID) ON DELETE CASCADE;

ALTER TABLE orders ADD FOREIGN KEY (customerID)
REFERENCES customers(customerID) ON DELETE CASCADE;

ALTER TABLE orders ADD FOREIGN KEY (shipVia)
REFERENCES shippers(shipperID) ON DELETE CASCADE;


DROP TABLE IF EXISTS suppliers;

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

\copy suppliers FROM '/Users/shoheisuzuki/workspace/euclidean-eukalyptus/work/05_week/northwind/suppliers.csv' DELIMITER ',' CSV HEADER NULL 'NULL';



DROP TABLE IF EXISTS products;

CREATE TABLE products(
productID INT PRIMARY KEY,
   productName VARCHAR(50),
   supplierID INT REFERENCES suppliers(supplierID),
   categoryID INT,
   quantityPerUnit VARCHAR(50),
   unitPrice DOUBLE PRECISION,
   unitsInStock INT,
   unitsOnOrder INT,
   reorderLevel INT,
   discontinued INT
);

\copy products FROM '/Users/shoheisuzuki/workspace/euclidean-eukalyptus/work/05_week/northwind/products.csv' DELIMITER ',' CSV HEADER NULL 'NULL';



DROP TABLE IF EXISTS order_details;

CREATE TABLE order_details(
orderID INT REFERENCES orders(orderID),
   productID INT REFERENCES products(productID),
   unitPrice DOUBLE PRECISION ,
   quantity INT,
   discount DOUBLE PRECISION
);

\copy order_details FROM '/Users/shoheisuzuki/workspace/euclidean-eukalyptus/work/05_week/northwind/order_details.csv' DELIMITER ',' CSV HEADER NULL 'NULL';



DROP TABLE IF EXISTS categories;

CREATE TABLE categories(
categoryID INT PRIMARY KEY,
   categoryName VARCHAR(50),
   description TEXT, 
   picture TEXT
);

\copy categories FROM '/Users/shoheisuzuki/workspace/euclidean-eukalyptus/work/05_week/northwind/categories.csv' DELIMITER ',' CSV HEADER NULL 'NULL';



ALTER TABLE products ADD FOREIGN KEY (categoryID)
REFERENCES categories(categoryID) ON DELETE CASCADE;



DROP TABLE IF EXISTS categories;

CREATE TABLE categories(
categoryID INT PRIMARY KEY,
   categoryName VARCHAR(50),
   description TEXT, 
   picture TEXT
);

\copy categories FROM '/Users/shoheisuzuki/workspace/euclidean-eukalyptus/work/05_week/northwind/categories.csv' DELIMITER ',' CSV HEADER NULL 'NULL';



ALTER TABLE products ADD FOREIGN KEY (categoryID)
REFERENCES categories(categoryID) ON DELETE CASCADE;



DROP TABLE IF EXISTS employees;

CREATE TABLE employees(
employeeID  INT PRIMARY KEY,
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
   reportsTo INT REFERENCES products(productID),
   photoPath TEXT
);

\copy employees FROM '/Users/shoheisuzuki/workspace/euclidean-eukalyptus/work/05_week/northwind/employees.csv' DELIMITER ',' CSV HEADER NULL 'NULL';


-- reportsT0 column on employee is foreign key for regionID on regions table?

DROP TABLE IF EXISTS country_code;

CREATE TABLE country_code(
country  VARCHAR(50),
   countryCode VARCHAR(50)
);

\copy country_code FROM '/Users/shoheisuzuki/workspace/euclidean-eukalyptus/work/05_week/northwind/country_code.csv' DELIMITER ',' CSV HEADER NULL 'NULL';
