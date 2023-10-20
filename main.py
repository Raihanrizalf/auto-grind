from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

# requirement
# pip install selenium==4.9.0
# pip install
if __name__ == '__main__':
 
    # create object
    edgeBrowser = webdriver.Edge(EdgeChromiumDriverManager().install())
 
    # open browser and navigate to facebook
    edgeBrowser.get('https://www.bing.com')
    time.sleep(60)
