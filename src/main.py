import flet as ft
from components.register_view import register_view
from components.login_view import login_view
from app.routes import route_change

# Colores suaves y relajantes
VERDE_SUAVE = "#D0F5E8"
BLANCO = "#FFFFFF"
ROSA_SUAVE = "#FDE4EC"
VERDE_ACENTO = "#A5D6A7"
ROSA_ACENTO = "#F8BBD0"
TEXTO_PRINCIPAL = "#4F4F4F"

def main(page: ft.Page):
    page.title = "Spa Sentirse Bien"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = VERDE_SUAVE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.on_route_change = lambda route: route_change(page, route)
    page.go(page.route)

ft.app(main)