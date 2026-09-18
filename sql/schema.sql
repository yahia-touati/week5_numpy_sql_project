drop table if exists ordor_items cascade;
drop table if exists orders cascade;
drop table if exists products cascade;
drop table if exists customers cascade;

create table customers(
    customer_id serial primary key,
    name varchar(100) not null,
    email varchar(100) unique ,
    city varchar(50),
    created_at timestamp default now()
);

create table products (
    product_id serial primary key,
    name varchar(100) not null,
    category varchar(50),
    price numeric(10, 2)not null,
    stock int default 0
);

create table orders (
    order_id serial primary key,
    customer_id int not null ,
    order_date date not null,
    status varchar(20) default 'pending',

    constraint fk_orders_customer
        foreign key (customer_id)
        references customers(customer_id)
        on delete cascade 
);

create table order_items (
    item_id serial primary key,
    order_id int not null,
    product_id int not null,
    quantity int not null check(quantity > 0),

    constraint fk_itmes_order
        foreign key (order_id)
        references orders(order_id)
        on delete cascade,
    constraint fk_items_product
        foreign key (product_id)
        references products(product_id)
        on delete restrict
);