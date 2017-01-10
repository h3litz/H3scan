__author__ = 'helit'
import sys
# import glob
import os
# import signal
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebKitWidgets import QWebPage

class Crawler(QWebPage):
    def __init__(self, url,file):
        QWebPage.__init__(self)
        self._url = url
        self._file = file

    def crawl(self):
        self.loadFinished.connect(self.__loadFinished)
        print('载入网页..')
        self.mainFrame().load(QUrl(self._url))

    def __loadFinished(self, result):
        print('执行脚本..')
        file = open(self._file,'w')
        file.write(self.mainFrame().toHtml())
        file.close()
        sys.exit(0)

def main():
    url = 'http://demo.aisec.cn/demo/aisec/'
    print(sys.path[0])
    file = os.path.join(sys.path[0], 'result/test.html')
    app = QApplication(sys.argv)
    crawler = Crawler(url,file)
    crawler.crawl()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
