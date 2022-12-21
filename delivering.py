import flet as ft
from flet import *


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


def delivering():
    _delivering = Column(
        visible=True if screen == 2 else False,
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
