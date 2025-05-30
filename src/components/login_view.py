import flet as ft

ROSA = "#F8BBD0"
BLANCO = "#FFFFFF"

def login_view(page: ft.Page):
    page.clean()
    email = ft.TextField(label="Correo electrónico", width=300, bgcolor=BLANCO)
    password = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300, bgcolor=BLANCO)
    mensaje = ft.Text()

    def login_usuario(ev):
        if not email.value or not password.value:
            mensaje.value = "Por favor, completa todos los campos."
            mensaje.color = "red"
        else:
            mensaje.value = "¡Inicio de sesión exitoso!"
            mensaje.color = "green"
        page.update()

    page.add(
        ft.Container(
            content=ft.Column([
                ft.Text("Formulario de Inicio de Sesión", size=30, color=ROSA, weight=ft.FontWeight.BOLD),
                email,
                password,
                ft.ElevatedButton("Iniciar Sesión", bgcolor="#AD1457", color=BLANCO, width=300, on_click=login_usuario),
                mensaje,
                ft.TextButton("Volver", on_click=lambda e: page.go("/"))
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20),
            padding=40,
            border_radius=20,
            bgcolor=BLANCO,
            shadow=ft.BoxShadow(blur_radius=20, color=ROSA, spread_radius=2)
        )
    )
