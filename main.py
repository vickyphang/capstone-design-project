from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import RPi.GPIO as GPIO
import sys, time, FloatSwitch
import irsensor
import requests
import ModulNotifikasi
import Relay
import RFID_read

#Tiap halaman dibikin class-nya masing-masing
class ui_menu(object):
    def setupUi(self, water):
        water.setObjectName("water")
        water.setGeometry(0,0,800,500)
        self.centralWidget = QtWidgets.QWidget(water)
        
        self.photo1 = QtWidgets.QLabel(self.centralWidget)
        self.photo1.setGeometry(0, 0, 1280, 720)
        self.photo1.setPixmap(QPixmap("/home/pi/Desktop/UserInterface/menu.png"))
        self.photo1.setScaledContents(True)
        
        self.pushButton1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton1.setGeometry(60, 285, 370, 315)
        self.pushButton1.setFlat(True)
        
        self.pushButton2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton2.setGeometry(455, 285, 370, 315)
        self.pushButton2.setFlat(True)
        
        self.pushButton3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton3.setGeometry(850, 285, 370, 315)
        self.pushButton3.setFlat(True)
        
        water.setCentralWidget(self.centralWidget)
        self.retranslateUi(water)
        QtCore.QMetaObject.connectSlotsByName(water)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("water", "water"))

        self.pushButton1.setText(_translate("water", ""))
        self.pushButton2.setText(_translate("water", ""))
        self.pushButton3.setText(_translate("water", ""))
        self.photo1.setText(_translate("water", ""))


class Ui_TaruhBotol(object):
    def setupUi(self, TaruhBotol):
        TaruhBotol.setObjectName("TaruhBotol")
        TaruhBotol.setGeometry(0,0,800,500)
        self.centralWidget = QtWidgets.QWidget(TaruhBotol)
        
        self.photo1 = QtWidgets.QLabel(self.centralWidget)
        self.photo1.setGeometry(0, 0, 1280, 720)
        self.photo1.setPixmap(QPixmap("/home/pi/Desktop/UserInterface/taruh_botol.png"))
        self.photo1.setScaledContents(True)
    
        TaruhBotol.setCentralWidget(self.centralWidget)
        self.retranslateUi(TaruhBotol)
        QtCore.QMetaObject.connectSlotsByName(TaruhBotol)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("TaruhBotol", "TaruhBotol"))
        
        self.photo1.setText(_translate("TaruhBotol",""))


class Ui_RFID(object):
    def setupUi(self, RFID):
        RFID.setObjectName("RFID")
        RFID.setGeometry(0,0,800,500)
        self.centralWidget = QtWidgets.QWidget(RFID)

        self.photo1 = QtWidgets.QLabel(self.centralWidget)
        self.photo1.setGeometry(0, 0, 1280, 720)
        self.photo1.setPixmap(QPixmap("/home/pi/Desktop/UserInterface/rfid.png"))
        self.photo1.setScaledContents(True)
    
        RFID.setCentralWidget(self.centralWidget)
        self.retranslateUi(RFID)
        QtCore.QMetaObject.connectSlotsByName(RFID)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("RFID", "RFID"))
        
        self.photo1.setText(_translate("RFID",""))
        
        
class Ui_StockHabis(object):
    def setupUi(self, StockHabis):
        StockHabis.setObjectName("StockHabis")
        StockHabis.setGeometry(0,0,800,500)
        self.centralWidget = QtWidgets.QWidget(StockHabis)
        
        self.photo1 = QtWidgets.QLabel(self.centralWidget)
        self.photo1.setGeometry(0, 0, 1280, 720)
        self.photo1.setPixmap(QPixmap("/home/pi/Desktop/UserInterface/air_habis.png"))
        self.photo1.setScaledContents(True)
        
        self.pushButton6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton6.setGeometry(QtCore.QRect(500, 370, 280, 60))
        self.pushButton6.setFlat(True)
    
        StockHabis.setCentralWidget(self.centralWidget)
        self.retranslateUi(StockHabis)
        QtCore.QMetaObject.connectSlotsByName(StockHabis)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("StockHabis", "StockHabis"))
        
        self.pushButton6.setText(_translate("StockHabis", ""))
        self.photo1.setText(_translate("StockHabis", ""))
        
        
