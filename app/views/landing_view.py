import flet as ft
from fletx import Xview
import flet as ft


class LandingView(Xview):
    def build(self):
        # ข้อมูลจำลอง
        active_tasks = 3
        completed_tasks = 5
        today_expense = 280  # บาท
        completed_exercise = 1
        meals = ["กระเพราไก่ ไข่ดาว", "ไก่กระเทียม", "ขนมปังแฮมชีส"]

        content = ft.Container(
    expand=True,
    padding=20,
    content=ft.Column(
        scroll=ft.ScrollMode.AUTO,
        spacing=20,
        controls=[
            ft.Text("ภาพรวมประจำวัน", size=24, weight=ft.FontWeight.BOLD),

            # Section 1: สถานะ Tasks
            ft.Card(
                content=ft.Container(
                    padding=16,
                    content=ft.Column([
                        ft.Text("สถานะงาน", size=18, weight=ft.FontWeight.BOLD),
                        ft.Row([
                            self._summary_card("📝 กำลังดำเนินการ", f"{active_tasks} งาน"),
                            self._summary_card("✅ สำเร็จแล้ว", f"{completed_tasks} งาน"),
                        ], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                    ])
                )
            ),

            # Section 2: รายจ่าย
            ft.Card(
                content=ft.Container(
                    padding=16,
                    content=ft.Column([
                        ft.Text("สุขภาพและการเงิน", size=18, weight=ft.FontWeight.BOLD),
                        ft.Row([
                            self._summary_card("💰 รายจ่ายวันนี้", f"{today_expense} บาท"),
                            self._summary_card("🏋️‍♀️ ออกกำลังกาย", f"{completed_exercise} รายการ"),
                        ], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                    ])
                )
            ),

            # Section 3: มื้ออาหาร
            ft.Card(
                content=ft.Container(
                    padding=16,
                    bgcolor=ft.Colors.AMBER_100,
                    border_radius=10,
                    content=ft.Column([
                        ft.Text("🍱 มื้ออาหารที่กิน", size=18, weight=ft.FontWeight.BOLD),
                        *[ft.Text(f"- {meal}", size=16) for meal in meals]
                    ])
                )
            ),
        ]
    )
)


        return ft.View(
            route='/',
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.START,
            drawer=self.state.create_drawer(self),
            bgcolor=ft.Colors.BLUE_GREY_50,
            controls=[
                self.state.create_appbar(self, 'OAKKY 365'),
                content
            ]
        )

    def _summary_card(self, title: str, subtitle: str):
        return ft.Container(
            width=160,
            padding=10,
            border_radius=12,
            content=ft.Column([
                ft.Text(title, size=16, weight=ft.FontWeight.BOLD),
                ft.Text(subtitle, size=20, weight=ft.FontWeight.BOLD),
            ])
        )
