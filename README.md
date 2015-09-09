# GamblerSpammer
Ferramenta desenvolvida para demonstrar a facilidade no envio de spam`s

#email.txt
Neste arquivo deve conter a mensagem que sera enviada, o conteudo dessa mensagem deve estar no formato de HTML como no exemplo abaixo sem o caracter #,

#<html>
# <head>
#    <title>GamblerSpammer</title>
#  </head>
#  <body>
#    <h1>Olá Mundo!</h1>
#  </body>
#</html>

#vitimas.txt
Inserir nesse arquivo as caixas de e-email que iram receber o spam, os emails devem estar um abaixo do outro como no exemplo abaixo,

tony@stark.com\r
doug@funny.com\r
tux@linux.org\r

#Bibliotecas adicionais
pip install smtplib
