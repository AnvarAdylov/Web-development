SELECT DISTINCT
    cat.category
FROM
    categories cat
INNER JOIN
    products prod ON cat.id = prod.category_id
INNER JOIN
    actions act ON prod.id = act.product_id
INNER JOIN
    suppliers sup ON act.supplier_id = sup.id
WHERE
    sup.id = (SELECT id FROM suppliers WHERE supplier='IDT')
    AND EXTRACT(YEAR FROM act.action_date) = 2016
    AND EXTRACT(MONTH FROM act.action_date) BETWEEN 6 AND 8;
