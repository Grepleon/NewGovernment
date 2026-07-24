import os
from dotenv import load_dotenv

load_dotenv()

name_project = os.getenv("NAMEPROJECT", "New Government")
bg_color = os.getenv("BGCOLOR", "black")
name_country = os.getenv("NAME", "Великая Земля")
first_year = int(os.getenv("YEAR", 2053))
width = int(os.getenv("WIDTH", 1000))
height = int(os.getenv("HEIGHT", 750))