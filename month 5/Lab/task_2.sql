SELECT
    cat.category AS "Название категории",
    SUM(act.qty) AS "Общее количество",
    SUM(act.price * act.qty) AS "Общая сумма товара"
FROM
    actions act
JOIN
    products prod ON act.product_id = prod.id
JOIN
    categories cat ON prod.category_id = cat.id
GROUP BY
    cat.category
ORDER BY
    SUM(act.price * act.qty) DESC;