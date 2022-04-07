#!/usr/bin/python3 

import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import (
    QWidget,
    QLineEdit,
    QGroupBox,
    QGridLayout,
    QPushButton,
    QLabel,
    QApplication,
    QHBoxLayout,
    QMessageBox
)
from modules.readconf import readconf
from modules.webview import SearchEngineView

class Magellan(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.config = readconf()
        self.mainbox = QGroupBox("Engines")
        self.secondwindow = None
        self.searchbox = QLineEdit()
        self.searchterm = None
        self.searchbutton = QPushButton("Search")
        self.searchbutton.setStyleSheet('')
        self.googlebutton = QPushButton('Google')
        self.googlebutton.setFixedHeight(20)
        self.yahoobutton = QPushButton('Yahoo')
        self.yahoobutton.setFixedHeight(20)
        self.bingbutton = QPushButton('Bing')
        self.bingbutton.setFixedHeight(20)
        self.duckduckgobutton = QPushButton('DuckduckGo')
        self.duckduckgobutton.setFixedHeight(20)
        self.qwantbutton = QPushButton('Qwant')
        self.qwantbutton.setFixedHeight(20)
        self.baidubutton = QPushButton('Baidu')
        self.baidubutton.setFixedHeight(20)
        self.aolbutton = QPushButton('Aol')
        self.aolbutton.setFixedHeight(20)
        self.askbutton = QPushButton('Ask')
        self.askbutton.setFixedHeight(20)
        self.excitebutton = QPushButton('Excite')
        self.excitebutton.setFixedHeight(20)
        self.yandexbutton = QPushButton('Yandex')
        self.yandexbutton.setFixedHeight(20)
        self.qihoobutton = QPushButton('QihooSE')
        self.qihoobutton.setFixedHeight(20)
        self.naverbutton = QPushButton('Naver')
        self.naverbutton.setFixedHeight(20)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Magellan World Browser")
        self.resize(350, 450)

        # main layout 
        layout = QHBoxLayout()
        layout.addWidget(self.mainbox)
        mainboxLayout = QGridLayout()
        #mainboxLayout.setSpacing(0)
        self.mainbox.setLayout(mainboxLayout)

        # searchbox
        mainboxLayout.addWidget(self.searchbox, 0, 0, 1, 2)

        self.searchbutton.clicked.connect(self.search)
        mainboxLayout.addWidget(self.searchbutton, 1, 0, 1, 2)

        # Browsers
        self.googlebutton.clicked.connect(self.webview)
        mainboxLayout.addWidget(self.googlebutton, 2, 0)

        self.yahoobutton.clicked.connect(self.webview)
        mainboxLayout.addWidget(self.yahoobutton, 2, 1)

        self.bingbutton.clicked.connect(self.webview)
        mainboxLayout.addWidget(self.bingbutton, 3, 0)

        self.duckduckgobutton.clicked.connect(self.webview)
        mainboxLayout.addWidget(self.duckduckgobutton, 3, 1)

        self.qwantbutton.clicked.connect(self.webview)
        mainboxLayout.addWidget(self.qwantbutton, 4, 0)

        self.baidubutton.clicked.connect(self.webview)
        mainboxLayout.addWidget(self.baidubutton, 4, 1)

        self.aolbutton.clicked.connect(self.webview)
        mainboxLayout.addWidget(self.aolbutton, 5, 0)
        
        self.askbutton.clicked.connect(self.webview)
        mainboxLayout.addWidget(self.askbutton, 5, 1)

        self.excitebutton.clicked.connect(self.webview)
        mainboxLayout.addWidget(self.excitebutton, 6, 0)

        self.yandexbutton.clicked.connect(self.webview)
        mainboxLayout.addWidget(self.yandexbutton, 6, 1)

        self.qihoobutton.clicked.connect(self.webview)
        mainboxLayout.addWidget(self.qihoobutton, 7, 0)

        self.naverbutton.clicked.connect(self.webview)
        mainboxLayout.addWidget(self.naverbutton, 7, 1)


        # Main layout
        self.setLayout(layout)


    def search(self):
        #self.search_engine = self.sender().text()
        # FAIRE UNE BOUCLE POUR UPDATE TOUS LES SEARCH_ENGINE
        # SEARCH_ENGINE LISTE EN DURE

        #self.search_engine = 'Google'
        search_engines = [
                "Google",
                "Yahoo",
                "Bing",
                "DuckduckGo",
                "Qwant"
        ]
        self.searchterm = self.searchbox.text()
        for engine in search_engines:
            self.webview_window = SearchEngineView(engine, self.searchterm)
            self.webview_window.update_webview(engine)
            print(engine)


    def webview(self):
        search_engine = self.sender().text()
        print('sender = ' +search_engine)
        if self.secondwindow is None:
            self.secondwindow = SearchEngineView(search_engine=search_engine, searchterm=self.searchterm)
            self.secondwindow.show()
        else:
            self.secondwindow.destroy()
            self.secondwindow = SearchEngineView(search_engine=search_engine, searchterm=self.searchterm)
            self.secondwindow.show()

stylesheet = """
    Magellan {
        background-color: #1E2021; 
    }
    QGroupBox {
        background-image: url("rosa_blue.png");
        background-repeat: no-repeat;
        background-position: center;
        background-color: #1E2021; 
        color: white;
    }
    QPushButton {
        background-color: #383C4A;
        color:white;
    }
    QLineEdit {
        background-color: #383C4A;
        color:white;
    }
"""

if __name__ == '__main__':
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
        app.setStyleSheet(stylesheet)

    fen = Magellan()
    fen.show()

    app.exec_()
