import pandas as pd 
import re

# -------------------------------------------------

text='start추출글자end'
re.findall('start(.*?)end',text)

# --------------------------------------------------
df=pd.DataFrame({
                "name":['Ali','Blig','Cliie'],
                "city":['BE','HA','DR'],
                "age":[24,27,20],
                "point":[58,90,67]
                }
)

print(df)
print(df.replace('BE','Berlin'))
print(df.replace('(.*)li(.*)',r'\1LI\2', regex=True))
print(df.rename(columns={'name':'changed_Name'}))