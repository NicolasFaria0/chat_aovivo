# Chat ao Vivo

Este é um simples aplicativo de chat ao vivo criado com a biblioteca **Flet**. Ele permite que os usuários se conectem a um chat, enviem mensagens em tempo real e interajam com outros participantes.

## Funcionalidades

### Tela Inicial:
- **Título**: "Chat"
- Um botão chamado **"Iniciar Chat"**, que ao ser clicado abre um **popup/modal/alerta**.

### Popup de Boas-Vindas:
- Ao clicar em **"Iniciar Chat"**, o popup exibe uma mensagem de boas-vindas.
- O popup solicita ao usuário que **digite seu nome** e oferece a opção de **entrar no chat**.

### Entrando no Chat:
- Ao clicar no botão **"Entrar no Chat"**, o nome do usuário é registrado e a tela de chat é carregada.
- O nome do usuário é exibido no chat com uma mensagem dizendo que ele entrou no chat.

### Interação no Chat:
- Os usuários podem **digitar suas mensagens** no campo de texto.
- O botão **"Enviar"** envia a mensagem para o chat, incluindo o **nome do usuário** e a **hora da mensagem**.
- Após enviar a mensagem, o campo de texto é **limpo** para a próxima mensagem.

## Tecnologias Usadas
- **Flet**: Usado para criar a interface do aplicativo e gerenciar os eventos de interação.
- **Datetime**: Usado para pegar a hora atual e exibir junto com as mensagens enviadas.

## Como Usar

### 1. Instalar o Flet:
Certifique-se de que a biblioteca **Flet** está instalada no seu ambiente Python. Para instalar o Flet, execute:

```bash
pip install flet

