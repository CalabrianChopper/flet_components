import flet as ft

def main(page: ft.Page):
    
    def add_task(p):
        check_box = ft.Checkbox(value=False)
        check_box_text = ft.Text(value= text_field.value, size=20)
        task_row = ft.Row(controls=[check_box,check_box_text],
                      alignment=ft.MainAxisAlignment.START)
        page.add(task_row)
        

    page.window.width = 500
    page.window.height = 700
    page.bgcolor = "#C0C78C"
    text_field = ft.TextField(width=350, color= "#FEFAE0")
    el_but = ft.FloatingActionButton(icon= ft.icons.ADD, 
                               bgcolor= "#A6B37D",
                               on_click= add_task)
    check_box = ft.Checkbox(value=True)
    check_box_text = ft.Text(value= "task 1", size=20)
    
    entries_row = ft.Row(controls=[text_field,el_but],
                         alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    
    task_row = ft.Row(controls=[check_box,check_box_text],
                      alignment=ft.MainAxisAlignment.START)
    
    page.add(
        entries_row
    )
    

ft.app(target= main)