SELECT
    act.action_date AS "Дата поставки",
    cat.category AS "Название категории",
    prod.product AS "Название товара",
    br.brand AS "Название бренда",
    act.price AS "Закупочная цена",
    act.qty AS "Количество"
FROM
    actions act
JOIN
    products prod ON act.product_id = prod.id
JOIN
    categories cat ON prod.category_id = cat.id
LEFT JOIN
    brands br ON prod.brand_id = br.id
ORDER BY
    act.action_date DESC;