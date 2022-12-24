from __future__ import print_function
import flet as ft
from flet import *


def submit(e):
    if e.control.value == "home":
        routes.current_step = "home"
        routes.display(routes.current_step)


def token():
    _token_input = Container(

        alignment=alignment.center,
        content=Column(
            [
                Text("TOKEN_INPUT", size=30),
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
                    on_submit=submit
                ),
            ],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
    )
    return _token_input


def header():
    _header = Container(
        content=Row(
            controls=[
                Image(src=f"/logo.png", width=160),
                Text('02 Dec 2019'),
            ], alignment=MainAxisAlignment.SPACE_BETWEEN,),
        margin=margin.symmetric(horizontal=60, vertical=50)
    )
    return _header


def footer():

    _footer = Container(
        image_src="/assets/foot.png",
        image_fit=ImageFit.FILL,
        # image_repeat=ImageRepeat.NO_REPEAT,
        content=Row(
            [
                Container(
                    margin=margin.symmetric(vertical=20, horizontal=100),
                    alignment=alignment.center,
                    expand=True,
                    content=Row(
                        controls=[
                            Image(src=f"/call.png", width=90,),
                            Text("Contact center : "),
                            Text("+250789393544 / +250789393544"),
                        ],
                        alignment=MainAxisAlignment.SPACE_AROUND,
                        vertical_alignment="center"
                    ),),
                Container(
                    margin=margin.symmetric(vertical=20, horizontal=200),
                    alignment=alignment.center,
                    expand=True,
                    content=Row(
                        controls=[
                            Text("Email : "),
                            Text("meggameds@info.com", expand=True),
                        ],
                        alignment=MainAxisAlignment.SPACE_AROUND,
                        vertical_alignment="center"
                    ),),
            ],
        ))
    return _footer
