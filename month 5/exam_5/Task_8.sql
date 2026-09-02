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