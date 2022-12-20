import flet as ft
from flet import *

import components
import routes


def main(page: ft.Page):
    page.title = "MEGA MEDS"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 1530
    page.window_height = 800
    page.window_frameless = True

    def open(e):
        _token_input.visible = True
        _token_input.update()

        _btn.visible = False
        _btn.update()

    def close(e):
        _token_input.visible = False
        _token_input.update()

        _btn.visible = True
        _btn.update()

        pass
    _btn = ElevatedButton(text="Elevated button", visible=False, on_click=open)

    _token_input = Container(

        alignment=alignment.center,
        content=Column(
            [
                Text("TOKEN_INPUT", size=30,),

                TextField(
                    text_align=TextAlign.CENTER,
                    text_size=20,
                    filled=True,
                    width=300,
                    height=70,
                    autofocus=True,
                    focused_bgcolor=colors.WHITE,
                    color=colors.BLACK,
                    border_color=colors.TRANSPARENT,
                    cursor_color=colors.BLACK,
                    keyboard_type=KeyboardType.NUMBER,
                    # on_submit=lambda e: print(e.control.value)
                    on_submit=close
                ),
            ],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
    )

    _landing_page = Container(
        alignment=alignment.center,
        border_radius=10,
        content=Column(
            [
                components.header(),
                # routes.display(routes.current_step),
                ElevatedButton(text="Elevated button", on_click=close),
                _btn,
                _token_input,
                components.footer(),
            ],
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=CrossAxisAlignment.CENTER),
        gradient=LinearGradient(
            begin=alignment.top_left,
            end=Alignment(0.8, 1),
            colors=[
                # D3E8EF
                "0xff7A9FA7",
                "0xffBDF3FF",
            ],
            rotation=math.pi / 3,
        ),
        expand=True
    )

    page.update()

    page.add(
        _landing_page
    )
    page.update()


ft.app(target=main, assets_dir="assets")
