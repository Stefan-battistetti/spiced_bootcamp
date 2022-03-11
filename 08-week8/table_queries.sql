--- inserting entrance with t0 timestamp into each table ---
	
--Mon
		INSERT INTO monday (timestamp, customer_no, location_1)
		SELECT 
		min(timestamp) - (1 * interval '1 minute') AS timestamp, 
		customer_no,
		'entrance' AS location_1
		FROM monday
		GROUP BY customer_no;
	--Tues
		INSERT INTO tuesday (timestamp, customer_no, location_1)
		SELECT 
		min(timestamp) - (1 * interval '1 minute') AS timestamp, 
		customer_no,
		'entrance' AS location_1
		FROM tuesday
		GROUP BY customer_no;
	--Wed
		INSERT INTO wednesday (timestamp, customer_no, location_1)
		SELECT 
		min(timestamp) - (1 * interval '1 minute') AS timestamp, 
		customer_no,
		'entrance' AS location_1
		FROM wednesday
		GROUP BY customer_no;
	--Thur
		INSERT INTO thursday (timestamp, customer_no, location_1)
		SELECT 
		min(timestamp) - (1 * interval '1 minute') AS timestamp, 
		customer_no,
		'entrance' AS location_1
		FROM thursday
		GROUP BY customer_no;
	--Fri
		INSERT INTO friday (timestamp, customer_no, location_1)
		SELECT 
		min(timestamp) - (1 * interval '1 minute') AS timestamp, 
		customer_no,
		'entrance' AS location_1
		FROM friday
		GROUP BY customer_no;

	
--- viewing customers with no checkout location (quality control only)---

SELECT *
FROM monday
WHERE customer_no NOT IN (
	SELECT customer_no
	FROM monday
	WHERE location_1 = 'checkout' 
	);	

SELECT *
FROM tuesday
WHERE customer_no NOT IN (
	SELECT customer_no
	FROM tuesday
	WHERE location_1 = 'checkout' 
	);	

SELECT *
FROM wednesday
WHERE customer_no NOT IN (
	SELECT customer_no
	FROM wednesday
	WHERE location_1 = 'checkout' 
	);

SELECT *
FROM thursday
WHERE customer_no NOT IN (
	SELECT customer_no
	FROM thursday
	WHERE location_1 = 'checkout' 
	);

SELECT *
FROM friday
WHERE customer_no NOT IN (
	SELECT customer_no
	FROM friday
	WHERE location_1 = 'checkout' 
	);
	


--- INSERTING CHECKOUT TO THOSE FOREVER IN STORE ---

INSERT INTO monday (timestamp, customer_no, location_1)
SELECT
	max(timestamp) + (1 * interval '1 minute') AS timestamp,
	customer_no,
	'checkout' AS location_1
	FROM 
		(SELECT *
		FROM monday
		WHERE customer_no NOT IN (
			SELECT customer_no
			FROM monday
			WHERE location_1 = 'checkout')
			) AS foo
	GROUP BY customer_no;
			
INSERT INTO tuesday (timestamp, customer_no, location_1)
SELECT
	max(timestamp) + (1 * interval '1 minute') AS timestamp,
	customer_no,
	'checkout' AS location_1
	FROM 
		(SELECT *
		FROM tuesday
		WHERE customer_no NOT IN (
			SELECT customer_no
			FROM tuesday
			WHERE location_1 = 'checkout')
			) AS foo
	GROUP BY customer_no;	

INSERT INTO wednesday (timestamp, customer_no, location_1)
SELECT
	max(timestamp) + (1 * interval '1 minute') AS timestamp,
	customer_no,
	'checkout' AS location_1
	FROM 
		(SELECT *
		FROM wednesday
		WHERE customer_no NOT IN (
			SELECT customer_no
			FROM wednesday
			WHERE location_1 = 'checkout')
			) AS foo
	GROUP BY customer_no;

INSERT INTO thursday (timestamp, customer_no, location_1)
SELECT
	max(timestamp) + (1 * interval '1 minute') AS timestamp,
	customer_no,
	'checkout' AS location_1
	FROM 
		(SELECT *
		FROM thursday
		WHERE customer_no NOT IN (
			SELECT customer_no
			FROM thursday
			WHERE location_1 = 'checkout')
			) AS foo
	GROUP BY customer_no;

INSERT INTO friday (timestamp, customer_no, location_1)
SELECT
	max(timestamp) + (1 * interval '1 minute') AS timestamp,
	customer_no,
	'checkout' AS location_1
	FROM 
		(SELECT *
		FROM friday
		WHERE customer_no NOT IN (
			SELECT customer_no
			FROM friday
			WHERE location_1 = 'checkout')
			) AS foo
	GROUP BY customer_no;

