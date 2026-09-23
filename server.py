from flask import Flask, redirect, render_template, request, url_for

from estudiante import Estudiante


app = Flask(__name__)


@app.route("/")
def inicio():
    return redirect(url_for("estudiantes"))


@app.route("/estudiantes")
def estudiantes():
    return render_template("estudiantes.html", estudiantes=Estudiante.get_all())


@app.route("/estudiantes/ver/<int:id_estudiante>")
def ver_estudiante(id_estudiante):
    estudiante = Estudiante.get_by_id(id_estudiante)
    if estudiante is None:
        return "Estudiante no encontrado", 404
    return render_template("estudiante_ver.html", estudiante=estudiante)


@app.route("/estudiantes/editar/<int:id_estudiante>")
def editar_estudiante(id_estudiante):
    estudiante = Estudiante.get_by_id(id_estudiante)
    if estudiante is None:
        return "Estudiante no encontrado", 404
    return render_template("estudiante_editar.html", estudiante=estudiante)


@app.route("/actualizar_estudiante", methods=["POST"])
def actualizar_estudiante():
    try:
        id_estudiante = int(request.form["id_estudiante"])
    except (KeyError, TypeError, ValueError):
        return "ID de estudiante invalido", 400

    nombre = request.form.get("nombre", "").strip()
    email = request.form.get("email", "").strip()
    estudiante = Estudiante.get_by_id(id_estudiante)

    if estudiante is None:
        return "Estudiante no encontrado", 404

    if not nombre or not email:
        return render_template(
            "estudiante_editar.html",
            estudiante=estudiante,
            error="Todos los campos son obligatorios.",
        ), 400

    resultado = Estudiante.actualizar(
        {"id_estudiante": id_estudiante, "nombre": nombre, "email": email}
    )
    if resultado is False:
        return render_template(
            "estudiante_editar.html",
            estudiante=estudiante,
            error="No fue posible actualizar el estudiante.",
        ), 500

    return redirect(url_for("estudiantes"))


@app.route("/eliminar_estudiante/<int:id_estudiante>")
def eliminar_estudiante(id_estudiante):
    resultado = Estudiante.eliminar({"id_estudiante": id_estudiante})
    if resultado is False:
        return "No fue posible eliminar el estudiante.", 500
    return redirect(url_for("estudiantes"))


if __name__ == "__main__":
    app.run(debug=True)
