import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect("coffee.sqlite")
        self.select_data()

    def select_data(self):
        query = "SELECT * FROM coffee"
        res = self.connection.cursor().execute(query).fetchall()
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)

        column_names = ["Название", "Степень обжарки", "Молотый/В зёрнах", "Описание", "Цена", "Объём"]
        self.tableWidget.setRowCount(1)
        for j in range(len(column_names)):
            self.tableWidget.setItem(
                0, j, QTableWidgetItem(column_names[j]))

        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                if j == 0:
                    continue
                self.tableWidget.setItem(
                    i + 1, j - 1, QTableWidgetItem(str(elem)))

    def closeEvent(self, event):
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())
