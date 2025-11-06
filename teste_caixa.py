import sys

from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QVBoxLayout, QHBoxLayout, QLineEdit, QTableWidget

class caixa2(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,1200,800)

        # criar os elementos que irão para a coluna da esquerda 
        # criar uma label para adicionar uma imagem
        # e depois adicionar a coluna da esquerda

        self.imagem_label = QLabel()
        self.imagem_label.setPixmap(QPixmap(".venv/pao.jpg"))
        self.imagem_label.setScaledContents(True)
        self.imagem_label.setFixedSize(600,300)

        self.codigo_produto_label = QLabel("Código do Produto:")
        self.codigo_produto_label.setStyleSheet("QLabel{font-size:15pt}")

        self.codigo_produto_edit = QLineEdit()
        self.codigo_produto_edit.setStyleSheet("QLineEdit{font-size:15pt}")

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tabela de Produtos")

        self.setGeometry(100,100,1000,500)

        self.tabela = QTableWidget()
        self.tabela.setColumnCount(6)
        self.tabela.setRowCount(5)
        colunas = ["Código", "Nome do produto", "Quantidade", "Preço Unitario", "Quantidade","Preço Total"]

        
        self.horizontal_layout = QHBoxLayout()
        # Adicionar a coluna da esquerda no layout horizontal
        self.horizontal_layout.addWidget(self.coluna_esquerda_label)
        # Adicionar a coluna da direita no layout horizontal
        self.horizontal_layout.addWidget(self.coluna_direita_label)
        # Adicionar o layout horizoltal na tela
        self.setLayout(self.horizontal_layout)

        self.vertical_layout.addWidget(self.tabela)
        self.setLayout(self.vertical_layout)



        # Adiocionar os elementos que ficarão ao lado esquerdo a um layout 
        # vertical que será aplicado na coluna da esquerda
        self.vetical_esquerda_layout = QVBoxLayout()
        self.vetical_esquerda_layout.addWidget(self.imagem_label)
        self.vetical_esquerda_layout.addWidget(self.codigo_produto_label)

    
        self.coluna_esquerda_label = QLabel()
        self.coluna_esquerda_label.setStyleSheet("QLabel{background-color:yellow}")

        # Adicionar o layout da esquerda á coluna da esquerda
        self.coluna_esquerda_label.setLayout(self.vetical_esquerda_layout)

        self.coluna_direita_label = QLabel()
        self.coluna_direita_label.setStyleSheet("QLabel{background-color:pink}")

    



app = QApplication(sys.argv)
janela = caixa2()
janela.show()
app.exec_()

        
