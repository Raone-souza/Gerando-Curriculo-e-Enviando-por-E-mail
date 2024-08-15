# Explicação do Código de Envio de E-mail com SMTP

    Este trecho de código tem como objetivo enviar um e-mail com um arquivo PDF anexado, utilizando o protocolo SMTP (Simple Mail Transfer Protocol). Abaixo, detalhamos o funcionamento de cada parte do código:


### Importações de Bibliotecas

    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders

    smtplib: Biblioteca padrão do Python para enviar e-mails usando o protocolo SMTP.

    MIMEText: Classe usada para criar a parte textual do e-mail.

    MIMEMultipart: Classe usada para criar uma mensagem com várias partes, como texto e anexos.

    MIMEBase: Classe usada para criar e anexar arquivos ao e-mail.

    encoders: Utilizado para codificar o anexo em base64, necessário para enviar arquivos em formato binário via e-mail.


### Configuração do Servidor SMTP

    server_smtp = ""
    port = 587
    sender_email = ""
    password = ""

    server_smtp: Endereço do servidor SMTP usado para enviar o e-mail (por exemplo, "smtp.gmail.com" para Gmail).

    port: Porta usada pelo servidor SMTP (587 é a porta comum para conexões TLS/STARTTLS).

    sender_email: E-mail do remetente, que será usado para enviar a mensagem.

    password: Senha do e-mail do remetente (ou uma senha de aplicativo gerada no caso de usar Gmail).


### Configuração do E-mail

    recive_email = ""
    subject = ""
    body = ""

    recive_email: E-mail do destinatário, que receberá o e-mail.

    subject: Assunto do e-mail.

    body: Corpo do e-mail, onde você pode escrever o conteúdo da mensagem.


### Criação do E-mail

    message = MIMEMultipart()
    message["from"] = sender_email
    message["to"] = recive_email
    message["subject"] = subject
    message.attach(MIMEText(body, "plain"))

    MIMEMultipart(): Cria um objeto de mensagem multipart, que permite anexar diferentes tipos de conteúdo (texto e anexos).

    message["from"]: Define o e-mail do remetente.

    message["to"]: Define o e-mail do destinatário.

    message["subject"]: Define o assunto do e-mail.

    attach(MIMEText(body, "plain")): Anexa o corpo do e-mail à mensagem.


### Anexando o Arquivo PDF

    pdf_filename = "Currículo.pdf"
    with open(pdf_filename, "rb") as attachment:
    part = MIMEBase("application", "pdf")
    part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header(
    "Content-Disposition",
    f"attachment; filename= {pdf_filename}",
    )

    message.attach(part)
    open(pdf_filename, "rb"): Abre o arquivo PDF em modo de leitura binária.
    MIMEBase("application", "pdf"): Cria uma instância MIMEBase para o arquivo PDF, especificando o tipo de conteúdo como "application/pdf".

    set_payload(attachment.read()): Lê o conteúdo do arquivo PDF e o define como o payload do anexo.

    encoders.encode_base64(part): Codifica o payload em base64 para garantir que o arquivo seja enviado corretamente.

    add_header("Content-Disposition", f"attachment; filename= {pdf_filename}"): Adiciona um cabeçalho ao anexo, especificando que ele é um arquivo anexado e definindo o nome do arquivo.

    message.attach(part): Anexa o arquivo PDF à mensagem.


### Conectando e Enviando o E-mail

    try:
    server = smtplib.SMTP(server_smtp, port)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, recive_email, message.as_string())
    print("E-mail enviado com sucesso!!!")

    except Exception as e:
    print(f"houve algum erro {e}")
    finally:

    server.quit()


    smtplib.SMTP(server_smtp, port): Inicia uma conexão com o servidor SMTP.

    server.starttls(): Inicia a criptografia TLS para a conexão, aumentando a segurança do envio do e-mail.

    server.login(sender_email, password): Faz login na conta de e-mail usando as credenciais fornecidas.

    server.sendmail(sender_email, recive_email, message.as_string()): Envia o e-mail com o anexo para o destinatário.

    server.quit(): Encerra a conexão com o servidor SMTP.


### Tratamento de Exceções

    O bloco try-except-finally garante que qualquer erro durante o processo de envio seja capturado e exibido, e que a conexão com o servidor SMTP seja fechada corretamente após o envio.