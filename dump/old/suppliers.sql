create table suppliers
(
    id       serial
        primary key,
    supplier varchar(50) not null,
    address  varchar(50),
    contacts varchar(50)
);

alter table suppliers
    owner to postgres;

