# importar o pacote sys(sistema) para o sistema operacional
# gerenciar a nossa janela e permitir com que ela entre em serviços
import sys
# Importar a biblioteca Pyqt5.QTWidgets, esta biblioteca, tem varios controles para usarmos na nossa janela.
# São eles: 
# QApplication -> A estrutura da janela, com elementos: - barra de titulo,maximizar,e fechar 
# QLabel -> Um rótulo, ou seja, um tedxto simples de apresentação
# QLineEdit -> Uma caixa de texto
# QPushButton -> Um botão para clicar
# QVBoxLayout -> Utilizado para organizar os elementos.
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox

# Importar uma nova biblioteca para trabalhar com imagens,
#  Vamos usar o controle chamado QPixmap do pacote GUI
from PyQt5.QtGui import QPixmap


# Iniciar a construção da janela como base o controle 
# QWidget. Ele possui as configurações iniciais de uma janela
class CadastroProduto(QWidget):
    # Para iniciar a janela, iremos usar a função chamada
    # __init__, que irá inicializar a nossa janela
    # O termo self é um reflexivo que trata da própria 
    # classe, neste CadastroProduto
    def __init__(self):
        super().__init__()

        # Define o texto que aparece na barra de titulo
        self.setWindowTitle("Cadastro de Produtos")

        # Definir a posição inicial da nossa janela, iremos setar valores para x e y e também dimensões largura e altura
        self.setGeometry(100,100,800,800)
        self.setFixedWidth(800)
# Vamos criar 2 labels que representarão as partes superior,
#  onde ficará a imagem,e a parte inferior, onde teremos os controles
        self.superior_label = QLabel()
        self.superior_label.setPixmap(QPixmap(".venv/livro.jpg"))
        self.superior_label.setScaledContents(True)
# Ajustar a altura da label
        self.superior_label.setFixedHeight(400)



        self.inferior_label = QLabel()
        self.inferior_label.setStyleSheet("QLabel{background-color:#01A5DB}")

        self.nome_label = QLabel("Nome do Produto")
        self.nome_label.setStyleSheet("QLabel{font-size:15pt}")
        self.nome_edit = QLineEdit()
        self.nome_edit.setStyleSheet("QLineEdit{font-size:15pt}")


        self.tipo_label = QLabel("Selecione o tipo do Produto")
        self.tipo_label.setStyleSheet("QLabel{font-size:15pt}")
        self.tipo_combo = QComboBox()
        self.tipo_combo.setStyleSheet("QComboBox{font-size:15pt}")
        self.tipo_combo.addItem("Informatica")
        self.tipo_combo.addItem("Vestuario")
        self.tipo_combo.addItem("Alimento")
        self.tipo_combo.addItem("Beleza")
        self.tipo_combo.addItem("Floricultura")
        self.tipo_combo.addItem("Papelaria")
        self.tipo_combo.addItem("Livros")

        self.descricao_label = QLabel("Descrição do Produto")
        self.descricao_label.setStyleSheet("QLabel{font-size:15pt}")
        self.descricao_edit = QLineEdit()
        self.descricao_edit.setStyleSheet("QLineEdit{font-size:15pt}")
        self.descricao_edit.setFixedHeight(100)


        self.preco_label = QLabel("Preço do Produto")
        self.preco_label.setStyleSheet("QLabel{font-size:15pt}")
        self.preco_edit = QLineEdit()
        self.preco_edit.setStyleSheet("QLineEdit{font-size:15pt}")


        self.gravar_botao = QPushButton("Gravar")
        self.gravar_botao.setStyleSheet("QPushButton{font-size:15pt; background-color:#002FDB; color:white}")
        # Adicionar ao botão gravar um comando de acionamento,
        #  pois quando esse botão for clicado ele chamará uma função
        #  que executará a gravção dos dados do produto em um arquivo de texto
        self.gravar_botao.clicked.connect(self.gravar)



        # organizar estes controles em um layout vertical
        self.v_controles = QVBoxLayout()
        
        self.v_controles.addWidget(self.nome_label)
        self.v_controles.addWidget(self.nome_edit)
        self.v_controles.addWidget(self.tipo_label)
        self.v_controles.addWidget(self.tipo_combo)
        self.v_controles.addWidget(self.descricao_label)
        self.v_controles.addWidget(self.descricao_edit)
        self.v_controles.addWidget(self.preco_label)
        self.v_controles.addWidget(self.preco_edit)
        self.v_controles.addWidget(self.gravar_botao)


        # adicionar os controles na parte inferior
        self.inferior_label.setLayout(self.v_controles)

# Vamos criar um controle de layout vertical para dispor as label 
# superior e inferior uma abaixo da outra restopectivamente
        self.v_layout = QVBoxLayout()

        self.v_layout.addWidget(self.superior_label)
        self.v_layout.addWidget(self.inferior_label)

# adiocionar o layout organizado na janela
        self.setLayout(self.v_layout)
    def gravar(self):
        arquivo = open("cadastro.txt","a",encoding="utf8")
        arquivo.write(f"Produto: {self.nome_edit.text()}\n")
        arquivo.write(f"Tipo: {self.tipo_combo.currentText()}\n")
        arquivo.write(f"Descrição: {self.descricao_edit.text()}\n")
        arquivo.write(f"Preço: R$ {self.preco_edit.text()}\n")
        arquivo.write("---------------------------------------------\n")
        arquivo.close()

# Vamos vincular o funcionamento da janela com o gerenciamento do sistema operacional. 
# Assim o sistema operacional sabera lidar com a jenela em memória.
app = QApplication(sys.argv)
# Instancia da janela para por em funcionamento
janela = CadastroProduto()
# Exibir a jenela na tela
janela.show()
# Executar a janela
app.exec_()