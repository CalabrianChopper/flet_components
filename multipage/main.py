import flet as ft
from flet_route import Routing, path
from multipage.views.home import Home
from multipage.views.page1 import Page1
from multipage.views.page2 import Page2

def main(page: ft.Page):
    
    app_routes = [
        
        path(url="/", view=Home),
        path(url = "/page1/:my_id", view = Page1),
        path(url = "/page2/:name", view = Page2),
        
    ]
    
    Routing(page=page, 
            app_route=app_routes)
    
    page.go(page.route)

ft.app(target= main)