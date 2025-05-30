import flet as ft

def user_panel(page: ft.Page):
    # Datos de ejemplo (luego se puede conectar a una base de datos)
    usuario = {
        "nombre": "Juan Pérez",
        "email": "juan@example.com",
        "telefono": "+54 911 1234-5678",
        "turnos_proximos": [
            {"fecha": "2024-05-30", "hora": "14:30", "servicio": "Masaje Relajante", "estado": "Confirmado"},
            {"fecha": "2024-06-15", "hora": "16:00", "servicio": "Facial Rejuvenecedor", "estado": "Pendiente"}
        ],
        "historial_turnos": [
            {"fecha": "2024-04-15", "servicio": "Manicura Spa", "estado": "Completado"},
            {"fecha": "2024-03-20", "servicio": "Masaje Relajante", "estado": "Completado"}
        ]
    }

    def crear_tarjeta_turno(turno, is_historial=False):
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Icon(ft.Icons.EVENT, color="#A5D6A7"),  # Aquí está el cambio: icons -> Icons
                    ft.Text(f"Fecha: {turno['fecha']}", color="#4F4F4F"),
                    ft.Text(f"Hora: {turno.get('hora', '-')}" if not is_historial else ""),
                ], spacing=10),
                ft.Text(f"Servicio: {turno['servicio']}", color="#666666"),
                ft.Container(
                    content=ft.Text(
                        turno['estado'],
                        color="#FFFFFF",
                        size=12,
                    ),
                    bgcolor="#A5D6A7" if turno['estado'] == "Completado" else "#F8BBD0",
                    padding=5,
                    border_radius=15,
                )
            ], spacing=5),
            bgcolor="#FFFFFF",
            padding=15,
            border_radius=10,
            border=ft.border.all(color="#E0E0E0", width=1),
        )

    page.add(
        ft.ListView(
            controls=[
                ft.Container(
                    content=ft.Column([
                        # Información Personal
                        ft.Container(
                            content=ft.Column([
                                ft.Text("Información Personal", size=24, weight=ft.FontWeight.BOLD, color="#4F4F4F"),
                                ft.Divider(),
                                ft.Row([
                                    ft.Icon(ft.Icons.PERSON, color="#A5D6A7"),
                                    ft.Text(f"Nombre: {usuario['nombre']}", color="#4F4F4F"),
                                ]),
                                ft.Row([
                                    ft.Icon(ft.Icons.EMAIL, color="#A5D6A7"),
                                    ft.Text(f"Email: {usuario['email']}", color="#4F4F4F"),
                                ]),
                                ft.Row([
                                    ft.Icon(ft.Icons.PHONE, color="#A5D6A7"),
                                    ft.Text(f"Teléfono: {usuario['telefono']}", color="#4F4F4F"),
                                ]),
                            ], spacing=15),
                            bgcolor="#FFFFFF",
                            padding=20,
                            border_radius=10,
                            shadow=ft.BoxShadow(blur_radius=5, color="#FDE4EC"),
                        ),

                        # Próximos Turnos
                        ft.Container(
                            content=ft.Column([
                                ft.Text("Próximos Turnos", size=24, weight=ft.FontWeight.BOLD, color="#4F4F4F"),
                                ft.Divider(),
                                ft.Column([
                                    crear_tarjeta_turno(turno) for turno in usuario['turnos_proximos']
                                ], spacing=10),
                            ]),
                            bgcolor="#FFFFFF",
                            padding=20,
                            border_radius=10,
                            shadow=ft.BoxShadow(blur_radius=5, color="#FDE4EC"),
                        ),

                        # Historial de Turnos
                        ft.Container(
                            content=ft.Column([
                                ft.Text("Historial de Turnos", size=24, weight=ft.FontWeight.BOLD, color="#4F4F4F"),
                                ft.Divider(),
                                ft.Column([
                                    crear_tarjeta_turno(turno, True) for turno in usuario['historial_turnos']
                                ], spacing=10),
                            ]),
                            bgcolor="#FFFFFF",
                            padding=20,
                            border_radius=10,
                            shadow=ft.BoxShadow(blur_radius=5, color="#FDE4EC"),
                        ),
                    ], spacing=20),
                    padding=40,
                    bgcolor="#D0F5E8",
                )
            ],
            expand=True,
            auto_scroll=True
        )
    )