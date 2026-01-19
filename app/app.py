from datetime import datetime
import bcrypt
from flask import Flask, render_template, request, redirect, url_for, session, flash
from BaseDeDatos import ConfiguracionBD
from Traduccion import traduccion

app = Flask(__name__)
app.secret_key = "Ariana_Grande"

db = ConfiguracionBD(app)
Traduccion = traduccion()


@app.route("/")
def home():
    texts, lang = Traduccion.get_texts(request.args.get("lang", "es"))
    return render_template("home.html", texts=texts, lang=lang)

@app.route("/index")
def index():
    texts, lang = Traduccion.get_texts(request.args.get("lang", "es"))
    return render_template("home.html", texts=texts, lang=lang)

@app.route("/about")
def about():
    texts, lang = Traduccion.get_texts(request.args.get("lang", "es"))
    return render_template("about.html", texts=texts, lang=lang)

@app.route("/contact")
def contact():
    texts, lang = Traduccion.get_texts(request.args.get("lang", "es"))
    return render_template("contact.html", texts=texts, lang=lang)

@app.route("/perfil")
def perfil():
    texts, lang = Traduccion.get_texts(request.args.get("lang", "es"))
    return render_template("perfil.html", texts=texts, lang=lang)

@app.route("/settings")
def settings():
    texts, lang = Traduccion.get_texts(request.args.get("lang", "es"))
    return render_template("settings.html", texts=texts, lang=lang)

@app.route("/logout")
def logout():
    session.clear()
    flash("Sesión cerrada correctamente")
    return redirect(url_for("login"))

@app.route("/set_language/<lang>")
def set_language(lang):
    return redirect(url_for("login", lang=lang))

@app.route("/login", methods=["GET", "POST"])
def login():
    texts, lang = Traduccion.get_texts(request.args.get("lang", "es"))
    if request.method == "POST":
        user_input = request.form["user"]
        password = request.form["password"]

        cursor = db.get_cursor(dict_cursor=True)
        cursor.execute("SELECT * FROM tbl_usuarios WHERE usuario = %s", [user_input])
        user = cursor.fetchone()
        cursor.close()

        if user and bcrypt.checkpw(password.encode('utf-8'), user['contrasena'].encode('utf-8')):
            session["usuario"] = user["usuario"]
            session["id_persona"] = user.get("id_persona")
            flash("Bienvenido, " + user["usuario"])
            return redirect(url_for("menu_principal", lang=lang))
        else:
            flash("Usuario o contraseña incorrectos")
    return render_template("login.html", texts=texts, lang=lang)


@app.route("/registro", methods=["GET", "POST"])
def registro():
    texts, lang = Traduccion.get_texts(request.args.get("lang", "es"))
    current_date = datetime.today().strftime('%Y-%m-%d')

    if request.method == "POST":
        primer_nombre = request.form["primer_nombre"]
        segundo_nombre = request.form.get("segundo_nombre", "")
        primer_apellido = request.form["primer_apellido"]
        segundo_apellido = request.form.get("segundo_apellido", "")
        fecha_nacimiento = request.form["fecha_nacimiento"]
        genero = request.form["genero"]
        id_rol = request.form["id_rol"]
        direccion = request.form.get("direccion", "")
        telefono = request.form.get("telefono", "")
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]
        id_localidad = request.form.get("id_localidad", "LOC001")

        if password != confirm_password:
            flash("Las contraseñas no coinciden", "danger")
            return render_template("register.html", texts=texts, lang=lang, current_date=current_date)

        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        try:
            # --- Insertar en tbl_persona ---
            cursor = db.get_cursor(dict_cursor=False)
            cursor.callproc("sp_insertar_tbl_persona", (primer_nombre, primer_apellido, fecha_nacimiento))
            id_persona = cursor.fetchone()[0]
            cursor.close()

            # --- Insertar en tbl_adicional_persona ---
            cursor = db.get_cursor(dict_cursor=False)
            cursor.callproc("sp_insertar_tbl_adicional_persona", (
                direccion, telefono, email, id_persona, int(id_rol), int(genero), id_localidad
            ))
            cursor.fetchone()
            cursor.close()

            # --- Insertar en tbl_usuarios ---
            cursor = db.get_cursor(dict_cursor=False)
            cursor.callproc("sp_insertar_tbl_usuarios", (username, hashed.decode('utf-8'), id_persona))
            cursor.fetchone()
            cursor.close()

            db.mysql.connection.commit()
            flash(f"Usuario registrado correctamente: {username}", "success")
            return redirect(url_for("login", lang=lang))

        except Exception as e:
            print("[ERROR] al registrar usuario:", e)
            flash(f"Error al registrar usuario: {e}", "danger")
            try:
                db.mysql.connection.rollback()
            except:
                pass

    return render_template("register.html", texts=texts, lang=lang, current_date=current_date)


