import flet as ft


def main(pagina: ft.Page):
    pagina.theme_mode = ft.ThemeMode.DARK


    def change_main_image(e):
        for elemento in options.controls:
            if elemento == e.control:
                elemento.opacity = 1
                main_image.src = elemento.content.src
            else:
                elemento.opacity = 0.5

        main_image.update()
        options.update()


    imagens_produto = ft.Container(
        bgcolor=ft.colors.WHITE,
        padding=ft.padding.all(30),
        aspect_ratio=9/16,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                main_image := ft.Image(
                    src='https://dasports.com.br/cdn/shop/files/los-angeles-lakers-nike-icon-edition-swingman-jersey-gold-luka-don_C4_8Di_C4_87-youth_ss5_p-202849486_pv-1_u-ckv5fga0j3hsrgotxrrp_v-xalafditxpnrpdb7y4ef.png?v=1738806116',
                ),

                options := ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            content=ft.Image(
                                src='https://dasports.com.br/cdn/shop/files/los-angeles-lakers-nike-icon-edition-swingman-jersey-gold-luka-don_C4_8Di_C4_87-youth_ss5_p-202849486_pv-1_u-ckv5fga0j3hsrgotxrrp_v-xalafditxpnrpdb7y4ef.png?v=1738806116',
                            ),
                            width=80,
                            height=80,
                            opacity=1,
                            on_click=change_main_image
                        ),
                        ft.Container(
                            content=ft.Image(
                                src='https://images.footballfanatics.com/los-angeles-lakers/los-angeles-lakers-nike-association-edition-swingman-jersey-white-luka-don%C4%8Di%C4%87-unisex_ss5_p-202849487+pv-1+u-sa2i3cumkfim08urwvvc+v-mqltjo7yy92yntc9d7b9.jpg?_hv=2&w=900',
                            ),
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image
                        ),
                        ft.Container(
                            content=ft.Image(
                                src='https://acdn-us.mitiendanube.com/stores/002/794/749/products/big-6236de797ebdf79ed417388408266384-1024-1024.jpg',
                            ),
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image
                        )
                    ]
                )
            ]
        )
    )

    detalhes_produto = ft.Container(
        padding=ft.padding.all(30),
        bgcolor=ft.colors.BLACK87,
        aspect_ratio=9/16,
        expand=True,
        content=ft.Column(
            controls=[
                ft.Text(
                    value='CAMISAS',
                    color=ft.colors.AMBER,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Text(
                    value='Camisa Lakers Luka Doncic Amarela',
                    color=ft.colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                    size=30,
                ),
                ft.Text(
                    value='Uniforme de basquete',
                    color=ft.colors.GREY,
                    italic=True,
                ),
                ft.ResponsiveRow(
                    columns=12,
                    controls=[
                        ft.Text(
                            col={'xs': 12, 'sm': 6},
                            value='R$ 499,90',
                            color=ft.colors.WHITE,
                            size=30,
                        ),
                        ft.Row(
                            col={'xs': 12, 'sm': 6},
                            controls=[
                                ft.Icon(
                                    name=ft.icons.STAR,
                                    color=ft.colors.AMBER if _ < 4 else ft.colors.WHITE,
                                ) for _ in range(5)
                            ]
                        )
                    ]
                ),
                ft.Tabs(
                    selected_index=0,
                    height=150,
                    indicator_color=ft.colors.AMBER,
                    label_color=ft.colors.AMBER,
                    unselected_label_color=ft.colors.GREY,
                    tabs=[
                        ft.Tab(
                            text='Descrição',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='O Los Angeles Lakers são um time de basquete localizado em Los Angeles, Califórnia. São conhecidos por serem um time das estrelas. Vestindo a camisa 77, Luka Doncic é a principal estrela da franquia. Que possui seu uniforme na versão Amarela.',
                                    color=ft.colors.GREY,
                                )
                            )
                        ),
                        ft.Tab(
                            text='Detalhes',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='Tabela de tamanhos:\nP = 100cm x 50cm\nM = 112cm x 54cm\nG = 125cm x 58cm\nGG = 130cm x 62cm',
                                    color=ft.colors.GREY,
                                )
                            )
                        )
                    ]
                ),
                ft.ResponsiveRow(
                    columns=12,
                    controls=[
                        ft.Dropdown(
                            col={'xs': 12, 'sm': 6},
                            width=float('inf'),
                            label='Cor',
                            label_style=ft.TextStyle(color=ft.colors.WHITE, size=16),
                            border_color=ft.colors.GREY,
                            border_width=0.5,
                            options=[
                                ft.dropdown.Option(text='Amarela'),
                                ft.dropdown.Option(text='Branca'),
                                ft.dropdown.Option(text='Roxa'),
                            ]
                        ),
                        ft.Dropdown(
                            col={'xs': 12, 'sm': 6},
                            width=float('inf'),
                            label='Quantidade',
                            label_style=ft.TextStyle(color=ft.colors.WHITE, size=16),
                            border_color=ft.colors.GREY,
                            border_width=0.5,
                            options=[
                                ft.dropdown.Option(text=f'{num} unid.') for num in range(1, 11)
                            ]
                        )
                    ]
                ),

            ]
        )
    )

    layout = ft.Container(
        width=900,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.CYAN),
        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            controls=[
                #imagens_produto,
                detalhes_produto
            ]
        )
    )


    pagina.add(layout)

ft.app(target=main)
