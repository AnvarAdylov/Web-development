create table categories
(
    id          serial
        primary key,
    category    varchar(45)  default 'name category'::character varying not null
        constraint category_unique
            unique,
    description varchar(100) default NULL::character varying
);

alter table categories
    owner to postgres;

