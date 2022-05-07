from math import prod
from pydoc import doc
import requests
from bs4 import BeautifulSoup as BS
from types import FunctionType

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

  return product_title,product_img_link,price_value,currency


def newegg_product_info(product_url):
  '''
  Newegg scraper function
  '''
  response = requests.get(product_url)
  if response.status_code != 200:
    return "Error"
  content = response.content
  soup = BS(content,"html.parser")
  li_tag = soup.find("li",{"class":"price-current"})
  if li_tag:
    price_value = li_tag.text
  else:
    price_value = None
  currency = "CAD"
  product_title_h1 = soup.find("h1",{"class":"product-title"})
  if product_title_h1:
    product_title = product_title_h1.text
  else:
    product_title = None
  product_img_link = soup.find("img",{"class":"product-view-img-original"})["src"]

  return product_title,product_img_link,price_value,currency



def forever21_product_info(product_url):
  '''
  Forever21 scraper function
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

  price_value_span = soup.find("div",{"class":"product__price-wrapper js-product-price"}).find("span")
  if price_value_span:
      price_value = price_value_span.text.replace("\n","")
  else:
      price_value = None

  currency = "CAD"
  
  return product_title,product_img_link,price_value,currency


def target_product_info(product_url):
  '''
  Target scraper function
  '''
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

  price_value_span = soup.find("div",{"class":"h-margin-b-x2"}).find("span")
  if price_value_span:
      price_value = price_value_span.text
  else:
      price_value = None

  currency = "CAD"
  
  return product_title,product_img_link,price_value,currency


def indigo_product_info(product_url):
  '''
  Indigo scraper function
  '''
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
  '''
  MemoryExpress scraper function
  '''
  response = requests.get(product_url)
  if response.status_code != 200:
    return "Error"
  content = response.content
  soup = BS(content,"html.parser")
  product_h1 = soup.find("header",{"class":"c-capr-header"}).find("h1")
  if product_h1:
      product_title = product_h1.text.replace("\n","").replace("\r","").strip()
      while '  ' in product_title:
        product_title = product_title.replace('  ', ' ')

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
  '''
  Nike scraper function
  '''
  response = requests.get(product_url)
  if response.status_code != 200:
    return "Error"
  content = response.content
  soup = BS(content,"html.parser")
  product_title_h1 = soup.find("h1",{"id":"pdp_product_title"})
  if product_title_h1:
    product_title = product_title_h1.text
  else:
    product_title = None
  product_img_link_tag = soup.find("img",{"class":"css-viwop1 u-full-width u-full-height css-m5dkrx"})
  if product_img_link_tag:
    product_img_link = product_img_link_tag["src"]
  price_value_div = soup.find("div",{"class":"product-price css-11s12ax is--current-price css-tpaepq"})
  if price_value_div:
    price_value = price_value_div.text
  else:
    price_value = None
  currency = "CAD"
  
  return product_title,product_img_link,price_value,currency

def lululemon_product_info(product_url):
  '''
  Lululemon scraper function
  '''
  response = requests.get(product_url)
  if response.status_code != 200:
    return "Error"
  content = response.content
  soup = BS(content,"html.parser")
  product_title = soup.find("h1",{"class":"OneLinkNoTx product-description_pdpTitle__3F7CP"}).text
  price_comps = soup.find("span",{"class":"price-1jnQj price"}).text.split("\xa0")
  price_value = " ".join(price_comps)
  currency = "CAD"
  product_img_link = None 

  return product_title,product_img_link,price_value,currency

def steam_product_info(product_url):
  '''
  Steam scraper function
  '''
  try:
    url_split = product_url.split("/")
    game_id = None
    
    for comp in url_split:
      if comp.isnumeric():
        game_id = comp
    
    if game_id is None:
      return "Error"
    
    api_url = f"https://store.steampowered.com/api/appdetails?appids={game_id}"
    resp_json = requests.get(api_url).json()[game_id]["data"]
    price_value = "Free" if resp_json["is_free"] else resp_json["price_overview"]['final_formatted']
    currency = "Invalid" if resp_json["is_free"] else resp_json["price_overview"]['currency']
    product_img_link = resp_json["header_image"]
    product_title = resp_json["name"]
    
    return product_title,product_img_link,price_value,currency
  except Exception:
    return "Error"


  
def get_scraper_function(store_name):
  '''
  Search scraper function
  '''
  all_globals = globals()
  for attribute in all_globals:
    module_value = all_globals[attribute]
    if isinstance(module_value,FunctionType):
      doc_string_name = module_value.__doc__.split(" scraper ")[0].replace("\n","").strip()
      if doc_string_name == store_name:
        return module_value
  
  return None
  

    
