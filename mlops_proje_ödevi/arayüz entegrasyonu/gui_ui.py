from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1232, 784)
        MainWindow.setAccessibleDescription("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0.954, y2:0.057, stop:0 rgba(6, 0, 57, 206), stop:0.965174 rgba(237, 129, 0, 200));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bg1 = QtWidgets.QWidget(self.centralwidget)
        self.bg1.setGeometry(QtCore.QRect(0, 0, 1231, 731))
        self.bg1.setStyleSheet("background-color: #FF0000;\n"
"background-image: url(:/bg/1.png);")
        self.bg1.setObjectName("bg1")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 10, 1211, 701))
        self.tabWidget_2.setStyleSheet("")
        self.tabWidget_2.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_2.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.proje_icerik = QtWidgets.QWidget()
        self.proje_icerik.setObjectName("proje_icerik")
        self.bg2 = QtWidgets.QWidget(self.proje_icerik)
        self.bg2.setGeometry(QtCore.QRect(10, 10, 1161, 671))
        self.bg2.setStyleSheet("background-color: #FF0000;\n"
"background-image: url(:/bg/1.png);")
        self.bg2.setObjectName("bg2")
        self.tablo = QtWidgets.QWidget(self.bg2)
        self.tablo.setGeometry(QtCore.QRect(610, 360, 511, 271))
        self.tablo.setStyleSheet("background-image: url(:/tabloo/a.png)\n"
"")
        self.tablo.setObjectName("tablo")
        self.seffaf_bg1 = QtWidgets.QWidget(self.proje_icerik)
        self.seffaf_bg1.setGeometry(QtCore.QRect(40, 40, 551, 611))
        self.seffaf_bg1.setStyleSheet("border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.954, y2:0.057, stop:0 rgba(221, 173, 132, 150), stop:0.965174 rgba(241, 211, 156, 150));\n"
"")
        self.seffaf_bg1.setObjectName("seffaf_bg1")
        self.proje_icerik_baslik_label = QtWidgets.QLabel(self.seffaf_bg1)
        self.proje_icerik_baslik_label.setGeometry(QtCore.QRect(190, 10, 181, 51))
        self.proje_icerik_baslik_label.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n"
"color: rgb(0,0,127);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.proje_icerik_baslik_label.setObjectName("proje_icerik_baslik_label")
        self.proje_icerik_metin_label = QtWidgets.QLabel(self.seffaf_bg1)
        self.proje_icerik_metin_label.setGeometry(QtCore.QRect(20, 50, 511, 541))
        self.proje_icerik_metin_label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0,0,0);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.proje_icerik_metin_label.setObjectName("proje_icerik_metin_label")
        self.veriseti_baslik = QtWidgets.QLabel(self.proje_icerik)
        self.veriseti_baslik.setGeometry(QtCore.QRect(630, 50, 131, 51))
        self.veriseti_baslik.setStyleSheet("font: bold 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(0, 0, 127);")
        self.veriseti_baslik.setObjectName("veriseti_baslik")
        self.veriseti_label = QtWidgets.QLabel(self.proje_icerik)
        self.veriseti_label.setGeometry(QtCore.QRect(630, 100, 501, 161))
        self.veriseti_label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.veriseti_label.setObjectName("veriseti_label")
        self.tabWidget_2.addTab(self.proje_icerik, "")
        self.uygulamamiz = QtWidgets.QWidget()
        self.uygulamamiz.setObjectName("uygulamamiz")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.uygulamamiz)
        self.lineEdit_16.setGeometry(QtCore.QRect(690, 470, 251, 91))
        self.lineEdit_16.setStyleSheet("border-radius: 25px;")
        self.lineEdit_16.setText("")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.bg3_3 = QtWidgets.QWidget(self.uygulamamiz)
        self.bg3_3.setGeometry(QtCore.QRect(10, 10, 1161, 671))
        self.bg3_3.setStyleSheet("background-color: #FF0000;\n"
"background-image: url(:/bg/1.png);")
        self.bg3_3.setObjectName("bg3_3")
        self.uygulamabaslik_label = QtWidgets.QLabel(self.uygulamamiz)
        self.uygulamabaslik_label.setGeometry(QtCore.QRect(500, 40, 181, 41))
        self.uygulamabaslik_label.setStyleSheet("font: bold 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(0, 0, 127);")
        self.uygulamabaslik_label.setObjectName("uygulamabaslik_label")
        self.uygulama1_label = QtWidgets.QLabel(self.uygulamamiz)
        self.uygulama1_label.setGeometry(QtCore.QRect(100, 80, 1011, 121))
        self.uygulama1_label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0,0,0);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.uygulama1_label.setObjectName("uygulama1_label")
        self.seffaf_bg = QtWidgets.QWidget(self.uygulamamiz)
        self.seffaf_bg.setGeometry(QtCore.QRect(10, 220, 1161, 361))
        self.seffaf_bg.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.954, y2:0.057, stop:0 rgba(221, 173, 132, 150), stop:0.965174 rgba(241, 211, 156, 150));")
        self.seffaf_bg.setObjectName("seffaf_bg")
        self.maxsicaklik_label = QtWidgets.QLabel(self.seffaf_bg)
        self.maxsicaklik_label.setGeometry(QtCore.QRect(36, 140, 231, 41))
        self.maxsicaklik_label.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n"
