from PyQt5 import QtCore, QtGui, QtWidgets
from mlops_projesi import predict_weather


class Ui_MainWindow(object):
    #butona tıklandığında tahmin fonksiyonunu çağır.
    def func(self):
        self.tahmin_buton.clicked.connect(self.tahmin)

    #Verileri alma, tahmin yapma ve sonucu yazdırma
    def tahmin(self):
        yagis = float(self.yagis_input.text())
        maxsicaklik = float(self.maxsicaklik_input.text())
        minsicaklik = float(self.minsicaklik_input.text())
        ruzgar = float(self.ruzgar_input.text())
        gun = int(self.gun_input.text())
        ay = int(self.ay_input.text())
        yil = int(self.yil_input.text())

        sonuc = predict_weather(yagis, maxsicaklik, minsicaklik, ruzgar, gun, ay, yil)
        self.sonuc_output.setText(sonuc)


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
        self.bg1.setStyleSheet("background-color: #FF0000;\n""background-image: url(:/bg/1.png);")
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
        self.bg2.setStyleSheet("background-color: #FF0000;\n""background-image: url(:/bg/1.png);")
        self.bg2.setObjectName("bg2")
        self.tablo = QtWidgets.QWidget(self.bg2)
        self.tablo.setGeometry(QtCore.QRect(610, 360, 511, 271))
        self.tablo.setStyleSheet("background-image: url(:/tabloo/a.png)\n""")
        self.tablo.setObjectName("tablo")
        self.seffaf_bg1 = QtWidgets.QWidget(self.proje_icerik)
        self.seffaf_bg1.setGeometry(QtCore.QRect(40, 40, 551, 611))
        self.seffaf_bg1.setStyleSheet("border-radius:10px;\n""background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.954, y2:0.057, stop:0 rgba(221, 173, 132, 150), stop:0.965174 rgba(241, 211, 156, 150));\n""")
        self.seffaf_bg1.setObjectName("seffaf_bg1")
        self.proje_icerik_baslik_label = QtWidgets.QLabel(self.seffaf_bg1)
        self.proje_icerik_baslik_label.setGeometry(QtCore.QRect(190, 10, 181, 51))
        self.proje_icerik_baslik_label.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n""color: rgb(0,0,127);\n""background-color: rgba(255, 255, 255, 0);")
        self.proje_icerik_baslik_label.setObjectName("proje_icerik_baslik_label")
        self.proje_icerik_metin_label = QtWidgets.QLabel(self.seffaf_bg1)
        self.proje_icerik_metin_label.setGeometry(QtCore.QRect(20, 50, 511, 541))
        self.proje_icerik_metin_label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n""color: rgb(0,0,0);\n""background-color: rgba(255, 255, 255, 0);")
        self.proje_icerik_metin_label.setObjectName("proje_icerik_metin_label")
        self.veriseti_baslik = QtWidgets.QLabel(self.proje_icerik)
        self.veriseti_baslik.setGeometry(QtCore.QRect(630, 80, 131, 51))
        self.veriseti_baslik.setStyleSheet("font: bold 14pt \"MS Shell Dlg 2\";\n""background-color: rgba(255, 255, 255, 0);\n""color: rgb(0, 0, 127);")
        self.veriseti_baslik.setObjectName("veriseti_baslik")
        self.veriseti_label = QtWidgets.QLabel(self.proje_icerik)
        self.veriseti_label.setGeometry(QtCore.QRect(630, 100, 501, 270))
        self.veriseti_label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n""color: rgb(0, 0, 0);\n""background-color: rgba(255, 255, 255, 0);")
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
        self.bg3_3.setStyleSheet("background-color: #FF0000;\n""background-image: url(:/bg/1.png);")
        self.bg3_3.setObjectName("bg3_3")
        self.uygulamabaslik_label = QtWidgets.QLabel(self.uygulamamiz)
        self.uygulamabaslik_label.setGeometry(QtCore.QRect(500, 40, 181, 41))
        self.uygulamabaslik_label.setStyleSheet("font: bold 18pt \"MS Shell Dlg 2\";\n""background-color: rgba(255, 255, 255, 0);\n""color: rgb(0, 0, 127);")
        self.uygulamabaslik_label.setObjectName("uygulamabaslik_label")
        self.uygulama1_label = QtWidgets.QLabel(self.uygulamamiz)
        self.uygulama1_label.setGeometry(QtCore.QRect(100, 80, 1011, 121))
        self.uygulama1_label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n""color: rgb(0,0,0);\n""background-color: rgba(255, 255, 255, 0);\n""")
        self.uygulama1_label.setObjectName("uygulama1_label")
        self.seffaf_bg = QtWidgets.QWidget(self.uygulamamiz)
        self.seffaf_bg.setGeometry(QtCore.QRect(10, 220, 1161, 361))
        self.seffaf_bg.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.954, y2:0.057, stop:0 rgba(221, 173, 132, 150), stop:0.965174 rgba(241, 211, 156, 150));")
        self.seffaf_bg.setObjectName("seffaf_bg")
        self.maxsicaklik_label = QtWidgets.QLabel(self.seffaf_bg)
        self.maxsicaklik_label.setGeometry(QtCore.QRect(36, 140, 231, 41))
        self.maxsicaklik_label.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n""color: rgb(0,0,0);\n""background-color: rgba(255, 255, 255, 0);")
        self.maxsicaklik_label.setObjectName("maxsicaklik_label")
        self.minsicaklik_label = QtWidgets.QLabel(self.seffaf_bg)
        self.minsicaklik_label.setGeometry(QtCore.QRect(40, 200, 231, 41))
        self.minsicaklik_label.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n""color: rgb(0,0,0);\n""background-color: rgba(255, 255, 255, 0);")
        self.minsicaklik_label.setObjectName("minsicaklik_label")
        self.yil_label = QtWidgets.QLabel(self.seffaf_bg)
        self.yil_label.setGeometry(QtCore.QRect(360, 290, 51, 41))
        self.yil_label.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n""color: rgb(0,0,0);\n""background-color: rgba(255, 255, 255, 0);")
        self.yil_label.setObjectName("yil_label")
        self.minsicaklik_input = QtWidgets.QLineEdit(self.seffaf_bg)
        self.minsicaklik_input.setGeometry(QtCore.QRect(280, 200, 171, 41))
        self.minsicaklik_input.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n""color: rgb(0, 0, 79);")
        self.minsicaklik_input.setObjectName("minsicaklik_input")
        self.maxsicaklik_input = QtWidgets.QLineEdit(self.seffaf_bg)
        self.maxsicaklik_input.setGeometry(QtCore.QRect(280, 140, 171, 41))
        self.maxsicaklik_input.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n""color: rgb(0, 0, 79);")
        self.maxsicaklik_input.setObjectName("maxsicaklik_input")
        self.ruzgar_input = QtWidgets.QLineEdit(self.seffaf_bg)
        self.ruzgar_input.setGeometry(QtCore.QRect(280, 80, 171, 41))
        self.ruzgar_input.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n""color: rgb(0, 0, 79);")
        self.ruzgar_input.setObjectName("ruzgar_input")
        self.yagis_label = QtWidgets.QLabel(self.seffaf_bg)
        self.yagis_label.setGeometry(QtCore.QRect(187, 20, 81, 41))
        self.yagis_label.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n""color: rgb(0,0,0);\n""background-color: rgba(255, 255, 255, 0);")
        self.yagis_label.setObjectName("yagis_label")
        self.yagis_input = QtWidgets.QLineEdit(self.seffaf_bg)
        self.yagis_input.setGeometry(QtCore.QRect(280, 20, 171, 41))
        self.yagis_input.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n""color: rgb(0, 0, 79);")
        self.yagis_input.setObjectName("yagis_input")
        self.ruzgar_label = QtWidgets.QLabel(self.seffaf_bg)
        self.ruzgar_label.setGeometry(QtCore.QRect(170, 80, 91, 41))
        self.ruzgar_label.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n""color: rgb(0,0,0);\n""background-color: rgba(255, 255, 255, 0);")
        self.ruzgar_label.setObjectName("ruzgar_label")
        self.gun_label = QtWidgets.QLabel(self.seffaf_bg)
        self.gun_label.setGeometry(QtCore.QRect(40, 290, 61, 41))
        self.gun_label.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n""color: rgb(0,0,0);\n""background-color: rgba(255, 255, 255, 0);")
        self.gun_label.setObjectName("gun_label")
        self.ay_label = QtWidgets.QLabel(self.seffaf_bg)
        self.ay_label.setGeometry(QtCore.QRect(210, 290, 61, 41))
        self.ay_label.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n""color: rgb(0,0,0);\n""background-color: rgba(255, 255, 255, 0);")
        self.ay_label.setObjectName("ay_label")
        self.gun_input = QtWidgets.QLineEdit(self.seffaf_bg)
        self.gun_input.setGeometry(QtCore.QRect(100, 290, 71, 41))
        self.gun_input.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n""color: rgb(0, 0, 79);")
        self.gun_input.setObjectName("gun_input")
        self.ay_input = QtWidgets.QLineEdit(self.seffaf_bg)
        self.ay_input.setGeometry(QtCore.QRect(260, 290, 71, 41))
        self.ay_input.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n""color: rgb(0, 0, 79);")
        self.ay_input.setObjectName("ay_input")
        self.yil_input = QtWidgets.QLineEdit(self.seffaf_bg)
        self.yil_input.setGeometry(QtCore.QRect(410, 290, 71, 41))
        self.yil_input.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n""color: rgb(0, 0, 79);")
        self.yil_input.setObjectName("yil_input")
        self.uygulama2_label = QtWidgets.QLabel(self.seffaf_bg)
        self.uygulama2_label.setGeometry(QtCore.QRect(580, -70, 531, 331))
        self.uygulama2_label.setMinimumSize(QtCore.QSize(531, 331))
        self.uygulama2_label.setMaximumSize(QtCore.QSize(16777215, 331))
        self.uygulama2_label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n""background-color: rgba(255, 255, 255, 0);")
        self.uygulama2_label.setObjectName("uygulama2_label")
        self.sonuc_output = QtWidgets.QLineEdit(self.seffaf_bg)
        self.sonuc_output.setGeometry(QtCore.QRect(753, 290, 171, 41))
        self.sonuc_output.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n""color: rgb(0, 85, 0);")
        self.sonuc_output.setObjectName("sonuc_output")
        self.sonuc_label = QtWidgets.QLabel(self.seffaf_bg)
        self.sonuc_label.setGeometry(QtCore.QRect(660, 290, 81, 41))
        self.sonuc_label.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n""color: rgb(0,0,0);\n""background-color: rgba(255, 255, 255, 0);")
        self.sonuc_label.setObjectName("sonuc_label")
        self.tahmin_buton = QtWidgets.QPushButton(self.seffaf_bg)
        self.tahmin_buton.setGeometry(QtCore.QRect(660, 190, 261, 41))
        self.tahmin_buton.setStyleSheet("font: bold 13pt \"MS Shell Dlg 2\";\n""color: rgb(0, 0, 79);")
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
        self.proje_icerik_metin_label.setText(_translate("MainWindow", 
        "BIM104 Makine Öğrenmesi dersi kapsamında dönem sonu projesi\n"
        "olarak gerçekleştirilen bu çalışma, Kaggle'dan indirilen bir hava\n"
        "durumu veri seti üzerinde makine öğrenmesi algoritmalarını\n"
        "kullanarak hava durumu tahmini yapmayı amaçlamaktadır. Proje,\n"
        "veri setinin özelliklerinin analizini içermekte ve uygun bir\n"
        "makine öğrenmesi algoritması seçimi yapıldıktan sonra bu algoritma\n"
        "üzerinde eğitim gerçekleştirilerek hava durumu tahmini yapılacaktır.\n\n"
        "Hava durumu tahmini, birçok endüstri için önemli bir bilgi kaynağıdır.\n"
        "Örneğin, tarım sektörü açısından yağmur veya kuraklık tahminleri,\n"
        "hasat zamanlaması ve ürün verimliliği açısından kritik öneme\n"
        "sahiptir. İnşaat ve taşımacılık sektörleri ise planlama ve güvenlik\n"
        "amaçlarıyla hava durumu tahminlerine ihtiyaç duymaktadır. Turizm\n"
        "endüstrisi de tatil planlaması için hava durumu tahminlerini\n"
        "gözlemlemektedir Ayrıca, afet yönetimi ve acil durum müdahaleleri\n"
        "gibi durumlarda hava durumu tahminleri hayat kurtarıcı olabilmektedir. \n"
        "Bu proje kapsamında, veri analizi ve temizleme aşamaları büyük bir\n"
        "önem taşımaktadır. Veri setinin analizi, veri kümesinin içeriğini\n"
        "anlama, özelliklerin dağılımını ve ilişkilerini inceleme, eksik verileri\n"
        "tespit etme ve aykırı değerlerle başa çıkma süreçlerini içerir. Sonrasında\n"
        "tahmin için en uygun model seçilip eğitilecek ve test edilecektir. Tüm\n"
        "bu süreçte MLFLOW'dan faydalanılacaktır.\n"))

        self.veriseti_baslik.setText(_translate("MainWindow", "Veri Seti"))
        self.veriseti_label.setText(_translate("MainWindow", "Kaggle Weather Prediction\n"
"Bala Vashan\n"
"Bu veri seti, hava durumu tahminlerine odaklanmak için\n"
"toplanan geniş kapsamlı bir veri kümesidir. Toplamda 6 \n"
"sütun ve 96.454 satır içermektedir. Her bir satır, belirli\n"
"bir zaman dilimindeki hava durumu ölçümlerini temsil eder.\n"
"Veri seti:\n"
"- Çoklu datalar ile tahmin yapabilmesine\n"
"- Verisinin çok olmasına yani fazla satır sayısından oluşmasına \n"
"dikkat edilerek seçilmiştir."))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.proje_icerik), _translate("MainWindow", "Proje İçeriği"))
        self.uygulamabaslik_label.setText(_translate("MainWindow", "UYGULAMA"))
        self.uygulama1_label.setText(_translate("MainWindow", 
    "İlk olarak date sütunu, datetime modülü ile yıl, ay ve gün olmak üzere üç ayrı sütuna ayrıştırıldı. Daha sonra date sütunu silindi.\n"
    "Ardından, tekrarlanan satırlar ve boş değerler içeren satırlar ortalama değerlerle güncellendi. Veri tipleri string olan sütunlar,\n"
    "sayısal değerlere dönüştürüldü. Veriler bağımlı ve bağımsız değişkenler olarak ayrıldı. MLflow kullanılarak farklı eğitim modellerinde\n"
    "eğitim işlemi gerçekleştirildi ve sonuç olarak en iyi performansı gösteren modelin Random Forest olduğu belirlendi. Ardından, Random\n"
    "Forest modeli için en iyi sonuçları veren ağırlıkların bulunması için MLflow kullanılarak model eğitimi yapıldı.Son olarak, en iyi\n"
    "parametrelerle Random Forest modeli eğitildi ve kullanıcı tarafından girilen veriler için tahmin yapabilen bir arayüz oluşturuldu."))
        self.maxsicaklik_label.setText(_translate("MainWindow", "Max. Hava Sıcaklığı:"))
        self.minsicaklik_label.setText(_translate("MainWindow", "Min. Hava Sıcaklığı:"))
        self.yil_label.setText(_translate("MainWindow", "Yıl:"))
        self.yagis_label.setText(_translate("MainWindow", "Yağış:"))
        self.ruzgar_label.setText(_translate("MainWindow", "Rüzgar:"))
        self.gun_label.setText(_translate("MainWindow", "Gün:"))
        self.ay_label.setText(_translate("MainWindow", "Ay: "))
        self.uygulama2_label.setText(_translate("MainWindow", 
"Bu uygulama, MLflow yapay zeka platformunun kullanılmasıyla hava\n"
"durumu tahmininde bulunma sürecini kapsar. Veri analizi, veri\n"
"temizleme, model seçimi, model eğitimi ve tahmin işlemlerinin\n"
"adımları sistematik bir şekilde uygulanmıştır.\n"))
        self.sonuc_label.setText(_translate("MainWindow", "Sonuç:"))
        self.tahmin_buton.setText(_translate("MainWindow", "Tahmin Et"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.uygulamamiz), _translate("MainWindow", "Uygulamamız"))

import background_rc
import tablo_rc

# UI'nin kullanılacağı sınıf veya fonksiyonun içinde:
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    ui.func()
    window.show()
    app.exec_()
