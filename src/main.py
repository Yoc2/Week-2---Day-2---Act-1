import flet as ft
from flet import Icons, Colors

def main(page: ft.Page):
    page.title = "Simple Static Flet UI"
    page.window_width = 400
    page.window_height = 800
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Simulated mobile screen layout
    mobile_screen = ft.Container(
        width=300,
        height=600,
        bgcolor=Colors.WHITE,
        border_radius=20,
        padding=20,
        border=ft.border.all(1, Colors.GREY_300),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                # Header with avatar and name
                ft.Row(
                    alignment=ft.MainAxisAlignment.START,
                    spacing=10,
                    controls=[
                        ft.CircleAvatar(
                            radius=20,
                            foreground_image_src="icon.png"  # ✅ correct argument
                        ),
                        ft.Text("James Ellison C. Lopez", size=14, weight="bold")
                    ]
                ),

                # Bottom static navigation
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    controls=[
                        ft.Column(controls=[ft.Icon(Icons.HOME), ft.Text("Home", size=12)]),
                        ft.Column(controls=[ft.Icon(Icons.CHAT), ft.Text("Chat", size=12)]),
                        ft.Column(controls=[ft.Icon(Icons.SETTINGS), ft.Text("Settings", size=12)]),
                    ]
                )
            ]
        )
    )

    page.add(mobile_screen)

ft.app(target=main)
