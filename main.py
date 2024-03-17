import requests
from bs4 import BeautifulSoup

#replace url with the game you want to check
URL = "https://store.steampowered.com/app/1174180/Red_Dead_Redemption_2/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="game_area_purchase")
#this finds the elements in the game page
current_sales = results.find_all("div", class_="discount_block game_purchase_discount")
game_elements = results.find_all("div", class_="game_area_purchase_game")
for current_sale, game_element in zip(current_sales, game_elements):
    current_sale_price = current_sale.find("div", class_="discount_final_price")
    original_price = current_sale.find("div", class_="discount_original_price")
    game_title = game_element.find("h1")
    game_description = game_element.find("p")
    sale_end = game_element.find("p", class_="game_purchase_discount_countdown")

    print("Title:" + game_title.text.strip())
    print("Description:" + game_description.text.strip())
    if sale_end:
        print("Sales end time:" + sale_end.text.strip())
    print("Current sales price:" + current_sale_price.text.strip())
    print("Original sales price:" + original_price.text.strip())
    print()



