import flet as ft

from app.utils.custom_text_style import CustomTextStyle
from app.utils.helpers import argb_to_hex, lighten_color


VERSION_SOFTWARE = "v1.2.3"

FONT_SIZE_ALERT_DIALOG=24

REQ_TIMEOUT_API=120
CONNECTION_TIMEOUT=10
SEARCH_TIMEOUT=60

BUTTON_TEXTFIELD_RADIUS = 30

BUTTON_TEXTFIELD_HEIGHT = 50

THEME_COLOR = "#000000"

TEXTFIELD = CustomTextStyle.text_field(color=ft.Colors.BLACK)

BUTTON_STYLE = ft.ButtonStyle(bgcolor=THEME_COLOR, color=ft.Colors.WHITE, text_style = CustomTextStyle.button(),shape= ft.RoundedRectangleBorder(radius=BUTTON_TEXTFIELD_RADIUS))

DISABLEDBUTTON_COLOR = '#6A6A6A'

DISABLED_THEME_COLOR = lighten_color(THEME_COLOR, 0.6)
DISABLED_SUBMIT_BUTTON_COLOR = lighten_color(argb_to_hex(255, 76, 176, 80), 0.6)
DISABLED_WARNING_BUTTON_COLOR = lighten_color(argb_to_hex(255, 255,152,0), 0.6)

ALMOST_BLACK_COLOR = '#2E2E2E'
 
