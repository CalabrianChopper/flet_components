import flet as ft
from flet_route import Params, Basket

def Page1(page: ft.Page, params: Params, basket: Basket):
    
    return ft.View(
        "/page1/:my_id",
        
        controls = [
            
            ft.Text("Pagina 1"),
            ft.ElevatedButton("Torna alla home page", on_click= lambda _ : page.go("/")),
            
        ]
    )