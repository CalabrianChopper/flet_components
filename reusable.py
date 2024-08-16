import flet as ft

from flet import UserControl
from flet import Text
from flet import Row
from flet import Page
from flet import ControlEvent
from flet import MainAxisAlignment
from flet import ElevatedButton

class increment_counter(UserControl):
    
    def __init__(self, text: str, start_numb: int=0) -> None:
        super().__init__()
        self.text = text
        self.start_numb = start_numb
        self.counter = start_numb
        self.text_numb = Text(value=str(start_numb), size=40)
        
    def increment(self, e: ControlEvent) -> None:
        self.counter += 1
        self.text_numb.value = str(self.counter)
        self.update()
        
    def build(self) -> Row:
        return Row(
            controls=[
                ElevatedButton(
                    self.text,
                    on_click= self.increment
                ),
                self.text_numb
            ],
            alignment = MainAxisAlignment.SPACE_BETWEEN,
            width = 300
        )
        
def main(page: Page) -> None:
    page.title = "Reusable app"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 400
    page.window_height = 500
    page.window.resizable = False
    
    page.add(increment_counter("People"))
    page.add(increment_counter("Animals", 10))
    
if __name__ == "__main__":
    ft.app(target=main)