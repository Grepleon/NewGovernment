import os
from dotenv import load_dotenv

load_dotenv()

name_project = os.getenv("NAMEPROJECT", "New Government")
bg_color = os.getenv("BGCOLOR", "black")
name_country = os.getenv("NAME", "Великая Земля")
first_year = int(os.getenv("YEAR", 2053))
width = int(os.getenv("WIDTH", 1200))
height = int(os.getenv("HEIGHT", 650))

base_off_button_color = os.getenv("BASEOFFBUTTONCOLOR")
base_off_bg_button_color = os.getenv("BASEOFFBGBUTTONCOLOR")
base_on_button_color = os.getenv("BASEONBUTTONCOLOR")
base_on_bg_button_color = os.getenv("BASEONBGBUTTONCOLOR")

dark_off_bg_button_color = os.getenv("DARKOFFBUTTONCOLOR")

cancel_off_button_color = os.getenv("CANCELOFFBUTTONCOLOR")
cancel_off_bg_button_color = os.getenv("CANCELOFFBGBUTTONCOLOR")
cancel_on_button_color = os.getenv("CANCELONBUTTONCOLOR")
cancel_on_bg_button_color = os.getenv("CANCELONBGBUTTONCOLOR")

main_button_coordinates = [int(coordinate) for coordinate in os.getenv("MAINBUTTONCOORDINATES").split()]
main_button_text = os.getenv("MAINBUTTONTEXT")

path_to_picture_into_main = os.getenv("PATHTOPICTUREINTOMAINMENU")
coordinates_picture_into_main = [int(coordinate) for coordinate in os.getenv("COORDINATESPICTUREINTOMAINMENU").split()]

number_main_button = 0

character_button_text = os.getenv("CHARACTERBUTTONTEXT")
character_button_coordinates = [int(coordinate) for coordinate in os.getenv("CHARACTERBUTTONCOORDINATES").split()]
cancel_character_button_coordinates = [int(coordinate) for coordinate in
                                       os.getenv("CANCELCHARACTERBUTTONCOORDINATES").split()]
cancel_charactor_button_text = os.getenv("CANCELCHARACTERBUTTONTEXT")

colors_noice = os.getenv("COLORSNOICE").split()
size_noice = int(os.getenv("SIZENOICE", 1))
quantity_noice = int(os.getenv("QUANTITYNOICE", 256))

path_to_frame_picture = os.getenv("PATHTOCHOOSECHARACTERPICTURE")
quantity_frames = int(os.getenv("QUANTITYFRAMESCHARACTER", 9))
coordinates_frame_picture = [int(coordinate) for coordinate in os.getenv("COORDINATESCHOOSECHARACTERPICTURE").split()]
frame_size_add = int(os.getenv("FRAMESIZEADD"))
frame_size_into = [int(coord) for coord in os.getenv("FRAMESIZEINTO").split()]
height_button_in_frame = int(os.getenv("HEIGHTBUTTONINFRAME"))

names_politicians = [politician for politician in os.getenv("NAMESCHARACTERS").split(", ")]
politicians_folder = os.getenv("FOLDERWITHPICTUREPOLITICIANS")

small_flag = os.getenv("SMALLFLAG")
normal_flag = os.getenv("NORMALFLAG")
hover_flag = os.getenv("HOVERFLAG")

format_pictures = os.getenv("FORMAT", '.png')