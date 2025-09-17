import json
from arrow import now
import flet as ft
from fletx import Xview
from datetime import datetime

from app.utils.helpers import argb_to_hex


class TodoList(Xview):
    def __init__(self, page: ft.Page, state=None, params=None):
        super().__init__(page, state, params)
        self.page = page
        self.state = state
        self.params = params

        self.tasks = []
        self.selected_date = None
        self.selected_time = None

        self.task_counter = ft.Text(
            "0 tasks, 0 completed", size=14, color=ft.Colors.BLACK, text_align=ft.TextAlign.CENTER, font_family="IBM")

        self.task_input = ft.TextField(hint_text="Enter task...", expand=True, border_radius=8, hint_style=ft.TextStyle(
            font_family="IBM", weight=ft.FontWeight.BOLD),
            content_padding=ft.padding.symmetric(horizontal=12, vertical=8))

        self.date_button = ft.ElevatedButton(
            "📅 Pick Date", on_click=self.open_date_picker)
        self.time_button = ft.ElevatedButton(
            "⏰ Pick Time", on_click=self.open_time_picker)

        self.priority_picker = ft.Dropdown(
            hint_text="Priority",
            hint_style=ft.TextStyle(
                font_family="IBM", weight=ft.FontWeight.BOLD),
            width=140,
            text_style=ft.TextStyle(font_family="IBM"),
            selected_trailing_icon=ft.Icon(ft.Icons.CHECK),
            border_radius=8,
            options=[
                ft.dropdown.Option("Do It Now"),
                ft.dropdown.Option("Decide"),
                ft.dropdown.Option("Dump It")
            ],
        )

        self.add_button = ft.ElevatedButton(
            text="Add Task",
            icon=ft.Icons.ADD,
            on_click=self.add_task,
            bgcolor=ft.Colors.BLACK,
            color=ft.Colors.WHITE,
            height=40,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
        )

        self.clear_button = ft.TextButton(
            text="Clear Completed",
            icon=ft.Icons.CLEAR_ALL,
            on_click=self.clear_completed,
            style=ft.ButtonStyle(color=ft.Colors.BLACK),
        )

        self.task_list = ft.ListView(
            expand=True, spacing=10, padding=ft.padding.only(top=10, bottom=10))

        self.completed_list = ft.ListView(
            expand=True, spacing=10, padding=ft.padding.only(top=10, bottom=10))

        self.mode_segment = ft.SegmentedButton(
            show_selected_icon=False,
            selected={""},
            allow_multiple_selection=False,
            segments=[
                ft.Segment(value="Date", label=ft.Text("Date"),
                           icon=ft.Icon(ft.Icons.DATE_RANGE)),
                ft.Segment(value="Time", label=ft.Text("Time"),
                           icon=ft.Icon(ft.Icons.ACCESS_TIME)),
            ],
            on_change=self.handle_segment_change,
        )

    def handle_segment_change(self, e):
        selected_list = json.loads(e.data)
        self.mode = selected_list[0] if selected_list else ""
        if self.mode == "Date":
            self.open_date_picker(e)
        elif self.mode == "Time":
            self.open_time_picker(e)

    def open_date_picker(self, e=None):
        self.date_picker = ft.DatePicker(
            first_date=datetime(year=2000, month=1, day=1),
            last_date=datetime(year=2030, month=12, day=31),
            on_change=self.set_date
        )
        self.page.overlay.append(self.date_picker)
        self.date_picker.open = True
        self.page.update()

    def open_time_picker(self, e=None):
        self.time_picker = ft.TimePicker(
            confirm_text="OK",
            help_text="Pick time",
            on_change=self.set_time
        )
        self.page.overlay.append(self.time_picker)
        self.time_picker.open = True
        self.page.update()

    def set_date(self, e):
        self.selected_date = e.data
        self.date_button.text = "Date Selected:", self.selected_date
        self.page.update()

    def set_time(self, e):
        self.selected_time = e.data
        self.time_button.text = "Time Selected:", self.selected_time,
        self.page.update()

    def get_priority_icon(self, level):
        icon_map = {
            "Do It Now": ("🔴", ft.Colors.RED),
            "Decide": ("🟠", ft.Colors.ORANGE),
            "Dump It": ("🟢", ft.Colors.GREEN),
        }
        label, color = icon_map.get(level, ("⚪", ft.Colors.GREY))
        return ft.Text(f"{label} {level}", size=12, color=color)

    def update_counter(self):
        total = len(self.tasks)
        completed = sum(1 for t in self.state.to_do_list if t["completed"])
        self.task_counter.value = f"{total} tasks, {completed} completed"
        self.page.update()

    def refresh_task_list(self):
        self.task_list.controls.clear()
        self.completed_list.controls.clear()

        for i, task in enumerate(self.tasks):
            if task["completed"]:
                self.completed_list.controls.append(self.create_task_item(task, i))
            else:
                self.task_list.controls.append(self.create_task_item(task, i))

        self.page.update()

    def add_task(self, e):
        text = self.task_input.value.strip()
        priority = self.priority_picker.value

        if text:
            if self.selected_date:
                date_obj = datetime.strptime(
                    self.selected_date[:10], "%Y-%m-%d")
                task_date = date_obj.strftime("%d-%m-%Y")
            else:
                task_date = "-"

            task_time = self.selected_time[:5] if self.selected_time else "-"

            task = {
                "text": text,
                "date": task_date,
                "time": task_time,
                "priority": priority or "Medium",
                "completed": False  
            }

            self.tasks.append(task)
            self.state.to_do_list.append(task)

            self.task_input.value = ""
            self.selected_date = None
            self.selected_time = None
            self.priority_picker.value = None

            self.refresh_task_list()
            self.update_counter()

    def clear_completed(self, e):
        self.tasks = [t for t in self.tasks if not t["completed"]]
        self.state.to_do_list = [t for t in self.state.to_do_list if not t["completed"]]
        self.refresh_task_list()
        self.update_counter()

    def create_task_item(self, task_data, index):
        def on_check(e):
            self.tasks[index]["completed"] = e.control.value

            for t in self.state.to_do_list:
                if t["text"] == task_data["text"] and t["date"] == task_data["date"] and t["time"] == task_data["time"]:
                    t["completed"] = e.control.value
                    break

            self.refresh_task_list()
            self.update_counter()

        def on_delete(e):
            self.tasks.pop(index)
            self.refresh_task_list()
            self.update_counter()

        return ft.Container(
            content=ft.Row(
                [
                    ft.Checkbox(value=task_data["completed"], on_change=on_check,
                                fill_color=ft.Colors.PRIMARY if task_data["completed"] else None),
                    ft.Column([
                        ft.Text(task_data["text"], size=16,
                                weight=ft.FontWeight.BOLD,
                             ),
                        ft.Row([
                            ft.Text(f"📅 {task_data['date']}", size=12),
                            ft.Text(f"⏰ {task_data['time']}", size=12),
                            self.get_priority_icon(task_data["priority"]),
                        ], spacing=8)
                    ], expand=True),
                    ft.IconButton(icon=ft.Icons.DELETE_OUTLINE, icon_color=ft.Colors.RED_400,
                                  tooltip="Delete", on_click=on_delete, icon_size=20),
                ],
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=12,
            border_radius=8,
            bgcolor=ft.Colors.GREY_50 if task_data["completed"] else ft.Colors.WHITE,
            border=ft.border.all(1, ft.Colors.GREY_200),
            shadow=ft.BoxShadow(spread_radius=0, blur_radius=2,
                                color=ft.Colors.BLACK12, offset=ft.Offset(0, 1)),
        )

    def build(self):
        content = ft.Container(
            content=ft.Card(
                content=ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Text(
                                            "To-Do List",
                                            size=28,
                                            weight=ft.FontWeight.BOLD,
                                            color=ft.Colors.BLACK,
                                            text_align=ft.TextAlign.CENTER,
                                            font_family="IBM"
                                        ),
                                        ft.Container(
                                            content=self.task_counter,
                                            padding=ft.padding.only(bottom=10)
                                        ),
                                        ft.Container(
                                            content=self.task_input,
                                            padding=ft.padding.only(bottom=10)
                                        ),
                                        ft.Container(
                                            content=ft.Row(
                                                controls=[
                                                    self.priority_picker,
                                                    self.mode_segment
                                                ],
                                                spacing=10
                                            ),
                                            padding=ft.padding.only(bottom=10)
                                        ),
                                        ft.Container(
                                            content=self.add_button,
                                            padding=ft.padding.only(top=15)
                                        ),
                                    ],
                                    spacing=10,
                                    expand=True,
                                ),
                                padding=ft.padding.all(10),
                                expand=True
                            ),

                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Text("Active Tasks 🙌🏽📆", size=18, weight=ft.FontWeight.W_600),
                                        ft.Container(
                                            content=self.task_list,
                                            expand=True,
                                            border_radius=8,
                                            padding=ft.padding.all(10),
                                            alignment=ft.alignment.center,
                                            bgcolor=ft.Colors.GREY_300,
                                        ),
                                        ft.Text("Completed Tasks 👌🏽✅", size=18, weight=ft.FontWeight.W_600),
                                        ft.Container(
                                            content=self.completed_list,
                                            expand=True,
                                            border_radius=8,
                                            padding=ft.padding.all(10),
                                            alignment=ft.alignment.center,
                                            bgcolor=ft.Colors.GREY_300,
                                        ),
                                        self.clear_button
                                    ],
                                    spacing=10,
                                    expand=True
                                ),
                                padding=ft.padding.all(10),
                                expand=True
                            )
                        ],
                        expand=True,
                        spacing=20
                    ),
                    padding=ft.padding.all(25),
                    expand=True
                ),
                elevation=30
            ),
            expand=True
        )

        return ft.View(
            route="/",
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            bgcolor=ft.Colors.GREY_300,
            drawer=self.state.create_drawer(self),
            controls=[
                self.state.create_appbar(self, "OAKKY 365"),
                content
            ]
        )
