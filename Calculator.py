from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont, QIcon
import sys


app=QApplication(sys.argv)
oyna=QWidget()

oyna.setWindowTitle("Calculator")
oyna.setWindowIcon(QIcon("D:\\DASTURLASH\\python\\PyQt5\\icon.png"))
oyna.setGeometry(700, 300, 350, 500)
oyna.setFixedSize(345,530)

kiritish=QLineEdit(oyna)
kiritish.move(65, 100)
kiritish.setFont(QFont("Times", 14))

knopka1=QPushButton("1",oyna)
knopka1.setGeometry(700, 300, 65, 65)
knopka1.move(20, 200)

knopka2=QPushButton("2",oyna)
knopka2.setGeometry(700, 300, 65, 65)
knopka2.move(100, 200)

knopka3=QPushButton("3",oyna)
knopka3.setGeometry(700, 300, 65, 65)
knopka3.move(180, 200)

knopka4=QPushButton("4",oyna)
knopka4.setGeometry(700, 300, 65, 65)
knopka4.move(20, 280)

knopka5=QPushButton("5",oyna)
knopka5.setGeometry(700, 300, 65, 65)
knopka5.move(100, 280)

knopka6=QPushButton("6",oyna)
knopka6.setGeometry(700, 300, 65, 65)
knopka6.move(180, 280)

knopka7=QPushButton("7",oyna)
knopka7.setGeometry(700, 300, 65, 65)
knopka7.move(20, 360)

knopka8=QPushButton("8",oyna)
knopka8.setGeometry(700, 300, 65, 65)
knopka8.move(100, 360)

knopka9=QPushButton("9",oyna)
knopka9.setGeometry(700, 300, 65, 65)
knopka9.move(180, 360)

knopka0=QPushButton("0",oyna)
knopka0.setGeometry(700, 300, 65, 65)
knopka0.move(100, 440)

knopka=QPushButton(",",oyna)
knopka.setGeometry(700, 300, 65, 65)
knopka.move(20, 440)

knopka_teng=QPushButton("=",oyna)
knopka_teng.setGeometry(700, 300, 65, 65)
knopka_teng.move(180, 440)

knopka_plus=QPushButton("+",oyna)
knopka_plus.setGeometry(700, 300, 65, 65)
knopka_plus.move(260, 200)

knopka_minus=QPushButton("-",oyna)
knopka_minus.setGeometry(700, 300, 65, 65)
knopka_minus.move(260, 280)

knopka_kop=QPushButton("*",oyna)
knopka_kop.setGeometry(700, 300, 65, 65)
knopka_kop.move(260, 360)

knopka_boluv=QPushButton("/",oyna)
knopka_boluv.setGeometry(700, 300, 65, 65)
knopka_boluv.move(260, 440)



def bir():
    txt = kiritish.text()
    kiritish.setText(txt+"1")

def ikki():
    txt = kiritish.text()
    kiritish.setText(txt+"2")

def uch():
    txt = kiritish.text()
    kiritish.setText(txt+"3")

def tort():
    txt = kiritish.text()
    kiritish.setText(txt+"4")

def besh():
    txt = kiritish.text()
    kiritish.setText(txt+"5")

def olti():
    txt = kiritish.text()
    kiritish.setText(txt+"6")

def yetti():
    txt = kiritish.text()
    kiritish.setText(txt+"7")

def sakkiz():
    txt = kiritish.text()
    kiritish.setText(txt+"8")

def toqqiz():
    txt = kiritish.text()
    kiritish.setText(txt+"9")

def nol():
    txt = kiritish.text()
    kiritish.setText(txt+"0")

def vergul():
    txt = kiritish.text()
    kiritish.setText(txt+",")

def plus():
    txt = kiritish.text()
    kiritish.setText(txt+"+")

def nimus():
    txt = kiritish.text()
    kiritish.setText(txt+"-")

def koop():
    txt = kiritish.text()
    kiritish.setText(txt+"*")

def bluv():
    txt = kiritish.text()
    kiritish.setText(txt+"/")

def teng():
    txt = kiritish.text()

    resualt=eval(txt)
    kiritish.setText(print(eval(txt)))
    kiritish.setText(str(resualt))

knopka1.clicked.connect(bir)
knopka2.clicked.connect(ikki)
knopka3.clicked.connect(uch)
knopka4.clicked.connect(tort)
knopka5.clicked.connect(besh)
knopka6.clicked.connect(olti)
knopka7.clicked.connect(yetti)
knopka8.clicked.connect(sakkiz)
knopka9.clicked.connect(toqqiz)
knopka0.clicked.connect(nol)
knopka_plus.clicked.connect(plus)
knopka_minus.clicked.connect(nimus)
knopka_kop.clicked.connect(koop)
knopka_boluv.clicked.connect(bluv)
knopka.clicked.connect(vergul)
knopka_teng.clicked.connect(teng)


oyna.show()
sys.exit(app.exec_())