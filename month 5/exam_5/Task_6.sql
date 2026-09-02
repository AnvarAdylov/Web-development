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

