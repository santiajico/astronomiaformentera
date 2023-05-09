#!/usr/bin/env python
import cgi
import smtplib
from email.message import EmailMessage

# Configurar los detalles del servidor SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Configurar los detalles del correo electrónico
destinatario = 'astronomiaformentera@gmail.com'
asunto = 'Nuevo mensaje de contacto'

# Obtener los datos del formulario
form = cgi.FieldStorage()
nombre = form.getvalue('nombre')
email = form.getvalue('email')
telefono = form.getvalue('telefono')
mensaje = form.getvalue('mensaje')

# Formatear el correo electrónico
msg = EmailMessage()
msg['From'] = email
msg['To'] = destinatario
msg['Subject'] = asunto
msg.set_content(f'Nombre: {nombre}\nEmail: {email}\nTelefono: {telefono}\nMensaje: {mensaje}')

# Enviar el correo electrónico
with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    smtp.starttls()
    smtp.login('tu_correo@gmail.com', 'tu_contrasena')
    smtp.send_message(msg)

# Redirigir al usuario a una página de confirmación
print('Location: confirmacion.html')
print('Content-type:text/html\r\n\r\n')
print('<html>')
print('<head>')
print('<title>Redireccionando...</title>')
print('<meta http-equiv="refresh" content="0;URL=confirmacion.html">')
print('</head>')
print('<body>')
print('</body>')
print('</html>')
