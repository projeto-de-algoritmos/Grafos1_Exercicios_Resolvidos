from cgitb import html
from flask import Flask, render_template, request, flash, redirect, url_for

adj_list = {
    "1": ["2", "7", "8"],
    "2": ["7", "1", "8"],
    "3": ["7"],
    "4": ["6", "8"],
    "5": ["5", "10"],
    "6": ["4", "5"],
    "7": ["1", "3", "4"],
    "8": ["1", "4", "9"],
    "9": ["8"],
    "10": ["5"],

}

app = Flask(__name__)  # sempre ao iniciar um site


# criar a primeira página do site
# route -> caminho que vem depois do dominio

# funcao -> o que quero exibir naquela página
# template


@app.route('/', methods=['GET', 'POST'])
def homepage():
    no = "1"
    if request.method == "GET":
        return render_template("homepage.html", no=no)

    else:

        palpite = str(request.form.get("name"))

        if (palpite in adj_list[no]):
            no = palpite
            return redirect(url_for('caminho', no_destino=no))
        else:
            return redirect(url_for('errou'))


@app.route('/caminho/<no_destino>', methods=['GET', 'POST'])
def caminho(no_destino):
    no = no_destino

    if request.method == "GET":
        return render_template("caminho.html", no=no)

    else:
        palpite = str(request.form.get("name"))
        if (palpite == "10" and palpite in adj_list[no]):
            return redirect(url_for('vitoria'))
        if (palpite in adj_list[no]):
            no = palpite
            return redirect(url_for('caminho', no_destino=no))
        else:
            return redirect(url_for('errou'))


@app.route('/errou', methods=['GET', 'POST'])
def errou():
    return render_template("errou.html")


@app.route('/vitoria', methods=['GET', 'POST'])
def vitoria():
    return render_template("vitoria.html")


# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
