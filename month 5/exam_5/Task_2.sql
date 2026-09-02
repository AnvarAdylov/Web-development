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
