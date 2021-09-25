from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('validar_primo.html', mensagem='Digite um número no \
                           campo abaixo e clique em verificar')


@app.route('/verificar/', methods=['POST'])
def verificar():
    numero = int(request.form['numero'])
    lista_primos = []
    lista_div = []
    lista_primos2 = []
    for i in range(2, numero + 1):
        for x in range(1, i + 1):
            if i >= x:
                if i % x == 0:
                    lista_div.append(x)
        if len(lista_div) == 2:
            lista_primos.append(i)
        lista_div = []
    for n in lista_primos:
        lista_primos2.append(str(n))
    string = ", ".join(lista_primos2)
    return render_template('validar_primo.html',
                           mensagem='Digite um número no campo abaixo e\
                           clique em verificar', numero=lista_primos,
                           retorno='Os números primos até o número ' +
                           str(numero) + ' são: ' + string)


if __name__ == '__main__':
    app.run(debug=True)
