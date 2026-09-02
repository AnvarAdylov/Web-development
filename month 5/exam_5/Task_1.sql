-- 1st task sql query
SELECT DISTINCT
    prod.product AS "Товар",
    SUM(del.quantity) AS "Количество"
FROM
    deliveries as del
INNER JOIN
    products prod ON prod.id = del.product_id
WHERE
    del.warehouse_id = 1
    AND
    EXTRACT(YEAR FROM del.action_date) = 2023
GROUP BY
    prod.product
UNION ALL
SELECT DISTINCT
    prod.product AS "Товар",
    SUM(tran.quantity) AS "Количество"
FROM
    transfers as tran
INNER JOIN
    products prod ON prod.id = tran.product_id
WHERE
    tran.warehouse_recipient_id = 1
    AND
    EXTRACT(YEAR FROM tran.action_date) = 2023
GROUP BY
    prod.product
-- 2nd task sql query
SELECT DISTINCT
    prod.product AS "Товар",
    SUM(pur.quantity) AS "Количество"
FROM
    purchases as pur
INNER JOIN
    products prod ON prod.id = pur.product_id
WHERE
    pur.warehouse_id = 2
    AND
    EXTRACT(YEAR FROM pur.action_date) = 2023
GROUP BY
    prod.product
UNION ALL
SELECT DISTINCT
    prod.product AS "Товар",
    SUM(tran.quantity) AS "Количество"
FROM
    transfers as tran
INNER JOIN
    products prod ON prod.id = tran.product_id
WHERE
    tran.warehouse_sender_id = 2
    AND
    EXTRACT(YEAR FROM tran.action_date) = 2023
GROUP BY
    prod.product
-- 3rd task sql query
SELECT DISTINCT
    "Категория",
    SUM("Количество")
FROM
    (
SELECT DISTINCT
    cat.category AS "Категория",
    SUM(del.quantity) AS "Количество"
FROM
    categories as cat
INNER JOIN
    products prod ON cat.id = prod.id
LEFT JOIN
    deliveries del ON prod.id = del.product_id
WHERE
    del.warehouse_id = 1
    AND
    EXTRACT(YEAR FROM del.action_date) = 2022
GROUP BY
    cat.category
UNION ALL
SELECT DISTINCT
    cat.category AS "Категория",
    SUM(tran.quantity) AS "Количество"
FROM
    categories as cat
INNER JOIN
    products prod ON cat.id = prod.id
LEFT JOIN
    transfers tran ON prod.id = tran.product_id
WHERE
    tran.warehouse_recipient_id = 1
    AND
    EXTRACT(YEAR FROM tran.action_date) = 2022
GROUP BY
    cat.category
) AS subquery
GROUP BY
    "Категория"
ORDER BY
    "Категория"
-- 4th task sql query
SELECT DISTINCT
    br.brand AS "Бренд",
    SUM(del.quantity) AS "Количество"
FROM
    deliveries as del
INNER JOIN
    products prod ON prod.id = del.product_id
LEFT JOIN
    brands br ON br.id = prod.brand_id
WHERE
    del.warehouse_id = 1
    AND
    EXTRACT(YEAR FROM del.action_date) = 2022
GROUP BY
    br.brand
UNION ALL
SELECT DISTINCT
    br.brand AS "Бренд",
    SUM(tran.quantity) AS "Количество"
FROM
    transfers as tran
INNER JOIN
    products prod ON prod.id = tran.product_id
LEFT JOIN
    public.brands br ON br.id = prod.brand_id
WHERE
    tran.warehouse_recipient_id = 1
    AND
    EXTRACT(YEAR FROM tran.action_date) = 2022
GROUP BY
    br.brand
-- 6th task sql query
SELECT DISTINCT
    prod.product AS "Товар",
    SUM(del.quantity) AS "Количество"
FROM
    deliveries as del
INNER JOIN
    products prod ON prod.id = del.product_id
INNER JOIN
    contragents cr ON cr.id = del.contragent_id
WHERE
    contragent_id = 1
    AND
    EXTRACT(YEAR FROM del.action_date) = 2023
GROUP BY
    prod.product
ORDER BY
    prod.product
-- 7th task sql query
SELECT DISTINCT
    prod.product AS "Товар",
    SUM(del.quantity) AS "Количество"
FROM
    deliveries as del
INNER JOIN
    products prod ON prod.id = del.product_id
INNER JOIN
    contragents cr ON cr.id = del.contragent_id
WHERE
    contragent_id = 1
    AND
    warehouse_id = 1
    AND
    EXTRACT(YEAR FROM del.action_date) = 2023
GROUP BY
    prod.product
ORDER BY
    prod.product
-- 8th task sql query
SELECT DISTINCT
    prod.product AS "Товар",
    SUM(pur.quantity) AS "Количество"
FROM
    purchases as pur
INNER JOIN
    products prod ON prod.id = pur.product_id
INNER JOIN
    contragents cr ON cr.id = pur.contragent_id
WHERE
    contragent_id = 1
    AND
    warehouse_id = 1
    AND
    EXTRACT(YEAR FROM pur.action_date) = 2023
GROUP BY
    prod.product
ORDER BY
    prod.product
-- 9th task sql query
SELECT DISTINCT
    "Контрагент",
    SUM("Количество") AS "Количество"
FROM (SELECT DISTINCT cr.agent          AS "Контрагент",
                      SUM(del.quantity) AS "Количество"
      FROM deliveries as del
        INNER JOIN
           products prod ON prod.id = del.product_id
        INNER JOIN
           contragents cr ON cr.id = del.contragent_id
      WHERE product_id = 3
        AND EXTRACT(YEAR FROM del.action_date) = 2023
      GROUP BY cr.agent
      ) AS subquery
GROUP BY "Количество" , "Контрагент"
ORDER BY "Количество" DESC
-- 10th task sql query
SELECT DISTINCT
    "Контрагент",
    SUM("Количество") AS "Количество"
FROM (SELECT DISTINCT cr.agent         AS "Контрагент",
                      SUM(pr.quantity) AS "Количество"
      FROM purchases as pr
               INNER JOIN
           products prod ON prod.id = pr.product_id
               INNER JOIN
           contragents cr ON cr.id = pr.contragent_id
      WHERE product_id = 2
        AND EXTRACT(YEAR FROM pr.action_date) = 2023
      GROUP BY pr.quantity, cr.agent
      ) AS subquery
GROUP BY
    "Контрагент"
ORDER BY
    "Количество" DESC
-- 11th task sql query
    SELECT DISTINCT
    prod.product AS "Товар",
    SUM(tran.quantity) AS "Количество"
FROM
    transfers as tran
INNER JOIN
    products prod ON prod.id = tran.product_id
WHERE
    tran.warehouse_recipient_id = 4
    AND
    EXTRACT(YEAR FROM tran.action_date) = 2023
GROUP BY
    prod.product
ORDER BY
    prod.product
-- 12th task sql query
SELECT DISTINCT
    prod.product AS "Товар",
    SUM(tran.quantity) AS "Количество"
FROM
    transfers as tran
INNER JOIN
    products prod ON prod.id = tran.product_id
WHERE
    tran.warehouse_sender_id = 2
    AND
    EXTRACT(YEAR FROM tran.action_date) = 2023
GROUP BY
    prod.product
ORDER BY
    prod.product