insert into customers (name, email, city, created_at) values
('Ali Ahmed',      'ali@example.com',     'Cairo',      '2025-01-01'),
('Sara Mohamed',   'sara@example.com',    'Alexandria', '2025-01-02'),
('Omar Khaled',    'omar@example.com',    'Giza',       '2025-01-03'),
('Layla Hassan',   'layla@example.com',   'Cairo',      '2025-01-05'),
('Youssef Nabil',  'youssef@example.com', 'Alexandria', '2025-01-07'),
('Mona Samir',     'mona@example.com',    'Cairo',      '2025-01-10'),
('Khaled Adel',    'khaled@example.com',  'Giza',       '2025-01-12'),
('Nour Ibrahim',   'nour@example.com',    'Mansoura',   '2025-01-15'),
('Hana Tarek',     'hana@example.com',    'Cairo',      '2025-01-18'),
('Mahmoud Ali',    'mahmoud@example.com', 'Alexandria', '2025-01-20');

insert into products (name, category, price, stock) values
('Laptop Pro 15',    'Electronics', 1200.00, 50),
('Wireless Mouse',   'Electronics',   25.00, 200),
('Mechanical Keyboard','Electronics', 85.00, 100),
('USB-C Hub',        'Electronics',   45.00, 150),
('Office Chair',     'Furniture',    250.00, 30),
('Standing Desk',    'Furniture',    400.00, 20),
('Notebook A5',      'Stationery',     5.00, 500),
('Pen Pack (10)',    'Stationery',     8.00, 300),
('Coffee Mug',       'Kitchen',       12.00, 100),
('Water Bottle',     'Kitchen',       18.00, 80),
('Desk Lamp',        'Furniture',     35.00, 60),
('Backpack',         'Accessories',   55.00, 40);

insert into orders (customer_id, order_date, status) values
(1,  '2025-01-05', 'delivered'),
(2,  '2025-01-07', 'delivered'),
(1,  '2025-01-10', 'delivered'),
(3,  '2025-01-12', 'delivered'),
(4,  '2025-01-15', 'delivered'),
(5,  '2025-01-18', 'delivered'),
(2,  '2025-01-20', 'delivered'),
(6,  '2025-01-25', 'delivered'),
(7,  '2025-02-01', 'delivered'),
(8,  '2025-02-03', 'delivered'),
(1,  '2025-02-05', 'delivered'),
(9,  '2025-02-08', 'delivered'),
(3,  '2025-02-10', 'delivered'),
(10, '2025-02-12', 'shipped'),
(4,  '2025-02-15', 'delivered'),
(5,  '2025-02-18', 'delivered'),
(2,  '2025-02-20', 'shipped'),
(6,  '2025-02-22', 'delivered'),
(7,  '2025-03-01', 'delivered'),
(8,  '2025-03-03', 'delivered'),
(1,  '2025-03-05', 'delivered'),
(9,  '2025-03-08', 'delivered'),
(10, '2025-03-10', 'shipped'),
(3,  '2025-03-12', 'delivered'),
(4,  '2025-03-15', 'delivered'),
(2,  '2025-03-18', 'delivered'),
(5,  '2025-03-20', 'shipped'),
(6,  '2025-03-22', 'delivered'),
(7,  '2025-03-25', 'pending'),
(8,  '2025-03-28', 'delivered');

insert into order_items (order_id, product_id, quantity) values
-- الطلب 1
(1, 1, 1), (1, 2, 2),
-- الطلب 2
(2, 3, 1), (2, 7, 5),
-- الطلب 3
(3, 5, 1),
-- الطلب 4
(4, 2, 1), (4, 8, 3),
-- الطلب 5
(5, 6, 1), (5, 11, 2),
-- الطلب 6
(6, 9, 2), (6, 10, 1),
-- الطلب 7
(7, 12, 1),
-- الطلب 8
(8, 1, 1), (8, 4, 2),
-- الطلب 9
(9, 7, 10),
-- الطلب 10
(10, 5, 1), (10, 11, 1),
-- الطلب 11
(11, 1, 1), (11, 2, 1), (11, 3, 1),
-- الطلب 12
(12, 9, 3),
-- الطلب 13
(13, 6, 1),
-- الطلب 14
(14, 10, 2), (14, 12, 1),
-- الطلب 15
(15, 4, 1),
-- الطلب 16
(16, 1, 1), (16, 5, 2),
-- الطلب 17
(17, 8, 5),
-- الطلب 18
(18, 3, 2), (18, 7, 3),
-- الطلب 19
(19, 2, 4),
-- الطلب 20
(20, 6, 1), (20, 11, 2),
-- الطلب 21
(21, 1, 2),
-- الطلب 22
(22, 12, 2), (22, 9, 1),
-- الطلب 23
(23, 5, 1),
-- الطلب 24
(24, 3, 1), (24, 4, 1),
-- الطلب 25
(25, 1, 1), (25, 2, 2), (25, 7, 5),
-- الطلب 26
(26, 6, 1),
-- الطلب 27
(27, 10, 1), (27, 11, 1),
-- الطلب 28
(28, 12, 1),
-- الطلب 29
(29, 8, 10),
-- الطلب 30
(30, 1, 1), (30, 5, 1);