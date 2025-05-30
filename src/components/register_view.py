import flet as ft

ROSA = "#F8BBD0"
BLANCO = "#FFFFFF"

def register_view(page: ft.Page):
    page.clean()
    nombre = ft.TextField(label="Nombre", width=300, bgcolor=BLANCO)
    email = ft.TextField(label="Correo electrónico", width=300, bgcolor=BLANCO)
    password = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300, bgcolor=BLANCO)
    mensaje = ft.Text()

    def registrar_usuario(ev):
        if not nombre.value or not email.value or not password.value:
            mensaje.value = "Por favor, completa todos los campos."
            mensaje.color = "red"
        else:
            mensaje.value = "¡Registro exitoso!"
            mensaje.color = "green"
        page.update()

    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Formulario de Registro", size=30, color=ROSA, weight=ft.FontWeight.BOLD),
                    nombre,
                    email,
                    password,
                    ft.ElevatedButton(
                        text="Registrarse",
                        width=300,
                        bgcolor="#A5D6A7",
                        color="#FFFFFF",
                        on_click=registrar_usuario
                    ),
                    ft.TextButton(
                        text="¿Ya tienes cuenta? Inicia sesión",
                        on_click=lambda _: page.go("/login")
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Divider(),
                                ft.Text(
                                    "¿Eres un profesional?",
                                    size=14,
                                    color="#666666",
                                    text_align=ft.TextAlign.CENTER
                                ),
                                ft.ElevatedButton(
                                    text="Registro para Profesionales",
                                    width=300,
                                    bgcolor="#F8BBD0",
                                    color="#4F4F4F",
                                    on_click=lambda _: page.go("/professional-register"),
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=20)
                                    )
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=10
                        )
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            ),
            padding=40,
            bgcolor="#FFFFFF",
            border_radius=10,
            width=400
        )
    )
