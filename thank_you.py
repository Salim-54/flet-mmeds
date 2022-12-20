import flet as ft
from flet import *


def finish():
    _finish = Container(
        border_radius=10,
        bgcolor="0xffD3E8EF",
        width=400,
        height=200,
        alignment=alignment.center,
        content=Text("THANK YOU!!!", size=40, color="black")
    )
    return _finish
