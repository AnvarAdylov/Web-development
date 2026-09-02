SELECT
    sup.supplier AS "Поставщик",
    SUM(act.qty * act.price) AS "Сумма"
FROM
    suppliers sup
INNER JOIN
    actions act ON sup.id = act.supplier_id
WHERE
    EXTRACT(YEAR FROM act.action_date) = 2016
GROUP BY
    sup.supplier
HAVING
    SUM(act.qty * act.price) > (
        SELECT
            SUM(act.qty * act.price)
        FROM
            actions act
        INNER JOIN
            suppliers sup ON act.supplier_id = sup.id
        WHERE
            sup.id = (SELECT id FROM suppliers WHERE supplier='IDT')
        AND
            EXTRACT(YEAR FROM act.action_date) = 2016
    );