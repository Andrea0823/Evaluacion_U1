from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
db_path = "bd.sqlite3"

@app.route('/')
def index():
    # Crear una nueva conexión y un cursor
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Ejecutar la consulta
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    cursor.execute("SELECT * FROM tablas")
    tablas = cursor.fetchall()

    cursor.execute("SELECT * FROM privilegios")
    privilegios = cursor.fetchall()

    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()

    return render_template("index.html", data={'usuarios': usuarios, 'privilegios':privilegios, 'tablas':tablas, 'v':'F'})

@app.route('/usuarios')
def usuarios():
    # Crear una nueva conexión y un cursor
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Ejecutar la consulta
    cursor.execute("SELECT * FROM usuarios")
    resultados = cursor.fetchall()

    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()

    data = {'results': resultados}
    return render_template("usuarios/usuarios.html", data=data)



@app.route('/insertar_usuario', methods=['POST'])
def insertar_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['password']
        rol = request.form['rol']
        status = request.form['status']

        # Crear una nueva conexión y un cursor
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Ejecutar la inserción
        cursor.execute("INSERT INTO usuarios(nombre, password, rol, status ) VALUES (?, ?, ?, ?)", (nombre, password, rol, status))
        conn.commit()

        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()

        # Redireccionar a la página de usuarios
        return redirect(url_for('usuarios'))


@app.route('/modificar_usuario', methods=['POST'])
def modificar_usuario():
    if request.method == 'POST':
        id_usuario = request.form['id']
        nombre = request.form['nombre']
        password = request.form['password']
        rol = request.form['rol']
        status = request.form['status']

        # Crear una nueva conexión y un cursor
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Ejecutar la actualización
        cursor.execute("UPDATE usuarios SET nombre=?, password=?, rol=?, status=? WHERE id_usuario=?", (nombre, password, rol, status, id_usuario))
        conn.commit()

        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()

        # Redireccionar a la página de usuarios
        return redirect(url_for('usuarios'))


@app.route('/consultar_usuario',  methods=['POST'])
def consultar_usuario():
    if request.method == 'POST':
        id_usuario = request.form['id']

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Ejecutar la consulta
        cursor.execute("SELECT * FROM usuarios WHERE id_usuario=?", (id_usuario))
        resultados = cursor.fetchall()

        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()

        data = {'results': resultados}
        return render_template("usuarios/usuarios.html", data=data)


@app.route('/eliminar_usuario',  methods=['POST'])
def eliminar_usuario():
    if request.method == 'POST':
        id_usuario = request.form['id']
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id_usuario=?", (id_usuario,))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('usuarios'))


@app.route('/privilegios')
def privilegios():
    # Crear una nueva conexión y un cursor
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Ejecutar la consulta
    cursor.execute("SELECT * FROM privilegios")
    resultados = cursor.fetchall()

    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()

    data = {'results': resultados}
    return render_template("privilegios/privilegios.html", data=data)

@app.route('/insertar_privilegios', methods=['POST'])
def insertar_privilegios():
    if request.method == 'POST':
        privilegio = request.form['privilegios']
        descripcion = request.form['descripcion']

        # Crear una nueva conexión y un cursor
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Ejecutar la inserción
        cursor.execute("INSERT INTO privilegios(privilegio, descripcion ) VALUES (?, ?)", (privilegio, descripcion))
        conn.commit()

        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()

        # Redireccionar a la página de privilegios
        return redirect(url_for('privilegios'))

@app.route('/modificar_privilegios', methods=['POST'])
def modificar_privilegios():
    if request.method == 'POST':
        id_privilegio = request.form['id']
        privilegio = request.form['privilegios']
        descripcion = request.form['descripcion']

        # Crear una nueva conexión y un cursor
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Ejecutar la actualización
        cursor.execute("UPDATE privilegios SET privilegio=?, descripcion=? WHERE id_privilegio=?", (privilegio, descripcion, id_privilegio))
        conn.commit()

        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()

        # Redireccionar a la página de usuarios
        return redirect(url_for('privilegios'))

@app.route('/consultar_privilegios',  methods=['POST'])
def consultar_privilegios():
    if request.method == 'POST':
        id_privilegio = request.form['id']

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Ejecutar la consulta
        cursor.execute("SELECT * FROM privilegios WHERE id_privilegio=?", (id_privilegio))
        resultados = cursor.fetchall()

        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()

        data = {'results': resultados}
        return render_template("privilegios/privilegios.html", data=data)

@app.route('/eliminar_privilegios',  methods=['POST'])
def eliminar_privilegios():
    if request.method == 'POST':
        id_privilegio = request.form['id']
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM privilegios WHERE id_privilegio=?", (id_privilegio,))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('privilegios'))

@app.route('/tablas')
def tablas():
    # Crear una nueva conexión y un cursor
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Ejecutar la consulta
    cursor.execute("SELECT * FROM tablas")
    resultados = cursor.fetchall()

    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()

    data = {'results': resultados}
    return render_template("tablas/tablas.html", data=data)

@app.route('/insertar_tablas', methods=['POST'])
def insertar_tablas():
    if request.method == 'POST':
        tabla = request.form['tablas']
        descripcion = request.form['descripcion']

        # Crear una nueva conexión y un cursor
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Ejecutar la inserción
        cursor.execute("INSERT INTO tablas(tabla, descripcion ) VALUES (?, ?)", (tabla, descripcion))
        conn.commit()

        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()

        # Redireccionar a la página de tablas
        return redirect(url_for('tablas'))

