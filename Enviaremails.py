import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import codecs
ahora = os.getcwd()
os.chdir(ahora)
class EnviarEmail:
    
    def __init__(self,receiver,body,propuesta,path, noadjuntar = False, sender = "ezequielcappello@gmail.com", password = "Eze13975"):
        self.sender = sender
        self.reciever = receiver
        # self.reciever = ','.join(receiver)
        self.password = password
        self.body = body
        self.propuesta = propuesta
        self.noadjuntar = noadjuntar
        self.path = path

    def adjuntar(self,pdfname,message):
        for file in pdfname:  
            binary_pdf = open(file, 'rb')
            nombre = os.path.basename(file)
            payload = MIMEBase('application', 'octate-stream', Name=nombre)
            payload.set_payload((binary_pdf).read())
            encoders.encode_base64(payload)
            payload.add_header('Content-Decomposition', 'attachment', filename= nombre)
            message.attach(payload)

    def enviar(self):
        with codecs.open(ahora + '\\Data\\firma.html',"r", "utf-8") as f:
            firma = f.read()
        session = smtplib.SMTP('smtp.gmail.com', 587)
        #Inicio la conexion
        session.starttls()
        try:
            #Me conecto con las credenciales
            session.login(self.sender, self.password)
        except:
            print('El email o la contraseña no son correctos.')
        message = MIMEMultipart()
        message['From'] = self.sender
        message['To'] = self.reciever
        message['Subject'] = '{}'.format(self.propuesta)
        message.attach(MIMEText(self.body, 'plain'))
        message.attach(MIMEText(firma, 'html'))

        if self.noadjuntar == False:
            pdfname = self.path
            self.adjuntar(pdfname,message)
        #Envio el email

        text = message.as_string()
        session.sendmail(self.sender, self.reciever, text)

        print('Email Enviado a {}'.format(self.reciever))