SELECT
    CASE
        WHEN "Год" = lag("Год") OVER (ORDER BY "Год", "Месяц" NULLS FIRST, "День" NULLS FIRST, "Order") THEN NULL
        ELSE "Год"::text
    END AS "Год",
    CASE
        WHEN "Месяц" = lag("Месяц") OVER (ORDER BY "Год", "Месяц" NULLS FIRST, "День" NULLS FIRST, "Order") THEN NULL
        ELSE "Месяц"::text
    END AS "Месяц",
    "День",
    "Сумма"
FROM (
    SELECT
        EXTRACT(YEAR FROM act.action_date) AS "Год",
        NULL AS "Месяц",
        NULL AS "День",
        NULL::numeric AS "Дата",
        SUM(act.qty * act.price) AS "Сумма",
        1 AS "Order"
    FROM
        actions act
    GROUP BY
        EXTRACT(YEAR FROM act.action_date)

    UNION ALL

    SELECT
        EXTRACT(YEAR FROM act.action_date) AS "Год",
        EXTRACT(MONTH FROM act.action_date) AS "Месяц",
        NULL AS "День",
        NULL::numeric AS "Дата",
        SUM(act.qty * act.price) AS "Сумма",
        2 AS "Order"
    FROM
        actions act
    GROUP BY
        EXTRACT(YEAR FROM act.action_date),
        EXTRACT(MONTH FROM act.action_date)

    UNION ALL

    SELECT
        EXTRACT(YEAR FROM act.action_date) AS "Год",
        EXTRACT(MONTH FROM act.action_date) AS "Месяц",
        act.action_date::text AS "День",
        NULL::numeric AS "Дата",
        SUM(act.qty * act.price) AS "Сумма",
        3 AS "Order"
    FROM
        actions act
    GROUP BY
        EXTRACT(YEAR FROM act.action_date),
        EXTRACT(MONTH FROM act.action_date),
        act.action_date
    ORDER BY
    "Год", "Order", "Месяц" NULLS FIRST, "День" NULLS FIRST
) AS subquery

