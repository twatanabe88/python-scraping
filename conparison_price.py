import requests
from bs4 import BeautifulSoup

keyword = input('比較したい商品名を入力してください:\n')

def get_rakuten():
    url = 'https://search.rakuten.co.jp/search/mall/' + keyword +'?s=2'
    responce = requests.get(url)
    html = responce.text
    soup = BeautifulSoup(html,'html.parser')
    items = soup.select('.searchresultitem')
    
    item_number = 0
    price_list = []
    
    for item in items:
        title = item.select_one('.title').text.replace('\n','')
        price = item.select_one('.important').text.replace(',','').replace('円','')
        price_list.append(price)
        print(item_number)
        print(title)
        print(price + '\n')
        item_number += 1
        
    selected_item_number = int(input('楽天: 商品番号を入力してください\n'))
    selected_price = int(price_list[selected_item_number])
    return selected_price
    
raktuen_price = get_rakuten()
print(raktuen_price)
    