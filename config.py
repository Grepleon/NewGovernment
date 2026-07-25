import os
from dotenv import load_dotenv

load_dotenv()

name_project = os.getenv("NAMEPROJECT", "New Government")
bg_color = os.getenv("BGCOLOR", "black")
name_country = os.getenv("NAME", "Великая Земля")
first_year = int(os.getenv("YEAR", 2053))
width = int(os.getenv("WIDTH", 1000))
height = int(os.getenv("HEIGHT", 750))

base_off_button_color = os.getenv("BASEOFFBUTTONCOLOR")
base_off_bg_button_color = os.getenv("BASEOFFBGBUTTONCOLOR")
base_on_button_color = os.getenv("BASEONBUTTONCOLOR")
base_on_bg_button_color = os.getenv("BASEONBGBUTTONCOLOR")

main_button_coordinates = [int(coordinate) for coordinate in os.getenv("MAINBUTTONCOORDINATES").split()]
main_button_text = os.getenv("MAINBUTTONTEXT")
