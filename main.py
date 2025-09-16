import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QMessageBox
)
from PySide6.QtCore import QSize

class BadUIApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Форма реєстрації з помилками")
        self.setMinimumSize(QSize(500, 200))

        self.setStyleSheet("""
            QWidget {
                background-color: #333;
                color: #FFFFFF;
            }
            QPushButton {
                background-color: #555;
                color: #00008B; /* DarkBlue */
                font-weight: bold;
                padding: 5px;
            }
            QLineEdit {
                background-color: #444;
                border: 1px solid #666;
            }
        """)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)

        # Створення віджетів
        username_label = QLabel("Ім'я користувача:")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Введіть ваше ім'я")

        password_label = QLabel("Пароль:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.submit_button = QPushButton("Відправити")
        
        self.clear_button = QPushButton("ОК")

        form_layout = QVBoxLayout()
        form_layout.addWidget(username_label)
        form_layout.addWidget(self.username_input)
        form_layout.addWidget(password_label)
        form_layout.addWidget(self.password_input)
        
        button_layout = QVBoxLayout()
        button_layout.addWidget(self.submit_button)
        button_layout.addWidget(self.clear_button)

        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)
        
        self.submit_button.clicked.connect(self.submit_form)
        self.clear_button.clicked.connect(self.clear_form)

    def submit_form(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if not username or not password:
             return

        QMessageBox.information(
            self,
            "Успіх!",
            f"Дякуємо за реєстрацію, {username}!\nВаш пароль: {password}"
        )

    def clear_form(self):
        self.username_input.clear()
        self.password_input.clear()
        print("Форму очищено!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BadUIApp()
    window.show()
    sys.exit(app.exec())
