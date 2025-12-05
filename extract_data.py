import requests
import pandas as pd

data=requests.get("https://jsonplaceholder.typicode.com/users").json()

df=pd.DataFrame(data)
df=df[['id','name','username','email']]
print(df)