import requests
import json
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def restocks_url(SKU):
  base_url = 'https://restocks.net/de/shop/search?q='
  request_url = base_url + SKU + '&page=1&filters[0][range][price][gte]=1'

  r = requests.get(request_url)

  json_restocks = json.loads(r.text)
  product_url = json_restocks["data"][0]['slug']
  print('Scraped Restocks URL: ' + product_url)
  return product_url

def format_list(price_list):
    result = ""
    for i in range(len(price_list)):
        if i % 2 == 0:
            result += price_list[i] + ": "
        else:
            result += price_list[i]
            if i < len(price_list) - 1 and price_list[i+1] != "":
                result += "\n"
    return result

def restocks_stock(SKU):
  base_url = 'https://restocks.net/de/shop/search?q='
  request_url = base_url + SKU + '&page=1&filters[0][range][price][gte]=1'

  r = requests.get(request_url)

  json_restocks = json.loads(r.text)
  product_url = json_restocks["data"][0]['slug']
  print('Scraped Restocks URL: ' + product_url)

  options = Options()
  options.headless = True
  driver = webdriver.Chrome(options=options)
  driver.get(product_url)

  cookies = driver.find_element(by=By.ID, value='save__first__localization__button')
  cookies.click()
  time.sleep(2)

  driver.execute_script("window.scrollBy(0,500)", "")

  size_list = driver.find_element(by=By.CLASS_NAME, value='select__label')
  size_list.click()
  time.sleep(2)

  prices = driver.find_element(by=By.CLASS_NAME, value='select__size__list').text
  prices_replace = prices.replace(" ½", ".5")
  prices_replace2 = prices_replace.replace("Notify me", "OOS")
  prices_replace3 = prices_replace2.replace(" €", "")
  price_list = prices_replace3.split("\n")

  driver.quit

  new_list2 = []
  for i in range(len(price_list)):
      if i % 2 == 0:
          size = price_list[i].replace('.5', '½')
          new_list2.append(size)
      else:
          if price_list[i] != 'OOS':
              price = float(price_list[i]) * 0.9 - 20
              price_formatted = '{:.2f}'.format(price) + '€'
              new_list2.append(price_formatted)
          else:
              new_list2.append(price_list[i])

  new_lst3 = []
  for item in new_list2:
      if item == "OOS":
          new_lst3.append("OOS!")
      else:
          new_lst3.append(item)


  formatted_list = format_list(new_lst3)

  return formatted_list

#print(restocks_stock("DV1310-401"))

def product_title(SKU):
  product_url_output = hypeboost_url(SKU)
  headers = {
      "cookie": "country=eyJpdiI6ImlCRDJaRExPQkZYNTNlMmM0OWFEQVE9PSIsInZhbHVlIjoiTFRaRW01UW5wNUY2RjZnQzViWGlPYWRtYVRmbmxxMXpoRjNzODlZZUdIZmNLWjZSTFp0Q3htbTFuYUF4ZGkwVSIsIm1hYyI6IjQ0MzBlZTdkZmNhYjVhYmJhMDAzNDhlNjQ3MGU5NzQ1YThkOTk0ZDRkNzYxZGQzYzg0ODI0ZWYzZWZhODBlZGYiLCJ0YWciOiIifQ%253D%253D; currency=eyJpdiI6ImFlbkxaNHJyOHdUZlJFRlJ2dGlna0E9PSIsInZhbHVlIjoieEx2OE01VHhzOGZ1eFdsM09IVDFIZmR6R1hieHpDRDZScWoweVhqTDZjUzY2a3FFUmhQZGdPV2piaFN3OTViTCIsIm1hYyI6IjgzMTY0NDExNzljYjM1MzFmZmM5ZTBhOGY0MjU3ZWViMjA2NjBjYmUwMjg0MDFkMmUyYmJiNTVjYTUxZTk5MjMiLCJ0YWciOiIifQ%253D%253D",
      "Content-Type": "application/json"
  }
  response = requests.request("GET", product_url_output, headers=headers)
  soup = BeautifulSoup(response.content, 'html.parser')
  title = soup.find('h1')
  title_text = title.get_text()
  print('Scraped title!')
  return title_text

