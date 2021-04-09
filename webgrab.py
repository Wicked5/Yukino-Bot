from bs4 import BeautifulSoup
import requests

def generate():
    description = ""
    website = requests.get("https://4anime.to/random")
    website2 = website.text
    soup = BeautifulSoup(website2, 'lxml')
    dsection = soup.find('div', class_ = "sixteen wide column synopsis")
    paragraphs = dsection.find_all('p')  
    workingones = [p for p in paragraphs if 'description-mobile' not in p.attrs.get('class', [])] 
    for i in workingones:
        description += i.text 
    psection = soup.find("div", class_ = "cover")
    p = str(psection.img).split("\"")
    photo = "https://4anime.to" + p[1]

    return "With courtesy of 4anime.to\n{}: {}\n{}".format(soup.title.text, description, photo)
    #return soup

