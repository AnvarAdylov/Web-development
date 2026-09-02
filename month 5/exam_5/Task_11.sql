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
