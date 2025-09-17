import flet as ft
from app.utils.constants import *
from datetime import datetime, timedelta


def create_appbar(self, title_str: str) -> ft.AppBar:

        DATEPICKER_BUTTON = ft.ButtonStyle(text_style=CustomTextStyle.button(font_size_delta=-2))
        APPBAR_TEXTSTYLE = CustomTextStyle.app_bar()

        

        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y    %H:%M")

       
        date_text = ft.Text(
            dt_string,
            text_align=ft.TextAlign.CENTER,
            style=APPBAR_TEXTSTYLE
        )

        def showdrawer(e):
            print(self.page.views)
            self.page.views[-1].drawer.open = True
            self.update()
            # self.page.client_storage.set("drawer", True)
            # self.page.drawer.open = True
            # self.page.drawer.update()

        

    


        return ft.AppBar(
            leading=ft.IconButton(
                content=ft.Icon(name=ft.Icons.MENU,color=ft.Colors.WHITE),
                on_click=lambda e : showdrawer(e)
            ),
            leading_width=50,
            title=ft.Row(
                controls=[
                    ft.Image(src="assets/oakky_logo.jpg", width=100, height=100),  
                    ft.Container(
                        date_text,
                        alignment=ft.alignment.center,
                        expand=True
                    ),
                    ft.ElevatedButton(
                            content=ft.Row(
                                controls=[
                                    ft.Icon(name=ft.Icons.REFRESH, color=ft.Colors.WHITE),
                                    ft.Text("Refresh", color=ft.Colors.WHITE),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=5
                            ),
                            style=DATEPICKER_BUTTON,
                            bgcolor=ft.Colors.GREY,
    
                        )
                                    
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.MainAxisAlignment.CENTER
            ),
            bgcolor=THEME_COLOR,
        )