@app.route('/modificar_tablas', methods=['POST'])
def modificar_tablas():
    if request.method == 'POST':
        id_tabla = request.form['id']
        tabla = request.form['tablas']
        descripcion = request.form['descripcion']

        # Crear una nueva conexión y un cursor
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Ejecutar la actualización
        cursor.execute("UPDATE tablas SET tabla=?, descripcion=? WHERE id_tabla=?", (tabla, descripcion, id_tabla))
        conn.commit()

        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()

        # Redireccionar a la página de usuarios
        return redirect(url_for('tablas'))

@app.route('/consultar_tablas',  methods=['POST'])
def consultar_tablas():
    if request.method == 'POST':
        id_tabla = request.form['id']

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Ejecutar la consulta
        cursor.execute("SELECT * FROM tablas WHERE id_tabla=?", (id_tabla))
        resultados = cursor.fetchall()

        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()

        data = {'results': resultados}
        return render_template("tablas/tablas.html", data=data)

@app.route('/eliminar_tablas',  methods=['POST'])
def eliminar_tablas():
    if request.method == 'POST':
        id_tabla = request.form['id']
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tablas WHERE id_tabla=?", (id_tabla,))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('tablas'))
    
@app.route('/productos')
def productos():
    # Crear una nueva conexión y un cursor
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Ejecutar la consulta
    cursor.execute("SELECT * FROM productos")
    resultados = cursor.fetchall()

    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()

    data = {'results': resultados}
    return render_template("productos/productos.html", data=data)
    
@app.route('/insertar_productos', methods=['POST'])
def insertar_productos():
    if request.method == 'POST':
        producto = request.form['productos']
        descripcion = request.form['descripcion']
        precio = request.form['precio']

        # Crear una nueva conexión y un cursor
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Ejecutar la inserción
        cursor.execute("INSERT INTO productos(producto, descripcion, precio ) VALUES (?, ?, ?)", (producto, descripcion, precio))
        conn.commit()

        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()

        # Redireccionar a la página de tablas
        return redirect(url_for('productos'))
    
@app.route('/modificar_productos', methods=['POST'])
def modificar_productos():
    if request.method == 'POST':
        id_producto = request.form['id']
        producto = request.form['productos']
        descripcion = request.form['descripcion']
        precio = request.form['precio']

        # Crear una nueva conexión y un cursor
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Ejecutar la actualización
        cursor.execute("UPDATE productos SET producto=?, descripcion=?, precio=? WHERE id_producto=?", (producto, descripcion, precio ,id_producto))
        conn.commit()

        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()

        # Redireccionar a la página de usuarios
        return redirect(url_for('productos'))

@app.route('/consultar_productos',  methods=['POST'])
def consultar_productos():
    if request.method == 'POST':
        id_producto = request.form['id']

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Ejecutar la consulta
        cursor.execute("SELECT * FROM productos WHERE id_producto=?", (id_producto))
        resultados = cursor.fetchall()

        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()

        data = {'results': resultados}
        return render_template("productos/productos.html", data=data)
    
@app.route('/eliminar_productos',  methods=['POST'])
def eliminar_productos():
    if request.method == 'POST':
        id_producto = request.form['id']
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE id_producto=?", (id_producto,))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('productos'))

@app.route('/asinar_privilegios',  methods=['POST'])
def asinar_privilegios():
    id_usuario = request.form['usuario']
    id_privilegio = request.form['privilegio']
    id_tabla = request.form['tabla']

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO usuarios_privilegios_tablas(id_usuario, id_privilegio, id_tabla) VALUES (?, ?, ?)", (id_usuario, id_privilegio, id_tabla))
    conn.commit()

    cursor.close()
    conn.close()

    # Redireccionar a la página de privilegios
    return redirect(url_for('index'))


@app.route('/consultasComandos',  methods=['POST'])
def consultasComandos():
    id_usuario = request.form['usuario']
    password = request.form['password']
    query = request.form['query']

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT id_usuario, password FROM usuarios WHERE id_usuario=? AND password=?", (id_usuario, password))
    resultado = cursor.fetchone()
    

    if resultado:
        
        id_usuario_encontrado = resultado[0]
        password_encontrada = resultado[1]

        # Validación y ejecución de la consulta
        consulta_sin_punto_y_coma = query.replace(";", "")
        consulta = query.split()

        if consulta[0].upper() == "SELECT":
            
            cursor.execute("SELECT id_tabla FROM tablas WHERE tabla=?", (consulta[-1].title().rstrip(';'),))
            tabla = cursor.fetchone()
            if tabla:
                id_tabla = tabla[0]
                
                cursor.execute("SELECT id_privilegio FROM privilegios WHERE privilegio=?", ("SELECT",))
                priv = cursor.fetchone()
                if priv:
                    id_priv = priv[0]
                    
                    cursor.execute("SELECT id_usuario, id_privilegio, id_tabla FROM usuarios_privilegios_tablas WHERE id_usuario=? AND id_privilegio=? and id_tabla=?", (id_usuario, id_priv, id_tabla))
                    resultado = cursor.fetchone()

                    if resultado:
                        print("se logro")
                        cursor.execute("SELECT * FROM usuarios")
                        usuarios = cursor.fetchall()
                        result = [usuarios]
                    else:
                        print("Sin permisos")
                        result = [{
                            'result': 'Sin permisos'
                        }]
                else:
                    print("No se encontró el privilegio.")
                    result = [{
                            'result': "No se encontró el privilegio."
                    }]
            else:
                print("No se encontró la tabla.")
                result = [{
                            'result': "No se encontró la tabla"
                        }]
        else:
            print("OTRO METODO")

    else:
        print("El usuario no existe.")
        result = [{
            'result': "El usuario no existe."
        }]

    return render_template("index.html", data=result)

if __name__ == "__main__":
    app.run(debug=True)


