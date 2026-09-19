-- Total revenue for each category
select 
    p.category,
    sum(p.price * ot.quantity) as wills,
    sum(ot.quantity) as units_sold,
    count(DISTINCT ot.order_id) as orders_number
from order_items ot 
join products p on p.product_id = ot.product_id
GROUP BY p.category
ORDER BY wills desc;

-- Display the number od customer orders and their names
select
    c.name,
    count(o.order_id) as order_number
from customers c
join orders o on c.customer_id = o.customer_id
group by c.name
order by order_number desc;

--
with total_revenue as(
    SELECT
        o.customer_id,
        sum(p.price * oi.quantity) as total
    from products p
    join order_items oi on p.product_id = oi.product_id
    join orders o on o.order_id = oi.order_id
    GROUP BY o.customer_id 
)
SELECT 
    c.name,
    c.city,
    tr.total
from customers c
join total_revenue tr on tr.customer_id = c.customer_id
ORDER BY tr.total desc 
limit 5;