class Ui_KartuTidakTerdaftar(object):
    def setupUi(self, KartuTidakTerdaftar):
        KartuTidakTerdaftar.setObjectName("KartuTidakTerdaftar")
        KartuTidakTerdaftar.setGeometry(0,0,800,500)
        self.centralWidget = QtWidgets.QWidget(KartuTidakTerdaftar)
        
        self.photo1 = QtWidgets.QLabel(self.centralWidget)
        self.photo1.setGeometry(0, 0, 1280, 720)
        self.photo1.setPixmap(QPixmap("/home/pi/Desktop/UserInterface/kartu_x.png"))
        self.photo1.setScaledContents(True) 
        
        KartuTidakTerdaftar.setCentralWidget(self.centralWidget)
        self.retranslateUi(KartuTidakTerdaftar)
        QtCore.QMetaObject.connectSlotsByName(KartuTidakTerdaftar)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("KartuTidakTerdaftar", "KartuTidakTerdaftar"))
        
        self.photo1.setText(_translate("KartuTidakTerdaftar", ""))
        
        
class Ui_SaldoKurang(object):
    def setupUi(self, SaldoKurang):
        SaldoKurang.setObjectName("SaldoKurang")
        SaldoKurang.setGeometry(0,0,800,500)
        self.centralWidget = QtWidgets.QWidget(SaldoKurang)
        
        self.photo1 = QtWidgets.QLabel(self.centralWidget)
        self.photo1.setGeometry(0, 0, 1280, 720)
        self.photo1.setPixmap(QPixmap("/home/pi/Desktop/UserInterface/saldo_habis.png"))
        self.photo1.setScaledContents(True)

        SaldoKurang.setCentralWidget(self.centralWidget)
        self.retranslateUi(SaldoKurang)
        QtCore.QMetaObject.connectSlotsByName(SaldoKurang)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("SaldoKurang", "SaldoKurang"))
        
        self.photo1.setText(_translate("SaldoKurang", ""))


