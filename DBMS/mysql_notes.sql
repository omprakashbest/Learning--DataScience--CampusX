CREATE DATABASE IF NOT EXISTS campusx;
USE campusx;

CREATE TABLE users_sample(
	user_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL unique,
    password VARCHAR(255) NOT NULL
);

-- single values insertion 
INSERT INTO users_sample (user_id, name, email, password) VALUES (NULL, 'Om', 'omprakashbest3@gmail.com', '12345');
INSERT INTO users_sample (user_id, name, email, password) VALUES (NULL, 'ankit', 'ankit@gmail.com', '12345'); 

-- Mulitple insertion 
INSERT INTO users_sample VALUES (NULL, 'Priya', 'priya@gmail.com', '12345'),
(NULL, 'Rahul', 'rahul@gmail.com', '1234'),
(NULL, 'Anshika', 'anshika@gmail.com', '1234');

-- SELECT KEY
-- select everything
SELECT * FROM smartphones;

-- select only model and prices columns.
SELECT model, price FROM smartphones;

-- select model and battery_capacity and OS
SELECT model, battery_capacity, os FROM smartphones;

-- Alias
SELECT model, battery_capacity AS mAHs,os AS 'Operating System' FROM smartphones;

-- create expression using columns
-- calculate the ppi of resolution_width and height used formula 
SELECT model,
sqrt((resolution_width*resolution_width) + (resolution_height*resolution_height)) / screen_size AS PPI
FROM smartphones;

-- Rating Columns change into out of 10.
SELECT model, rating/10 as Rating 
FROM smartphones;

-- creating Constants Columns 
SELECT model, 'smartphones' as 'type'
FROM smartphones; 

-- Distinct(unique) values from a column
SELECT DISTINCT(brand_name) AS ALL_Brands
FROM smartphones;

-- Example: How many brands in processor
SELECT DISTINCT(processor_brand) as all_processor
FROM smartphones;

-- DISTINCT combo
SELECT DISTINCT brand_name, processor_brand
FROM smartphones;

-- filter rows where clause
-- Q: find all samsung phones
SELECT brand_name, model, price, rating/10 as rating
FROM smartphones
WHERE brand_name = 'samsung';

-- Q: find all phones wiht price > 50,000
SELECT * FROM smartphones
WHERE price > 50000;

-- BETWEEN OPERATOR
-- Q: find all phones in the price range of 10,000 and 20,000?

-- one way 
select * from smartphones where 
price > 10000 and price < 20000;

-- Second way using between operator.
SELECT * FROM 
smartphones
WHERE price BETWEEN 10000 and 20000;

-- Q: find phones with rating > 80 and price < 25000
SELECT * FROM smartphones 
WHERE rating > 80 AND price < 25000;

-- Q: find all samsung phones with ram > 8GB
SELECT * FROM smartphones 
WHERE brand_name = 'samsung' and ram_capacity > 8;

-- Q: find all samsung phones with snapdragon processor ?
SELECT * FROM smartphones
WHERE brand_name = 'samsung' and processor_brand = 'snapdragon';

-- Q: find brands who sell phones with price > 50000
SELECT DISTINCT brand_name
FROM smartphones 
WHERE price > 50000;

-- IN and  NOT IN operator 
-- One way
select * from
smartphones
where processor_brand = 'snapdragon' or 
processor_brand = 'exynos' or 
processor_brand = 'bionic';

-- Second way using IN operator
SELECT * FROM 
smartphones
WHERE processor_brand IN ('snapdragon', 'exynos', 'bionic');

-- UPDATE operation
-- Example: 
UPDATE smartphones
SET processor_brand = 'demensity'
WHERE processor_brand = 'mediatek';

-- DELETE operation
-- Example:
DELETE FROM 
smartphones
WHERE price > 200000;

-- Another Example:
DELETE FROM 
smartphones
WHERE primary_camera_rear > 150 AND brand_name = 'samsung';

-- Types of Functions in SQL
-- 1. Aggregate functions:
-- MAX/MIN

-- Q: find the minimum and maximum price ?
SELECT MAX(price) AS MAX_price
FROM smartphones;

SELECT MIN(price) as Min_price
FROM smartphones;

-- find the maximum and minimum ram capacity value
SELECT MAX(ram_capacity) 
FROM smartphones;

SELECT MIN(ram_capacity) 
FROM smartphones;

