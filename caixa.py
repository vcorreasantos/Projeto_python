import sys

import webbrowser
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QVBoxLayout, QHBoxLayout, QLineEdit, QTableWidget, QTableWidgetItem , QMessageBox, QInputDialog 

class caixa(QWidget):
    def __init__(self):
        super().__init__()

        self.total = 0.0
        self.linha = 0

        self.setGeometry(50,50,1200,800)

        # criar os elementos que irão para a coluna da esquerda 
        # criar uma label para adicionar uma imagem
        # e depois adicionar a coluna da esquerda

        self.setWindowTitle("Caixa da Padaria")
        self.setGeometry(50,50,1200,800)
        self.setFixedSize(1200,800)

        self.setWindowIcon(QIcon(".venv/paozinho.png"))

        # ------------------ imagem ---------------------------
        self.imagem_label = QLabel()
        self.imagem_label.setPixmap(QPixmap(".venv/coffe.jpg"))
        self.imagem_label.setScaledContents(True)
        self.imagem_label.setFixedSize(600,300)
        # ----------------- fim da imagem ----------------------

        # ------------------ codigo ------------------------------
        self.codigo_produto_label = QLabel("Código do Produto:")
        self.codigo_produto_label.setStyleSheet("QLabel{font-size:15pt}")

        self.codigo_produto_edit = QLineEdit()
        self.codigo_produto_edit.setStyleSheet("QLineEdit{font-size:15pt}")
        # ------------------- fim do codigo ---------------------------
       
        # ------------------- nome --------------------------------------
        self.nome_produto_label = QLabel("Nome do Produto:")
        self.nome_produto_label.setStyleSheet("QLabel{font-size:15pt}")

        self.nome_produto_edit = QLineEdit()
        self.nome_produto_edit.setStyleSheet("QLineEdit{font-size:15pt}")
        # ------------------- fim do nome ---------------------------------

        # ------------------ Descricao do produto ------------------------
        self.descricao_produto_label = QLabel("Descrição do Produto:")
        self.descricao_produto_label.setStyleSheet("QLabel{font-size:15pt}")

        self.descricao_produto_edit = QLineEdit()
        self.descricao_produto_edit.setStyleSheet("QLineEdit{font-size:15pt}")
        # ------------------- fim da descricao ----------------------------

        # ----------------------- quantidade -----------------------------
        self.quantidade_produto_label = QLabel("Quantidade do Produto:")
        self.quantidade_produto_label.setStyleSheet("QLabel{font-size:15pt}")

        self.quantidade_produto_edit = QLineEdit()
        self.quantidade_produto_edit.setStyleSheet("QLineEdit{font-size:15pt}")
        # -------------------------- fim da quantidade ---------------------

        # ---------------------------- Preco -----------------------------------
        self.preco_produto_label = QLabel("Preço Unitário do Produto:")
        self.preco_produto_label.setStyleSheet("QLabel{font-size:15pt}")

        self.preco_produto_edit = QLineEdit()
        self.preco_produto_edit.setStyleSheet("QLineEdit{font-size:15pt}")
        # ---------------------------- fim do preco -----------------------------

        # ---------------------------- sub total ---------------------------------------
        self.subtotal_produto_label = QLabel("Sub-Total:")
        self.subtotal_produto_label.setStyleSheet("QLabel{font-size:15pt}")

        self.subtotal_produto_edit = QLineEdit("Tecle F2 para salvar")
        self.subtotal_produto_edit.setStyleSheet("QLineEdit{font-size:15pt; width: 400}")
        self.subtotal_produto_edit.setEnabled(False)
        # ---------------------------- fim do sub total ------------------------------
        
        

        
        # Adiocionar os elementos que ficarão ao lado esquerdo a um layout 
        # vertical que será aplicado na coluna da esquerda
        self.vetical_esquerda_layout = QVBoxLayout()
        self.vetical_esquerda_layout.addWidget(self.imagem_label)
        self.vetical_esquerda_layout.addWidget(self.codigo_produto_label)
        self.vetical_esquerda_layout.addWidget(self.codigo_produto_edit)
        self.vetical_esquerda_layout.addWidget(self.nome_produto_label)
        self.vetical_esquerda_layout.addWidget(self.nome_produto_edit)
        self.vetical_esquerda_layout.addWidget(self.descricao_produto_label)
        self.vetical_esquerda_layout.addWidget(self.descricao_produto_edit)
        self.vetical_esquerda_layout.addWidget(self.quantidade_produto_label)
        self.vetical_esquerda_layout.addWidget(self.quantidade_produto_edit)
        self.vetical_esquerda_layout.addWidget(self.preco_produto_label)
        self.vetical_esquerda_layout.addWidget(self.preco_produto_edit)
        self.vetical_esquerda_layout.addWidget(self.subtotal_produto_label)
        self.vetical_esquerda_layout.addWidget(self.subtotal_produto_edit)
        # ----------------------------- fim -------------------------------

        # ======================= Tabela ===============================
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(5)
        self.tabela.setRowCount(10)
        colunas = ["Código","Nome do produto", "Quantidade","Preço Unitário","Preço Total"]

        self.tabela.setHorizontalHeaderLabels(colunas)
        self.tabela.setStyleSheet("QTableWidget{backgroud:red}")

        self.vertical_direita_layout = QVBoxLayout()
        self.vertical_direita_layout.addWidget(self.tabela)
        # ===============================================================

        self.total_label= QLabel("Total a pagar:")
        self.total_label.setStyleSheet("Qlabel{font-size:20pt}")

        self.total_edit = QLineEdit()
        self.total_edit.setStyleSheet("QLineEdit{font-size:20pt}")
        self.vertical_direita_layout.addWidget(self.total_label)
        self.vertical_direita_layout.addWidget(self.total_edit)



        
        self.coluna_esquerda_label = QLabel()
        self.coluna_esquerda_label.setStyleSheet("QLabel{background-color:#F6CFFA}")

        # Adicionar o layout da esquerda á coluna da esquerda
        self.coluna_esquerda_label.setLayout(self.vetical_esquerda_layout)


        self.coluna_direita_label = QLabel()
        self.coluna_direita_label.setStyleSheet("QLabel{background-color:#F5CFFA}")
        self.coluna_direita_label.setFixedSize(600,800)
        
        self.coluna_direita_label.setLayout(self.vertical_direita_layout)
        
        self.horizontal_layout = QHBoxLayout()
        # Adicionar a coluna da esquerda no layout horizontal
        self.horizontal_layout.addWidget(self.coluna_esquerda_label)
        # Adicionar a coluna da direita no layout horizontal
        self.horizontal_layout.addWidget(self.coluna_direita_label)
        # Adicionar o layout horizoltal na tela
        self.setLayout(self.horizontal_layout)


        self.keyPressEvent = self.capturaTecla
    def capturaTecla(self, e):
        if(e.key()==Qt.Key_F2):
            # print(self.quantidade_produto_edit.text())
            # print(self.preco_produto_edit.text())
            print(float(self.quantidade_produto_edit.text()) * float(self.preco_produto_edit.text()))
            self.subtotal_produto_edit.setText(str(float(self.quantidade_produto_edit.text()) * float(self.preco_produto_edit.text())))

        elif(e.key()==Qt.Key_F3):
            print(self.codigo_produto_edit.text())
            self.tabela.setItem(self.linha,0,QTableWidgetItem(self.codigo_produto_edit.text()))
            self.tabela.setItem(self.linha,1,QTableWidgetItem(self.nome_produto_edit.text()))
            self.tabela.setItem(self.linha,2,QTableWidgetItem(self.quantidade_produto_edit.text()))
            self.tabela.setItem(self.linha,3,QTableWidgetItem(self.preco_produto_edit.text()))
            self.tabela.setItem(self.linha,4,QTableWidgetItem(self.subtotal_produto_edit.text()))

            self.linha = self.linha + 1
            self.total = self.total + float(self.subtotal_produto_edit.text())

            self.total_edit.setText(str(self.total))
           
        elif(e.key()==Qt.Key_F4):
            op = QMessageBox.question(self,"Pagemento", "Deseja efetuar o pagamento?")
            if op == QMessageBox.Yes:
                rs,ok = QInputDialog().getText(self,"Forma de pagamento","Escolha uma forma de pagamento:\n1- Pix\n2- Cartão de Crédito\n3- Cartão de Débito\n4- Dinheiro\n5- Voucher")
                if ok :
                   # Vamos criar uma lista (array) 
                   # para guardar todos os dados 
                   # da tabela para criar uma nota fiscal
                    dados = []
                    for linha in range(self.tabela.rowCount()):
                        dados_linha = []
                        for coluna in range(self.tabela.columnCount()):
                            item = self.tabela.item(linha,coluna)
                            if item:
                                dados_linha.append(item.text())
                            else:
                                break
                                #  dados_linha.append("")
                                dados.append(dados_linha)
                    nota = """
                                <html>
                                <head>
                                <title> Nota Fiscal </title>
                                <style>
                                    body{
                                    text-align:center
                                    }
                                    table{
                                    margin-left:auto;
                                    margin-right:auto;
                                    border:2px solid blue
                                    }
                                </style>
                                </head>
                                <body>
                                <h1> Nota Fiscal de Compras </h1>
                                <table>
                                <tr>
                                    <th>Cód.</th>
                                    <th>Descrição</th>
                                    <th>Qtd.</th>
                                    <th>Preço</th>
                                    <th>Preço Total</th>
                                </tr>
                                """
                    for lin in dados:
                        nota = nota + "<tr>"
                        for col in lin: 
                            nota = nota + "<td>"+col+"</td>"
                        nota = nota + "</tr>"
                    nota = nota + """
                                </table>
                                </body>
                                </html>
                          """
                    arq = open("nota.html","w")
                    arq.write(nota)
                    arq.close()
                    webbrowser.open("nota.html")


            else:
             print("")
            


app = QApplication(sys.argv)
janela = caixa()
janela.show()
app.exec_()

        
