from bs4 import BeautifulSoup
import requests
import pandas

response = requests.get("https://www.amazon.com.tr/b/ref=s9_acss_bw_cg_headgam_1c1_w?node=22829868031&pf_rd_m=A1UNQM1SR2CHM&pf_rd_s=merchandised-search-7&pf_rd_r=YRFA04QAS1PJTW832ERM&pf_rd_t=101&pf_rd_p=c51bd60a-849e-4037-80dd-2f0c707aad25&pf_rd_i=22828872031")
print(response)

soup = BeautifulSoup(response.text,"lxml")


products = soup.find_all("div","_octopus-search-result-card_style_apbSearchResultItem__2-mx4")
print(products)
print(type(products))

dict_products = {"name": [],"price": []}

for i in products:
    p_name = i.find("span","a-size-base-plus a-color-base a-text-normal")
    p_price = i.find("span","a-price-whole")
    dict_products["name"].append(p_name)
    dict_products["price"].append(p_price)

print(dict_products)