
import requests
from bs4 import BeautifulSoup
toy_name= []
toy_price= []
data_string = ""
url=requests.get("https://www.amazon.eg/-/en/l/21860119031/ref=s9_acss_bw_cg_atf3601_2c1_w?pf_rd_m=A1ZVRGNO5AYLOV&pf_rd_s=merchandised-search-10&pf_rd_r=E2AG67SRMQXEF939V4XW&pf_rd_t=101&pf_rd_p=02d50b66-6a33-44f0-bdfd-e57af797c401&pf_rd_i=18022503031")
result=url.content
#print(result)
soup=BeautifulSoup(url.text,'html.parser')
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
print(toy_name, toy_price)
#print(len(product_title),len(product_price))




