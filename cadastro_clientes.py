import sys
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QVBoxLayout, QHBoxLayout, QPushButton

class CadastroClientes(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cadastro de Clientes")
        self.setGeometry(50,50,1000,800)
        self.setFixedSize(1200,800)

        self.setWindowIcon(QIcon(".venv/doce.png"))

        self.horizontal_layout = QHBoxLayout()
        self.esquerda_label = QLabel()
        self.esquerda_label.setPixmap(QPixmap(".venv/gatinho.jpg"))
        self.esquerda_label.setScaledContents(True)


        self.direita_label = QLabel()
        self.direita_label.setFixedWidth(600)
        self.direita_label.setStyleSheet("QLabel{background-color:#DB6BA1}")

        self.vertical_layout = QVBoxLayout()
        self.titulo_layout = QLabel("Cadatro de Clientes")
        self.titulo_layout.setStyleSheet("QLabel{font-family:Broadway;font-weight:bold;font-style:italic;font-size:20pt;color:#2C1621}")
        self.vertical_layout.addWidget(self.titulo_layout)
        # ------------------ Nome do Cliente ----------------------------------------
        self.nome_label = QLabel("Nome Completo:")
        self.nome_label.setStyleSheet("QLabel{font-size:15pt}")

        self.nome_edit = QLineEdit()
        self.nome_edit.setStyleSheet("QLineEdit{font-size:15pt}")

        self.vertical_layout.addWidget(self.nome_label)
        self.vertical_layout.addWidget(self.nome_edit)
        # ----------------- Fim do nome do Cliente ----------------------------------



        # ----------------------- E-mail do Cliente ------------------------------------
        self.email_label = QLabel("E-mail:")
        self.email_label.setStyleSheet("QLabel{font-size:15pt}")

        self.email_edit = QLineEdit()
        self.email_edit.setStyleSheet("QLineEdit{font-size:15pt}")

        self.vertical_layout.addWidget(self.email_label)
        self.vertical_layout.addWidget(self.email_edit)
        # ----------------------- Fim do E-mail do Cliente ---------------------------------


        # ----------------------- Telefone do Cliente ------------------------------------
        self.telefone_label = QLabel("Telefone:")
        self.telefone_label.setStyleSheet("QLabel{font-size:15pt}")

        self.telefone_edit = QLineEdit()
        self.telefone_edit.setStyleSheet("QLineEdit{font-size:15pt}")

        self.vertical_layout.addWidget(self.telefone_label)
        self.vertical_layout.addWidget(self.telefone_edit)

        # ------------------------ Fim do Telefone do cliente----------------------------------

        # ------------------------ Endereço do Cliente ----------------------------------------
        self.endereco_label = QLabel("Endereço:")
        self.endereco_label.setStyleSheet("QLabel{font-size:15pt}")

        self.endereco_edit = QLineEdit()
        self.endereco_edit.setStyleSheet("QLineEdit{font-size:15pt}")

        self.vertical_layout.addWidget(self.endereco_label)
        self.vertical_layout.addWidget(self.endereco_edit)

        # ---------------------- Fim do Endereço do Cliente ------------------------------------


        # ------------------------ CPF do Cliente --------------------------------------
        self.cpf_label = QLabel("Digite seu CPF:")
        self.cpf_label.setStyleSheet("QLabel{font-size:15pt}")

        self.cpf_edit = QLineEdit()
        self.cpf_edit.setStyleSheet("QLineEdit{font-size:15pt}")

        self.vertical_layout.addWidget(self.cpf_label)
        self.vertical_layout.addWidget(self.cpf_edit)

        # ----------------------- Fim do CPF do Cliente ---------------------------------

        # ---------------------- Data de nascimento do Cliente ---------------------------
        self.data_label = QLabel("Digite sua Data de Nascimento:")
        self.data_label.setStyleSheet("QLabel{font-size:15pt}")

        self.data_edit = QLineEdit()
        self.data_edit.setStyleSheet("QLineEdit{font-size:15pt}")

        self.vertical_layout.addWidget(self.data_label)
        self.vertical_layout.addWidget(self.data_edit)

        # ---------------------- Fim da data de nascimento do Cliente --------------------

        #  -------------------------- Genero do Cliente -----------------------------------
        self.genero_label = QLabel("Gênero:")
        self.genero_label.setStyleSheet("QLabel{font-size:15pt}")

        self.genero_combo = QComboBox()
        self.genero_combo.setStyleSheet("QComboBox{font-size:15pt}")
        self.genero_combo.addItem("Feminino")
        self.genero_combo.addItem("Masculino")
        self.genero_combo.addItem("Prefiro não dizer")

        self.vertical_layout.addWidget(self.genero_label)
        self.vertical_layout.addWidget(self.genero_combo)

        # ----------------------------- Fim do Genero -------------------------------

        # ----------------------------- Botão ----------------------------------------
        self.cadastrar_botao = QPushButton("Cadastrar")
        self.cadastrar_botao.setStyleSheet("QPushButton{font-size:15pt; background-color:#FC129B; color:white}")


        self.vertical_layout.addWidget(self.cadastrar_botao)
        self.cadastrar_botao.clicked.connect(self.cadastrar)

        # --------------------------- Fim do Botão ---------------------------------

        self.direita_label.setLayout(self.vertical_layout)

        self.horizontal_layout.addWidget(self.esquerda_label)
        self.horizontal_layout.addWidget(self.direita_label)

        self.setLayout(self.horizontal_layout)

    def cadastrar(self):
        arquivo = open("cadastroclientes.txt","a",encoding="utf8")
        arquivo.write(f"Nome: {self.nome_edit.text()}\n")
        arquivo.write(f"E-mail: {self.email_edit.text()}\n")
        arquivo.write(f"Telefone: {self.telefone_edit.text()}\n")
        arquivo.write(f"Endereço:  {self.endereco_edit.text()}\n")
        arquivo.write(f"CPF:  {self.cpf_edit.text()}\n")
        arquivo.write(f"Data de Nascimento: {self.data_edit.text()}\n")
        arquivo.write(f"Gênero:  {self.genero_combo.currentText()}\n")
        arquivo.write("---------------------------------------------\n")
        arquivo.close()

app = QApplication(sys.argv)
janela = CadastroClientes()
janela.show()
app.exec_()