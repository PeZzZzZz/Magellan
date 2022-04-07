#!/usr/bin/python3 


import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
    QHBoxLayout,
    QGroupBox
)

class SearchEngineView(QWidget):
    def __init__(self, search_engine=None, searchterm=None):
        QWidget.__init__(self)
        self.setWindowTitle("Magellan World Browser")
        self.setStyleSheet("background-color: #1E2021; color: white;")
        self.search_engine = search_engine
        self.searchterm = searchterm
        self.mainbox = QGroupBox(search_engine)
        self.webview = QWebEngineView()

        self.googleview = QWebEngineView()
        self.yahooview = QWebEngineView()
        self.bingview = QWebEngineView()
        self.duckduckgoview = QWebEngineView()
        self.qwantview = QWebEngineView()
        self.baiduview = QWebEngineView()
        self.aolview = QWebEngineView()
        self.askview = QWebEngineView()
        self.exciteview = QWebEngineView()
        self.yandexview = QWebEngineView()
        self.qihooview = QWebEngineView()
        self.naverview = QWebEngineView()

        self.mainboxLayout = QHBoxLayout()

        self.initUI()

    def initUI(self):
        layout = QHBoxLayout()
        layout.addWidget(self.mainbox)

        mainboxLayout = QHBoxLayout()
        self.mainbox.setLayout(mainboxLayout)

        #self.search_engine = 'google'
        print(self.search_engine)
        if self.search_engine == 'Google':
            self.update_webview(self.search_engine)
            mainboxLayout.addWidget(self.googleview)
        if self.search_engine == 'Yahoo':
            self.update_webview(self.search_engine)
            mainboxLayout.addWidget(self.yahooview)
            print(self.yahooview.url())
        if self.search_engine == 'Bing':
            self.update_webview(self.search_engine)
            mainboxLayout.addWidget(self.bingview)
            print(self.bingview.url())
        if self.search_engine == 'DuckduckGo':
            self.update_webview(self.search_engine)
            mainboxLayout.addWidget(self.duckduckgoview)
            print(self.duckduckgoview.url())
        if self.search_engine == 'Qwant':
            self.update_webview(self.search_engine)
            mainboxLayout.addWidget(self.qwantview)
            print(self.qwantview.url())
        if self.search_engine == "Baidu":
            self.update_webview(self.search_engine)
            mainboxLayout.addWidget(self.baiduview)
            print(self.baiduview.url())
        if self.search_engine == "AOL":
            self.update_webview(self.search_engine)
            mainboxLayout.addWidget(self.aolview)
            print(self.aolview.url())
        if self.search_engine == "Ask":
            self.update_webview(self.search_engine)
            mainboxLayout.addWidget(self.askview)
            print(self.askview.url())
        if self.search_engine == "Excite":
            self.update_webview(self.search_engine)
            mainboxLayout.addWidget(self.exciteview)
            print(self.exciteview.url())
        if self.search_engine == "Yandex":
            self.update_webview(self.search_engine)
            mainboxLayout.addWidget(self.yandexview)
            print(self.yandexview.url())
        if self.search_engine == "QihooSE":
            self.update_webview(self.search_engine)
            mainboxLayout.addWidget(self.qihooview)
            print(self.qihooview.url())
        if self.search_engine == "Naver":
            self.update_webview(self.search_engine)
            mainboxLayout.addWidget(self.naverview)
            print(self.naverview.url())

        self.setLayout(layout)

    #def webview_(self, search_engine):

    def update_webview(self, search_engine):
        if search_engine == 'Google':
            url = 'https://www.google.com/search?channel=fs&q=%s' % self.searchterm
            self.googleview.setUrl(QUrl(url))
            self.googleview.update()
        if search_engine == 'Yahoo':
            url = 'https://fr.search.yahoo.com/search?p=%s' % self.searchterm
            self.yahooview.setUrl(QUrl(url))
            self.yahooview.update()
        if search_engine == 'Bing':
            url = 'https://www.bing.com/search?q=%s' % self.searchterm
            self.bingview.setUrl(QUrl(url))
            self.bingview.update()
        if search_engine == 'DuckduckGo':
            url = 'https://duckduckgo.com/?q=%s' % self.searchterm
            self.duckduckgoview.setUrl(QUrl(url))
            self.duckduckgoview.update()
        if search_engine == 'Qwant':
            url = 'https://www.qwant.com/?q=%s' % self.searchterm
            self.qwantview.setUrl(QUrl(url))
            self.qwantview.update()
        if search_engine == "Baidu":
            url = "https://www.baidu.com/s?wd=%s" % self.searchterm
            self.baiduview.setUrl(QUrl(url))
            self.baiduview.update()
        if search_engine == "AOL":
            url = "https://search.aol.com/aol/search;_ylt=AwrJ7J3W3k1ivucAPyBoCWVH;_ylc=X1MDMTE5NzgwMzg4MARfcgMyBGZyAwRmcjIDc2ItdG9wLXNlYXJjaARncHJpZANIVEJrUlJmQVRleW5EN0QzSkFuTlBBBG5fcnNsdAMwBG5fc3VnZwMxMARvcmlnaW4Dc2VhcmNoLmFvbC5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzQEcXVlcnkDVEVTVAR0X3N0bXADMTY0OTI3MDQ5NQ--?q=%s" % self.searchterm
            self.aolview.setUrl(QUrl(url))
            self.aolview.update()
        if search_engine == "Ask":
            url = "https://www.ask.com/web?q=%s" % self.searchterm
            self.askview.setUrl(QUrl(url))
            self.askview.update()
        if search_engine == "Excite":
            url = "https://results.excite.com/serp?q=%s" % self.searchterm
            self.exciteview.setUrl(QUrl(url))
            self.exciteview.update()
        if search_engine == "Yandex":
            url = "https://yandex.com/search/?text=%s" % self.searchterm
            self.yandexview.setUrl(QUrl(url))
            self.yandexview.update()
        if search_engine == "QihooSE":
            url = "https://www.so.com/s?q=%s" % self.searchterm
            self.qihooview.setUrl(QUrl(url))
            self.qihooview.update()
        if search_engine == "Naver":
            url = "https://search.naver.com/search.naver?query=%s" % self.searchterm
            self.naverview.setUrl(QUrl(url))
            self.naverview.update()

if __name__ == '__main__':

    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    search_engine = 'google'
    fen = SearchEngineView(search_engine=search_engine)
    fen.show()

    app.exec()