@app.route("/impactos_ambientales")
def impactos_ambientales():
    return render_template("modales/impactos_ambientales.html")


@app.route("/actualizar_perfil", methods=["POST"])
def actualizar_perfil():
    flash("Perfil actualizado correctamente", "success")
    return redirect(url_for("menu_principal"))


@app.route("/menu_principal")
def menu_principal():
    texts, lang = Traduccion.get_texts(request.args.get("lang", "es"))
    return render_template("menu_principal.html", texts=texts, lang=lang)


@app.route('/dashboard_admin')
def dashboard_admin():
    texts, lang = Traduccion.get_texts(request.args.get("lang", "es"))
    return render_template('dashboard_admin.html', texts=texts, lang=lang)


@app.route('/dashboard_autoridad_prueba')
def dashboard_autoridad_prueba():
    texts, lang = Traduccion.get_texts(request.args.get("lang", "es"))
    return render_template('dashboard_autoridad.html', texts=texts, lang=lang)


@app.route('/modal_ver_reportes')
def modal_ver_reportes():
    dashboard = request.args.get('dashboard', 'dashboard_admin')  
    lang = request.args.get('lang', 'es')
    texts, lang = Traduccion.get_texts(lang)

    cursor = db.get_cursor(dict_cursor=True)
    cursor.callproc('sp_mostrar_tbl_tickets')
    tickets = cursor.fetchall()
    cursor.close()
    return render_template('modales/modal_ver_reportes.html', tickets=tickets, texts=texts, lang=lang, dashboard=dashboard)


@app.route("/registro_reporte", methods=["GET", "POST"])
def registro_reporte():
    lang = request.args.get("lang", "es")
    texts, lang = Traduccion.get_texts(lang)
    localidades, barrios, categorias, impactos = [], [], [], []

    try:
        cursor = db.get_cursor(dict_cursor=True)
        cursor.callproc('sp_mostrar_tbl_localidades')
        localidades = cursor.fetchall()
        cursor.close()

        cursor = db.get_cursor(dict_cursor=True)
        cursor.callproc('sp_mostrar_tbl_barrio', [None])
        barrios = cursor.fetchall()
        cursor.close()

        cursor = db.get_cursor(dict_cursor=True)
        cursor.callproc('sp_mostrar_tbl_categoria_ambiental')
        categorias = cursor.fetchall()
        cursor.close()

        cursor = db.get_cursor(dict_cursor=True)
        cursor.callproc('sp_mostrar_tbl_impacto_ambiental')
        impactos = cursor.fetchall()
        cursor.close()
    except Exception as e:
        print("[ERROR] al cargar datos:", e)
        flash("Error al cargar los datos del formulario", "danger")

    if request.method == "POST":
        descripcion = request.form.get("descripcion", "").strip()
        id_categoria = request.form.get("id_categoria")
        id_estado = "EST002"
        id_localidad = request.form.get("id_localidad")
        id_impacto = request.form.get("id_impacto")
        id_barrio = request.form.get("id_barrio")
        id_severidad = None
        id_persona = session.get("id_persona")

        if not id_persona:
            flash("Usuario no autenticado.", "danger")
            return render_template(
                "modales/registro_reporte.html",
                texts=texts,
                lang=lang,
                localidades=localidades,
                barrios=barrios,
                categorias=categorias,
                impactos=impactos
            )

        evidencia = None
        if "evidencia" in request.files and request.files["evidencia"].filename != "":
            evidencia = bytearray(request.files["evidencia"].read())

        try:
            cursor = db.get_cursor(dict_cursor=False)
            ticket_out = 0

            cursor.callproc("sp_insertar_tbl_tickets", (
                descripcion, datetime.now(), id_categoria, id_severidad,
                id_estado, id_localidad, id_impacto, id_barrio, id_persona, evidencia,
                ticket_out
            ))

            # Recuperar el OUT
            cursor.execute("SELECT @_sp_insertar_tbl_tickets_10")
            ticket_id = cursor.fetchone()[0]

            cursor.close()
            db.mysql.connection.commit()
            flash(f"Reporte registrado correctamente. ID: {ticket_id}", "success")

        except Exception as e:
            print("[ERROR] al registrar reporte:", e)
            try:
                db.mysql.connection.rollback()
            except:
                pass
            flash(f"Error al registrar el reporte: {e}", "danger")

    return render_template(
        "modales/registro_reporte.html",
        texts=texts,
        lang=lang,
        localidades=localidades,
        barrios=barrios,
        categorias=categorias,
        impactos=impactos
    )



if __name__ == "__main__":
    app.run(debug=True, port=5000)