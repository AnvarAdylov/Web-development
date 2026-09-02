SELECT
    sup.supplier AS "Поставщик",
    NULL AS "Категория товара",
    SUM(act.qty * act.price) AS "Итоговая сумма"
FROM
    suppliers sup
INNER JOIN
    actions act ON sup.id = act.supplier_id
WHERE
    EXTRACT(YEAR FROM act.action_date) = 2016
GROUP BY
    sup.supplier

UNION ALL

SELECT
    sup.supplier AS "Поставщик",
    cat.category AS "Категория товара",
    SUM(act.qty * act.price) AS "Итоговая сумма"
FROM
    suppliers sup
INNER JOIN
    actions act ON sup.id = act.supplier_id
INNER JOIN
    products prod ON act.product_id = prod.id
INNER JOIN
    categories cat ON prod.category_id = cat.id
WHERE
    EXTRACT(YEAR FROM act.action_date) = 2016
GROUP BY
    sup.supplier, cat.category
ORDER BY
    "Поставщик", "Категория товара" NULLS FIRST;