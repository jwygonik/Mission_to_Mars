# Import Splinter and BeautifulSoup

from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# Set up Splinter

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# Visit the mars nasa news site

url = 'https://redplanetscience.com'
browser.visit(url)


# Optional delay for loading the page

browser.is_element_present_by_css('div.list_text', wait_time=1)



# Set up html parser
    # slide_elem - variable to look for the <div /> tag and its descendent 

html = browser.html

news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')



# assign the title and summary text to variables 

slide_elem.find('div', class_='content_title')



# use the parent element (slide_elem) to find the first 'a' tag and save it as news title

news_title = slide_elem.find('div', class_='content_title').get_text()
news_title
 


# In[20]:


# Use the parent element to find the paragraph text

news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[21]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# Use Dev tools to look for all the button elements

# Find and click the full image button

full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# Parse the resulting html w/ soup

html = browser.html

img_soup = soup(html, 'html.parser')



# find the relative image url
    # .get('src') pulls the link to the image

img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel



# Use the base url to create an absolute url

img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url



# Scrape the entire table with Pandas .read_html() function
    # pd.read_html - specifically searches for and returns list of tables found in the HTML
    # specifying index of 0 tells pandas to pull only the first table it encounters/the first item in the list
    # df.columns - assigns columns to the new df
    # df.set_index - turns the description column into the dfs index
    # inplsce=True means updated index remains in place

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df



# Use .to_html() function to convert out DF back to HTML ready code

df.to_html()



# End the session 

browser.quit()

