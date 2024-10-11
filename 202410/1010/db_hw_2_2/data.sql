-- Active: 1728541880118@@127.0.0.1@3306
CREATE Table orders (
  order_id INTEGER PRIMARY KEY autoincrement,
  order_data DATE,
  total_amount REAL
);

INSERT INTO orders (
  order_data, total_amount
)
VALUES ('2023-07-15', 50.99),
  ('2023-07-16', 75.5),
  ('2023-07-17', 30.25);

CREATE TABLE customers (
  customer_id INTEGER PRIMARY KEY autoincrement,
  name TEXT,
  email TEXT,
  phone TEXT
);

INSERT INTO customers (
  name, email, phone
)
VALUES ('허균', 'hong.gildong@example.com', '010-1234-5678'),
  ('김영희', 'kim.younghee@example.com', '010-9876-5432'),
  ('이철수', 'lee.cheolsu@example.com', '010-5555-4444');

UPDATE customers SET name='홍길동' WHERE customer_id=1;
DELETE FROM orders WHERE order_id=3;

SELECT * FROM orders;
SELECT * FROM customers;