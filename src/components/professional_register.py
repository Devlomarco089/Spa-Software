import flet as ft

def professional_register_view(page: ft.Page):
    # Campos del formulario
    nombre = ft.TextField(
        label="Nombre Completo",
        border_color="#A5D6A7",
        text_size=14,
        width=300
    )
    
    email = ft.TextField(
        label="Correo Electrónico",
        border_color="#A5D6A7",
        text_size=14,
        width=300
    )
    
    telefono = ft.TextField(
        label="Teléfono",
        border_color="#A5D6A7",
        text_size=14,
        width=300
    )
    
    especialidad = ft.Dropdown(
        label="Especialidad",
        width=300,
        border_color="#A5D6A7",
        options=[
            ft.dropdown.Option("Masajista"),
            ft.dropdown.Option("Cosmetóloga"),
            ft.dropdown.Option("Manicurista"),
            ft.dropdown.Option("Podóloga")
        ]
    )
    
    experiencia = ft.TextField(
        label="Años de Experiencia",
        border_color="#A5D6A7",
        text_size=14,
        width=300,
        input_filter=ft.NumbersOnlyInputFilter()
    )
    
    password = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        border_color="#A5D6A7",
        width=300
    )
    
    confirm_password = ft.TextField(
        label="Confirmar Contraseña",
        password=True,
        can_reveal_password=True,
        border_color="#A5D6A7",
        width=300
    )

    # Mensaje de error/éxito
    mensaje = ft.Text(
        color="#FF0000",
        size=12
    )

    def validar_formulario(e):
        if not all([
            nombre.value, 
            email.value, 
            telefono.value, 
            especialidad.value,
            experiencia.value,
            password.value, 
            confirm_password.value
        ]):
            mensaje.value = "Por favor complete todos los campos"
            mensaje.color = "#FF0000"
            page.update()
            return

        if password.value != confirm_password.value:
            mensaje.value = "Las contraseñas no coinciden"
            mensaje.color = "#FF0000"
            page.update()
            return

        # Aquí iría la lógica para guardar el profesional en la base de datos
        mensaje.value = "Registro exitoso!"
        mensaje.color = "#4CAF50"
        page.update()

    page.add(
        ft.Container(
            content=ft.Column([
                ft.Text(
                    "Registro de Profesional",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color="#4F4F4F"
                ),
                ft.Text(
                    "Complete el formulario para registrarse como profesional",
                    size=16,
                    color="#666666"
                ),
                nombre,
                email,
                telefono,
                especialidad,
                experiencia,
                password,
                confirm_password,
                mensaje,
                ft.ElevatedButton(
                    text="Registrarse",
                    width=300,
                    bgcolor="#A5D6A7",
                    color="#FFFFFF",
                    on_click=validar_formulario
                ),
                ft.TextButton(
                    text="¿Ya tienes cuenta? Inicia sesión",
                    on_click=lambda _: page.go("/login")
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20),
            padding=40,
            bgcolor="#FFFFFF",
            border_radius=10,
            width=400
        )
    )