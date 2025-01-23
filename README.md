Chat ao Vivo 
Este é um simples aplicativo de chat ao vivo criado com a biblioteca Flet. Ele permite que os usuários se conectem a um chat, enviem mensagens em tempo real e interajam com outros participantes.

Funcionalidades
Tela Inicial:

Título: Chat
Um botão chamado "Iniciar Chat", que ao ser clicado abre um popup/modal/alerta.
Popup de Boas-Vindas:

Ao clicar em "Iniciar Chat", o popup exibe uma mensagem de boas-vindas.
O popup solicita ao usuário que digite seu nome e tenha a opção de entrar no chat.
Entrando no Chat:

Ao clicar no botão "Entrar no Chat", o nome do usuário é registrado e a tela de chat é carregada.
O nome do usuário é exibido no chat com uma mensagem dizendo que ele entrou no chat.
Interação no Chat:

Os usuários podem digitar suas mensagens no campo de texto.
O botão "Enviar" envia a mensagem para o chat, incluindo o nome do usuário e a hora da mensagem.
Após enviar a mensagem, o campo de texto é limpo para a próxima mensagem.
Tecnologias Usadas:

Flet: Usado para criar a interface do aplicativo e gerenciar os eventos de interação.
Datetime: Usado para pegar a hora atual e exibir junto com as mensagens enviadas.
Como Usar
Instalar o Flet: Certifique-se de que a biblioteca Flet está instalada no seu ambiente Python. Para instalar o Flet, execute:

bash
Copiar
Editar
pip install flet
Rodar o Aplicativo: Execute o script Python para iniciar o aplicativo. O aplicativo será aberto em um navegador da web.

bash
Copiar
Editar
python app.py
Interagir com o Chat:

Na tela inicial, clique no botão "Iniciar Chat".
Digite seu nome no popup e clique em "Entrar no Chat".
Depois de entrar, você pode começar a digitar e enviar mensagens.
Explicação do Código
O código começa criando a tela inicial com o título "Chat" e um botão "Iniciar Chat".
Ao clicar no botão, um popup é exibido com um campo para inserir o nome do usuário.
Quando o botão "Entrar no Chat" é clicado, o popup fecha e a tela de chat é exibida.
O chat é gerenciado por um Column, e as mensagens enviadas são exibidas dentro dessa coluna.
O envio de mensagens é feito através do campo de texto e o botão "Enviar".
A mensagem é enviada com a hora atual e o nome do usuário, e depois de enviada, o campo de mensagem é limpo.
Personalização
Você pode personalizar a interface do chat e o comportamento do aplicativo, como adicionar novos elementos ou funcionalidades.
Também pode modificar o estilo visual do aplicativo com o Flet.
Licença
Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.
