select
    id as customer_id,
    first_name,
    last_name

from {{ source('bigquery', 'customers') }}
-- `dbt-tutorial`.jaffle_shop.customers