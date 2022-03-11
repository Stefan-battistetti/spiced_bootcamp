-- Count the number of products in the products table.
SELECT COUNT ( DISTINCT productname) AS "Unique_Products" FROM products;

-- Separate currently available and discontinued products
SELECT COUNT ( DISTINCT unitsinstock) AS "Unique_unitsinstock" FROM products;

SELECT COUNT ( DISTINCT discontinued) AS "Unique_discontinued" FROM products;

-- Frequently ordered products
SELECT productname, unitsonorder FROM products WHERE unitsonorder!=0;

-- Calculate the percentage of a product on the total number of orders.
SELECT unitsonorder*0.1*1000 / (SELECT SUM(unitsonorder) FROM products) FROM products WHERE unitsonorder!=0;

-- From the Customers table, retrieve all rows containing your country.
SELECT * FROM customers WHERE country='France';

