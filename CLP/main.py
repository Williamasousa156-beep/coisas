from flask import Flask, render_template, request

mensagens_do_dia = []

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    mensagem = None
    if request.method == 'POST':
        mensagem = request.form['message']
        mensagens_do_dia.append(mensagem)

    return render_template ('index.html', msg = mensagens_do_dia)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)