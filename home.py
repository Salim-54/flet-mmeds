import flet as ft
from flet import *
import time

import components


def main(page: ft.Page):
    page.title = "MEGA MEDS"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 1530
    page.window_height = 800
    page.window_frameless = True

    def token_typing(e):
        _token_input.content.controls[0].color = "white"
        _token_input.content.controls[0].value = "TOKEN_INPUT"
        _token_input.update()

    def progress_bar(w):
        return ProgressBar(bgcolor="0xffBDF3FF", color="white", width=w, bar_height=2)

    def to_prescription(s):
        _token_input.content.controls.insert(1, progress_bar(300))
        _token_input.update()
        time.sleep(2)
        _token_input.content.controls.pop(1)
        _token_input.update()
        print(s.control.value)
        if (s.control.value == "7254"):
            time.sleep(1)
            _actual_content.content = _prescription
            _actual_content.update()
        else:
            _token_input.content.controls[0].value = "INVALID_TOKEN"
            _token_input.content.controls[0].color = "red"
            _token_input.update()
            print("Waapi bro")

    def to_waiting(s):
        pass

    def to_delivering(s):
        print('assasa')
        _prescription.controls.insert(1, progress_bar(400))
        _prescription.update()
        time.sleep(1.7)
        _prescription.controls.pop(1)
        _prescription.update()
        time.sleep(0.5)
        _actual_content.content = _delivering
        _actual_content.update()

    def to_thank_you(s):
        _actual_content.content = _finish
        _actual_content.update()

    def open(e):
        # _prescription.visible = False
        # _prescription.update()

        # _token_input.visible = True
        # _token_input.update()

        # _btn.visible = False
        # _btn.update()
        pass

    def close(e):
        # _token_input.visible = False
        # _token_input.update()
        # _prescription.visible = True
        # _prescription.update()
        # _actual_content.content = _prescription
        # _actual_content.update()
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

    _delivering = Column(
        # visible=True if screen == 2 else False,
        controls=[
            Text("DELIVERING", size=30, color="black"),
            Container(
                padding=padding.only(top=10),
                border_radius=10,
                width=400,
                height=200,
                bgcolor="0xffD3E8EF",
                alignment=alignment.center,
                content=Column(
                    controls=[

                        Column(
                            expand=True,
                            controls=[
                                Text("DRUG 2 Biprophene",
                                     size=30, color="black"),

                                Text("Coming ...", color="black")
                            ],
                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment=CrossAxisAlignment.CENTER
                        ),

                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    horizontal_alignment=CrossAxisAlignment.CENTER
                )
            )],
        alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER)

    _prescription = Column(
        # visible=True if screen == 1 else False,
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
                                on_click=to_delivering
                            )
                        ),
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    horizontal_alignment=CrossAxisAlignment.CENTER
                )
            )],
        alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER)

    # _btn = ElevatedButton(text="Elevated button", visible=False, on_click=open)

    _token_input = Container(
        # visible=True if screen != 1 & screen != 2 & screen != 3 & screen != 4 else False,
        alignment=alignment.center,
        content=Column(
            [
                # progress_bar(),
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
                    on_submit=to_prescription,
                    on_change=token_typing
                ),
            ],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
    )

    _finish = Container(
        border_radius=10,
        bgcolor="0xffD3E8EF",
        width=400,
        height=200,
        alignment=alignment.center,
        content=Text("THANK YOU!!!", size=40, color="black")
    )

    _actual_content = AnimatedSwitcher(
        _token_input,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
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
                # _token_input,
                # _prescription,
                # _delivering,
                _actual_content,


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
