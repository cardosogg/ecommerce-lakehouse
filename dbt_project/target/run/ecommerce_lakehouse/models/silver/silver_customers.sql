
    

    create  table
      "lakehouse"."main"."silver_customers__dbt_tmp"
  
    
    as (
      

SELECT
    customer_id,
    CAST(signup_date AS DATE) AS signup_date,
    UPPER(state) AS state,
    CURRENT_TIMESTAMP as dbt_updated_at
FROM read_parquet('../data/bronze/customers.parquet')
    );
    
  