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


def prescription():
    _prescription = Column(
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
                                )
                            )
                        ),
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    horizontal_alignment=CrossAxisAlignment.CENTER
                )
            )],
        alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER)
    return _prescription
