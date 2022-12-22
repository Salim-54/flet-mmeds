import flet as ft
from flet import *
import requests
import time

import components

url = "http://localhost:3000/api/v1/prescriptions"
pay_load = {"token": 7067506, }

data = {}


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

    def check_token(pay_load, s):
        try:
            _token_input.content.controls.insert(1, progress_bar(300))
            _token_input.update()
            print(pay_load)
            response = requests.get(url, json={"token": pay_load})
            if response.status_code == 200:
                _token_input.content.controls.pop(1)
                _token_input.update()
                global data
                data = response.json()["data"]
                print(data)
                time.sleep(2)
                s.control.value = ""
                _actual_content.content = prescription(data)
                _actual_content.update()
                return response

            else:
                time.sleep(2)
                _token_input.content.controls.pop(1)
                _token_input.update()
                _token_input.content.controls[0].value = "INVALID_TOKEN"
                _token_input.content.controls[0].color = "red"
                _token_input.update()
                print("Waapi bro")

        except requests.exceptions.RequestException as e:
            print(e)
            return None

    def to_prescription(s):

        pay_load = int(s.control.value)
        print(pay_load)
        check_token(pay_load, s)

    def to_delivering(s):

        _actual_content.content.controls.insert(1, progress_bar(400))
        _actual_content.update()
        time.sleep(1.7)
        _actual_content.content.controls.pop(1)
        _actual_content.update()
        for i, med in enumerate(data["medicines"], start=1):
            time.sleep(2)
            _actual_content.content = delivering(i, med)
            _actual_content.update()

        time.sleep(3)
        _actual_content.content = _finish
        _actual_content.update()

        time.sleep(5)
        to_thank_you()

    def to_thank_you():
        _actual_content.content = _finish
        _actual_content.update()
        time.sleep(0.5)
        _actual_content.content = _token_input
        _actual_content.update()

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

            Container(
                width=150,
                alignment=alignment.center_left,
                content=Row(controls=[
                    Text(number, color="black", expand=True),
                    Text(med, color="black"),
                ],
                    alignment=MainAxisAlignment.CENTER,
                    vertical_alignment=CrossAxisAlignment.CENTER),
            ),
            Container(
                width=120,
                alignment=alignment.center_left,
                content=Row(controls=[
                    Text(f"{dose}", color="black"),
                    Text(time, color="black"),
                ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=CrossAxisAlignment.CENTER),
            ),
        ],
            alignment=MainAxisAlignment.SPACE_AROUND,
            vertical_alignment=CrossAxisAlignment.CENTER
        )

    def delivering(i, med):
        _delivering = Column(
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
                                    Text("DRUG {} {}".format(i, med["medName"]),
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
        return _delivering

    #####################################################################

    def prescription(values):

        # send page to a page
        lv = ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

        for i, med in enumerate(values['medicines'], start=1):
            lv.controls.append(re_usable("{}.".format(str(i)), "{}".format(med["medName"]),
                                         med["medNumber"], "{}".format(med["pattern"])),)

        _statics = Column(
            expand=True,
            controls=[

                re_usable_static(
                    "DOCTOR", values["doctor"]),
                re_usable_static(
                    "INSTITUTION", values["institution"]),
                re_usable_static(
                    "RECEIVER", values["patient"]),
                re_usable_static(
                    "OFFERING DATE", " 02 Dec 2022"),
                re_usable_static(
                    "PAYMENT", values["payment"]),
                Container(
                    height=10
                ),
                Text("MEDS ({})".format(
                    len(values['medicines'])), color="black"),
                Container(
                    height=10
                ),
                lv,
                # word("dmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")


                # list(values['medicines']),



                # re_usable("1.", "Biprophene",
                #           32, "1 - 2 - 3"),
                # re_usable("1.", "Biprophene",
                #           32, "1 - 2 - 3"),


            ],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )

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
                            _statics,

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

        def list(list):
            for i in range(len(list)):
                _prescription.controls[1].content.controls[0].append(re_usable("{}.".format(
                    i+1), "Biprophene",                                                                        32, "1 - 2 - 3"),)
            page.update()
        return _prescription

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
                _actual_content,


                components.footer(),
            ],
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=CrossAxisAlignment.CENTER),
        gradient=LinearGradient(
            begin=alignment.top_left,
            end=Alignment(0.8, 1),
            colors=[
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
