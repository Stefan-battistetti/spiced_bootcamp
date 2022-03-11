-- 1. Get the names and the quantities in stock for each product
SELECT productname, quantityperunit, unitsinstock
FROM products;

-- 2. Get a list of current products (Product ID and name).
SELECT productid, productname
FROM products
WHERE unitsinstock > 0;

-- 3. Get a list of the most and least expensive products (name and unit price).
SELECT  productname, unitprice
FROM products
WHERE unitprice = (SELECT MAX(unitprice) FROM products) 
OR unitprice = (SELECT MIN(unitprice) FROM products)
ORDER BY unitprice DESC;

-- 4. Get products that cost less than $20.
SELECT productid, productname, unitprice
FROM products
WHERE unitprice < 20
ORDER BY unitprice DESC;

-- 5. Get products that cost between $15 and $25.
SELECT productid, productname, unitprice
FROM products
WHERE unitprice BETWEEN 15 AND 25
ORDER BY unitprice DESC;

-- 6. Get products above average price.
SELECT productid, productname, unitprice
FROM products
WHERE unitprice >= (SELECT AVG(unitprice) FROM products)
ORDER BY unitprice DESC;

-- 7. Find the ten most expensive products.
SELECT productid, productname, unitprice
FROM products
ORDER BY unitprice DESC
LIMIT 10;

-- 8. Get a list of discontinued products (Product ID and name).
SELECT productid, productname
FROM products
WHERE discontinued = 1;

-- 9. Count current and discontinued products.
SELECT COUNT(discontinued = 0 OR NULL) AS count_current_product, COUNT(discontinued = 1 OR NULL) AS count_discontinued_product
FROM products;

-- 10. Find products with less units in stock than the quantity on order.
SELECT productid, productname, unitsinstock, unitsonorder, unitsinstock - unitsonorder AS difference
FROM products
WHERE unitsinstock >= unitsonorder
ORDER BY difference ASC;

-- 11. Find the customer who had the highest order amount
SELECT o.orderid, c.customerid, c.companyname, od.productid, od.unitprice, od.quantity, od.discount, od.unitprice*od.quantity*(1-od.discount) AS amount_order
FROM orders o
JOIN customers c
ON o.customerid = c.customerid
JOIN order_details od
ON o.orderid = od.orderid
ORDER BY amount_order DESC
LIMIT 1;
-- quantity on order_dtails table is per unit, discount is total discount here.

-- Get orders for a given employee and the according customer
-- if name is Nancy Davolio.
SELECT o.employeeid, o.orderid, c.companyname
FROM orders o
JOIN employees e
ON o.employeeid = e.employeeid
JOIN customers c
ON o.customerid = c.customerid
WHERE e.lastname = 'Davolio' AND e.firstname = 'Nancy';

-- 13. Find the hiring age of each employee
SELECT employeeid, birthdate, hiredate, DATE_PART('year', hiredate)- DATE_PART('year', birthdate)AS hiring_age
FROM employees;
-- difference between year of birthdate and year of hiredate

-- which of our customers never made any orders
SELECT companyname
FROM orders o 
RIGHT JOIN customers c
ON o.customerid = c.customerid
WHERE orderid IS NULL;

-- what is the average weight of all orders delivered to each country
-- average weight more than 10
SELECT c.country, AVG(o.freight) AS weight
FROM orders o
INNER JOIN customers c
ON o.customerid = c.customerid
GROUP BY c.country
HAVING AVG(o.freight) > 10
ORDER BY weight DESC;


-- what is the total revenue delivered to each country?
-- e.g. total money made from all orders to each country
SELECT c.country, SUM(od.unitprice*od.quantity*(1-od.discount)) AS total_revenue
FROM order_details od
JOIN orders o
ON od.orderid = o.orderid
JOIN customers c
ON o.customerid = c.customerid
GROUP BY c.country
ORDER BY total_revenue DESC;

SELECT *
FROM country_code

























