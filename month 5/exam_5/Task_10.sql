SELECT DISTINCT
    "Контрагент",
    SUM("Количество") AS "Количество"
FROM (SELECT DISTINCT cr.agent         AS "Контрагент",
                      SUM(pr.quantity) AS "Количество"
      FROM purchases as pr
               INNER JOIN
           products prod ON prod.id = pr.product_id
               INNER JOIN
           contragents cr ON cr.id = pr.contragent_id
      WHERE product_id = 2
        AND EXTRACT(YEAR FROM pr.action_date) = 2023
      GROUP BY pr.quantity, cr.agent
      ) AS subquery
GROUP BY
    "Контрагент"
ORDER BY
    "Количество" DESC