
    
    

select
    category as unique_field,
    count(*) as n_records

from "lakehouse"."main"."gold_sales_summary"
where category is not null
group by category
having count(*) > 1


