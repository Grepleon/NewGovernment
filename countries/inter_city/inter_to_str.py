from countries.country import Country
from politicians.politician import Politician
from countries.cities.base_city import City
from countries.areas.base_area import Area

def inter_to_str(country:Country, area:Area, city:City, politician:Politician) -> str:
    return f"Ваша популярность: {round(city.vote(politician) / 1000, 1)}%"