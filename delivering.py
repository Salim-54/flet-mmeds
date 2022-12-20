import flet as ft
from flet import *


def delivering():
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
    return _delivering
