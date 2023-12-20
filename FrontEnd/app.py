from flask import Flask, redirect, url_for, render_template, request, flash
import requests
from flask_cors import CORS

app = Flask(__name__)
link = "192.168.137.234:3000"
app.secret_key = "appKey"
CORS(app)

@app.route('/')
def index():

    return render_template("index.html")


@app.route('/categorias')
def categorias():
    try:
        response = requests.get(f'http://{link}/categoria')
        if response.status_code == 200:
            categorias = response.json()
            return render_template("categorias.html", categorias=categorias)
        else:
            return "Error al obtener los categorias"
    except:
        return "Error al obtener los categorias"



@app.route('/productos')
def productos():
    try:
        response = requests.get(f'http://{link}/productos')
        if response.status_code == 200:
            productos = response.json()
            return render_template("productos.html", productos=productos)
        else:
            return "Error al obtener los productos"
    except:
        return "Error al obtener los productos"



@app.route('/movimientos')
def movimientos():
    try:
        response = requests.get(f'http://{link}/movimiento_inventarios')
        if response.status_code == 200:
            movimientos = response.json()
            for movimiento in movimientos:
                producto_name = get_product_name(movimiento['producto_id'])
                movimiento['producto_name'] = producto_name
            return render_template("movimientos.html", movimientos=movimientos)
        else:
            return "Error al obtener los productos"
    except:
        return "Error al obtener los productos"


@app.route('/prodcutos_categorias')
def prodcutos_categorias():
    try:
        response = requests.get(f'http://{link}/productos_categoria')
        if response.status_code == 200:
            procats = response.json()
            for procat in procats:
                producto_name = get_product_name(procat['producto_id'])
                categoria_name = get_categoria_name(procat['categoria_id'])
                procat['producto_name'] = producto_name
                procat['categoria_name'] = categoria_name
            return render_template("productos_categoria.html", procats=procats)
        else:
            return "Error al procesar"
    except:
        return "Error al procesar"



#################### Otras rutas ###################

@app.route('/inCategoria')
def inCategoria():

    return render_template("insertCategoria.html")


@app.route('/inC', methods=["POST"])
def inC():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        categoria_data = {
            "categoria": {  # Agrega el nivel de anidación "categoria"
                "nombre": nombre,
            }
        }
        try:
            response = requests.post(f"http://{link}/categoria", json=categoria_data)
            if response.status_code == 201:
                # Categoría creada exitosamente
                flash("Categoría creada con éxito!")
                return redirect(url_for("categorias"))
            else:
                error_message = response.json().get("error", "Error desconocido")
                flash("Error al crear la categoría: {}".format(error_message))
                return redirect(url_for("inCategoria"))
        except requests.HTTPError as e:
            flash("Error al crear la categoría: {}".format(e.response.text))
            return redirect(url_for("inCategoria"))
        except Exception as e:
            flash("Error al crear la categoría: {}".format(e))
            return redirect(url_for("inCategoria"))


@app.route("/actualizarcat/<int:id>")
def actualizarcat(id):
    try:
        response = requests.get(f'http://{link}/categoria/{id}')
        if response.status_code == 200:
            categoria = response.json()
            return render_template("actualizarCategoria.html", categoria = categoria)
        else:
            return "Error al obtener los productos"
    except:
        return "Error al obtener los productos"


##actualizar
@app.route('/actualizarcat/<int:id>', methods=["GET", "POST"])
def update_categoria(id):
    if request.method == "POST":
        nombre = request.form.get("nombre")
        categoria_data = {
            "categoria": {
                "nombre": nombre,
            }
        }
        try:
            response = requests.put(f"http://{link}/categoria/{id}", json=categoria_data)
            if response.status_code == 200:
                # Categoría actualizada exitosamente
                flash("Categoría actualizada con éxito!")
                return redirect(url_for("categorias"))
            else:
                # Error al actualizar la categoría
                error_message = response.json().get("error", "Error desconocido")
                flash("Error al actualizar la categoría: {}".format(error_message))
                return redirect(url_for("categorias"))
        except requests.HTTPError as e:
            # Error de la API
            flash("Error al actualizar la categoría: {}".format(e.response.text))
            return redirect(url_for("categorias"))
        except Exception as e:
            # Error de conexión o inesperado
            flash("Error al actualizar la categoría: {}".format(e))
            return redirect(url_for("categorias"))


