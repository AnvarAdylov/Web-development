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