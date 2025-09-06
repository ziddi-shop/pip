import os

print("@nobi_shops")

meta = [
    "telebot",
    "OneClick",
    "stdiomask",
    "user_agent",
    "instaloader",
    "requests",
    "rich",
    "pyfiglet",
    "colorama",
    "InstagramAPI",
    "generate_user_agent",
    "selenium",
    "cfonts",               
    "pycryptodome"
    "fake_useragent"
    "asmix"          
]

for package in meta:
    os.system(f"pip install {package}")

print("done.")
