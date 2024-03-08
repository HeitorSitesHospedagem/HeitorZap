# Titulo: HectorZap
# Botao: de iniciar chat
    # clicou no botao:
        # popup / model
            # Titulo: Bem vindo ao HectorZap
            # campo: escreva seu nome no chat
            # botao: entrar no chat
# chat
# embaixo do chat
    # campo de Digite sua mensagem
    # botao de enviar

# flet -> framework do Python
# pip install flet

import flet as ft # importar

def main(pagina): # criar a funcao princial/main
    texto = ft.Text("HeitorZap")

    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem):
        # adicionar mensagem no chat
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        print("Enviar mensagem")
        pagina.pubsub.send_all(f"{nome_usuario.value}: {campo_mensagem.value}")
        # limpe o campo mensagem
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_mensagem, botao_enviar])
    def entrar_chat(evento):
        print("Entrar no chat")
        # fechar o popup
        popup.open = False
        # tirar o botao iniciar chat
        pagina.remove(botao_iniciar)
        # tirar o titulo HeitorZap
        pagina.remove(texto)
        # criar o chat
        pagina.add(chat)
        pagina.pubsub.send_all(f"{nome_usuario.value} entrou no chat")
        # colocar o campo de digitar mensagem
        # criar o botao de enviar
        pagina.add(linha_enviar)
        pagina.update()

    titulo_popup = ft.Text("Bem vindo ao HeitorZap")
    nome_usuario = ft.TextField(label="Escreva seu nome no chat")
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=titulo_popup,
        content=nome_usuario,
        actions=[botao_entrar]
    )

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update() # atualizar a pagina para o popup

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER) # criar o app chamando a funcao principal
# colocar no google , view=ft.WEB_BROWSER