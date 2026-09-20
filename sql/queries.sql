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

-- Display the number of customer orders and their names
select
    c.name,
    count(o.order_id) as order_number
from customers c
join orders o on c.customer_id = o.customer_id
group by c.name
order by order_number desc;

-- The top 5  clients  by total revenue 
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

-- Q4 Monthly revenue 
select 
    to_char(o.order_date,'YYYY-MM') as month,
    sum(p.price * oi.quantity) as total
from products p
join order_items oi on p.product_id = oi.product_id
join orders o on o.order_id = oi.order_id
group by  to_char(o.order_date,'YYYY-MM')
order by month;

-- Q5 Avrage order value 
select 
round(avg(order_total), 2) as avg_order_value
from(
    select
            oi.order_id,
            sum(p.price * oi.quantity) as order_total
        from products p 
        join order_items oi on p.product_id = oi.product_id
        GROUP BY oi.order_id
    ) as order_totals;

-- Q6 Sales by city
select 
    sum(p.price * oi.quantity) as total_revenue,
    c.city
    from order_items oi 
    join orders o on o.order_id = oi.order_id
    join customers c on c.customer_id = o.customer_id
    join products p on p.product_id = oi.product_id
GROUP BY c.city
order by total_revenue desc;

--Q7 Order status percentage 
select 
    round((delivered * 100.0 / total ),2) as percentag_delivered,
    round((shipped * 100.0 / total),2) as percentage_shipped,
    round((pending * 100.0 / total),2) as percentage_pending
from(
    select
        count(*) as total,
        count(case WHEN status = 'delivered' then 1 end) as delivered,
        count(case WHEN status = 'shipped' then 1 end) as shipped,
        count(case WHEN status = 'pending' then 1 end) as pending
    from orders
    )as number_status      
