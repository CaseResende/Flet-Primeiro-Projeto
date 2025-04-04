import flet as ft



def main(pagina: ft.Page):
    texto = ft.Text('Olá, Mundo!')

    pagina.add(texto)

ft.app(target=main)