-- Q: find the price of the costlist samsung phone ?
SELECT MAX(price) 
FROM smartphones
WHERE brand_name = 'samsung';

-- AVG (Average)
-- Q: find avg rating of apple phones
SELECT AVG(rating)
FROM smartphones
WHERE brand_name = 'apple'; 

-- SUM
SELECT SUM(price)
FROM smartphones;

-- COUNT
-- Q: find the number of oneplus phones ?
SELECT COUNT(*)
FROM smartphones
WHERE brand_name = 'oneplus';

-- COUNT(DISTINCT)
-- Q: find the number of brands available ?
SELECT COUNT(DISTINCT(brand_name)) 
FROM smartphones;

-- STD (standard deviation)
-- Q: find std of screen sizes
SELECT STD(screen_size)
FROM smartphones;

-- Variance
-- Q: find variance of screen size
SELECT variance(screen_size)
FROM smartphones;


-- SCALAR FUNCITONS --

-- ABS absolute value
-- Q: find difference from avg rating of all samsung phone ratings

-- ROUND --
-- Q:  round the ppi to 1 decimal place
SELECT model,
ROUND(sqrt((resolution_width*resolution_width) + (resolution_height*resolution_height)) / screen_size, 1) AS PPI
FROM smartphones;

-- CEIL / FLOOR
-- Example: 
SELECT CEIL(screen_size) 
FROM smartphones;

SELECT FLOOR(screen_size)
FROM smartphones;


-- SQL Grouping + Sorting ----
-- SORTING Data 

-- Q: find top 5 samsung phones with biggest screen size ?
SELECT model, price, screen_size
FROM smartphones
WHERE brand_name = 'samsung'select * from smartphones where 
price > 10000 and price < 20000;
ORDER BY screen_size desc, price
limit 5;

-- Q: Sort all the phones in descreasing order of number of total cameras ?
SELECT brand_name, model, (num_rear_cameras + num_front_cameras) as total_cameras
FROM smartphones
ORDER BY total_cameras desc;

-- Q: sort data on the basis of ppi in descreasing order ?
SELECT model, 
round(sqrt(resolution_width*resolution_width + resolution_height*resolution_height) / screen_size, 2) as ppi
FROM smartphones
ORDER BY ppi desc;

-- Q: find the phone with 2nd largest battery capacity ?
SELECT model, battery_capacity
FROM smartphones 
ORDER BY battery_capacity desc 
LIMIT 1,1; -- OFFSET (where to start,nums of rows to fetch)

-- Q: find the name and rating of the worst rated apple phone ?
SELECT model, rating 
FROM smartphones
WHERE brand_name = 'apple'
ORDER BY rating
limit 1;

-- Q: sort phones alphabetically and then on the basis of rating in desc order ?
SELECT *
FROM smartphones
ORDER BY brand_name, rating desc;

-- Q: sort phones alphabetically and then on the basis of price in asc order ?
SELECT *
FROM smartphones
ORDER BY brand_name, price asc;


-- GROUPING DATA -------

-- Q1: Group smartphones by brand_name and get the count, average price, max rating, avg screen_size and avg battery capacity ?
SELECT brand_name, COUNT(*) as total_phones, round(AVG(price)) as average_price, MAX(rating) as max_rating,
round(AVG(screen_size),1) as avg_screen_size, round(AVG(battery_capacity)) as avg_battery_capacity
FROM smartphones
GROUP BY brand_name
ORDER BY total_phones desc;

-- Q2: Group smartphones by whether they have an NFC and get the average price and rating ?
SELECT has_nfc, round(AVG(price)) as avg_price, ROUND(AVG(rating)) as avg_Rating
FROM smartphones
GROUP BY has_nfc; 

-- Q3: Group smartphones by extended memory available and get the average price ?
SELECT extended_memory_available, ROUND(AVG(price)) as avg_price
FROM smartphones
GROUP BY extended_memory_available;

-- Q4: Group smartphones by the brand and processor brand and get the count of models and the average primary camera resolution (rear)
SELECT brand_name, processor_brand, COUNT(*) as models , ROUND(AVG(primary_camera_rear)) AS resolution_rear
FROM  smartphones
GROUP BY brand_name, processor_brand;

-- Q: Find top 5 most costly phone brands ?
SELECT brand_name, ROUND(AVG(price)) AS price
FROM smartphones
GROUP BY brand_name
ORDER BY price desc
LIMIT 5;

