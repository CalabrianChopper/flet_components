import flet as ft

from flet import Page
from flet import Row
from flet import Text
from flet import KeyboardEvent


def main(page: Page) -> None:
    page.title = "Lettore Tastiera"
    page.spacing = 30
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    
    #Eventi dei tasti
    
    key: Text = Text(
                    value= "Key",
                    size= 30
                    )
    shift: Text = Text(
                    value= "Shift",
                    size= 30,
                    color= "red"
                    )
    ctrl: Text = Text(
                    value= "Control",
                    size= 30,
                    color= "blue"
                    )
    alt: Text = Text(
                    value= "Alt",
                    size= 30,
                    color= "green"
                    )
    
    #Gestione eventi
    
    def on_keyboard(e: KeyboardEvent) -> None:
        key.value = e.key
        shift.visible = e.shift
        ctrl.visible = e.ctrl
        alt.visible = e.alt
        print(e.data)
        page.update()
        
    #Link dell'evenjto alla pagina
    
    page.on_keyboard_event = on_keyboard
    
    #Pagina principale
    
    page.add(
        Text("Premi una combinazione di tasti"),
        Row(
            controls=[
                key,
                shift,
                ctrl,
                alt
            ],
            alignment = ft.MainAxisAlignment.CENTER
        )
    )
    
if __name__ == "__main__":
    ft.app(target=main)