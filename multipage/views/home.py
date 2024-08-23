import flet as ft
from flet_route import Params, Basket

def Home(page: ft.Page, params: Params, basket: Basket):
    

    return ft.View(
        "/",
        
        controls= [
            
            ft.Text("This is home view"),
            ft.ElevatedButton("Go to page 1", on_click= lambda _: page.go("/page1/10")),
            ft.ElevatedButton("Go to page 2", on_click= lambda _: page.go("/page2/FletApp"))
            
        ]
    )