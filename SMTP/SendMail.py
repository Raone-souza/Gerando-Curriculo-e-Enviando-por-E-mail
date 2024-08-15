import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#configurando servidor SMTP
server_smtp = ""
port = 587
sender_email = ""
password = ""

#config email
recive_email = ""
subject = ""
body = ""


#criando email
message = MIMEMultipart()
message["from"] = sender_email
message["to"] = recive_email
message["subject"] = subject
message.attach(MIMEText(body, "plain"))

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

#conectando o e-mail
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