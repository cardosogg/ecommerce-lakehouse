

SELECT
    p.category,
    COUNT(s.sale_id) AS total_orders,
    SUM(s.quantity) AS total_quantity_sold,
    ROUND(SUM(s.total_amount), 2) AS total_revenue,
    CURRENT_TIMESTAMP AS dbt_updated_at
FROM "lakehouse"."main"."silver_sales" s
JOIN "lakehouse"."main"."silver_products" p 
    ON s.product_id = p.product_id
GROUP BY p.category