import os
import smtplib
from flask import render_template
from email.mime.image import MIMEImage
from email.message import EmailMessage
from email.utils import make_msgid

class CorreoEcorisk:
    GMAIL_USUARIO = 'soporte.ecorisk@gmail.com'
    GMAIL_CLAVE = 'bwwx qnpu kpmh xmjr'  # Contraseña de aplicación
    
    LOGO_PATH = "static/img/logo_ecorisk.png"
    MASCOTA_PATH = "static/img/Tucan.png"     
    MANUAL_PATH = "static/docs/manual_bienvenida_ecorisk.pdf"

    @staticmethod
    def crear_mensaje(destinatario, asunto, contenido_texto, contenido_html=None, archivos_adjuntos=None):
        mensaje = EmailMessage()
        mensaje['Subject'] = asunto
        mensaje['From'] = CorreoEcorisk.GMAIL_USUARIO
        mensaje['To'] = destinatario
        mensaje.set_content(contenido_texto)

        if contenido_html:
            # Crear IDs únicos para las imágenes
            cid_logo = make_msgid(domain='ecorisk.com')[1:-1]
            cid_mascota = make_msgid(domain='ecorisk.com')[1:-1]

            contenido_html = contenido_html.replace("cid:logo_ecorisk.png", f"cid:{cid_logo}")
            contenido_html = contenido_html.replace("cid:mascota.png", f"cid:{cid_mascota}")
            mensaje.add_alternative(contenido_html, subtype='html')

            # Incrustar imágenes
            for path, cid, name in [
                (CorreoEcorisk.LOGO_PATH, cid_logo, "logo_ecorisk.png"),
                (CorreoEcorisk.MASCOTA_PATH, cid_mascota, "mascota.png")
            ]:
                if os.path.exists(path):
                    with open(path, 'rb') as img:
                        imagen = MIMEImage(img.read())
                        imagen.add_header('Content-ID', f'<{cid}>')
                        imagen.add_header('Content-Disposition', 'inline', filename=name)
                        mensaje.get_payload()[-1].add_related(imagen)

        # Adjuntar archivos (PDF del manual)
        if archivos_adjuntos:
            for archivo in archivos_adjuntos:
                if os.path.exists(archivo):
                    with open(archivo, 'rb') as f:
                        mensaje.add_attachment(
                            f.read(),
                            maintype='application',
                            subtype='pdf',
                            filename=os.path.basename(archivo)
                        )
        return mensaje

    @staticmethod
    def enviar_mensaje(mensaje):
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(CorreoEcorisk.GMAIL_USUARIO, CorreoEcorisk.GMAIL_CLAVE)
                smtp.send_message(mensaje)
            print(f"✅ Correo enviado a {mensaje['To']}")
            return True
        except Exception as e:
            print(f"❌ Error al enviar correo: {e}")
            return False

    @staticmethod
    def enviar_bienvenida(destinatario, nombre):
        asunto = "🌱 ¡Bienvenido a EcoRisk!"
        texto = f"Hola {nombre},\n\nBienvenido a EcoRisk. Adjuntamos tu manual de bienvenida en PDF.\n\nEquipo EcoRisk"

        html = render_template("correo/bienvenida.html", nombre=nombre)

        # Adjuntar el manual PDF
        mensaje = CorreoEcorisk.crear_mensaje(
            destinatario,
            asunto,
            texto,
            contenido_html=html,
            archivos_adjuntos=[CorreoEcorisk.MANUAL_PATH]
        )
        return CorreoEcorisk.enviar_mensaje(mensaje)