-- Q: which brand makes the smallest screen smartphones ?
SELECT brand_name, AVG(screen_size) as screen
FROM smartphones
GROUP BY brand_name
ORDER BY screen
LIMIT 1;

-- Q: Group smartphones by the brand, and find the brand with the highest number of models that have both NFC and and IR blaster  ?
SELECT brand_name, COUNT(*) as models
FROM smartphones
WHERE has_nfc = 'True' and has_ir_blaster = 'True'
GROUP BY brand_name
ORDER BY models
LIMIT 1;

-- Q: find all samsung 5g enabled smartphones and find out the avg price for NFC and non-NFC phones ?
select brand_name, has_nfc, avg(price)
from smartphones
where brand_name = 'samsung' and has_5g = 'True'
group by has_nfc;


-- HAVING clause --

-- Q: find the avg rating of smartphones brands which have more than 20 phones ?
select brand_name,COUNT(*) as count, ROUND(AVG(rating)) as avg_rating
FROM smartphones 
GROUP BY brand_name
HAVING count > 20;


-- Q: find the top 3 brands with the highest avg ram that have a refresh rate of at least 90Hz and fast charging available and don't consider
-- brands which have less than 10 phones ?
SELECT brand_name,
AVG(ram_capacity) as avg_ram
FROM smartphones
WHERE refresh_rate >= 90 and fast_charging_available = 1
GROUP BY brand_name
HAVING COUNT(*) > 10
ORDER BY avg_ram desc
LIMIT 3;


-- Q: find the avg price of all the phone brands with avg rating > 70 and num_phones more than 10 among all 5g enabled phones ?

SELECT brand_name ,ROUND(AVG(price)) as avg_price, ROUND(AVG(rating)) as avg_rating 
FROM smartphones
WHERE has_5g = 'True' 
GROUP BY brand_name
HAVING COUNT(*) > 10 and avg_rating > 70;

-- Practice 
-- Q: Find the Top 5 batsman in IPL

SELECT batter, sum(batsman_run) as total_runs
FROM ipl
group by batter
order by total_runs desc 
LIMIT 5;

-- Q: find the 2nd highest 6 hitter in IPL
SELECT batter, count(*) as sixer
FROM ipl
WHERE batsman_run = 6
GROUP BY batter
ORDER BY sixer desc
LIMIT 1, 1;

-- Q: find the 10 batsman with centuries in IPL 
SELECT ID, batter, SUM(batsman_run) as centuries
FROM ipl
GROUP BY batter, ID
HAVING centuries >= 100
ORDER BY batter desc 
LIMIT 10;

-- Q: Find the top 5 batsman with highest strike rate who have played a minimum of 1000 balls 
SELECT batter, sum(batsman_run), count(batsman_run), ROUND((sum(batsman_run)/count(batsman_run)) * 100, 2) as strike_rate
FROM ipl
group by batter 
HAVING COUNT(batsman_run) > 1000
ORDER BY strike_rate DESC LIMIT 5;


-- JOINS --

-- CROSS JOIN --
SELECT * FROM sql_join.users t1
CROSS JOIN sql_join.groups t2;

-- INNER JOIN --
SELECT * FROM sql_join.membership t1
INNER JOIN sql_join.users t2
ON t1.user_id = t2.user_id;

-- LEFT JOIN --
SELECT * FROM sql_join.membership m
LEFT JOIN sql_join.users u 
ON m.user_id = u.user_id;

-- RIGHT JOIN --
SELECT * FROM sql_join.membership m
RIGHT JOIN sql_join.users u
ON m.user_id = u.user_id;

-- FULL OUTER JOIN -- 
SELECT * FROM sql_join.membership m
LEFT JOIN sql_join.users u 
ON m.user_id = u.user_id
UNION
SELECT * FROM sql_join.membership m
RIGHT JOIN sql_join.users u
ON m.user_id = u.user_id;


-- SQL Set Operator -- 
-- UNION --
SELECT * FROM sql_join.person1 
UNION 
SELECT * FROM sql_join.person2;

-- UNION ALL --
SELECT * FROM sql_join.person1 
UNION ALL
SELECT * FROM sql_join.person2;

-- INTERSECT --
SELECT * FROM sql_join.person1
INTERSECT
SELECT * FROM sql_join.person2;

-- EXCEPT or MINUS --
SELECT * FROM sql_join.person1
EXCEPT
SELECT * FROM sql_join.person2;

