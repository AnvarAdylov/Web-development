SELECT DISTINCT
    "Контрагент",
    SUM("Количество") AS "Количество"
FROM (SELECT DISTINCT cr.agent          AS "Контрагент",
                      SUM(del.quantity) AS "Количество"
      FROM deliveries as del
        INNER JOIN
           products prod ON prod.id = del.product_id
        INNER JOIN
           contragents cr ON cr.id = del.contragent_id
      WHERE product_id = 3
        AND EXTRACT(YEAR FROM del.action_date) = 2023
      GROUP BY cr.agent
      ) AS subquery
GROUP BY "Количество" , "Контрагент"
ORDER BY "Количество" DESC
