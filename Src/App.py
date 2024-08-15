# importando as bibliotecas necessarias para esse sistema
from fpdf import FPDF 
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


# Inicia o processo, 
# saudando o usuário e explicando que ele vai preencher as informações do currículo
print("Bem-vindo(as), agora vamos prencher todas as informações para fazer seu curriculo! \n")
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 24)
nome = input("informe seu nome completo: ")
pdf.cell(w=0, h=20, txt=f" {nome} ", ln=1, align="C")
print("\n")


# Inicia a seção de informações pessoais
print("adicionado informações pessoais ")
pdf.set_font('arial', '', 12)
endereço = input("informe seu endereço, numero e CEP: ")
pdf.cell(w=0, h=7, txt=f"Endereço: {endereço} ", ln=1)

tel= input("informe seu numero de telefone: ")
pdf.cell(w=0, h=7, txt=f"Telefone: {tel}", ln=1)

email = input("informe seu Email: ")
pdf.cell(w=0, h=7, txt=f"E-Mail: {email}", ln=1)

user_linkdin = input("informe seu perfil do LinkedIn: ")
pdf.cell(w=0, h=7, txt=f"LinkedIn: {user_linkdin}", ln=1)

user_github = input("informe seu perfil do GitHub: ")
pdf.cell(w=0, h=7, txt=f"GitHub: {user_github}", ln=1)
print("\n")


# Inicia a seção de objetivo profissional
print("adicionado objetivo profissional")
pdf.set_font('arial', 'b', 14)
pdf.cell(w=0, h=20, txt="Objetivo Profissional ", ln=1)

pdf.set_font('arial', '', 12)
objetivo_profissional = input("informe seu objetivo profissional: ")
pdf.cell(w=0, h=2, txt=f" {objetivo_profissional} ", ln=1)
print("\n")


# Inicia a seção de escolaridade/Formação acadêimca
print("adicionado  sua escolaridade/Formação acadêimca ")
pdf.set_font('arial', 'b', 14)
pdf.cell(w=0, h=20, txt="Formação Acadêmica ", ln=1)

pdf.set_font('arial', '', 12)
Nome_Formação = input("informe o nome do seu curso: ")
pdf.cell(w=0, h=6, txt=f"Nome do curso: {Nome_Formação}", ln=1)

Nome_faculdade = input("informe a sua instituição: ")
pdf.cell(w=0, h=6, txt=f"Instituição de ensino: {Nome_faculdade}", ln=1)

data_conclusao = input("informe a data de conclusão do curso: ")
pdf.cell(w=0, h=6, txt=f"Data de conclusão ou Previsão de conclusão: {data_conclusao}", ln=1)
print("\n")


# Inicia a seção de Experiência Profissional
print("adicionado  sua Experiência Profissional")
pdf.set_font('arial', 'b', 14)
pdf.cell(w=0, h=20, txt="Experiência Profissional", ln=1)

pdf.set_font('arial', '', 12)
nome_empresa = input("informe o nome da empresa: ")
pdf.cell(w=0, h=6, txt=f"Nome da Empresa: {nome_empresa}", ln=1)

Cargo = input("informe seu cargo e o período: ")
pdf.cell(w=0, h=6, txt=f"Cargo / período: {Cargo}", ln=1)

Atividade_Respo = input("informe suas principais ativiadades e Resposabilidades no cargo: ")
pdf.cell(w=0, h=6, txt=f"Principais ativiadades e Resposabilidades: {Atividade_Respo}", ln=1)
print("\n")


# Inicia a seção de projetos pessoais
print("adicionado  seus projetos pessoais ")
pdf.set_font('arial', 'b', 14)
pdf.cell(w=0, h=20, txt="Projetos", ln=1)

pdf.set_font('arial', '', 12)
Nome_projeto = input("informe o nome do seu projeto: ")
pdf.cell(w=0, h=6, txt=f"Nome do projeto: {Nome_projeto} ", ln=1)

Link_prjeto = input("informe o link do projeto: ")
pdf.cell(w=0, h=6, txt=f"Link do projeto: {Link_prjeto}", ln=1)

Tec_habilidade = input("informe tecnologias utilizadas no porjeto: ")
pdf.cell(w=0, h=6, txt=f"tecnologias utilizadas: {Tec_habilidade}", ln=1)
print("\n")


# Inicia a seção de Cursos e Qualificações
print("adicionado  seus Cursos e Qualificações")
pdf.set_font('arial', 'b', 14)
pdf.cell(w=0, h=20, txt="Qualificações e Cursos", ln=1)

pdf.set_font('arial', '', 12)
Nome_curso = input("informe o nome do curso: ")
pdf.cell(w=0, h=6, txt=f"Nome do curso: {Nome_curso}", ln=1)

inst_curso = input("informe a instuiição: ")
pdf.cell(w=0, h=6, txt=f"Instituição: {inst_curso}", ln=1)

Carga_horaria = input("informe a carga horária: ")
pdf.cell(w=0, h=6, txt=f"Duração / Carga Horária: {Carga_horaria}", ln=1)
print("\n")


# Inicia a seção de Habilidades e Conhecimento
print("adicionado suas Habilidades e Conhecimento ")
pdf.set_font('arial', 'b', 14)
pdf.cell(w=0, h=20, txt="Habilidades / Conhecimento", ln=1)

pdf.set_font('arial', '', 12)
Idiomas = input("informe seus idiomas: ")
pdf.cell(w=0, h=6, txt=f"Idiomas: {Idiomas}", ln=1)

Conhecimento_Técnicos = input("informe seus Conhecimento Técnicos: ")
pdf.cell(w=0, h=6, txt=f"Conhecimento Técnicos: {Conhecimento_Técnicos}", ln=1)

habilidades_relevantes= input("informe suas habilidades relevantes: ")
pdf.cell(w=0, h=5, txt=f"Outras habilidades relevantes: {habilidades_relevantes}", ln=1)
print("\n")


# Por fim, Gera o PDF salvando como 'curriculo.pdf'
pdf.output('Currículo.pdf')


# Verifica se o PDF foi gerado com sucesso e exibe uma mensagem correspondente
if os.path.exists('Currículo.pdf'):
    print("PDF gerado com sucesso!")
else:
    print("Erro: O PDF não foi gerado.")


# Etapa de envio do PDF por e-mail via SMTP
# Configurações do e-mail
server_smtp = "smtp.gmail.com"
port = 587
sender_email = "raone199807@gmail.com"
password = "mooyrzpbbvmnaikl"
recive_email = "raone199807@gmail.com"
subject = "Segue em anexo o currículo para vaga..."
body = "Olá, \n\nSegue em anexo o meu currículo para a vaga. \n\nObrigado!"


# Criando o e-mail
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recive_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))


# Anexando o arquivo PDF no E-mail
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

# Enviando o e-mail e fazendo uma verificação se o envio foi corretamente
try:
    server = smtplib.SMTP(server_smtp, port)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, recive_email, message.as_string())
    print("E-mail enviado com sucesso!!!")
except Exception as e:
    print(f"Houve algum erro: {e}")
finally:
    server.quit()