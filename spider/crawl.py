__author__ = 'helit'
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebKitWidgets import QWebPage
# from xml import etree

#use QtWebkit to get the final webpage
class WebRender(QWebPage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.__loadFinished)
        self.mainFrame().load(QUrl(url))
        # self.app.platformName(minimal)
        self.app.exec_()

    def __loadFinished(self, result):
        self.frame = self.mainFrame()
        self.app.quit()

url = 'http://demo.aisec.cn/demo/aisec/'
r = WebRender(url)
html = r.frame.toHtml()
print(html)