"color: rgb(0,0,0);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.maxsicaklik_label.setObjectName("maxsicaklik_label")
        self.minsicaklik_label = QtWidgets.QLabel(self.seffaf_bg)
        self.minsicaklik_label.setGeometry(QtCore.QRect(40, 200, 231, 41))
        self.minsicaklik_label.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n"
"color: rgb(0,0,0);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.minsicaklik_label.setObjectName("minsicaklik_label")
        self.yil_label = QtWidgets.QLabel(self.seffaf_bg)
        self.yil_label.setGeometry(QtCore.QRect(360, 290, 51, 41))
        self.yil_label.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n"
"color: rgb(0,0,0);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.yil_label.setObjectName("yil_label")
        self.minsicaklik_input = QtWidgets.QLineEdit(self.seffaf_bg)
        self.minsicaklik_input.setGeometry(QtCore.QRect(280, 200, 171, 41))
        self.minsicaklik_input.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 79);")
        self.minsicaklik_input.setObjectName("minsicaklik_input")
        self.maxsicaklik_input = QtWidgets.QLineEdit(self.seffaf_bg)
        self.maxsicaklik_input.setGeometry(QtCore.QRect(280, 140, 171, 41))
        self.maxsicaklik_input.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 79);")
        self.maxsicaklik_input.setObjectName("maxsicaklik_input")
        self.ruzgar_input = QtWidgets.QLineEdit(self.seffaf_bg)
        self.ruzgar_input.setGeometry(QtCore.QRect(280, 80, 171, 41))
        self.ruzgar_input.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 79);")
        self.ruzgar_input.setObjectName("ruzgar_input")
        self.yagis_label = QtWidgets.QLabel(self.seffaf_bg)
        self.yagis_label.setGeometry(QtCore.QRect(187, 20, 81, 41))
        self.yagis_label.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n"
"color: rgb(0,0,0);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.yagis_label.setObjectName("yagis_label")
        self.yagis_input = QtWidgets.QLineEdit(self.seffaf_bg)
        self.yagis_input.setGeometry(QtCore.QRect(280, 20, 171, 41))
        self.yagis_input.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 79);")
        self.yagis_input.setObjectName("yagis_input")
        self.ruzgar_label = QtWidgets.QLabel(self.seffaf_bg)
        self.ruzgar_label.setGeometry(QtCore.QRect(170, 80, 91, 41))
        self.ruzgar_label.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n"
"color: rgb(0,0,0);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.ruzgar_label.setObjectName("ruzgar_label")
        self.gun_label = QtWidgets.QLabel(self.seffaf_bg)
        self.gun_label.setGeometry(QtCore.QRect(40, 290, 61, 41))
        self.gun_label.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n"
"color: rgb(0,0,0);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.gun_label.setObjectName("gun_label")
        self.ay_label = QtWidgets.QLabel(self.seffaf_bg)
        self.ay_label.setGeometry(QtCore.QRect(210, 290, 61, 41))
        self.ay_label.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n"
"color: rgb(0,0,0);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.ay_label.setObjectName("ay_label")
        self.gun_input = QtWidgets.QLineEdit(self.seffaf_bg)
        self.gun_input.setGeometry(QtCore.QRect(100, 290, 71, 41))
        self.gun_input.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 79);")
        self.gun_input.setObjectName("gun_input")
        self.ay_input = QtWidgets.QLineEdit(self.seffaf_bg)
        self.ay_input.setGeometry(QtCore.QRect(260, 290, 71, 41))
        self.ay_input.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 79);")
        self.ay_input.setObjectName("ay_input")
        self.yil_input = QtWidgets.QLineEdit(self.seffaf_bg)
        self.yil_input.setGeometry(QtCore.QRect(410, 290, 71, 41))
        self.yil_input.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 79);")
        self.yil_input.setObjectName("yil_input")
        self.uygulama2_label = QtWidgets.QLabel(self.seffaf_bg)
        self.uygulama2_label.setGeometry(QtCore.QRect(580, -70, 531, 331))
        self.uygulama2_label.setMinimumSize(QtCore.QSize(531, 331))
        self.uygulama2_label.setMaximumSize(QtCore.QSize(16777215, 331))
        self.uygulama2_label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(255, 255, 255, 0);")
        self.uygulama2_label.setObjectName("uygulama2_label")
        self.sonuc_output = QtWidgets.QLineEdit(self.seffaf_bg)
        self.sonuc_output.setGeometry(QtCore.QRect(753, 290, 171, 41))
        self.sonuc_output.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 0);")
        self.sonuc_output.setObjectName("sonuc_output")
        self.sonuc_label = QtWidgets.QLabel(self.seffaf_bg)
        self.sonuc_label.setGeometry(QtCore.QRect(660, 290, 81, 41))
        self.sonuc_label.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n"