#class controller isinya fungsi atau method untuk kendaliin logika apa yang harus dijalankan
class Controller:

    def __init__(self):
        pass
        
    def logika(self):
        stock = FloatSwitch.CekStockAir()
        if stock == 1:
            print('stock ada')
            self.Show_menu()
        elif stock == 0:
            self.Show_StockHabis()
            print('stock habis')
            #syntax biar GUI tidak freeze ketika ada proses backend
            self.timer = QTimer()
            self.timer.setInterval(500)
            self.timer.timeout.connect(self.logika2)
            self.timer.start()
       
    def logika2(self):
        #Matiin Modul Kontainer dan kirim notifikasi email ke pemilik
        Relay.ModulKontainerOff()
        ModulNotifikasi.KirimNotifikasi()
        self.timer.stop()
    
    def CekRefill(self):
        stock = FloatSwitch.CekStockAir()
        if stock == 1:
            print('stock ada')
            kontainer = Relay.ModulKontainerOn()
            if kontainer == 1:
                self.Show_menu()
                self.hide_StockHabis()
    
    def pilih500(self):
        self.Show_RFID()
        self.logika3()
        self.hide_water()
    
    def logika3(self):
        self.timer = QTimer()
        self.timer.setInterval(2000)
        self.timer.timeout.connect(self.deteksiRFID)
        self.timer.start()
        
    def deteksiRFID(self):
        id=RFID_read.bacaRFID()
        
        if id>0:
            print("id terdeteksi")
            self.timer.stop()
            
        url = 'https://bulbous-markets.000webhostapp.com/proses.php'
        obj = {'uid': id, 'harga':'500'}

        x = requests.post(url, data = obj)
        respon = x.json()
        status = respon['Detail']['Status']

        if status=="Transaksi Sukses":
            self.Show_TaruhBotol()
            self.hide_RFID()
            
            self.timer = QTimer()
            self.timer.setInterval(1000)
            self.timer.timeout.connect(self.deteksi)
            self.timer.start()
            
        elif status=="ID Belum Terdaftar":
            self.Show_KartuTidakTerdaftar()
            self.hide_RFID()
            self.logika6()
            
        elif status=="Saldo tidak cukup":
            self.Show_SaldoKurang()
            self.hide_RFID()
            self.logika6()
            
    def logika6(self):
        #syntax delay buat tampilin halaman selama 5 detik, terus balik halaman menu
        loop = QEventLoop()
        QTimer.singleShot(5000, loop.quit)
        loop.exec_()
        self.Show_menu()
        self.hide_KartuTidakTerdaftar()
        self.hide_SaldoKurang()
        
    def deteksi(self):
        botol = irsensor.deteksibotol2()
        print(botol)
        
        if botol==1:
            self.timer.stop()
            
            self.timer = QTimer()
            self.timer.setInterval(1000)
            self.timer.timeout.connect(self.pompa500)
            self.timer.start()
    
    def pompa500(self):
        #aktifin relay selama time.sleep
        pompa = Relay.pompa(15.8)
        if pompa==1:
            self.timer.stop()
            self.Show_menu()
            self.hide_TaruhBotol()
            
    def pilih1000(self):
        self.Show_RFID()
        self.logika4()
        self.hide_water()
        
    def logika4(self):
        self.timer = QTimer()
        self.timer.setInterval(2000)
        self.timer.timeout.connect(self.deteksiRFID2)
        self.timer.start()
        
    def deteksiRFID2(self):
        id=RFID_read.bacaRFID()
        
        if id>0:
            print("id terdeteksi")
            self.timer.stop()
            
        url = 'https://bulbous-markets.000webhostapp.com/proses.php'
        obj = {'uid': id, 'harga':'1000'}

        x = requests.post(url, data = obj)
        respon = x.json()
        status=respon['Detail']['Status']

        if status=="Transaksi Sukses":
            self.Show_TaruhBotol()
            self.hide_RFID()
            
            self.timer = QTimer()
            self.timer.setInterval(1000)
            self.timer.timeout.connect(self.deteksi2)
            self.timer.start()
            
        elif status=="ID Belum Terdaftar":
            self.Show_KartuTidakTerdaftar()
            self.hide_RFID()
            self.logika6()
            
        elif status=="Saldo tidak cukup":
            self.Show_SaldoKurang()
            self.hide_RFID()
            self.logika6()
        
    def deteksi2(self):
        botol=irsensor.deteksibotol2()
        print(botol)
        
        if botol==1:
            self.timer.stop()
            
            self.timer = QTimer()
            self.timer.setInterval(1000)
            self.timer.timeout.connect(self.pompa1000)
            self.timer.start()
    
    def pompa1000(self):
        #aktifin relay selama time.sleep
        pompa = Relay.pompa(31.6)
        if pompa==1:
            self.timer.stop()
            self.Show_menu()
            self.hide_TaruhBotol()
            
    def pilih1500(self):
        self.Show_RFID()
        self.logika5()
        self.hide_water()
        
    def logika5(self):
        self.timer = QTimer()
        self.timer.setInterval(2000)
        self.timer.timeout.connect(self.deteksiRFID3)
        self.timer.start()
        
    def deteksiRFID3(self):
        id=RFID_read.bacaRFID()
        
        if id>0:
            print("id terdeteksi")
            self.timer.stop()
            
        url = 'https://bulbous-markets.000webhostapp.com/proses.php'
        obj = {'uid': id, 'harga':'1500'}

        x = requests.post(url, data = obj)
        respon = x.json()
        status=respon['Detail']['Status']

        if status=="Transaksi Sukses":
            self.Show_TaruhBotol()
            self.hide_RFID()
            
            self.timer = QTimer()
            self.timer.setInterval(1000)
            self.timer.timeout.connect(self.deteksi3)
            self.timer.start()
            
        elif status=="ID Belum Terdaftar":
            self.Show_KartuTidakTerdaftar()
            self.hide_RFID()
            self.logika6()
            
        elif status=="Saldo tidak cukup":
            self.Show_SaldoKurang()
            self.hide_RFID()
            self.logika6()
            
    def deteksi3(self):
        botol=irsensor.deteksibotol2()
        print(botol)
        
        if botol==1:
            self.timer.stop()
            
            self.timer = QTimer()
            self.timer.setInterval(1000)
            self.timer.timeout.connect(self.pompa1500)
            self.timer.start()
    
    def pompa1500(self):
        #aktifin relay selama time.sleep
        pompa = Relay.pompa(47.4)
        if pompa==1:
            self.timer.stop()
            self.Show_menu()
            self.hide_TaruhBotol()

        
    #Halaman Menu----------------------------------------------------------#
    def Show_menu(self):
        self.water = QtWidgets.QMainWindow()
        self.ui = ui_menu()
        self.ui.setupUi(self.water)
        
        self.ui.pushButton1.clicked.connect(self.pilih500)
        self.ui.pushButton2.clicked.connect(self.pilih1000)
        self.ui.pushButton3.clicked.connect(self.pilih1500)
    
        self.water.showMaximized()
        
    def hide_water(self):
        self.water = QtWidgets.QMainWindow()
        self.ui = ui_menu()
        self.ui.setupUi(self.water)
        self.water.hide()
        
    def Show_TaruhBotol(self):
        self.TaruhBotol = QtWidgets.QMainWindow()
        self.ui = Ui_TaruhBotol()
        self.ui.setupUi(self.TaruhBotol)

        self.TaruhBotol.showMaximized()
        
    def hide_TaruhBotol(self):
        self.TaruhBotol = QtWidgets.QMainWindow()
        self.ui = Ui_TaruhBotol()
        self.ui.setupUi(self.TaruhBotol)
        self.TaruhBotol.hide()
        
    def Show_RFID(self):
        self.RFID = QtWidgets.QMainWindow()
        self.ui = Ui_RFID()
        self.ui.setupUi(self.RFID)
        
        self.RFID.showMaximized()
        
    def hide_RFID(self):
        self.RFID = QtWidgets.QMainWindow()
        self.ui = Ui_RFID()
        self.ui.setupUi(self.RFID)
        self.RFID.hide()
        
    def Show_StockHabis(self):
        self.StockHabis = QtWidgets.QMainWindow()
        self.ui = Ui_StockHabis()
        self.ui.setupUi(self.StockHabis)
        
        self.ui.pushButton6.clicked.connect(self.CekRefill)
        
        self.StockHabis.showMaximized()
        
    def hide_StockHabis(self):
        self.StockHabis = QtWidgets.QMainWindow()
        self.ui = Ui_StockHabis()
        self.ui.setupUi(self.StockHabis)
        self.StockHabis.hide()
        
    def Show_KartuTidakTerdaftar(self):
        self.KartuTidakTerdaftar = QtWidgets.QMainWindow()
        self.ui = Ui_KartuTidakTerdaftar()
        self.ui.setupUi(self.KartuTidakTerdaftar)
        
        self.KartuTidakTerdaftar.showMaximized()
        
    def hide_KartuTidakTerdaftar(self):
        self.KartuTidakTerdaftar = QtWidgets.QMainWindow()
        self.ui = Ui_KartuTidakTerdaftar()
        self.ui.setupUi(self.KartuTidakTerdaftar)
        self.KartuTidakTerdaftar.hide()
        
    def Show_SaldoKurang(self):
        self.SaldoKurang = QtWidgets.QMainWindow()
        self.ui = Ui_SaldoKurang()
        self.ui.setupUi(self.SaldoKurang)
        
        self.SaldoKurang.showMaximized()
        
    def hide_SaldoKurang(self):
        self.SaldoKurang = QtWidgets.QMainWindow()
        self.ui = Ui_SaldoKurang()
        self.ui.setupUi(self.SaldoKurang)
        self.SaldoKurang.hide()
    #-------------------------------------------------------------------------#
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Controller = Controller()
    Controller.logika()
    sys.exit(app.exec_())