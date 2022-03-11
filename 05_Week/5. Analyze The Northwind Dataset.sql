-- Get the names and the quantities in stock for each product.
SELECT productname, unitsinstock FROM products;

-- Get a list of current products (Product ID and name).
SELECT productid, productname FROM products;

-- Get a list of the most and least expensive products (name and unit price).
SELECT productname, unitprice FROM products WHERE unitprice = (SELECT MAX(unitprice)
FROM products) OR unitprice = (SELECT MIN(unitprice) FROM products);

-- Get products that cost less than $20.
SELECT productname, unitprice FROM products WHERE unitprice<20;

-- Get products that cost between $15 and $25.
SELECT productname, unitprice FROM products WHERE unitprice BETWEEN 15 AND 25;

-- Get products above average price.
SELECT productname, unitprice FROM products WHERE unitprice> (SELECT AVG(unitprice) FROM products);

-- Find the ten most expensive products.
SELECT productname, unitprice FROM products WHERE unitprice> (SELECT AVG(unitprice)
FROM products) ORDER BY unitprice DESC LIMIT 10;

-- Get a list of discontinued products (Product ID and name).
SELECT productid, productname, discontinued FROM products;

-- Count current and discontinued products.
SELECT COUNT(discontinued) FROM products WHERE discontinued=0;

-- Find products with less units in stock than the quantity on order.
SELECT productname,unitsinstock,unitsonorder FROM products WHERE unitsonorder>unitsinstock;

-- Find the customer who had the highest order amount
SELECT orders.customerid, order_details.quantity
FROM orders LEFT JOIN order_details
ON orders.orderid = order_details.orderid
ORDER BY order_details.quantity DESC;
-- Get orders for a given employee and the according customer
SELECT orderid,customerid,employeeid FROM orders;

-- Find the hiring age of each employee
SELECT FLOOR(('2022-01-01'-birthdate)/365.25) FROM employees;

-- Create views and/or named queries for some of these queries
CREATE VIEW sales_by_customer_temp AS
SELECT orders.customerid, order_details.quantity
FROM orders LEFT JOIN order_details
ON orders.orderid = order_details.orderid
ORDER BY order_details.quantity DESC;