import flet as ft
from flet import *

import components


def main(page: ft.Page):
    page.title = "MEGA MEDS"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 1530
    page.window_height = 800
    page.window_frameless = True

    def open(e):
        _prescription.visible = False
        _prescription.update()

        _token_input.visible = True
        _token_input.update()

        # _btn.visible = False
        # _btn.update()

    def close(e):
        _token_input.visible = False
        _token_input.update()
        _prescription.visible = True
        _prescription.update()

        pass

    def re_usable_static(key, value):
        return Row(controls=[
            Container(
                margin=margin.only(left=30),
                width=150,
                content=Row(controls=[
                    Text(key, color="black", expand=True),
                    Text(" :   ", color="black")
                ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=CrossAxisAlignment.CENTER,
                ),),

            Text(value, color="black", expand=True),],
            alignment=MainAxisAlignment.SPACE_AROUND,
            vertical_alignment=CrossAxisAlignment.CENTER
        )

    def re_usable(number, med, dose, time):
        return Row(controls=[
            Row(controls=[
                Text(number, color="black"),
                Text(med, color="black"),
            ],
                alignment=MainAxisAlignment.CENTER,
                vertical_alignment=CrossAxisAlignment.CENTER),
            Text(f"{dose}", color="black"),
            Text(time, color="black"),],
            alignment=MainAxisAlignment.SPACE_AROUND,
            vertical_alignment=CrossAxisAlignment.CENTER
        )
    _prescription = Column(
        visible=False,
        controls=[
            Text("PRESCRIPTION", size=30, color="black"),
            Container(
                padding=padding.only(top=10),
                width=400,
                height=400,
                bgcolor="0xffD3E8EF",
                alignment=alignment.center,
                content=Column(
                    controls=[

                        Column(
                            expand=True,
                            controls=[

                                re_usable_static(
                                    "DOCTOR", "NDAYISABYE Salim"),
                                re_usable_static(
                                    "INSTITUTION", "GIHUNDWE HOSPITAL"),
                                re_usable_static(
                                    "RECEIVER", "BYIRINGIRO Edson"),
                                re_usable_static(
                                    "OFFERING DATE", " 02 Dec 2022"),
                                re_usable_static(
                                    "PAYMENT", "Paid"),
                                Container(
                                    height=10
                                ),
                                Text(f"MEDS (3)", color="black"),
                                Container(
                                    height=10
                                ),
                                re_usable("1.", "Biprophene", 32, "1 - 2 - 3"),
                                re_usable("1.", "Biprophene", 32, "1 - 2 - 3"),
                                re_usable("1.", "Biprophene", 32, "1 - 2 - 3"),

                            ],
                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment=CrossAxisAlignment.CENTER
                        ),
                        Container(
                            height=40,
                            margin=margin.only(bottom=10, right=20),
                            alignment=alignment.center_right,
                            content=ElevatedButton(

                                "WITHDRAW",
                                bgcolor="0xffD9D9D9",
                                color="black",
                                style=ButtonStyle(
                                    shape=RoundedRectangleBorder(radius=2),
                                ),
                                # on_click=lambda e:print('djdjjddj')
                                on_click=open
                            )
                        ),
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    horizontal_alignment=CrossAxisAlignment.CENTER
                )
            )],
        alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER)

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
                # ElevatedButton(text="Elevated button", on_click=close),
                # _btn,
                _token_input,
                _prescription,

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
