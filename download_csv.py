import requests
import pandas as pd
url = 'https://raw.githubusercontent.com//dbt-labs//jaffle_shop//core-v1.0.0//seeds//raw_payments.csv'
res = requests.get(url, allow_redirects=True)
with open('raw_payments.csv', 'wb') as f:
    f.write(res.content)
df = pd.read_csv('raw_payments.csv')
print(df.head())