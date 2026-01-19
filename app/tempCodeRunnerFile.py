from flask import app, render_template, request
from app.BaseDeDatos import db
from app import Traduccion


@app.route('/modal_ver_reportes')
def modal_ver_reportes():
    dashboard = request.args.get('dashboard', 'dashboard_admin')  
    lang = request.args.get('lang', 'es')
    texts, lang = Traduccion.get_texts(lang)

    cursor = db.get_cursor()
    cursor.callproc('sp_mostrar_tbl_tickets')
    tickets = cursor.fetchall()
    cursor.close()
    return render_template('modal_ver_reportes.html', tickets=tickets, texts=texts, lang=lang, dashboard=dashboard)