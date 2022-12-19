
import requests
from bs4 import BeautifulSoup
toy_name= []
toy_price= []
page_num=1
data_string = ""

while page_num != 29:
    result=requests.get(f"https://www.amazon.eg/s?k=toys&i=toys&rh=n%3A21860119031&page=3&language=en&qid=1671358382&ref=sr_pg_{page_num}")
    print(url)
    res=url.content #url.text
    #print(result)
    soup=BeautifulSoup(res,'html.parser')
    page_num += 1
    productTitle =soup.find_all('span',{'class':'a-size-base a-color-base'})#DEF ALL
    productPrice=soup.find_all('span',{'class':'a-price','data-a-size':'l','data-a-color':'base'})
    for item in productTitle:
        data_string = data_string + item.get_text()
        toy_name.append(data_string)
        data_string = ""
    for item in productPrice:
        data_string = data_string + item.get_text()
        toy_price.append(data_string)
        data_string = ""
    print(toy_name)
    print(toy_price)

print("page switched")




