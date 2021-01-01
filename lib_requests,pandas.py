import requests
import pandas as pd 

dart_url='http://dart.fss.or.kr/pdf/download/excel.do?rcp_no=20201116001248&dcm_no=7549051&lang=ko'
user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

resp=requests.get(dart_url, headers={'user-agent':user_agent})
resp.content

from io import BytesIO
table=BytesIO(resp.content)

sheets=['연결 재무상태표','손익계산서','현금흐름표']
for sheet in sheets:
    get_bs=pd.read_excel(table,sheet_name=sheet,skiprows=5)
    get_bs.to_csv(sheet+'_companyname.csv', encoding='utf-8')