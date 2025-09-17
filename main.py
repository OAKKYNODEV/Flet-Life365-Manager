import flet as ft
import os
from fletx import Xapp, route
from app.states.global_state import GlobalState
from app.views.landing_view import LandingView
from app.views.todo_list import TodoList
from app.views.finance_manage_view import  ExpenseIncomeView
icon_path = os.path.join(os.path.dirname(__file__), 'assets', 'oak_icon.ico')


def main(page: ft.Page):

    page.title = "OAKKY365"
    
    page.window.icon = icon_path
    page.add(ft.SafeArea(ft.Text("Hello World")))
    page.fonts = {
        "IBM": "fonts/IBMPlexSansThai-Regular.ttf",
        "RaleWay": "fonts/Raleway-Regular.ttf",
    }
    page.add(ft.Text("Welcome to OAKKY365"))



    Xapp(
            page=page,
            state=GlobalState,
            init_route='/',
            routes=[
                route(route="/", view=LandingView),
                route(route="/todo-list", view=TodoList),
                route(route="/finance", view =ExpenseIncomeView)
            ],
        )

ft.app(target=main, view=ft.FLET_APP)  # << สำคัญ