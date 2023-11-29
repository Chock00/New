import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint

# Там цвет жёлтый и его еле видно, и периодически окружность появляется за кнопкой
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)                                                                  

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_eli(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()
    
    def draw_eli(self, qp):
        qp.setPen(QColor(255, 255, 0))
        dia = randint(30, 100)
        levverh = (randint(0, 550), randint(0, 400))
        qp.drawEllipse(levverh[0], levverh[1], dia, dia)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())