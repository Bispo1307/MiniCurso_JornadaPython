# Criar o BispoZap

# Botão: Iniciar o Chat
    # Quando eu clicar no botão:
    # Janela / Dialog / Modal / PopUp
        # Titulo: Bem vindo ao BispoZap
        # Campo de Texto: Escreva seu nome no chat
        # Botão: Entrar no chat
            # Clicou no botão:
            # Fechar o Dialog
                # Criar o chat
                # Criar o campo de mensagem: Digite sua mensagem
                # Botão enviar
                    # Quando clicar no botão:
                    # Envie a mensagem para o chat

# Importar o Flet
import flet as ft

# Criar a função principal (main) do seu aplicativo
def main(pagina):
    
    # Criar os elementos
    titulo = ft.Text("BispoZap")

    titulo_janela = ft.Text("Bem vindo ao BispoZap")
    campo_nome = ft.TextField(label="Digite o seu nome")

    def enviar_mensagem_tunel(mensagem):
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)
        pagina.pubsub.send_all(mensagem)
        chat.controls.append(texto_mensagem)
        pagina.update()

    # WebSocket -> Tunel de Comunicação
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        mensagem = f"{campo_nome.value}: {campo_mensagem.value}"
        # Enviar a mensagem no tunel
        pagina.pubsub.send_all(mensagem)
        pagina.update()

        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Escreva sua mensagem")
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    arquivo = ft.FilePicker()
    chat = ft.Column()
    linha_mensagem = ft.Row([campo_mensagem, botao_enviar])
    def entrar_chat(evento):
        print("Entrou no chat")
        # Fechar a janela / Dialog
        janela.open = False
        # Tirar o titulo
        pagina.remove(titulo)
        # Tirar o botão iniciar
        pagina.remove(botao_iniciar)

        # Criar o Chat
        # Criar o campo digite sua mensagem
        pagina.add(campo_mensagem)
        # Botão enviar
        pagina.add(linha_mensagem)
        pagina.update()

    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)


    janela = ft.AlertDialog(
        title=titulo_janela,
        content=campo_nome,
        actions=[botao_entrar]
    )

    def abrir_dialog(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_dialog)

    # Colocar os elementos da página
    pagina.add(titulo)
    pagina.add(botao_iniciar)

# Rodar o seu aplicativo
ft.app(main, ft.WEB_BROWSER)