def stockx_url(SKU):
  url = "https://stockx.com/api/browse?_search=" + SKU

  headers = {
          'accept': 'application/json',
          'accept-encoding': 'utf-8',
          'accept-language': 'en-DE',
          'app-platform': 'Iron',
          'referer': 'https://stockx.com/en-DE',
          'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
          'sec-fetch-dest': 'empty',
          'sec-fetch-mode': 'cors',
          'sec-fetch-site': 'same-origin',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
          'x-requested-with': 'XMLHttpRequest'
      }

  request1 = requests.get(url=url, headers=headers)

  product_id = json.loads(request1.text)
  product_id_final = product_id['Products'][0]['id']


  ID = product_id_final
  url_stockX = "https://stockx.com/" + ID
  print("Scraped StockX URL: " + url_stockX)
  return url_stockX

def hypeboost_product_url(SKU):
    url = "https://hypeboost.com/en/search/shop?keyword=" + SKU
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    for a in soup.find_all('a', href=True):
      print("Product URL:", a['href'])

    url2 = a['href']
    print(url2)
    return url2

def sneakit_url(SKU):
  produkt_code = SKU
  global url
  url = f"https://sneakit.com/search/products/{produkt_code}?query={produkt_code}&page=1"
  print("Scraped Sneakit URL!", url)
  return url

def sneakit_product_url(SKU):
  raw = sneakit_info(SKU)
  slug = raw['data'][0]['slug']
  p_url = "https://sneakit.com/product/" + slug
  print("Scraped Sneakit Product URL:" + p_url)
  return p_url

def sneakit_info(SKU):
  sneakit_url_r = sneakit_url(SKU)
  r = requests.get(sneakit_url_r)
  global output
  output = json.loads(r.text)
  print("Scraped Sneakit info!")
  return output

def sneakit_image(SKU):
  raw = sneakit_info(SKU)
  image = raw['data'][0]['productable']['preview_img_public_url']
  #print(image)
  print("Scraped Image!")
  return image

def hypeboost_url(SKU):
  url = "https://hypeboost.com/en/search/shop?keyword=" + SKU

  headers = {
      "cookie": "country=eyJpdiI6ImlCRDJaRExPQkZYNTNlMmM0OWFEQVE9PSIsInZhbHVlIjoiTFRaRW01UW5wNUY2RjZnQzViWGlPYWRtYVRmbmxxMXpoRjNzODlZZUdIZmNLWjZSTFp0Q3htbTFuYUF4ZGkwVSIsIm1hYyI6IjQ0MzBlZTdkZmNhYjVhYmJhMDAzNDhlNjQ3MGU5NzQ1YThkOTk0ZDRkNzYxZGQzYzg0ODI0ZWYzZWZhODBlZGYiLCJ0YWciOiIifQ%253D%253D; currency=eyJpdiI6ImFlbkxaNHJyOHdUZlJFRlJ2dGlna0E9PSIsInZhbHVlIjoieEx2OE01VHhzOGZ1eFdsM09IVDFIZmR6R1hieHpDRDZScWoweVhqTDZjUzY2a3FFUmhQZGdPV2piaFN3OTViTCIsIm1hYyI6IjgzMTY0NDExNzljYjM1MzFmZmM5ZTBhOGY0MjU3ZWViMjA2NjBjYmUwMjg0MDFkMmUyYmJiNTVjYTUxZTk5MjMiLCJ0YWciOiIifQ%253D%253D",
      "Content-Type": "application/json"
  }

  response = requests.request("GET", url, headers=headers)

  soup = BeautifulSoup(response.content, 'html.parser')

  for a in soup.find_all('a', href=True):
    print('Scraped product url!')
    return a['href']