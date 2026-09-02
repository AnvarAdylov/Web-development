SELECT
    act.action_date AS "Дата поставки",
    cat.category AS "Название категории",
    prod.product AS "Название товара",
    br.brand AS "Название бренда",
    act.price AS "Закупочная цена",
    act.qty AS "Количество",
    sup.supplier AS "Поставщик"
FROM
    actions act
JOIN
    products prod ON act.product_id = prod.id
JOIN
    categories cat ON prod.category_id = cat.id
LEFT JOIN
    brands br ON prod.brand_id = br.id
JOIN
    suppliers sup ON act.supplier_id = sup.id
WHERE
    sup.supplier = '4U' AND
    act.action_date BETWEEN '2015-08-01' AND '2015-08-31'
ORDER BY
    act.action_date DESC
LIMIT
    3;