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

