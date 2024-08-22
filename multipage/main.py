import flet as ft
from flet_route import Routing, path
from views.home import Home
from views.page1 import Page1
from views.page2 import Page2

def main(page: ft.Page):
    
    elm1 = ft.Text("Ciao", color = "green")
    elm2 = ft.Text("Mi chiamo fracesco", color = "blue")
    
    page.controls.append(elm1)
    page.add(elm2)

ft.app(target= main)