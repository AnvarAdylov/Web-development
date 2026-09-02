create table brands
(
    id    serial
        primary key,
    brand varchar(45) not null
);

alter table brands
    owner to postgres;

