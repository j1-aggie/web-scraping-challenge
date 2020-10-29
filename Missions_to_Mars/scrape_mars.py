# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import pymongo
from selenium import webdriver

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():

    browser = init_browser()
    
    # Mars News URL of page to be scraped
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")

    # Retrieve the latest news title and paragraph
    data = soup.find("li", class_="slide")
    news_title = data.find('div', class_='content_title').a.text
    news_paragraph = data.find('div', class_='article_teaser_body').text

    
    # Mars Image to be scraped
    # jpl_nasa_url = 'https://www.jpl.nasa.gov'
    img_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(img_url)
    html = browser.html
    soup = bs(html, 'html.parser')
    # Retrieve featured image link
    image = soup.find("li", class_="slide").a["data-fancybox-href"]
    featured_image_url = "https://www.jpl.nasa.gov" + image

    # Mars facts to be scraped, converted into html table
    facts_url = "https://www.space-facts.com/mars/"
    browser.visit(facts_url)
    html = browser.html
    soup = bs(html, 'html.parser')
    table = pd.read_html(facts_url)
    facts_df = table[0]
    facts_df.columns = ["description", "value"]
    facts_df.set_index("description", inplace=True)
    facts_df.to_html('table.html')
    facts_html = facts_df.to_html()
    
    
   
    
    
    # Mars hemisphere name and image to be scraped
    #usgs_url = 'https://astrogeology.usgs.gov'
    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemispheres_url)
    html = browser.html
    soup = bs(html, 'html.parser')

    data = soup.find_all("div", class_="item")
    
    # Mars hemispheres products data
    #all_mars_hemispheres = hemispheres_soup.find('div', class_='collapsible results')
    #mars_hemispheres = all_mars_hemispheres.find_all('div', class_='item')
    
    hemisphere_img_urls = []
    # Iterate through each hemisphere data
    for d in data:
        title = d.find("h3").text

        img_url = d.a["href"]
    
        url = "https://astrogeology.usgs.gov" + img_url
    
        # use requests to get full images url 
        response = requests.get(url)
    
        # create soup object
        soup = bs(response.text,"html.parser")
    
        # find full image url
        new_url = soup.find("img", class_="wide-image")["src"]
    
        # create full image url
        full_url = "https://astrogeology.usgs.gov" + new_url
        
        #make a dict and append to the list
        hemisphere_img_urls.append({"title": title, "img_url": full_url})

    # Mars 
    mars_data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image_url": featured_image_url,
        "html_table": facts_html,        
        "hemisphere_img_urls": hemisphere_img_urls
    }

       
    browser.quit()
    return mars_data