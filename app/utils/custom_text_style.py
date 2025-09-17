import flet as ft


class CustomTextStyle:
    ''' 
        Class Method for Text Style
        Use this class for every text styles in the program
    '''
    FONT_FAMILY = "IBM"

    NORMAL_FONT_SIZE = 22
    SMALL_FONT_SIZE = 17
    VERY_SMALL_FONT_SIZE = 12
    LARGE_FONT_SIZE = 30
    APPBAR_FONT_SIZE = 26

    DRAWER_FONT_SIZE = 18

    BUTTON_FONT_SIZE = 20
    TEXTFIELD_FONT_SIZE = 18

    TEXT_INFO_COLOR = ft.Colors.BLACK
    APPBAR_TEXT_COLOR = ft.Colors.WHITE
    DRAWER_TEXT_COLOR = ft.Colors.BLACK
    TEXT_BUTTON_COLOR = ft.Colors.WHITE
    TEXTFIELD_LABEL_COLOR = ft.Colors.GREY

    @classmethod
    def normal(
        cls,
        color: str = None,
        is_bold: bool = True,
        font_size_delta: int = 0,
        letter_spacing: float = 0.0
    ) -> ft.TextStyle:
        ''' Text style for normal size '''
        return ft.TextStyle(
            size=cls.NORMAL_FONT_SIZE + font_size_delta,
            font_family=cls.FONT_FAMILY,
            color=color or cls.TEXT_INFO_COLOR,
            weight=ft.FontWeight.BOLD if is_bold else ft.FontWeight.NORMAL,
            letter_spacing=letter_spacing,
        )

    @classmethod
    def small(cls, font_size_delta: int = 0, is_bold: bool = True, color: str = None, letter_spacing: float = 0.0) -> ft.TextStyle:
        ''' Text style for small size '''
        return ft.TextStyle(
            size=cls.SMALL_FONT_SIZE + font_size_delta,
            font_family=cls.FONT_FAMILY,
            color=color or cls.TEXT_INFO_COLOR,
            weight=ft.FontWeight.BOLD if is_bold else ft.FontWeight.NORMAL,
            letter_spacing=letter_spacing,
        )

    @classmethod
    def very_small(cls, font_size_delta: int = 0, is_bold: bool = True, color: str = None, letter_spacing: float = 0.0) -> ft.TextStyle:
        ''' Text style for small size '''
        return ft.TextStyle(
            size=cls.VERY_SMALL_FONT_SIZE + font_size_delta,
            font_family=cls.FONT_FAMILY,
            color=color or cls.TEXT_INFO_COLOR,
            weight=ft.FontWeight.BOLD if is_bold else ft.FontWeight.NORMAL,
            letter_spacing=letter_spacing,
        )

    @classmethod
    def large(
        cls,
        color: str = None,
        is_bold: bool = True,
        font_size_delta: int = 0,
        letter_spacing: float = 0.0
    ) -> ft.TextStyle:
        ''' Text style for normal size '''
        return ft.TextStyle(
            size=cls.LARGE_FONT_SIZE + font_size_delta,
            font_family=cls.FONT_FAMILY,
            color=color or cls.TEXT_INFO_COLOR,
            weight=ft.FontWeight.BOLD if is_bold else ft.FontWeight.NORMAL,
            letter_spacing=letter_spacing,
        )

    @classmethod
    def drawer(cls, is_bold: bool = True, letter_spacing: float = 0) -> ft.TextStyle:
        ''' Text style for Drawer '''
        return ft.TextStyle(
            size=cls.DRAWER_FONT_SIZE,
            font_family=cls.FONT_FAMILY,
            weight=ft.FontWeight.BOLD if is_bold else ft.FontWeight.W_600,
            # color=color or cls.DRAWER_TEXT_COLOR,
            letter_spacing=letter_spacing,
        )

    @classmethod
    def app_bar(cls, font_size_delta: int = 0, color: str = None, is_bold: bool = True, letter_spacing: float = 0) -> ft.TextStyle:
        ''' Text style for App bar (No size)'''
        return ft.TextStyle(
            size=cls.APPBAR_FONT_SIZE + font_size_delta,
            font_family=cls.FONT_FAMILY,
            color=color or cls.APPBAR_TEXT_COLOR,
            weight=ft.FontWeight.BOLD if is_bold else ft.FontWeight.NORMAL,
            letter_spacing=letter_spacing,
        )

    @classmethod
    def button(cls, font_size_delta: int = 0, is_bold: bool = True, color: str = None, letter_spacing: float = 0.0) -> ft.TextStyle:
        ''' Text style for Button's text '''
        return ft.TextStyle(
            size=cls.BUTTON_FONT_SIZE + font_size_delta,
            font_family=cls.FONT_FAMILY,
            color=color if color else cls.TEXT_BUTTON_COLOR,
            weight=ft.FontWeight.BOLD if is_bold else ft.FontWeight.NORMAL,
            letter_spacing=letter_spacing,
        )

    @classmethod
    def text_field(cls, font_size_delta: int = 0, is_bold: bool = True, color: str = None, letter_spacing: float = 0.0) -> ft.TextStyle:
        ''' Text style for Text field '''
        return ft.TextStyle(
            size=cls.TEXTFIELD_FONT_SIZE + font_size_delta,
            font_family=cls.FONT_FAMILY,
            color=color or cls.TEXTFIELD_LABEL_COLOR,
            weight=ft.FontWeight.BOLD if is_bold else ft.FontWeight.NORMAL,
            letter_spacing=letter_spacing,
        )

    @classmethod
    def custom(cls, font_size: int, font_weight: ft.FontWeight = ft.FontWeight.NORMAL, color: str = ft.Colors.BLACK, letter_spacing: float = 0.0) -> ft.TextStyle:
        ''' Custom text style '''
        return ft.TextStyle(
            size=font_size,
            font_family=cls.FONT_FAMILY,
            color=color,
            weight=font_weight,
            letter_spacing=letter_spacing,
        )
