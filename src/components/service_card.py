import flet as ft

def service_card(service: dict):
    return ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    service["nombre"],
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="#4F4F4F"
                ),
                ft.Text(
                    service["descripcion"],
                    size=14,
                    color="#666666",
                    text_align=ft.TextAlign.JUSTIFY
                ),
                ft.Row(
                    [
                        ft.Icon(
                            name=ft.Icons.ACCESS_TIME,
                            color="#A5D6A7",
                            size=20
                        ),
                        ft.Text(
                            f"{service['duracion']} min",
                            color="#666666"
                        )
                    ],
                    spacing=5
                ),
                ft.Text(
                    f"${service['precio']}",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color="#4F4F4F"
                )
            ],
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.START
        ),
        width=300,
        padding=20,
        bgcolor="#FFFFFF",
        border_radius=10,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=10,
            color="#FDE4EC"
        )
    )