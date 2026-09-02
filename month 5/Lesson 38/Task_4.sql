SELECT
    cat.category AS "Категория товара",
    EXTRACT(YEAR FROM act.action_date) AS "Год",
    SUM(act.price*act.qty)/SUM(act.qty) AS "Среднегодовая цена",
    MAX(act.price) AS "Максимальная цена за год",
    MIN(act.price) AS "Минимальная цена за год"
FROM
    actions act
INNER JOIN
    products prod ON act.product_id = prod.id
INNER JOIN
    categories cat ON prod.category_id = cat.id
GROUP BY
    cat.category, EXTRACT(YEAR FROM act.action_date)
ORDER BY
    cat.category, EXTRACT(YEAR FROM act.action_date);