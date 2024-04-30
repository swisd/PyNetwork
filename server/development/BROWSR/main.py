from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QWidget
import os
import sys


class ThunderBrowser(QMainWindow):

    def __init__(self):

        super(ThunderBrowser, self).__init__()
        
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
    
        self.window = QWidget()

        self.window.setStyleSheet("background-color: #f0f0ff;" )

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)
        self.url_bar.setMinimumWidth(100)

        self.go_btn = QPushButton("GO")
        self.go_btn.setMaximumWidth(40)

        self.back_btn = QPushButton("<-")
        self.back_btn.setMaximumWidth(40)

        self.forward_btn = QPushButton("->")
        self.forward_btn.setMaximumWidth(40)

        self.reload_btn = QPushButton("*")
        self.reload_btn.setMaximumWidth(40)

        self.home_btn = QPushButton("/\\")
        self.home_btn.setMaximumWidth(40)

        
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)
        self.horizontal.addWidget(self.reload_btn)
        self.horizontal.addWidget(self.home_btn)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.url_bar)

        self.browser = QWebEngineView()

        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
        self.reload_btn.clicked.connect(self.browser.reload)

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.tabs.tabBar().setContextMenuPolicy(Qt.PreventContextMenu)
        self.tabs.tabBar().setTabsClosable(True)
        self.tabs.tabBar().tabCloseRequested.connect(lambda index: self.tabs.removeTab(index))
        self.tabs.tabBar().addTab("+")
        self.tabs.tabBar().tabBarClicked.connect(self.tab_bar_clicked)

        self.browser.setUrl(QUrl("https://google.com"))

        self.window.setLayout(self.layout)
        self.window.show()

    def navigate(self, url):
        if not url.startswith("http"):
            url = "http://" + url
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))
    
    def add_new_tab(self, qurl=None):
        if qurl is None:
            qurl = QUrl("https://google.com")
        
        self.browser.setUrl(qurl)

        i = self.tabs.addTab(self.browser, "New Tab")
        self.tabs.setCurrentIndex(i)

    def tab_bar_clicked(self, index):
        if index == self.tabs.count() - 1:
            self.add_new_tab()

    

app = QApplication([])
window = ThunderBrowser()
app.exec_()

