import requests
from bs4 import BeautifulSoup


url = "https://khwbn789.github.io/site-web-home-design/shop.html"


def get_text_if_not_none(e):
    if e:
        return e.text.strip()
    return None


# Récupérer le contenu d'une page web

response = requests.get(url)
response.encoding = response.apparent_encoding

if response.status_code == 200:
    html = response.text
    f = open("boutique.html", "w")
    f.write(html)
    f.close()
    print("File 'boutique.html' is generated !")
    print()

    # parser le contenu html avec BeautifulSoup
    soup = BeautifulSoup(html, "html5lib")

    page_title = soup.find('title').text
    print("The page title is: ", page_title)
    print()

    div_navbar = soup.find("div", class_="nav-links")
    e_navbar_links = div_navbar.find_all("a")
    for e_navbar_link in e_navbar_links:
        print("Navbar Links: ", e_navbar_link.text)
        print()
    
    categories_titles = soup.find_all("h1", class_="design-category")
    for category_title in categories_titles:
        print("Categories titles: ", category_title.text)
        print()

    prices_list = []
    prices = soup.find_all("p", class_="product-price")
    for price in prices:
        prices_list.append(price.text)
    
    print("Liste of prices: ", prices_list)
    print()

else:
    print("ERROR code " + str(response.status_code))

print("End of scraping!")

