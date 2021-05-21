import sys
from PyQt5 import QtWidgets

import add


class ExampleApp(QtWidgets.QMainWindow, add.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.addBook)

    def addBook(self):
        Title = self.lineEdit.text()
        Autor = self.lineEdit_2.text()
        Year = self.spinBox_2.text()
        Vol = self.spinBox.text()

        f = open("books.txt", "r", encoding="utf-8")

        k = f.read()
        k = k.split("\n----\n")
        for i in range(0, len(k) - 1):
            k[i] = k[i].split("\n")
            k[i][3] = int(k[i][3])
        k.pop(-1)

        b = True

        for i in range(0, len(k)):
            if Title == k[i][0] and Autor == k[i][1] and Year == k[i][2]:
                k[i][3]+=Vol
                b = False

        if b:


            f = open("books.txt","a",encoding="utf-8")

            f.write(Title + "\n")
            f.write(Autor + "\n")
            f.write(Year + "\n")
            f.write(Vol + "\n")
            f.write("----"+"\n")
        else:
            for i in range(0, len(k)):
                f.write(k[i][0] + "\n")
                f.write(k[i][1] + "\n")
                f.write(k[i][2] + "\n")
                f.write(k[i][3] + "\n")
                f.write("----" + "\n")

        f.close()





def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()