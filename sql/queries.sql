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

--
select
    c.name,
    count(o.order_id) as order_number
from customers c
join orders o on c.customer_id = o.customer_id
group by c.name
order by order_number desc;