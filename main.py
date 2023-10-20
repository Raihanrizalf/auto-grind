from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

# requirement
# pip install selenium==4.9.0
# pip install webdriver-manager

# Keyword List (generated using AI)
keywords = [
    "Variable",
    "Function",
    "Loop",
    "If statement",
    "Array",
    "Class",
    "Method",
    "Interface",
    "Inheritance",
    "Polymorphism",
    "Abstraction",
    "Encapsulation",
    "Algorithm",
    "Data structure",
    "Stack",
    "Queue",
    "Linked list",
    "Tree",
    "Graph",
    "Hash table",
    "Sorting",
    "Searching",
    "Recursion",
    "Binary",
    "Compiler",
    "Interpreter",
    "Bytecode",
    "Source code",
    "Binary code",
    "Debugging",
    "Testing",
    "Unit test",
    "Integration test",
    "Continuous integration",
    "Version control",
    "Git",
    "Repository",
    "Branching",
    "Merging",
    "Pull request",
    "Agile",
    "Scrum",
    "Kanban",
    "Waterfall",
    "Software development",
    "Web development",
    "Mobile development",
    "Game development",
    "Artificial intelligence"
]

if __name__ == '__main__':
 
    # create object
    edgeBrowser = webdriver.Edge(EdgeChromiumDriverManager().install())

    edgeBrowser.get('https://www.bing.com')
    time.sleep(5)

    for i, keyword in enumerate(keywords, 1):
      form = WebDriverWait(edgeBrowser, 10).until(EC.presence_of_element_located((By.ID, 'sb_form_q')))
      time.sleep(1)
      form.clear()
      form.send_keys(keywords[i])
      form.send_keys(Keys.ENTER)
      time.sleep(1)

# notes:
# this script tested and works using selenium 4.9.0 & python 3.11.3