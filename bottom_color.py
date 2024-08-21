from flet import *

def main(page: Page) -> None:
    page.window.width = 400
    
    page.padding = 0
    page.spacing = 0
    
    def changeposition(e):
        ids = e.control.data.controls[0].value
        print(ids)
        
        controls=[
            bottom_bar.content.controls[0],
            bottom_bar.content.controls[1],
            bottom_bar.content.controls[2]
        ]
        
        for i, control in enumerate(controls):
            control.content.controls[1].visible = (i == ids)
            control.bgcolor = e.control.data.controls[1].value if i == ids else "white"
            page.controls[0].bgcolor = e.control.data.controls[1].value
            
        page.update()
    
    bottom_bar = Container(
        bgcolor= "white",
        padding= 20,
        bottom= 10,
        left= 10,
        right= 10,
        width= page.window.width,
        border_radius= border_radius.only(
            bottom_left= 30,
            bottom_right= 30
        ),
        content= Row([
            Container(
                bgcolor= "red200",
                border_radius= 30,
                padding= 10,
                animate= animation.Animation(300, "cubic"),
                content=Row([
                    IconButton(
                        icon="home",
                        icon_size=30,
                        data= Row([Text(0), Text("red200")]),
                        on_click= changeposition
                    ),
                    Text(
                        "Home",
                        size= 20,
                        visible= True
                    )
                ])
            ),
            Container(
                bgcolor= "white",
                border_radius= 30,
                padding= 10,
                animate= animation.Animation(300, "cubic"),
                content=Row([
                    IconButton(
                        icon="person",
                        icon_size=30,
                        data= Row([Text(1), Text("yellow")]),
                        on_click= changeposition
                    ),
                    Text(
                        "Person",
                        size= 20,
                        visible= True
                    )
                ])
            ),
            Container(
                bgcolor= "white",
                border_radius= 30,
                padding= 10,
                animate= animation.Animation(300, "cubic"),
                content=Row([
                    IconButton(
                        icon="bookmark",
                        icon_size=30,
                        data= Row([Text(2), Text("blue200")]),
                        on_click= changeposition
                    ),
                    Text(
                        "Bookmark",
                        size= 20,
                        visible= True
                    )
                ])
            ),
            
        ],
        alignment= "spaceBetween")
    )
    
    my_content = Container(
        padding= 10, 
        animate= animation.Animation(300, "easeIn"),
        alignment= alignment.center,
        content = Text(
            "MyApp",
            size=50
        )
    )
    
    
    page.add(
        Container(
            width= page.window.width,
            height= page.window.height,
            animate= animation.Animation(300, "easeIn"),
            bgcolor= "red200",
            content= Stack([
                my_content, 
                bottom_bar
            ])
        )
    )
    
if __name__ == "__main__":
    app(target= main)