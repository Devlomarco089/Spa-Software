import flet as ft
import os

# Colores suaves y relajantes
VERDE_SUAVE = "#D0F5E8"
BLANCO = "#FFFFFF"
ROSA_SUAVE = "#FDE4EC"
VERDE_ACENTO = "#A5D6A7"
ROSA_ACENTO = "#F8BBD0"
TEXTO_PRINCIPAL = "#4F4F4F"


def home_view(page: ft.Page):
    page.clean()
    
    # Obtener ruta absoluta de la imagen
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, "..", "assets", "skincare-2357980_640.jpg")
    
    # Verificar si el archivo existe
    if not os.path.exists(image_path):
        print(f"Error: No se encuentra la imagen en: {image_path}")
        return

    page.add(
        ft.Stack(
            [
                ft.Image(
                    src=image_path,
                    fit=ft.ImageFit.COVER,
                    expand=True,
                    width=page.width,
                    height=page.height,
                ),
                ft.Container(
                    expand=True,
                    bgcolor=None,
                    content=ft.Row(
                        [
                            ft.Container(
                                content=ft.Column(
                                    [
                                        ft.Text(
                                            "¡Bienvenido a Spa Sentirse Bien!",
                                            size=24,
                                            weight=ft.FontWeight.BOLD,
                                            color=TEXTO_PRINCIPAL,
                                            text_align=ft.TextAlign.LEFT
                                        ),
                                        ft.Text(
                                            '"Relájate, renueva y sonríe en cada visita"',
                                            size=16,
                                            italic=True,
                                            color=ROSA_ACENTO,
                                            text_align=ft.TextAlign.LEFT
                                        ),
                                        ft.Container(
                                            content=ft.ElevatedButton(
                                                "Iniciar Sesión",
                                                width=150,
                                                bgcolor=VERDE_ACENTO,
                                                color=TEXTO_PRINCIPAL,
                                                on_click=lambda e: page.go("/login"),
                                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20)),
                                            ),
                                            margin=ft.margin.only(top=15)
                                        ),
                                        ft.Container(
                                            content=ft.ElevatedButton(
                                                "Registrarse",
                                                width=150,
                                                bgcolor=ROSA_ACENTO,
                                                color=TEXTO_PRINCIPAL,
                                                on_click=lambda e: page.go("/register"),
                                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20)),
                                            ),
                                            margin=ft.margin.only(top=8)
                                        ),
                                        ft.Container(
                                            content=ft.ElevatedButton(
                                                "Ver Servicios",
                                                width=150,
                                                bgcolor=VERDE_ACENTO,
                                                color=TEXTO_PRINCIPAL,
                                                on_click=lambda e: page.go("/services"),
                                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20)),
                                            ),
                                            margin=ft.margin.only(top=8)
                                        ),
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.START,
                                    spacing=10,
                                    tight=True  # Esto hace que la columna tome el mínimo espacio necesario
                                ),
                                width=300,  # Mantenemos el ancho original
                                height=300,  # Fijamos una altura específica
                                padding=20,
                                bgcolor=f"{BLANCO}ee",
                                border_radius=15,
                                shadow=ft.BoxShadow(blur_radius=15, color=ROSA_SUAVE, spread_radius=1),
                                margin=ft.margin.only(left=40, top=40),  # Agregamos margen superior
                                alignment=ft.alignment.top_center  # Alineamos el contenido arriba
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.START,  # Cambiamos a alineación superior
                        expand=True
                    )
                ),
            ],
            expand=True,
        )
    )
