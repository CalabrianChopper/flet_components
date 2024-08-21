import flet as ft

from flet import Page
from flet import app
from flet import Column, Row, ResponsiveRow, Tabs, Tab
from flet import Container, Icon, Text, ElevatedButton, Stack, BoxShadow, BoxShape
from flet import MainAxisAlignment, CrossAxisAlignment
from flet import GestureDetector, MouseCursor, AlertDialog
from flet import margin, border

def main(page: Page) -> None:
    page.window.width = 300
    page.scroll = "always"
    
    my_icons = [
        "home",
        "create",
        "person",
        "settings",
        "favorite",
        "grade",
        "shopping_cart_checkout",
        "expand_circle_down"
    ]
    
    def youchange(e):
        pass
    
    def youtaphere(e):
        page.dialog = AlertDialog(
            title= Text(
                "Open you dialog",
                size = 30
                ),
            content= Text(
                "This Sample"
            ),
            actions=[
                ElevatedButton("Close"),
                ElevatedButton("Test")
            ],
        )
        page.dialog.open = True
        page.update()
    
    t = Tabs(
        selected_index= 0,
        animation_duration= 100,
        indicator_color= "green",
        scrollable= True,
        on_change= youchange,
        tabs=[]
    )
    
    for x in my_icons:
        t.tabs.append(
            Tab(
                tab_content= Icon(
                    name = x,
                    size = 25,
                    color = "white"
                )
            )
        )
    
    mylist = Container(
        margin=margin.only(
            top=page.window.height/2
        ),
        content= Column(
            [
                Icon(name = "home", size = 50),
                Text("home Screen", size = 30)
            ],
            alignment= "center"
        )
    )
    
    listnavicon = Container(
        shadow = BoxShadow(
            spread_radius= 1,
            blur_radius= 15
        ),
    margin = margin.only(
        top = page.window.height-100,
        left = 10,
        right = 10
        ),
    border_radius= 30,
    width= page.window.width,
    bgcolor= "green",
    padding= 10,
    
    )
    
    page.overlay.append(
        Stack([
                    ResponsiveRow([
                        Column(
                            col = 12,
                            controls = [
                                listnavicon
                            ]
                        )
                    ]),
                    Container(
                        padding= 19,
                        margin= margin.only(
                            top = page.window.height - 150,
                            left = page.window.width/2 - 35,
                            right = page.window.width/2 - 35,
                        ),
                        bgcolor= "green",
                        border = border.all(5, "white"),
                        shape = BoxShape.CIRCLE,
                        content= GestureDetector(
                            mouse_cursor= MouseCursor.CLICK,
                            on_tap= youtaphere,
                            content= Icon(
                                name = "add",
                                size = 40
                            )
                        )
                    )
                ]
            )
        )
    
    page.add(
        Row(
            [
                mylist
            ],
            alignment = "center"
        )
    )
    
    

if __name__ == "__main__":
    app(target=main)