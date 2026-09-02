SELECT DISTINCT
    prod.product
FROM
    products prod
LEFT JOIN
    actions act ON prod.id = act.product_id
LEFT JOIN
    suppliers sup ON act.supplier_id = sup.id
WHERE
    sup.id != (SELECT id FROM suppliers WHERE supplier='IDT') OR
    sup.supplier IS NULL;