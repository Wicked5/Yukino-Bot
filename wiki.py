from bs4 import BeautifulSoup
import requests

def look_up(topic):
    result = ""
    source = requests.get("https://en.wikipedia.org/wiki/{}".format(topic)).text

    soup = BeautifulSoup(source, 'lxml')

    try:
        information = soup.find("div", class_= "mw-parser-output")
        paragraphs = information.find_all('p')                                                         # give all the paragraphs under the mw-parser-output section
        other_paragraph = [p for p in paragraphs if 'mw-empty-elt' not in p.attrs.get('class', [])]    # iterate over the paragraphs and give back if not a mw-empty-elt class paragraph
        result = other_paragraph[0].text  #since the paragraphs with p under the class "mw-parser-output" are stored as an array, take 1st element to take 1st paragraph 
        
    
    except AttributeError: #if the webpage doesn't exist, neither does html code nor the attributes. Thus it would return an AttributeError
        result = "This topic could not be found, please try another search"
        return result 

    return result 