-- SELF JOIN --
SELECT * FROM sql_join.users1 t1
JOIN sql_join.users1 t2
ON t1.emergency_contact = t2.user_id;

-- Joining on more than one column
SELECT * FROM sql_join.students t1
JOIN sql_join.class t2 
ON t1.class_id = t2.class_id 
AND t1.enrollment_year = t2.class_year;

-- Joining more than 2 tables 
SELECT * FROM sql_join.order_details t1
INNER JOIN sql_join.orders t2
ON t1.order_id = t2.order_id 
INNER JOIN sql_join.users t3
ON t2.user_id = t3.user_id;

-- Filtering the Columns
-- 1. Find order_id, name and city by joining users and orders ?
SELECT t1.order_id, t2.name, t2.city
FROM sql_join.orders t1
INNER JOIN sql_join.users t2
ON t1.user_id = t2.user_id;

-- 2. Find order_id, product category by joining order_details and category.
SELECT t1.order_id, t2.vertical
FROM sql_join.order_details t1
INNER JOIN sql_join.category t2
ON t1.category_id = t2.category_id;

-- Filtering the Rows
-- Find all the orders placed in pune ?
SELECT * 
FROM sql_join.orders t1
INNER JOIN sql_join.users t2
ON t1.user_id = t2.user_id
WHERE t2.city = 'Pune';

-- Find all orders under Chairs category ?
SELECT *
FROM sql_join.order_details t1
INNER JOIN sql_join.category t2 
ON t1.category_id = t2.category_id
WHERE t2.vertical = 'Chairs';

-- Practice Questions:
-- Q: Find all profitable orders ?
SELECT t1.order_id, SUM(t2.profit) as profit
FROM sql_join.orders t1
INNER JOIN sql_join.order_details t2
ON t1.order_id = t2.order_id 
GROUP BY t1.order_id 
HAVING profit > 0;

-- Find the curstomer who has placed max number of orders ?

SELECT name, count(*) as num_orders 
FROM orders t1
INNER JOIN users t2
ON t1.user_id = t2.user_id 
GROUP BY name
ORDER BY num_orders desc 
limit 1; 

-- Which is the most profitable category ?
SELECT vertical, sum(profit)
FROM order_details t1
INNER JOIN category t2
ON t1.category_id = t2.category_id
GROUP BY vertical
ORDER BY sum(profit) desc
LIMIT  1;

-- which is the most profitable state ?
SELECT state, sum(profit)
FROM orders t1
INNER JOIN order_details t2
ON t1.order_id = t2.order_id
INNER JOIN users t3
ON t1.user_id = t3.user_id
group by state
ORDER BY sum(profit) desc
LIMIT 1;

-- Find all categories with profit higher than 5000 ?
SELECT vertical, sum(profit) as num_profit
FROM order_details t1
INNER JOIN category t2
ON t1.category_id = t2.category_id
GROUP BY vertical
HAVING num_profit > 5000;


-- Subquery --
-- Example :
-- Q: Find the movie with highest rating score?
SELECT * FROM movies
WHERE score = (SELECT MAX(score) FROM movies); 

-- Independent Subquery - Scalar Subquery --

-- Q: Find the movie with highest profit (vs order by) ?
SELECT * FROM movies 
WHERE (gross - budget) = (SELECT MAX(gross - budget) FROM movies); 

-- Q: Find how many movies have a rating > avg of all the movies ratings (find the cout of above average movies) ?
SELECT COUNT(*) FROM movies
WHERE score > (SELECT AVG(score) FROM movies);

-- Q: Find the highest rated movie of 2000 ?
SELECT * FROM movies 
WHERE year = 2000 AND score = (SELECT MAX(score) 
FROM movies WHERE year = 2000);

-- Q: Find the highest rated movie among all movies whose number of votes are > the dataset avg votes ?
SELECT * FROM movies
WHERE score = (SELECT MAX(score) FROM movies 
WHERE votes > (SELECT AVG(votes) FROM movies));


-- Independent Subquery - Row Subquery(One col Multi Rows) --

-- Q: Find all users who never ordered ?
SELECT * FROM users 
WHERE user_id NOT IN(
    SELECT DISTINCT(user_id) FROM orders);

-- Q: Find all the movies made by top 3 directors (in terms of total gross income) ?
-- cte -> common table expression [just for now ] -> MySQL doesn't yet support 'LIMIT & IN/ALL/ANY/SOME in subquery'.
WITH top_directors as (SELECT director FROM movies 
                            GROUP BY director 
                            ORDER BY SUM(gross) DESC
                            LIMIT 3
)
SELECT * FROM movies
WHERE director IN (SELECT * FROM top_directors);

