create table products
(
    id          serial
        primary key,
    category_id integer     not null
        constraint fk_brand
            references categories
            on update cascade,
    brand_id    integer
        constraint fk_category
            references brands
            on update cascade,
    product     varchar(45) not null,
    price       numeric(10, 2) default 0.00,
    description varchar(100)   default NULL::character varying
);

alter table products
    owner to postgres;

