{{ config(materialized='table') }}

SELECT
    order_id AS sale_id,
    customer_id,
    product_id,
    quantity,
    total_amount,
    CAST(order_timestamp AS TIMESTAMP) AS order_timestamp,
    CURRENT_TIMESTAMP as dbt_updated_at
FROM read_parquet('../data/bronze/sales.parquet')