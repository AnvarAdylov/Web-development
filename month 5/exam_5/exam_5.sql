CREATE TABLE warehouses (
    id          SERIAL PrIMARY KEY,
    warehouse   varchar(45) NOT NULL
);

CREATE TABLE contragents (
    id          SERIAL PrIMARY KEY,
    agent       varchar(45) NOT NULL,
    address     VARCHAR(50),
    contacts    VARCHAR(50)
);

CREATE TABLE deliveries (
    id              SERIAL PrIMARY KEY,
    action_date     date NOT NULL,
    product_id      int NOT NULL,
    contragent_id   int NOT NULL,
    warehouse_id    int NOT NULL,
    quantity        decimal(10,3) NOT NULL DEFAULT '0.000',
    CONSTRAINT FK_product FOREIGN KEY (product_id) REFERENCES products (id),
    CONSTRAINT FK_agent FOREIGN KEY (contragent_id) REFERENCES contragents (id),
    CONSTRAINT FK_warehouse FOREIGN KEY (warehouse_id) REFERENCES warehouses (id)
);

CREATE TABLE purchases (
    id                  SERIAL PrIMARY KEY,
    action_date         date NOT NULL,
    product_id          int NOT NULL,
    warehouse_id        int NOT NULL,
    contragent_id       int NOT NULL,
    quantity            decimal(10,3) NOT NULL DEFAULT '0.000',
    CONSTRAINT FK_product FOREIGN KEY (product_id) REFERENCES products (id),
    CONSTRAINT FK_agent FOREIGN KEY (contragent_id) REFERENCES contragents (id),
    CONSTRAINT FK_warehouse FOREIGN KEY (warehouse_id) REFERENCES warehouses (id)
);

CREATE TABLE transfers (
    id                          SERIAL PrIMARY KEY,
    action_date                 date NOT NULL,
    product_id                  int NOT NULL,
    warehouse_sender_id          int NOT NULL,
    warehouse_recipient_id      int NOT NULL,
    quantity                    decimal(10,3) NOT NULL DEFAULT '0.000',
    CONSTRAINT FK_product FOREIGN KEY (product_id) REFERENCES products (id),
    CONSTRAINT FK_warehouse_receiver FOREIGN KEY (warehouse_recipient_id) REFERENCES warehouses (id),
    CONSTRAINT FK_warehouse_sender FOREIGN KEY (warehouse_sender_id) REFERENCES warehouses (id)
);

CREATE TABLE categories (
    id              SERIAL PRIMARY KEY,
    category        varchar(45) NOT NULL DEFAULT 'name category',
    description     varchar(100) DEFAULT NULL,
    CONSTRAINT category_unique UNIQUE (category)
);

CREATE TABLE brands (
  id    serial PRIMARY KEY,
  brand varchar(45) NOT NULL
);

CREATE TABLE products (
  id serial PRIMARY KEY,
  category_id int NOT NULL,
  brand_id int DEFAULT NULL,
  product varchar(45) NOT NULL,
  price decimal(10,2) DEFAULT '0.00',
  description varchar(100) DEFAULT NULL,
  CONSTRAINT FK_brand FOREIGN KEY (category_id) REFERENCES categories (id) ON UPDATE  CASCADE,
  CONSTRAINT FK_category FOREIGN KEY (brand_id) REFERENCES brands (id) ON UPDATE CASCADE
);