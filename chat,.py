# Tela inicial:
    # Titulo: Chat
    # Botão: Iniciar Chat
        # quando clicar no botao:
        # abrir um popup/modal/alerta
            # titulo: Bem vindo ao Chat ao Vivo
            # botao: entrar no chat
                # quando clicar no botao:
                # fechar o popup/modal/alerta
                    # carregar o chat
                    # carregar o campo de mensagem
                    # botao enviar
                        # quando clicar no botao:
                        # enviar a mensagem
                        #limpar campo de mensagem

import flet as ft
from datetime import datetime
# função principal para rodar o app
def main(pagina):
    # titulo
    titulo = ft.Text("Chat ao Vivo")

    def enviar_mensagem_tunel(mensagem):
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        hora_atual = datetime.now().strftime("%H:%M")
        mensagem = f"{hora_atual} - {nome_usuario}: {texto_campo_mensagem}"
        pagina.pubsub.send_all(mensagem)
        campo_enviar_mensagem.value = ""
        pagina.update()

    campo_enviar_mensagem = ft.TextField(label="Digite sua mensagem", on_submit = enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click = enviar_mensagem)

    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])

    chat = ft.Column()

    def entrar_chat(evento):
        popup.open = False
        pagina.remove(titulo)
        pagina.remove(botao)
        

        pagina.add(chat)

        pagina.add(linha_enviar)

        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} entrou no chat"
        pagina.pubsub.send_all(mensagem)

        pagina.update()

    # criar o popup
    titulo_popup = ft.Text(" Bem vindo ao Chat ao Vivo")
    caixa_nome = ft.TextField(label= "Digite seu nome",on_submit = entrar_chat)
    botao_popup = ft.ElevatedButton("Entrar no chat", on_click = entrar_chat)
    popup = ft.AlertDialog(title=titulo_popup, content = caixa_nome,
                            actions = [botao_popup] )

    # botao inicial
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        
        
    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup) 
    
    # colocar os elementos na tela
    pagina.add(titulo)
    pagina.add(botao)
# executar a fução utilizando o flet
ft.app(main, view=ft.WEB_BROWSER )