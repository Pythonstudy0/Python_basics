# 주가가져오기 : urllib,bs4
import urllib,bs4

def get_stock_html(company):
    stock_html=urllib.request.urlopen('https://finance.naver.com/item/main.nhn?code='+company).read()
    stock_parser=bs4.BeautifulSoup(stock_html,'html.parser')
    return stock_parser

def get_stock_pr(comapny):
    stock_obj=get_stock_html(company)
    stock_pr=stock_obj.find('p',{'class':'no_today'})
    stock_pr1=stock_pr.find('span',{'class':'blind'})
    return stock_pr1.text
    

companies=['035720','092190']
for company in companies:
    print(company,get_stock_pr(company),'KRW')    