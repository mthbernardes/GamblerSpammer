from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import email.utils
import smtplib

#Configuracoes Credenciais
conta			= 'email@example.com'
senha			= 'senha'

#Configuracoes Email
#Email apresentado para a vitima
email_falso = 'obama@whitehouse.com'

#Nome email falso
nome = 'President Obama'

#Assunto do E-mail
assunto = 'YES WE CAN'

#Arquivo com conteudo do e-mail
file_email = 'email.txt'

#Arquivo com a lista de emails
lista_vitima = 'vitimas.txt'

#Servidor SMTP
servidor = 'smtp.example.com'
porta = 587

def vitimas():
	file = open(lista_vitima)
	vitimas = file.readlines()
	for vitima in vitimas:
		vitima = vitima.rstrip()
		arquivo_email(vitima)

def arquivo_email(vitima):
	file = open(file_email, 'rb')
	conteudo = file.read()
	envia_email(conteudo, vitima)

def envia_email(conteudo, vitima):
	print ('[+] - GERANDO EMAIL - [+]')
	mail = MIMEMultipart('alternative')
	mail["Subject"] = assunto
	mail["From"] = email.utils.formataddr((nome,email_falso))
	mail["To"] = vitima
	mail["Reply-to"] = email_falso
	texto = MIMEText(conteudo, 'html')
	mail.attach(texto)
	try:
		print '[+] - ENVIANDO E-MAIL PARA: %s - [+]' %(vitima)
		gm = smtplib.SMTP(servidor, porta)
		gm.ehlo()
		gm.starttls()
		gm.ehlo()
		gm.login(conta, senha)
		gm.sendmail(mail["From"], vitima, mail.as_string())
		gm.close()
		print '[+] - E-MAIL ENVIADO COM SUCESSO - [+]'
		print
	except:
		print ('[!] - ERRO AO ENVIAR E-MAIL - [!]')
		print
vitimas()
