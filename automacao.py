import os
import smtplib
from email.message import EmailMessage
from segredos import senha

EMAIL_ADDRESS ='michaelrodrigues@canaverde.com.br'
EMAIL_PASSWORD = senha

msg = EmailMessage()
msg['subject'] = 'Equipamento novo para inventário'
msg['from']= ' michaelrodrigue'
msg['To']= 'michael.pires.rodrigues@gmail.com'

msg.set_content('')