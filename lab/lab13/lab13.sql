.read data.sql


CREATE TABLE average_prices AS
  SELECT category AS category, AVG(MSRP) AS average_price FROM products GROUP BY category;


CREATE TABLE lowest_prices AS
  SELECT store AS store, item AS item, MIN(price) FROM inventory GROUP BY item;


CREATE TABLE shopper_list_helper AS
  SELECT category AS category, name AS name, MIN(MSRP/rating) AS score FROM products GROUP BY category;

CREATE TABLE shopping_list AS
  SELECT p.name AS name, s.store AS store FROM shopper_list_helper AS p, lowest_prices AS s
  	WHERE p.name = s.item;

CREATE TABLE total_bandwidth AS
  SELECT SUM(Mbs) FROM shopping_list AS list, stores AS s WHERE s.store = list.store;

