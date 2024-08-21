import flet as ft

class Task(ft.UserControl):
    
    def __init__(self, task_name, task_delete):
        super().__init__()
        self.task_name = task_name
        self.task_delete = task_delete
        
    def editClick(self, e):
        pass

    def saveClick(self, e):
        pass
    
    def deleteClick(self, e):
        pass
        
    def build(self):
        self.displayTask = ft.Checkbox(label=self.task_name, 
                                       value=False)
        self.editName = ft.TextField()
        
        self.displayView = ft.Row(controls=[self.displayTask,
                                            ft.Row(controls=[ft.IconButton(ft.icons.CREATE_OUTLINED,
                                                                           on_click=editClick),
                                                             ft.IconButton(ft.icons.DELETE_OUTLINED,
                                                                           on_click=deleteClick)])])
        
        self.editView = ft.Row(visible= False,
                               controls=[self.editName,
                                         ft.IconButton(ft.icons.DELETE_OUTLINED,
                                                        on_click=saveClick)])
        
        return ft.Column(controls=[self.displayView,
                                   self.editView])

class TaskApp(ft.UserControl):
    
    def build(self):
        self.text_field = ft.TextField(width=350)
        self.btn = ft.FloatingActionButton(icon = ft.icons.ADD,
                                           on_click= self.addClick)
        self.tasks = ft.Column()
        taskRow = ft.Column(controls=[ft.Row(controls=[self.text_field, 
                                                       self.btn]), 
                                      self.tasks])
        return taskRow
    
    def addClick(self, e):
        task = Task(self.text_field.value)
    
    def taskDelete(self, task):
        pass
    


def main(page: ft.Page):
    page.title = "QMT ToDo app"
    page.window.width = 500
    page.window.height = 700
    page.bgcolor = "#C0C78C"
    
    taskingApp = TaskApp()
    page.add(taskingApp)
    
ft.app(target= main)