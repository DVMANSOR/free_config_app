from PyQt5.QtWidgets import *
from PyQt5 import uic
import wget
from threading import Thread
import os

configs = []

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("gui.ui", self)
        self.show()
        self.setWindowTitle("Config By Mansour :)")
        self.setFixedWidth(550)
        self.setFixedHeight(370)
        Thread(target=self.load_configs).start()
        self.list.activated.connect(self.update)
    
    def load_configs(self):
        global loaded
        for i in range(7):
            try:
                wget.download(f"https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/Sub{i+1}.txt", f"config{i+1}.txt")
                self.label.setText(f"Config {i+1} is Ready")
            except:
                self.label.setText(f"Config {i+1} Have Error")
        self.list.setEnabled(True)

        for x in range(7):
            f = open(f"config{x+1}.txt", 'r')
            text = f.read()
            configs.append(text)
            f.close()

        for l in range(7):
            os.remove(f"config{l+1}.txt")

        self.label.setText("All Configs is Ready")


    def update(self):
        self.text_box.clear()
        selected = self.list.currentText()
        number = selected[-1]
        print(number)
        text = configs[int(number)-1]
        self.text_box.insertPlainText(text)


def main():
    App = QApplication([])
    window = MyGUI()
    App.exec_()

if __name__ == "__main__":
    main()