import flet as ft
from flet_route import Params, Basket

def Page2(page: ft.Page, params: Params, basket: Basket):
    
    return ft.View(
        "/page2/:name",
        
        controls = [
            
            ft.Text("Pagina 2"),
            ft.ElevatedButton("Torna alla home page", on_click= lambda _ : page.go("/")),
            
        ]
    )