-- Q: Find all movies of all those actors whose filmography's avg rating > 8.5 (take 25000 votes as cutoff) ?
SELECT * FROM movies
where star IN( 
    SELECT star FROM movies
    where votes > 25000
    GROUP BY star 
    HAVING AVG(score) > 8.5
);

-- Independent Subquery - Table Subquery (Multi col Multi Row) --
-- Q: Find the most profitable movie of each year ?
SELECT * FROM movies
WHERE (year, gross - budget) IN 
(SELECT year, MAX(gross - budget) FROM movies GROUP BY year);

-- Find the highest rated movie of each genre votes cutoff of 25000 ?
SELECT * FROM movies
WHERE (genre, score) IN (SELECT genre, MAX(score)
                            FROM movies
                            WHERE votes > 25000
                            GROUP BY genre
                            )
AND votes > 25000;

-- Q: Find the highest grossing movies of top 5 actor/director combo in terms of total gross income?
WITH top_duos as (
    SELECT star, director, MAX(gross)
    FROM movies
    GROUP BY star, director
    ORDER BY SUM(gross) DESC LIMIT 5
)
SELECT * FROM movies
WHERE (star, director, gross) IN (SELECT * FROM top_duos);


-- Correlated Subquery -- 

-- Q: Find all the movies that have a rating higher than the average rating of movies in the same genre ?
SELECT * FROM movies m1
WHERE score > (SELECT AVG(score) FROM movies m2 WHERE m2.genre = m1.genre);

-- Q: Find the favorite food of each customer ?

WITH fav_food as (
    SELECT t2.user_id, name, f_name, COUNT(*) as frequency FROM users t1
    JOIN orders t2 ON t1.user_id = t2.user_id 
    JOIN order_details t3 ON t2.order_id = t3.order_id 
    JOIN food t4 ON t3.f_id = t4.f_id 
    GROUP BY t2.user_id, t1.name, t3.f_id, t4.f_name
)
SELECT * FROM fav_food f1 
WHERE frequency = (
    SELECT MAX(frequency)
    FROM fav_food f2 
    WHERE f2.user_id = f1.user_id
);

-- Usage with SELECT -- 
-- Q: Get the percentage of votes for each movie compared to the total number of votes.?
SELECT name, (votes/(SELECT SUM(votes) FROM movies))*100 percentage FROM movies;

-- Q: Display all movie name, genre, score and avg(score) of genre ?
SELECT name, genre, score,
(SELECT AVG(score) FROM movies m2 WHERE m2.genre = m1.genre)
FROM movies m1;

-- Usage WITH FROM
-- Q: Display average rating of all the restaurants ?
SELECT r_name, avg_rating
FROM (SELECT r_id, AVG(restaurant_rating) as avg_rating
        FROM orders GROUP BY r_id) t1 
        JOIN restaurants t2 
        ON t1.r_id = t2.r_id;

-- Usage WITH HAVING -- 
-- Q: Find genres having avg score > avg score of all the movies ?
SELECT genre, AVG(score)
FROM movies
GROUP BY genre
HAVING AVG(score) > (SELECT AVG(score) FROM movies);

-- Usage WITH INSERT --
-- Populate an already created loyal_customers table with records of only those customers who have ordered food more than 3 times.
CREATE table loyal_users (
    user_id INTEGER NULL,
    name VARCHAR(50) NULL,
    money INTEGER NULL
);

INSERT INTO loyal_users (user_id, name)
SELECT t1.user_id, t2.name
FROM orders t1
JOIN users t2 ON
t1.user_id = t2.user_id
GROUP BY t1.user_id, t2.name
HAVING COUNT(*) > 3;

SELECT * FROM loyal_users;


-- Usage WITH UPDATE --
-- Populate the money cols of loyal_customer table using the orders table. Provide a 10% app money to all customers based on their order value.?
UPDATE loyal_users 
SET money = (SELECT SUM(amount) * 0.1
                FROM orders 
                WHERE orders.user_id = loyal_users.user_id);

-- Usage WITH DELETE
-- Delete all the customers record who have never ordered ?
DELETE FROM users
WHERE user_id NOT IN (SELECT DISTINCT(user_id) FROM orders);






