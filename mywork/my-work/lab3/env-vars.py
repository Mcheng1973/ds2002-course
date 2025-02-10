
#!/usr/bin/env python3
import os

fav_color = input("What is your favorite color? ")
hobby = input("What is your favorite hobby? ")
dream_city = input("What city do you dream of living in?")

os.environ["FAV_COLOR"] = fav_color
os.environ["HOBBY"] = hobby
os.environ["DREAM_CITY"] = dream_city

print(os.getenv("FAV_COLOR"))
print(os.getenv("HOBBY"))
print(os.getenv("DREAM_CITY"))
