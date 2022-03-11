5.3. SQL Queries.SQL

-- First sql Queries
-- Count total number of products
--
-- 1) Count the number of products in the products table.

SELECT count(productid) FROM products;

 count
-------
    77
(1 row)

-- #####Separate currently available and discontinued products########
--
-- 2) Count separate numbers for currently available and discontinued products.

SELECT count(productid) AS AvailableProducs FROM products WHERE unitsinstock > 0;
SELECT count(productid) AS outofstock FROM products WHERE discontinued <> 0;
SELECT count(productid) AS AVAIBLE, count(productid) AS OutOfStock FROM products WHERE unitsinstock > 0 AND discontinued <> 0;

-- 3)


METABASE
-- subquery has been created by the metabase itself
SELECT "source"."totalsale" AS "totalsale", "source"."firstname" AS "firstname", "source"."lastname" AS "lastname"
--"my" query of the sales per employee from northwind
FROM (
select sum(orderdetails.quantity*orderdetails.unitprice) totalsale, firstname, lastname
from orders
left join order_details as orderdetails on orderdetails.orderid=orders.orderid
left join employees on orders.employeeid=employees.employeeid
left join products on orderdetails.productid=products.productid
group by firstName,lastname
order by totalsale desc
) "source"
LIMIT 1048575
