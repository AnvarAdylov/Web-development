SELECT
    CASE
        WHEN "Поставщик" = lag("Поставщик") OVER (ORDER BY "Поставщик", "Год" NULLS FIRST, "Категория товара" NULLS FIRST) THEN NULL
        ELSE "Поставщик"::text
    END AS "Поставщик",
    CASE
        WHEN "Год" = lag("Год") OVER (ORDER BY "Поставщик", "Год" NULLS FIRST, "Категория товара" NULLS FIRST) THEN NULL
        ELSE "Год"::text
    END AS "Год",
    "Категория товара",
    "Сумма"
FROM (
    SELECT
        sup.supplier AS "Поставщик",
        NULL AS "Год",
        NULL AS "Категория товара",
        SUM(act.qty * act.price) AS "Сумма"
    FROM
        suppliers sup
    LEFT JOIN
        actions act ON sup.id = act.supplier_id
    GROUP BY
        sup.id, sup.supplier

    UNION ALL

    SELECT
        sup.supplier AS "Поставщик",
        EXTRACT(YEAR FROM act.action_date) AS "Год",
        NULL AS "Категория товара",
        SUM(act.qty * act.price) AS "Сумма"
    FROM
        suppliers sup
    LEFT JOIN
        actions act ON sup.id = act.supplier_id
    GROUP BY
        sup.id, sup.supplier, EXTRACT(YEAR FROM act.action_date)

    UNION ALL

    SELECT
        sup.supplier AS "Поставщик",
        EXTRACT(YEAR FROM act.action_date) AS "Год",
        cat.category AS "Категория товара",
        SUM(act.qty * act.price) AS "Сумма"
    FROM
        suppliers sup
    LEFT JOIN
        actions act ON sup.id = act.supplier_id
    LEFT JOIN
        products prod ON act.product_id = prod.id
    LEFT JOIN
        categories cat ON prod.category_id = cat.id
    GROUP BY
        sup.id, sup.supplier, EXTRACT(YEAR FROM act.action_date), cat.category
    ORDER BY
        "Поставщик", "Год" NULLS FIRST, "Категория товара" NULLS FIRST
) AS subquery

