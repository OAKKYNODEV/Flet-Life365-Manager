import time

import flet as ft

from app.utils.custom_text_style import CustomTextStyle
from app.utils.constants import *


def create_drawer(self):
    LOGOUT_BUTTON = ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor=ft.Colors.RED, padding=ft.padding.symmetric(
        vertical=20, horizontal=65), shape=ft.RoundedRectangleBorder(radius=10),)

    DRAWER_TEXTSTYLE = CustomTextStyle.drawer()

    SUBMENU_STYLE = CustomTextStyle.custom(
        font_size=16, font_weight=ft.FontWeight.BOLD, color="")

    def handle_dismissal(e):
        print("Drawer dismissed")

    def handle_change(e):
        print(f"Selected Index changed: {e.selected_index}")

    def goto(path):
        print("\n-------------------------------------------------------------")
        print(f"Drawer clicked: {path}")
        print("-------------------------------------------------------------\n")
        self.pop_go(path)

    drawer = ft.NavigationDrawer(
        on_dismiss=handle_dismissal,
        on_change=handle_change,
        elevation=None,
        controls=[
            ft.Container(
                content=ft.Column(
                    controls=[
                        # /////TopDrawer////////
                        ft.Container(

                            margin=ft.margin.only(top=20, left=45),
                            content=ft.Column(
                                controls=[
                                    ft.Image(
                                        src="assets/images/logo_golf.png", width=200, height=200),
                                    ft.Text(
                                        "Hello OAKKY AITTHIPHON",
                                        style=CustomTextStyle.normal()
                                    ),
                                ],

                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            ), height=300
                        ),
                        # /////////////////
                        ft.Divider(thickness=2),
                        # /////MenuDrawer////////
                        ft.Container(
                            padding=ft.padding.only(left=5),
                            content=ft.Column(
                                controls=[
                                                                        ft.ListTile(
                                        leading=ft.Icon(ft.Icons.SELF_IMPROVEMENT),
                                        selected=self.page.route == '/',
                                        selected_color=ft.Colors.WHITE,
                                        selected_tile_color=THEME_COLOR,
                                        title=ft.Text(
                                            "OAKKY Progress", style=DRAWER_TEXTSTYLE),
                                        on_click=lambda _: goto('/'),
                                        bgcolor=ft.Colors.WHITE
                                    ),
                                    ft.ListTile(
                                        leading=ft.Icon(ft.Icons.PLAYLIST_ADD_CHECK_SHARP),
                                        selected=self.page.route == '/todo-list',
                                        selected_color=ft.Colors.WHITE,
                                        selected_tile_color=THEME_COLOR,
                                        title=ft.Text(
                                            "To-Do List", style=DRAWER_TEXTSTYLE),
                                        on_click=lambda _: goto('/todo-list'),
                                        bgcolor=ft.Colors.WHITE
                                    ),
                                    ft.ListTile(
                                        leading=ft.Icon(ft.Icons.ATTACH_MONEY),
                                        selected=self.page.route == '/finance',
                                        selected_color=ft.Colors.WHITE,
                                        selected_tile_color=THEME_COLOR,
                                        title=ft.Text(
                                            "รายรับ รายจ่าย", style=DRAWER_TEXTSTYLE),
                                        on_click=lambda _: goto('/finance'),
                                        # on_click=lambda _: self.pop_all_go("/buy_coupon"),
                                        bgcolor=ft.Colors.WHITE
                                    ),
                                    ft.ListTile(
                                        leading=ft.Icon(ft.Icons.FOOD_BANK),
                                        selected=self.page.route == '/reprint',
                                        selected_color=ft.Colors.WHITE,
                                        selected_tile_color=THEME_COLOR,
                                        title=ft.Text(
                                            "มื้ออาหาร", style=DRAWER_TEXTSTYLE),
                                        on_click=lambda _: goto("/reprint"),
                                        bgcolor=ft.Colors.WHITE
                                    ),
                                                                        ft.ListTile(
                                        leading=ft.Icon(ft.Icons.VIEW_LIST),
                                        selected=self.page.route == '/reprint',
                                        selected_color=ft.Colors.WHITE,
                                        selected_tile_color=THEME_COLOR,
                                        title=ft.Text(
                                            "โปรแกรมออกกำลังกาย", style=DRAWER_TEXTSTYLE),
                                        on_click=lambda _: goto("/reprint"),
                                        bgcolor=ft.Colors.WHITE
                                    ),


                                ]
                            )

                        ),
                        # //////////////////

                        # /////SubMenu////////
                        ft.ExpansionTile(
                            title=ft.Container(
                                padding=ft.padding.only(left=6),
                                content=ft.Row(
                                    controls=[
                                        ft.Icon(
                                            ft.Icons.ADD_SHARP),
                                        ft.Text(
                                            "Utils Tool", style=DRAWER_TEXTSTYLE),
                                    ],
                                    alignment=ft.MainAxisAlignment.START,
                                    spacing=12,
                                ),
                            ),
                            initially_expanded=self.page.route in [
                                "/report_by_group", "/report_by_coupon", "/report_summary"],
                            controls=[
                                ft.ListTile(
                                    title=ft.Text(
                                        "Remove Background", style=SUBMENU_STYLE),
                                    selected=self.page.route == '/report_by_group',
                                    selected_color=ft.Colors.WHITE,
                                    selected_tile_color=THEME_COLOR,
                                    on_click=lambda _: goto(
                                        "/report_by_group"),
                                    bgcolor=ft.Colors.WHITE
                                ),
                                ft.ListTile(
                                    title=ft.Text(
                                        "Read Text From Image", style=SUBMENU_STYLE),
                                    selected=self.page.route == '/report_by_coupon',
                                    selected_color=ft.Colors.WHITE,
                                    selected_tile_color=THEME_COLOR,
                                    on_click=lambda _: goto(
                                        "/report_by_coupon"),
                                    bgcolor=ft.Colors.WHITE
                                ),
                                ft.ListTile(
                                    title=ft.Text(
                                        "Convert File", style=SUBMENU_STYLE),
                                    selected=self.page.route == '/report_summary',
                                    selected_color=ft.Colors.WHITE,
                                    selected_tile_color=THEME_COLOR,
                                    on_click=lambda _: goto("/report_summary"),
                                    bgcolor=ft.Colors.WHITE
                                ),
                            ],
                        ),
                        # ft.Container(
                        #     padding=ft.padding.only(left=5),
                        #     content=ft.Column(
                        #         controls=[
                        #             ft.ListTile(
                        #                 leading=ft.Image(
                        #                     src="assets/images/shotgun.png"),
                        #                 title=ft.Text(
                        #                     "Shotgun", style=DRAWER_TEXTSTYLE),
                        #                 selected=self.page.route == '/shotgun',
                        #                 selected_color=ft.Colors.WHITE,
                        #                 selected_tile_color=THEME_COLOR,
                        #                 on_click=lambda _: goto("/shotgun"),
                        #                 bgcolor=ft.Colors.WHITE
                        #             ),
                        #         ]
                        #     )
                        # ),

                        # //////////////////

                        ft.Container(height=200),
                        ft.Container(
                            alignment=ft.alignment.center,
                            content=ft.ElevatedButton(
                                "Logout",
                                on_click=lambda _: self.pop_all_go("/login"),
                                style=LOGOUT_BUTTON,
                            ),
                        ),
                        ft.Container(
                            expand=True,
                            alignment=ft.alignment.center,
                            content=ft.Text(
                                f"Golf Starter {VERSION_SOFTWARE} | Developed by ITD",
                                style=CustomTextStyle.small(
                                    font_size_delta=-2),
                            )
                        ),
                    ],
                ),
                height=1014,
                bgcolor=ft.Colors.WHITE
            )
        ],
    )

    return drawer
