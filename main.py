import sys

from PyQt5 import QtWidgets
import random
import untitled

class ExampleApp(QtWidgets.QMainWindow, untitled.Ui_MainWindow):
    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.gettalon)

    def gettalon(self):
        Name = self.lineEdit.text()
        Autor = self.lineEdit_2.text()
        Title = self.lineEdit_3.text()
        Year = self.spinBox.text()
        Time = self.timeEdit.time().toString()
        if Name == "" or Autor == "" or Title =="":
            self.label_6.setText("Неполные данные")
        else:
            f = open("books.txt", "r", encoding="utf-8")

            k = f.read()
            k = k.split("\n----\n")
            for i in range(0, len(k)-1):
                k[i] = k[i].split("\n")
                k[i][3]=int(k[i][3])
            k.pop(-1)


            for i in range(0, len(k)):
                if Title == k[i][0] and Autor == k[i][1]  and Year ==k[i][2]:
                    if k[i][3]==0:
                        self.label_6.setText("Данной книги нет в наличии")
                    else:
                        k[i][3]-=1
                        self.label_6.setText("Ваш талон №"+str(random.randint(0,10000))+" выдан")
                else:
                    self.label_6.setText("Книга не найдена")

            f = open("books.txt","w",encoding="utf-8")

            for i in range(0, len(k)):
                f.write(k[i][0] + "\n")
                f.write(k[i][1] + "\n")
                f.write(k[i][2] + "\n")
                f.write(k[i][3] + "\n")
                f.write("----" + "\n")






def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()
if __name__ == '__main__':
    main()