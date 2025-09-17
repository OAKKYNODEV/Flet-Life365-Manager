import flet as ft
from datetime import datetime


class ExpenseIncomeView:
    def __init__(self, page: ft.Page, state=None, params=None):
        self.page = page
        self.state = state
        self.params = params

        self.income_list = []  # เก็บข้อมูลรายรับ-รายจ่ายเป็น dict

        # Controls
        self.amount_field = ft.TextField(
            label="จำนวนเงิน",
            prefix_text="฿",
            keyboard_type=ft.KeyboardType.NUMBER,
            width=200,
        )
        self.category_dropdown = ft.Dropdown(
            label="หมวดหมู่",
            width=200,
            options=[
                ft.dropdown.Option("อาหาร"),
                ft.dropdown.Option("เดินทาง"),
                ft.dropdown.Option("ช้อปปิ้ง"),
                ft.dropdown.Option("รายรับอื่น ๆ"),
                ft.dropdown.Option("เงินเดือน"),
            ],
        )
        self.type_dropdown = ft.Dropdown(
            label="ประเภท",
            width=200,
            options=[
                ft.dropdown.Option("รายรับ"),
                ft.dropdown.Option("รายจ่าย"),
            ],
            
        )
        self.note_field = ft.TextField(
            label="หมายเหตุ",
            multiline=True,
            max_lines=2,
            width=400,
        )

        self.date_button = ft.ElevatedButton(
            text="เลือกวันที่",
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=self.open_date_picker,
        )
        self.selected_date_text = ft.Text(
            "ยังไม่เลือกวันที่", italic=True, color=ft.Colors.GREY
        )

        self.save_button = ft.ElevatedButton(
            text="💾 บันทึก",
            icon=ft.Icons.SAVE,
            on_click=self._on_save,
            bgcolor=ft.Colors.BLUE,
            color=ft.Colors.WHITE,
            width=120,
        )

        self.list_view = ft.ListView(
            expand=True,
            spacing=5,
            padding=10,
            auto_scroll=True,
        )

        # container แสดงจำนวนรายการทั้งหมด
        self.summary_text = ft.Text("0 รายการ", size=14, italic=True)

    def open_date_picker(self, e=None):
        self.date_picker = ft.DatePicker(
            first_date=datetime(year=2000, month=1, day=1),
            last_date=datetime(year=2030, month=12, day=31),
            on_change=self._on_date_selected
        )
        self.page.overlay.append(self.date_picker)
        self.date_picker.open = True
        self.page.update()

    def _on_date_selected(self, e):
        self.selected_date_text.value = self.date_picker.value.strftime("%d/%m/%Y")
        self.page.update()

    def alert_date(self):
        if self.date_picker.value is None:
            dlg = ft.AlertDialog(
                title=ft.Text("กรุณาเลือกวันที่ก่อนบันทึก!"),
            )
            self.page.dialog = dlg
            dlg.open = True
            self.page.update()
            return False  # วันที่ยังไม่ถูกเลือก
        return True  # วันที่ถูกเลือกแล้ว


    def _on_save(self, e):
        # Validate amount input
        if not self.amount_field.value or self.amount_field.value.strip() == "":
            print("Amount field is empty. Please enter a valid amount.")
            return

        try:
            amount = float(self.amount_field.value)
        except ValueError:
            print("Invalid number entered in the amount field.")
            return

        # Validate date input
        if not self.alert_date():
            return  # หยุดการทำงานหากยังไม่เลือกวันที่

        record = {
            "amount": amount,
            "category": self.category_dropdown.value,
            "type": self.type_dropdown.value,
            "note": self.note_field.value or "-",
            "date": self.date_picker.value.strftime("%d/%m/%Y"),
        }
        self.income_list.append(record)

        self._refresh_list()

        # Clear form
        self.amount_field.value = ""
        self.category_dropdown.value = None
        self.type_dropdown.value = "รายจ่าย"
        self.note_field.value = ""
        self.date_picker.value = None
        self.selected_date_text.value = "ยังไม่เลือกวันที่"

        self.page.update()



    def _refresh_list(self):
        self.list_view.controls.clear()

        for i, rec in enumerate(self.income_list):
            # ฟังก์ชันลบรายการ
            def on_delete(e, index=i):
                self.income_list.pop(index)
                self._refresh_list()
                self.page.update()

            item = ft.ListTile(
                leading=ft.Icon(
                    ft.Icons.MONEY_OFF if rec["type"] == "รายจ่าย" else ft.Icons.MONEY
                ),
                title=ft.Text(f'{rec["category"]} - {rec["amount"]:.2f} บาท'),
                subtitle=ft.Text(f'{rec["type"]} | วันที่ {rec["date"]}'),
                trailing=ft.Row(
                    controls=[
                        ft.Text(rec["note"], italic=True, size=12, color=ft.Colors.GREY_600),
                        ft.IconButton(
                            icon=ft.Icons.DELETE,
                            icon_color=ft.Colors.RED,
                            tooltip="ลบรายการ",
                            on_click=on_delete,
                        ),
                    ],
                    spacing=10,
                ),
            )
            self.list_view.controls.append(item)

        self.summary_text.value = f"{len(self.income_list)} รายการ"
        self.page.update()

    def build(self):
        left_panel = ft.Column(
            [
                ft.Text("💼 บันทึกรายรับรายจ่าย", size=26, weight=ft.FontWeight.BOLD),
                ft.Card(
                    content=ft.Container(
                        padding=20,
                        content=ft.Column(
                            [
                                self.amount_field,
                                self.category_dropdown,
                                self.type_dropdown,
                                self.note_field,
                                ft.Row(
                                    [self.date_button, self.selected_date_text],
                                    alignment=ft.MainAxisAlignment.START,
                                ),
                                self.save_button,
                            ],
                            spacing=15,
                        ),
                    ),
                    elevation=3,
                ),
            ],
            spacing=20,
            expand=1,
        )
        right_panel = ft.Column(
            [
                ft.Text("📄 รายการที่บันทึกไว้", size=20, weight=ft.FontWeight.BOLD),
                self.summary_text,
                ft.Divider(),
                ft.Container(
                    expand=True,
                    content=ft.Card(
                        expand=True,
                        content=ft.Container(
                            content =
                            ft.Row(controls=[
                                             ft.Container(
                                    content=
                                     self.list_view,     
                                )
                            ]
                   
                                
                            )
                        ),
                    ),
                ),
            ],
            spacing=10,
            expand=1,
        )



        layout = ft.Row(
            [left_panel, right_panel], expand=True, spacing=30
        )

        return ft.View(
            route="/finance",
            controls=[
                self.state.create_appbar(self, "OAKKY 365"),
                ft.Container(padding=20, content=layout, expand=True),
            ],
            bgcolor=ft.Colors.BLUE_GREY_50,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.START,
        )
    
    def onBuildComplete(self):
        print("✅ ExpenseIncomeView: Build Completed")
