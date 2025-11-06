from flask import Flask, request, render_template, redirect, url_for

# Para inicar nossa aplicação iremos 
# chamar o frameWork Flask

app = Flask(__name__)

lista_produtos = [
    {"id":1, "nome":"Pão","tipo":"Padaria","preco":13.99},
    {"id":2,"nome":"Leite","tipo":"Alimento","preco":6.00},
    {"id":3,"nome":"Presunto","tipo":"Frios","preco":60.00}
]

@app.route("/pagina")
def pagina():
    return render_template("index.html",produtos =lista_produtos)

app.run(debug=True)