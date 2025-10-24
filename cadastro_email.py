import sys
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QComboBox,QVBoxLayout,QHBoxLayout,QLineEdit,QTableWidget,QMessageBox,QInputDialog,QPushButton,QCheckBox, QFrame,QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt, QSize

class email(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(50,50,500,800)

        self.setWindowTitle("Welcome to email")
        self.setGeometry(50,50,500,800)
        self.setFixedSize(550,800)

        self.vertical_layout = QVBoxLayout()
        
        # ---------------------- titulo ----------------------------------------
        self.titulo_label = QLabel("Welcome to email")
        self.titulo_label.setStyleSheet("QLabel{font-family:Open Sans;font-size:20pt;color:#000000}")
        self.titulo_label.setAlignment(Qt.AlignCenter)
        self.vertical_layout.addWidget(self.titulo_label)
        # ------------------------- fim do titulo --------------------------------
       
        # --------------------------- subtitulo ----------------------------------
        self.sub_titulo_label = QLabel("Please login to account")
        self.sub_titulo_label.setStyleSheet("QLabel{font-size:12pt;color:#000000}")
        self.sub_titulo_label.setAlignment(Qt.AlignCenter)
        self.vertical_layout.addWidget(self.sub_titulo_label)
        # ----------------------------- fim do subtitulo -------------------------

        # ----------------------------- email -------------------------------------
        self.email_label = QLabel("Email Adress")
        self.email_label.setStyleSheet("QLabel{font-size:10pt}")
        self.email_label.setAlignment(Qt.AlignCenter)

        self.email_input = QLineEdit()
        self.email_input.setStyleSheet("""
            QLineEdit {
                border: 2px solid #ccc;
                border-radius: 15px;
                padding: 8px;
                background-color: #fff;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 2px solid #0078d7;
            }
        """)
        self.vertical_layout.addWidget(self.email_label)
        self.vertical_layout.addWidget(self.email_input)
        # ------------------------------ fim do email --------------------------------

        # ------------------------------ senha ----------------------------------------
        self.senha_label = QLabel("Password")
        self.senha_label.setStyleSheet("QLabel{font-size:10pt}")
        self.senha_label.setAlignment(Qt.AlignCenter)

        self.senha_input = QLineEdit()
        self.senha_input.setStyleSheet("""QLineEdit {border: 2px solid #ccc;border-radius: 15px;padding: 8px;background-color: #fff;font-size: 14px;}QLineEdit:focus {border: 2px solid #0078d7;}""")

        self.vertical_layout.addWidget(self.senha_label)
        self.vertical_layout.addWidget(self.senha_input)
        # ----------------------------- fim da senha ----------------------------------
        self.check = QCheckBox("remenber me")
        self.vertical_layout.addWidget(self.check)
        # ------------------------------------------------------------------------------
        self.forgot_label = QLabel("Forgot your password?")
        self.forgot_label.setAlignment(Qt.AlignRight)
        self.forgot_label.setStyleSheet("""QLabel {color: #0078d7;font-size: 13px;} QLabel:hover {color: #005fa3;}""")
        self.forgot_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.vertical_layout.addWidget(self.forgot_label)
        # -------------------------------------------------------------------------------
        # ----------------------------- Botao -------------------------------------------
        self.imagem_botao = QLabel()
        pixmap = QPixmap(".venv/botao1.png")  # caminho da sua imagem
        pixmap = pixmap.scaled(150, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation)  # ajusta tamanho
        self.imagem_botao.setPixmap(pixmap)
        self.imagem_botao.setAlignment(Qt.AlignCenter)  # centraliza
        self.vertical_layout.addWidget(self.imagem_botao)
        # ----------------------------- fim do Botao ------------------------------------
        self.new_user_label = QLabel()
        self.new_user_label.setText(
            'New user? <span style="color:#0078d7; text-decoration: underline;">Create an Account</span>'
            )
        self.new_user_label.setAlignment(Qt.AlignCenter)
        self.new_user_label.setTextInteractionFlags(Qt.TextBrowserInteraction) 
        self.vertical_layout.addWidget(self.new_user_label)
        # -------------------------------------------------------------------------------
        self.or_label = QLabel("or")
        self.or_label.setAlignment(Qt.AlignCenter)
        self.vertical_layout.addWidget(self.or_label)
        # --------------------------------------------------------------------------------

        # --------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------
        self.social_frame = QFrame()
        self.social_frame.setFixedHeight(200)
        self.social_frame.setStyleSheet("background-color: #03091F")
        self.vertical_layout.addWidget(self.social_frame)
        # ---------------------------------------------------------------------------------
        self.social_layout = QHBoxLayout()
        self.social_frame.setLayout(self.social_layout)

        self.botao_facebook = QLabel()
        pixmap_fb = QPixmap(".venv\loginface.png").scaled(200, 80)
        self.botao_facebook.setPixmap(pixmap_fb)


        self.social_layout.addWidget(self.botao_facebook, alignment=Qt.AlignLeft | Qt.AlignCenter)

        # ----------------------------------------------------------------------------------------
        
        # ---------------------------------------------------------------------------------------
        self.botao_google = QLabel()
        pixmap_google = QPixmap(".venv\logingoogle.png").scaled(250, 90)
        self.botao_google.setPixmap(pixmap_google)
        self.social_layout.addWidget(self.botao_google, alignment=Qt.AlignRight | Qt.AlignCenter)
        # -------------------------------------------------------------------------------------

        
        # ----------------- adicionar ---------------------------
        
        self.setLayout(self.vertical_layout)
       


app = QApplication(sys.argv)
janela = email()
janela.show()
app.exec_()