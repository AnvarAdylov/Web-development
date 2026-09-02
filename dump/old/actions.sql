create table actions
(
    id          serial
        primary key,
    action_date date                         not null,
    product_id  integer                      not null
        constraint fk_product
            references products,
    supplier_id integer                      not null
        constraint fk_supplier
            references suppliers,
    qty         numeric(10, 3) default 0.000 not null,
    price       numeric(10, 2) default 0.00  not null
);

alter table actions
    owner to postgres;

