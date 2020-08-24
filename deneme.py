import pymysql
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import requests
from bs4 import BeautifulSoup


class uygulama(QDialog):
    def __init__(self, parent=None, pymysql=None):
        super(uygulama, self).__init__(parent)
        grid = QGridLayout()

        grid.addWidget(QLabel("Altın Alış ve Satış fiyatı"), 0, 0)
        self.etiket = QLabel("Alış:")
        grid.addWidget(self.etiket, 1, 0)
        self.etiket2 = QLabel("Satış:")
        grid.addWidget(self.etiket2, 2, 0)
        self.etiket3 = QLabel(" ")
        grid.addWidget(self.etiket3, 1, 1)
        self.etiket4 = QLabel(" ")
        grid.addWidget(self.etiket4, 2, 1)

        buton = QPushButton("yenile")
        buton.clicked.connect(self.yenile)
        grid.addWidget(buton, 3, 0, 1, 2)

        grid.addWidget(QLabel("Önceki verilere göre altın verileri için tıklayınız..."), 4, 0)

        button = QPushButton("Grafik...")
        button.clicked.connect(self.tahminleme)
        grid.addWidget(button, 4, 0, 1, 2)

        self.setLayout(grid)
        self.setWindowTitle("uygulama")

        url = "http://bigpara.hurriyet.com.tr/altin/"
        url2 = "https://uzmanpara.milliyet.com.tr/altin-fiyatlari/"

        response2 = requests.get(url2)
        html2 = response2.content
        soup2 = BeautifulSoup(html2, "html.parser")

        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html, "html.parser")

        span = soup.find("span", {"class": "box"})
        alis = span.find("span", {"class": "value"}).text
        self.alis = alis.replace(",", ".")

        satis = soup2.find("div", {"class": "realTimeBoxR"}).text
        satis = satis.replace("SATIŞ (TL)", "")
        self.satis = satis.replace(",", ".")

        import pymysql

        conn = pymysql.connect(user='root', password='', host='localhost', database='proje')

        cur = conn.cursor()
        mySql_insert_query = """INSERT INTO altin (alis,satis)
                                        VALUES (%s, %s) """

        values = (self.alis, self.satis)
        cur.execute(mySql_insert_query, values)

        cursor = conn.cursor(pymysql.cursors.DictCursor)

        query = "SELECT * FROM `altin`"
        cursor.execute(query)

        data = cursor.fetchall()

        for row in data:
            alma = (row['alis'])
            satma = (row['satis'])

        conn.commit()

        conn.close()

        self.etiket3.setText(self.alis)
        self.etiket4.setText(self.satis)

    def tahminleme(self):
        import pandas as pd
        import matplotlib.pyplot  as plt
        import numpy as np

        df = pd.read_csv("C:/Users/kapla/OneDrive/Masaüstü/altin.csv", sep=";")
        y = df.alis.values.reshape(-1, 1)
        x = df.gun.values.reshape(-1, 1)
        plt.scatter(x, y)
        plt.ylabel("Altın Alış")
        plt.xlabel("Gün")
        # Kütüphane cagırma
        from sklearn.preprocessing import PolynomialFeatures
        from sklearn.linear_model import LinearRegression

        # Regresyonları Çagırma
        poly = PolynomialFeatures(degree=10)
        linear = LinearRegression()

        x_poly = poly.fit_transform(x)  #
        linear.fit(x_poly, y)  #

        y_headtahmincizgisi = linear.predict(x_poly)  #

        plt.plot(x, y_headtahmincizgisi, color="green", label="poly")
        plt.legend()  # Sol üste yazı atıyor
        plt.show()

    def yenile(self, grid=QGridLayout()):
        self.etiket3.setText(self.alis)
        self.etiket4.setText(self.satis)
        print(self.alis, self.satis)


app = QApplication([])
pencere = uygulama()
pencere.show()
app.exec()