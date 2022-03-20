from random import choice
import requests
from bs4 import BeautifulSoup

themes = ['love','sad','time','death','faith','happiness', 'hope', 'humour','inspiration','philosophy','poetry', 'relationships','science','writing']

def themeList():
    return themes


def generateData():
    generateQuotes.getQuotes(themes)


def randomtheme():
    return choice(themes)


def change_theme():
    theme = randomtheme()



# generateQuotes from goodreads coz why not?
# this serves as the corpus for markovify
def getQuote(themes):
    for theme in themes:
        print(theme)
        print(("Generating file for {}.").format(theme))
        filename = ("corpus/{}.txt").format(theme)
        with open(filename, 'wb') as f:  
                    for i in range(1, 101):
                        print(i)
                        quotes_page = requests.get(
                            ("https://www.goodreads.com/quotes/tag/{}?page={}").format(theme, i)).text
                        soup = BeautifulSoup(
                            quotes_page,
                            "html.parser")


                        for notNeeded in soup(["script", "style", "span", "a"]):
                            notNeeded.extract()

                        quotes = [
                            quote for quote in soup.find_all(
                                'div',
                                attrs={'class': 'quoteText'})]
                        for q in quotes:
                            text = q.find_all(text=True)
                            for line in text:
                                if line.strip() == "―" or line.strip() == ",":
                                    continue
                                f.write(line.strip().encode('utf-8'))
                                f.write('\n'.encode('utf-8'))  # separate quotes