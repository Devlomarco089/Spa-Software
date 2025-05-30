import flet as ft
import httpx

from .service_card import service_card

API_URL = "https://web-production-5825.up.railway.app/api/servicios/"

def services_view(page: ft.Page):
    page.clean()

    titulo = ft.Text(
        "Nuestros Servicios",
        size=32,
        weight=ft.FontWeight.BOLD,
        color="#4F4F4F",
        text_align=ft.TextAlign.CENTER
    )

    subtitulo = ft.Text(
        "Descubre nuestra variedad de tratamientos para tu bienestar",
        size=16,
        color="#666666",
        text_align=ft.TextAlign.CENTER
    )

    servicios_grid = ft.GridView(
        runs_count=3,
        max_extent=350,
        spacing=20,
        run_spacing=20,
        padding=20
    )

    def cargar_servicios():
        try:
            response = httpx.get(API_URL)
            response.raise_for_status()
            servicios = response.json()

            servicios_grid.controls.clear()
            for servicio in servicios:
                servicios_grid.controls.append(service_card(servicio))

            page.update()

        except Exception as e:
            servicios_grid.controls.append(ft.Text(f"Error al cargar servicios: {e}", color="red"))
            page.update()




    cargar_servicios()


    content_scrollable = ft.Column(
        [
            titulo,
            subtitulo,
            servicios_grid
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
        scroll=ft.ScrollMode.AUTO,
        expand=True
    )


    page.add(
        ft.Container(
            content=content_scrollable,
            padding=40,
            bgcolor="#D0F5E8",
            expand=True
        )
    )

    