@app.route("/eliminarCategoria/<int:id>", methods=["GET", "POST"])
def eliminarCategoria(id):
    try:
        response = requests.delete(f"http://{link}/categoria/{id}")

        if response.status_code == 204:
            flash("Categoría eliminada con éxito!")
        elif response.status_code == 404:
            flash("La categoría no existe")
        else:
            flash(f"Error al eliminar la categoría: código {response.status_code}")

    except requests.RequestException as e:
        flash(f"Error al eliminar la categoría: {e}")

    return redirect(url_for("categorias"))


@app.route("/inProductos")
def inProductos():

    return render_template("insertProductos.html")

@app.route("/inP", methods=["POST"])
def inP():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        stock = request.form.get("stock")
        precio = request.form.get("precio")
        producto_data = {
            "productos": {  # Agrega el nivel de anidación "categoria"
                "nombre": nombre,
                "stock": stock,
                "precio": precio,
            }
        }
        try:
            response = requests.post(f"http://{link}/productos", json=producto_data)
            if response.status_code == 201:
                # Categoría creada exitosamente
                flash("Producto creada con éxito!")
                return redirect(url_for("productos"))
            else:
                error_message = response.json().get("error", "Error desconocido")
                flash("Error al crear el producto: {}".format(error_message))
                return redirect(url_for("inProductos"))
        except requests.HTTPError as e:
            flash("Error al crear el producto: {}".format(e.response.text))
            return redirect(url_for("inProductos"))
        except Exception as e:
            flash("Error al crear el producto: {}".format(e))
            return redirect(url_for("inProductos"))

@app.route("/inMovimientos")
def inMovimientos():
    response = requests.get(f'http://{link}/movimiento_inventarios')
    movimientos = response.json()
    for movimiento in movimientos:
        producto_name = get_product_name(movimiento['producto_id'])
        movimiento['producto_name'] = producto_name
    return render_template("insertMovimientos.html", movimientos=movimientos)


@app.route("/inM", methods=["POST"])
def inM():

    if request.method == "POST":

        producto_id = request.form["producto_id"]
        cantidad = request.form["cantidad"]
        fecha_movimiento = request.form["fecha_movimiento"]
        tipo_movimiento = request.form["tipo_movimiento"]
        movimiento_data = {
            "movimiento_inventarios": {  # Agrega el nivel de anidación "categoria"
            "producto_id": producto_id,
            "cantidad": cantidad,
            "fecha_movimiento": fecha_movimiento,
            "tipo_movimiento": tipo_movimiento
            }
        }
        print("Movimiento Data:", movimiento_data)
        try:
            response = requests.post(f"http://{link}/movimiento_inventarios", json=movimiento_data)
            if response.status_code == 201:
                # Categoría creada exitosamente
                flash("Producto creada con éxito!")
                return redirect(url_for("movimientos"))
            else:
                error_message = response.json().get("error", "Error desconocido")
                flash("Error al crear el producto: {}".format(error_message))
                return redirect(url_for("inMovimientos"))
        except requests.HTTPError as e:
            flash("Error al crear el producto: {}".format(e.response.text))
            return redirect(url_for("inMOvimientos"))
        except Exception as e:
            flash("Error al crear el producto: {}".format(e))
            return redirect(url_for("inMOvimientos"))







def get_product_name(product_id):
    response = requests.get('http://'+link+'/productos/{}'.format(product_id))
    if response.status_code == 200:
        producto = response.json()
        return producto['nombre']
    else:
        return None

def get_categoria_name(cat_id):
    response = requests.get('http://'+link+'/categoria/{}'.format(cat_id))
    if response.status_code == 200:
        categoria = response.json()
        return categoria['nombre']
    else:
        return None


if __name__ == '__main__':
    url = 'http://127.0.0.1:3000'
    CORS(app,origins=[url])
    app.run(host='127.0.0.1', port=9696)