--- Inserting Exit into each day table ---

INSERT INTO monday (timestamp, customer_no, location_1)
SELECT
	max(timestamp) + (1 * interval '1 minute') AS timestamp,
	customer_no,
	'exit' AS location_1
	FROM 
		(SELECT *
			FROM monday 
			WHERE location_1 = 'checkout'
			) AS foo
	GROUP BY customer_no;
	
INSERT INTO tuesday (timestamp, customer_no, location_1)
SELECT
	max(timestamp) + (1 * interval '1 minute') AS timestamp,
	customer_no,
	'exit' AS location_1
	FROM 
		(SELECT *
			FROM tuesday 
			WHERE location_1 = 'checkout'
			) AS foo
	GROUP BY customer_no;
	
INSERT INTO wednesday (timestamp, customer_no, location_1)
SELECT
	max(timestamp) + (1 * interval '1 minute') AS timestamp,
	customer_no,
	'exit' AS location_1
	FROM 
		(SELECT *
			FROM wednesday 
			WHERE location_1 = 'checkout'
			) AS foo
	GROUP BY customer_no;
	
INSERT INTO thursday (timestamp, customer_no, location_1)
SELECT
	max(timestamp) + (1 * interval '1 minute') AS timestamp,
	customer_no,
	'exit' AS location_1
	FROM 
		(SELECT *
			FROM thursday 
			WHERE location_1 = 'checkout'
			) AS foo
	GROUP BY customer_no;
	
INSERT INTO friday (timestamp, customer_no, location_1)
SELECT
	max(timestamp) + (1 * interval '1 minute') AS timestamp,
	customer_no,
	'exit' AS location_1
	FROM 
		(SELECT *
			FROM friday 
			WHERE location_1 = 'checkout'
			) AS foo
	GROUP BY customer_no;
	
--- CREATING SINGLE TABLE WITH LOC1 AND LOC2 AND UNIQUE CUSTOMER NUMBERS ---

CREATE TABLE weekly_minute_data
AS
	SELECT 
	timestamp,
	CONCAT('01-', customer_no ) AS cust_id,
	location_1,
	CASE 
		WHEN location_1 = 'exit' THEN 'exit'
		ELSE LAG (location_1, -1) OVER (ORDER BY customer_no ASC, TIMESTAMP ASC)
		END AS location_2
	FROM monday
UNION ALL
	SELECT 
	timestamp,
	CONCAT('02-', customer_no ) AS cust_id,
	location_1,
	CASE 
		WHEN location_1 = 'exit' THEN 'exit'
		ELSE LAG (location_1, -1) OVER (ORDER BY customer_no ASC, TIMESTAMP ASC)
		END AS location_2
	FROM tuesday
UNION ALL
	SELECT 
	timestamp,
	CONCAT('03-', customer_no ) AS cust_id,
	location_1,
	CASE 
		WHEN location_1 = 'exit' THEN 'exit'
		ELSE LAG (location_1, -1) OVER (ORDER BY customer_no ASC, TIMESTAMP ASC)
		END AS location_2
	FROM wednesday
UNION ALL
	SELECT 
	timestamp,
	CONCAT('04-', customer_no ) AS cust_id,
	location_1,
	CASE 
		WHEN location_1 = 'exit' THEN 'exit'
		ELSE LAG (location_1, -1) OVER (ORDER BY customer_no ASC, TIMESTAMP ASC)
		END AS location_2
	FROM thursday
UNION ALL
	SELECT 
	timestamp,
	CONCAT('05-', customer_no ) AS cust_id,
	location_1,
	CASE 
		WHEN location_1 = 'exit' THEN 'exit'
		ELSE LAG (location_1, -1) OVER (ORDER BY customer_no ASC, TIMESTAMP ASC)
		END AS location_2
	FROM friday;

--- Creating table with just location_1 plus entrance and exit ---

CREATE TABLE weekly_loc1_data
AS
	SELECT 
	timestamp,
	CONCAT('01-', customer_no ) AS cust_id,
	location_1
	FROM monday
UNION ALL
	SELECT 
	timestamp,
	CONCAT('02-', customer_no ) AS cust_id,
	location_1
	FROM tuesday
UNION ALL
	SELECT 
	timestamp,
	CONCAT('03-', customer_no ) AS cust_id,
	location_1
	FROM wednesday
UNION ALL
	SELECT 
	timestamp,
	CONCAT('04-', customer_no ) AS cust_id,
	location_1
	FROM thursday
UNION ALL
	SELECT 
	timestamp,
	CONCAT('05-', customer_no ) AS cust_id,
	location_1
	FROM friday;
