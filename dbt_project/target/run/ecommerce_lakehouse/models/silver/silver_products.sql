
    

    create  table
      "lakehouse"."main"."silver_products__dbt_tmp"
  
    
    as (
      

SELECT
    product_id,
    category,
    unit_price,
    CURRENT_TIMESTAMP as dbt_updated_at
FROM read_parquet('../data/bronze/products.parquet')
    );
    
  