# Web development frameworks
# collection of modules or packages which help in writing web applications or web development
# Frameworks provide functionalities to perform operations for developing web applications:
# URL routing - mechanism of mapping the url directly to the code that creates the web page
# Input Form, Handling  and validation
# Output Formats with Templating Engine(allows developers to generate desired  content types) e.g html, xml or json
# Database connection, manipulation using Object Relational Mapper -code library automates the transfer of data
# web security
# Session storage and retrieval

""" web scrapping - extracting data from various websites"""
# it is a technique employed to extract large amount of data from websites
# whereby the data is extracted and saved to a local file in your computer or to a database:
# Document load - load the entire document which is your html page
# parsing -interprete your document
# Extraction
# Transformation -convert the data into useful formats
# libraries - beautiful soap, pattern, scrapy, mechanize

# # Demo - scrape flipkart
# fetching details like name of the product, price and ratings of the searched products
# search the name of the product

from bs4 import BeautifulSoup as soup
import urlopen as uReq
my_url = "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
uClient = uReq(my_url)  # uReq basically opens up the connection
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class": "col_2-gKeQ"})
