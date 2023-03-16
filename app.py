from flask import Flask, request

from controllers import analisar_notas_do_aluno

app = Flask(__name__)


@app.route("/")
def main():
    primeira_nota = request.args.get("primeira")
    segunda_nota = request.args.get("segunda")

    resultado_da_media = analisar_notas_do_aluno(
        primeira_nota=float(primeira_nota),
        segunda_nota=float(segunda_nota)
    )
    return f"{primeira_nota} + {segunda_nota} = {resultado_da_media}"


if __name__ == "__main__":
    app.run(debug=True)
