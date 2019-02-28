#!/usr/bin/env python
# coding: utf-8

#import dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import pandas as pd
import time
from urllib.request import urlopen
import re

def scrape():

    ## MARS NEWS


    # In[3]:


    #pointing to the directory where chromedriver exists
    executable_path = {"executable_path":"C:\chromedriver_win32\chromedriver"}
    browser = Browser("chrome", **executable_path, headless = False)


    # In[4]:


    #visiting the page
    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)


    # In[5]:


    #using bs to write it into html
    news_html = browser.html
    news_soup = bs(news_html,"html.parser")


    # In[6]:


    headline = news_soup.find("div",class_="content_title").text
    news_paragraph = news_soup.find("div", class_="article_teaser_body").text
    print(headline)
    print("-----------")
    print(news_paragraph)


    # In[7]:


    ## MARS IMAGE


    # In[8]:


    #pointing to the directory where chromedriver exists
    executable_path = {"executable_path":"C:\chromedriver_win32\chromedriver"}
    browser = Browser("chrome", **executable_path, headless = False)


    # In[9]:


    #visiting the page
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)


    # In[10]:


    #using bs to write it into html
    image_html = browser.html
    image_soup = bs(image_html,"html.parser")


    # In[11]:


    #navigate to link
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(2)

    # In[12]:


    browser.click_link_by_partial_text('more info')
    time.sleep(2)
    #get html code once at page
    img_html = browser.html

    #parse
    img_soup = bs(img_html, "html.parser")

    #find path and make full path
    img_path = img_soup.find('figure', class_='lede').a['href']
    featured_image_url = "https://www.jpl.nasa.gov" + img_path


    # In[13]:


    featured_image_url


    # In[14]:


    ## MARS WEATHER


    # In[15]:


    #pointing to the directory where chromedriver exists
    executable_path = {"executable_path":"C:\chromedriver_win32\chromedriver"}
    browser = Browser("chrome", **executable_path, headless = False)


    # In[16]:


    #visiting the page
    weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(weather_url)


    # In[17]:


    #using bs to write it into html
    weather_html = browser.html
    weather_soup = bs(weather_html,"html.parser")


    # In[18]:


    mars_weather = weather_soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    print(mars_weather)


    # In[19]:


    ## MARS FACTS


    # In[20]:


    facts_url = "https://space-facts.com/mars/"
    facts_table = pd.read_html(facts_url)


    # In[21]:


    facts_table


    # In[22]:


    facts_df = facts_table[0]
    facts_df.columns = ["Parameter", "Values"]
    facts_df.set_index(["Parameter"])
    facts_df.head()


    # In[23]:


    facts_html = facts_df.to_html()
    facts_df.to_html('mars_facts_table.html')
    facts_html


    # In[24]:


    ## MARS HEMISPHERE


    # In[25]:


    #pointing to the directory where chromedriver exists
    executable_path = {"executable_path":"C:\chromedriver_win32\chromedriver"}
    browser = Browser("chrome", **executable_path, headless = False)


    # In[27]:



    url_hemisphere = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_hemisphere)


    # In[28]:



    #Setting the base url
    hemisphere_base_url = "https://astrogeology.usgs.gov/"


    # In[29]:


    hemisphere_img_urls = []
    results = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[1]/a/img").click()
    time.sleep(2)
    cerberus_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    time.sleep(1)
    cerberus_image = browser.html
    soup = bs(cerberus_image, "html.parser")
    cerberus_url = soup.find("img", class_="wide-image")["src"]
    cerberus_img_url = hemisphere_base_url + cerberus_url
    print(cerberus_img_url)
    cerberus_title = soup.find("h2",class_="title").text
    print(cerberus_title)
    back_button = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
    cerberus = {"image title":cerberus_title, "image url": cerberus_img_url}
    hemisphere_img_urls.append(cerberus)


    # In[30]:


    results1 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[2]/a/img").click()
    time.sleep(2)
    schiaparelli_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    time.sleep(1)
    schiaparelli_image = browser.html
    soup = bs(schiaparelli_image, "html.parser")
    schiaparelli_url = soup.find("img", class_="wide-image")["src"]
    schiaparelli_img_url = hemisphere_base_url + schiaparelli_url
    print(schiaparelli_img_url)
    schiaparelli_title = soup.find("h2",class_="title").text
    print(schiaparelli_title)
    back_button = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
    schiaparelli = {"image title":schiaparelli_title, "image url": schiaparelli_img_url}
    hemisphere_img_urls.append(schiaparelli)


    # In[31]:


    results1 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[3]/a/img").click()
    time.sleep(2)
    syrtis_major_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    time.sleep(1)
    syrtis_major_image = browser.html
    soup = bs(syrtis_major_image, "html.parser")
    syrtis_major_url = soup.find("img", class_="wide-image")["src"]
    syrtis_major_img_url = hemisphere_base_url + syrtis_major_url
    print(syrtis_major_img_url)
    syrtis_major_title = soup.find("h2",class_="title").text
    print(syrtis_major_title)
    back_button = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
    syrtis_major = {"image title":syrtis_major_title, "image url": syrtis_major_img_url}
    hemisphere_img_urls.append(syrtis_major)


    # In[32]:


    results1 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[4]/a/img").click()
    time.sleep(2)
    valles_marineris_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    time.sleep(1)
    valles_marineris_image = browser.html
    soup = bs(valles_marineris_image, "html.parser")
    valles_marineris_url = soup.find("img", class_="wide-image")["src"]
    valles_marineris_img_url = hemisphere_base_url + syrtis_major_url
    print(valles_marineris_img_url)
    valles_marineris_title = soup.find("h2",class_="title").text
    print(valles_marineris_title)
    back_button = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
    valles_marineris = {"image title":valles_marineris_title, "image url": valles_marineris_img_url}
    hemisphere_img_urls.append(valles_marineris)


    # In[33]:


    hemisphere_img_urls

    scraped_data={
        "Headlline": headline,
        "News": news_paragraph,
        "Weather": mars_weather,
        "Image URL": featured_image_url,
        "Mars Facts": facts_table,
        "Hemisphere URLs": hemisphere_img_urls
    }


