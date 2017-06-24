"""For Database Entries"""
from sqlalchemy.orm import create_engine
from sqlalchemy.orm import sessionmaker
from catalog import db
from catalog.models import User, Category, Item


def add_items(category, item_names):
	for name in item_names:
		item = Item(name = name, category_id = category.id)
		db.add(item)
	db.commit()

def add_item(category, item):
    item.category_id = category.id
    db.add(item)
    db.commit()


user = User(name = "Yang Yuan",
    email = "yanginvincible@longlivesummons.org",
    picture = "http://2.bp.blogspot.com/-S5USSONx5P0/VnEOIKKvJOI/AAAAAAAAsZw/KrKRoPui3Vk/s0-Ic42/000.jpg")

db.add(user)
db.commit()


category1 = Category(name = "Martial Arts")
db.add(category1)

category2 = Category(name = "Painting Arts")
db.add(category2)

category3 = Category(name = "Music Arts")
db.add(category3)

category4 = Category(name = "Calligraphy")
db.add(category4)

category5 = Category(name = "Strategy Arts(board games)") 

db.commit()


add_item(category1, Item(user = user,
                         name = "Kung Fu",
                         description = "Learnt by skill and practice."))
add_item(category1, Item(user = user,
                         name = "Martial Art",
                         description = "The Military Kung Fu."))
add_item(category1, Item(user = user,
                         name = "Law of the fist",
                         description = "Basically Curled Finger skills."))

add_item(category2, Item(user = user,
                         name = "Gongbi(meticulous)",
                         description = "uses highly detailed brushstrokes that delimits details very precisely."))
add_item(category2, Item(user = user,
                         name = "Ink and Wash",
                         description = "loosely termed watercolour or brush painting"))


add_item(category3, Item(user = user,
                         name = "Zither",
                         description = "Chinese musical instrument."))
add_item(category3, Item(user = user,
                         name = "Ichigenkin",
                         description = "Japanese single chord Zither."))
add_item(category3, Item(user = user,
                         name = "Geomungo",
                         description = "Korean Orchestral Zither."))

add_item(category4, Item(user = user,
                         name = "Chinese Calligrphy",
                         description = "The method of writing Chinese characters."))
add_item(category4, Item(user = user,
                         name = "Japanese Calligraphy",
                         description = "The technique to write Japanese Characters."))
add_item(category4, Item(user = user,
                         name = "Korean Calligraphy",
                         description = "The way to imprint Korean Characters."))

add_item(category5, Item(user = user,
                         name = "Go",
                         description = "Traditional Chinese Strategy Game."))
add_item(category5, Item(user = user,
                         name = "Chess",
                         description = "Strategy game developed in India.Played on a 8x8 Square."))
add_item(category5, Item(user = user,
                         name = "Backgammon",
                         description = "Traditional Korean strategy(signifying life and death) game"))
