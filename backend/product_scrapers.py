import requests
from bs4 import BeautifulSoup as BS

def ebay_product_info(product_url):
  '''
  Ebay scraper function
  '''
  response = requests.get(product_url)
  if response.status_code != 200:
    return "Error"
  content = response.content
  soup = BS(content,"html.parser")
  price_value = soup.find("span",{"itemprop":"price"})["content"]
  currency = soup.find("span",{"itemprop":"priceCurrency"})["content"]
  product_title = soup.find("h1",{"class":"x-item-title__mainTitle"}).text
  product_img_link = soup.find("img",{"id":"icImg"})["src"]

  return product_title,price_value,currency,product_img_link


def newegg_product_info(product_url):
  '''
  Newegg scraper function
  '''
  response = requests.get(product_url)
  if response.status_code != 200:
    return "Error"
  content = response.content
  soup = BS(content,"html.parser")
  price_value = soup.find("li",{"class":"price-current"}).text
  currency = "CAD"
  product_title = soup.find("h1",{"class":"product-title"}).text
  product_img_link = soup.find("img",{"class":"product-view-img-original"})["src"]

  return product_title,price_value,currency,product_img_link

def forever21_product_info(product_url):
  '''
  Forever 21 scraper function
  '''
  response = requests.get(product_url)
  if response.status_code != 200:
    return "Error"
  content = response.content
  soup = BS(content,"html.parser")
  product_h1 = soup.find("h1",{"class":"header product__header"})
  if product_h1:
      product_title = product_h1.text
  else:
      product_title = None
      
  product_img= soup.find("img")
  if product_img:
      product_img_link = product_img["src"]
  else:
      product_img_link = None

  price_value_span = soup.find("span",{"class":"product__price "})
  if price_value_span:
      price_value = price_value_span.text
  else:
      price_value = None

  currency = "CAD"
  
  return product_title,product_img_link,price_value,currency


def target_product_info(product_url):
  response = requests.get(product_url)
  if response.status_code != 200:
    return "Error"
  content = response.content
  soup = BS(content,"html.parser")
  product_h1 = soup.find("h1",{"data-test":"product-title"})
  if product_h1:
      product_title = product_h1.text
  else:
      product_title = None
      
  product_img= soup.find("img",{"class":"media__ScalableImage-sc-1ea3f06-0 cpKRLA"})
  if product_img:
      product_img_link = product_img["src"]
  else:
      product_img_link = None

  price_value_span = soup.find("span",{"data-test":"product-price"})
  if price_value_span:
      price_value = price_value_span.text
  else:
      price_value = None

  currency = "CAD"
  
  return product_title,product_img_link,price_value,currency


def indigo_product_info(product_url):
  response = requests.get(product_url)
  if response.status_code != 200:
    return "Error"
  content = response.content
  soup = BS(content,"html.parser")
  product_h1 = soup.find("h1",{"class":"common-title product-title item-page__main-title"})
  if product_h1:
      product_title = product_h1.text.replace("\n","").strip()
  else:
      product_title = None
      
  product_img = soup.find("img",{"class":"product-image__image"})
  if product_img:
      product_img_link = product_img["src"]
  else:
      product_img_link = None

  price_value_span = soup.find("span",{"class":"item-price__price-amount"})
  if price_value_span:
      price_value = price_value_span.text.replace("\n","").strip().replace("Only$","")
  else:
      price_value = None

  currency = "CAD"
  
  return product_title,product_img_link,price_value,currency

def memory_exp_product_info(product_url):
  response = requests.get(product_url)
  if response.status_code != 200:
    return "Error"
  content = response.content
  soup = BS(content,"html.parser")
  product_h1 = soup.find("header",{"class":"c-capr-header"}).find("h1")
  if product_h1:
      product_title = product_h1.text.replace("\n","").strip()
  else:
      product_title = None
      
  product_img = soup.find("div",{"class":"c-capr-images__focus"}).find("img")
  if product_img:
      product_img_link = product_img["src"]
  else:
      product_img_link = None

  price_value_span = soup.find("div",{"class":"GrandTotal c-capr-pricing__grand-total"}).find("div")
  if price_value_span:
      price_value = price_value_span.text.replace("\n","").strip().replace("Only$","")
  else:
      price_value = None

  currency = "CAD"
  
  return product_title,product_img_link,price_value,currency



def nike_product_info(product_url):
  response = requests.get(product_url)
  if response.status_code != 200:
    return "Error"
  content = response.content
  soup = BS(content,"html.parser")
  product_title = soup.find("h1",{"id":"pdp_product_title"}).text
  product_img_link = soup.find("img",{"class":"css-viwop1 u-full-width u-full-height css-m5dkrx"})["src"]
  price_value = soup.find("div",{"class":"product-price css-11s12ax is--current-price css-tpaepq"}).text
  
  return product_title,product_img_link,price_value

def lululemon_product_info(product_url):
  response = requests.get(product_url)
  if response.status_code != 200:
    return "Error"
  content = response.content
  soup = BS(content,"html.parser")
  product_title = soup.find("h1",{"class":"OneLinkNoTx product-description_pdpTitle__3F7CP"}).text
  price_comps = soup.find("span",{"class":"price-1jnQj price"}).text.split("\xa0")
  price_value,currency = price_comps
  return product_title,price_value,currency

def steam_product_info(product_url):
  response = requests.get(product_url)
  if response.status_code != 200:
    return "Error"
  content = response.content
  soup = BS(content,"html.parser")
  product_title = soup.find("div",{"class":"apphub_AppName"}).text
  product_image_url = soup.find("img",{"class":"game_header_image_full"})["src"]
  
  price_value = soup.find("div",{"class":"game_purchase_price price"}).text.replace("\r","").replace("\n","").replace("\t","")
  currency = "USD"
  return product_title,price_value,currency,product_image_url
  


