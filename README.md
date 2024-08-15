# Gerador de Currículo e Envio por E-mail 📄✉️

## Visão Geral

    Este projeto consiste em um sistema desenvolvido em Python que permite gerar currículos em formato PDF com informações personalizadas e, em seguida, enviá-los por e-mail de forma automatizada. Podendo enviar pelo gmail, hotmail e hostinger.


## Funcionalidades Principais 📋
    1. Geração de Currículo em PDF

    Gerando o Currículo: O usuário preenche informações pessoais e profissionais, que são automaticamente formatadas e inseridas em um arquivo PDF.

    Envio de E-mail com Anexo: Após gerar o PDF, o sistema permite enviar o currículo com anexo diretamente para o e-mail especificado.

    Personalização Completa: Cada seção do currículo pode ser personalizada pelo usuário, incluindo informações de contato, formação acadêmica, experiência profissional, habilidades, e muito mais.

    2. Envio Automático por E-mail

    Após a geração do currículo, o sistema utiliza o protocolo SMTP para enviar o PDF diretamente para um endereço de e-mail especificado.
    O envio é feito de forma segura, com autenticação do remetente e suporte para anexos, garantindo que o currículo chegue ao destinatário em perfeitas condições.

    3. Interface de Linha de Comando (CLI)

    O sistema opera totalmente via linha de comando, solicitando ao usuário as informações necessárias e exibindo mensagens de sucesso ou erro durante o processo.
    Simplicidade e eficiência são os focos desta interface, permitindo que o usuário crie e envie seu currículo em poucos minutos.

## Estrutura do Código 🗂️

    Geração do PDF:

    Utiliza a biblioteca FPDF para criar e estruturar o currículo em formato PDF.
    O usuário insere dados como nome, endereço, experiência, formação, entre outros, e o sistema os organiza automaticamente no PDF.

    Envio de E-mail:

    Utiliza as bibliotecas smtplib e MIME para configurar o servidor SMTP, criar o corpo do e-mail e anexar o PDF gerado.
    Após configurar o servidor SMTP, o sistema envia o e-mail com o currículo anexado para o destinatário desejado.


## Tecnologias Utilizadas 🛠️

    Python: Linguagem de programação principal usada para desenvolver o sistema.

    FPDF: Biblioteca Python para geração de arquivos PDF.

    smtplib: Módulo padrão do Python utilizado para o envio de e-mails via protocolo SMTP.

    email.mime: Submódulo utilizado para criar mensagens de e-mail complexas, incluindo múltiplos tipos de conteúdo e anexos.


## Como usar o sistema 😁⚡

    Para utilizar o sistema "Gerador de Currículo e Envio por E-mail", siga as etapas abaixo:


    1. Primeiro clone o Repositório:

    clone o repositório para sua máquina local utilizando o comando:
    git clone https://github.com/seuusuario/gerador-curriculo-email.git

    Navegue até o diretório do projeto:
    cd gerador-curriculo-email


    2. Instale as Dependências:

    O projeto utiliza algumas bibliotecas externas, que você pode instalar utilizando o pip:
    pip install fpdf smtplib.


    3. Configuração de Segurança do Gmail:

    Para enviar e-mails pelo sistema, você precisará habilitar a autenticação de dois fatores na sua conta do Gmail e gerar uma senha de aplicativo. 

    Isso é necessário para garantir que o sistema possa enviar e-mails de forma segura.
    Acesse sua conta do Gmail, vá em Gerenciar sua Conta Google > Segurança > Senhas de aplicativos.

    Escolha a opção para criar uma nova senha de aplicativo, selecione "Email" como o tipo de aplicativo, e "Outro (nome personalizado)" para nomear. Copie a senha gerada e utilize-a no código como a password.

    4. Configure as Credenciais de E-mail:

    Abra o arquivo Python principal (gerador_curriculo.py) em um editor de texto e configure as variáveis com suas credenciais de e-mail:

    server_smtp = "servido smtp (gmail, hotmail, hostinger)"
    port = "porta"
    sender_email = "seu_email@gmail.com"
    password = "sua_senha"
    recive_email = "email_destinatario@gmail.com"
    subject = "assunto do e-mail"
    body = "corpo do e-mail"

    Obs: Para segurança, evite deixar a senha diretamente no código.


    5. Execute o Script:

    Com todas as configurações feitas, você pode executar o script:

    python gerador_curriculo_email.py
    O script irá pedir para você preencher várias informações pessoais e profissionais. Após preencher os dados, ele irá gerar um arquivo PDF com seu currículo e enviá-lo automaticamente para o e-mail configurado.


    Personalização:

    Se necessário, você pode personalizar o código para adicionar ou modificar as seções do currículo conforme suas necessidades. Basta editar as partes correspondentes no código fonte.


## Contribuições 🤝

    Estamos abertos a contribuições e sugestões para melhorar continuamente este projeto. Se você gostaria de contribuir, por favor, entre em contado conosco através deste Email: raone199807@gmail.com ou pelo linkedin: www.linkedin.com/in/raonesouza

    Sinta-se à vontade para explorar mais sobre o projeto e interagir conosco através de issues e pull requests!
