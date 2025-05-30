import flet as ft
from datetime import datetime

def professional_panel(page: ft.Page):
    # Datos de ejemplo del profesional
    profesional = {
        "nombre": "María González",
        "especialidad": "Masajista Profesional",
        "email": "maria@spasentirse.com",
        "telefono": "+54 911 5678-1234",
        "turnos_del_dia": [
            {
                "hora": "09:00",
                "cliente": "Ana López",
                "servicio": "Masaje Relajante",
                "duracion": "60 min",
                "estado": "Pendiente"
            },
            {
                "hora": "10:30",
                "cliente": "Carlos Ruiz",
                "servicio": "Masaje Descontracturante",
                "duracion": "45 min",
                "estado": "Confirmado"
            }
        ]
    }

    def crear_tarjeta_turno(turno):
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Icon(ft.Icons.ACCESS_TIME, color="#A5D6A7"),
                    ft.Text(
                        f"{turno['hora']} - {turno['cliente']}", 
                        size=16, 
                        weight=ft.FontWeight.BOLD,
                        color="#4F4F4F"
                    ),
                ], spacing=10),
                ft.Row([
                    ft.Text(turno['servicio'], color="#666666"),
                    ft.Text(f"Duración: {turno['duracion']}", color="#666666"),
                ], spacing=10),
                ft.Container(
                    content=ft.Text(
                        turno['estado'],
                        color="#FFFFFF",
                        size=12,
                    ),
                    bgcolor="#A5D6A7" if turno['estado'] == "Confirmado" else "#F8BBD0",
                    padding=5,
                    border_radius=15,
                )
            ], spacing=10),
            bgcolor="#FFFFFF",
            padding=20,
            border_radius=10,
            border=ft.border.all(color="#E0E0E0", width=1),
        )

    def imprimir_turnos(e):
        
        fecha_actual = datetime.now().strftime("%d/%m/%Y")
        contenido = f"""
AGENDA DE TURNOS - {profesional['nombre']}
Fecha: {fecha_actual}
=====================================

"""
        for turno in profesional['turnos_del_dia']:
            contenido += f"""
Hora: {turno['hora']}
Cliente: {turno['cliente']}
Servicio: {turno['servicio']}
Duración: {turno['duracion']}
Estado: {turno['estado']}
-------------------------------------
"""
        
        dlg = ft.AlertDialog(
            title=ft.Text("Imprimir Turnos"),
            content=ft.Column([
                ft.TextField(
                    value=contenido,
                    multiline=True,
                    read_only=True,
                    min_lines=10,
                    max_lines=15,
                    width=400
                ),
                ft.Row([
                    ft.TextButton(
                        "Copiar al Portapapeles",
                        on_click=lambda _: page.set_clipboard(contenido)
                    ),
                    ft.TextButton("Cerrar", on_click=lambda _: setattr(dlg, "open", False)),
                ], alignment=ft.MainAxisAlignment.END)
            ])
        )
        page.dialog = dlg
        dlg.open = True
        page.update()

    page.add(
        ft.ListView(
            controls=[
                ft.Container(
                    content=ft.Column([
                        # Panel Superior - Información Personal
                        ft.Container(
                            content=ft.Column([
                                ft.Row([
                                    ft.CircleAvatar(
                                        content=ft.Text(
                                            profesional["nombre"][0],
                                            size=30,
                                            weight=ft.FontWeight.BOLD
                                        ),
                                        bgcolor="#A5D6A7",
                                        color="#FFFFFF",
                                    ),
                                    ft.Column([
                                        ft.Text(
                                            profesional["nombre"],
                                            size=24,
                                            weight=ft.FontWeight.BOLD,
                                            color="#4F4F4F"
                                        ),
                                        ft.Text(
                                            profesional["especialidad"],
                                            size=16,
                                            color="#666666"
                                        ),
                                    ]),
                                ], alignment=ft.MainAxisAlignment.START),
                                ft.Divider(),
                                ft.Row([
                                    ft.Icon(ft.Icons.EMAIL, color="#A5D6A7"),
                                    ft.Text(profesional["email"], color="#4F4F4F"),
                                ]),
                                ft.Row([
                                    ft.Icon(ft.Icons.PHONE, color="#A5D6A7"),
                                    ft.Text(profesional["telefono"], color="#4F4F4F"),
                                ]),
                            ], spacing=15),
                            bgcolor="#FFFFFF",
                            padding=20,
                            border_radius=10,
                            shadow=ft.BoxShadow(blur_radius=5, color="#FDE4EC"),
                        ),

                        # Panel de Turnos del Día
                        ft.Container(
                            content=ft.Column([
                                ft.Row([
                                    ft.Text(
                                        "Turnos del Día",
                                        size=24,
                                        weight=ft.FontWeight.BOLD,
                                        color="#4F4F4F"
                                    ),
                                    ft.IconButton(
                                        icon=ft.Icons.PRINT,
                                        icon_color="#A5D6A7",
                                        tooltip="Imprimir Turnos",
                                        on_click=imprimir_turnos
                                    ),
                                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                                ft.Divider(),
                                ft.Column([
                                    crear_tarjeta_turno(turno) 
                                    for turno in profesional['turnos_del_dia']
                                ], spacing=10),
                            ], spacing=20),
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