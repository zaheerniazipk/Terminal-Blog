from database import Database
from menu import Menu


# Database Interaction
Database.initialize()

menu = Menu()
menu.run_menu()