"color: rgb(0,0,0);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.sonuc_label.setObjectName("sonuc_label")
        self.tahmin_buton = QtWidgets.QPushButton(self.seffaf_bg)
        self.tahmin_buton.setGeometry(QtCore.QRect(660, 190, 261, 41))
        self.tahmin_buton.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 79);")
        self.tahmin_buton.setObjectName("tahmin_buton")
        self.tabWidget_2.addTab(self.uygulamamiz, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1232, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.proje_icerik_baslik_label.setText(_translate("MainWindow", "PROJE İÇERİĞİ"))
        self.proje_icerik_metin_label.setText(_translate("MainWindow", "BIM104 Makine Öğrenmesi dersi kapsamında dönem sonu proje \n"
"ödev yapılmıştır.Bu proje, makine öğrenmesi algoritmaları kullanarak \n"
"Kaggle\'dan indirilen bir veri seti üzerinden hava durumu tahmini \n"
"yapmayı amaçlar. Veri setinin özelliklerinin analizi ve uygun \n"
"algoritmanın seçimi sonrasında, makine öğrenmesi modeli eğitilerek \n"
"hava durumu tahmini gerçekleştirilecektir. "))
        self.veriseti_baslik.setText(_translate("MainWindow", "Veri Seti"))
        self.veriseti_label.setText(_translate("MainWindow", "Weather in Szeged 2006-2016\n"
"12 Sütun 96.454 Satır\n"
"Bu veri seti, Macaristan\'ın Szeged şehrinde 2006-2016 yılları \n"
"arasındaki hava durumu verilerini içermektedir.  Veri seti:\n"
"- Çoklu datalar ile tahmin yapabilmesine\n"
"- Verisinin çok olmasına yani fazla satır sayısından oluşmasına \n"
"dikkat edilerek seçilmiştir."))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.proje_icerik), _translate("MainWindow", "Proje İçeriği"))
        self.uygulamabaslik_label.setText(_translate("MainWindow", "UYGULAMA"))
        self.uygulama1_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Aynı satırlar çıkartıldı. Eksik değerler &quot;Bilinmiyor&quot; ya da &quot;0&quot; olarak doldurulur. String değerler uygun integer değerlere çevrilir. </p><p align=\"center\">Random Forest modeli uygulanır. Stick Label operasyonu uygulanır.</p></body></html>"))
        self.maxsicaklik_label.setText(_translate("MainWindow", "Max. Hava Sıcaklığı:"))
        self.minsicaklik_label.setText(_translate("MainWindow", "Min. Hava Sıcaklığı:"))
        self.yil_label.setText(_translate("MainWindow", "Yıl:"))
        self.yagis_label.setText(_translate("MainWindow", "Yağış:"))
        self.ruzgar_label.setText(_translate("MainWindow", "Rüzgar:"))
        self.gun_label.setText(_translate("MainWindow", "Gün:"))
        self.ay_label.setText(_translate("MainWindow", "Ay: "))
        self.uygulama2_label.setText(_translate("MainWindow", "Hava  durumu  tahmini, çeşitli  endüstriler için önemli bir bilgidir.\n"
"Örneğin, tarım sektörü için yağmur veya kuraklık tahminleri hasat\n"
"zamanlaması ve ürün verimliliği açısından kritik olabilir. Inşaat ve\n"
"taşımacılık  sektörleri ise  planlama ve güvenlik için  hava durumu\n"
"tahminlerine ihtiyaç duyarlar. Turizm endüstrisi de tatil planlaması \n"
"için hava durumu tahminlerine bakar."))
        self.sonuc_label.setText(_translate("MainWindow", "Sonuç:"))
        self.tahmin_buton.setText(_translate("MainWindow", "Tahmin Et"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.uygulamamiz), _translate("MainWindow", "Uygulamamız"))
import background_rc
import tablo_rc
