import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from bs4 import BeautifulSoup as soup

class Client(QWebEnginePage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self._on_load_finished)
        self.load(QUrl(url))
        self.app.exec_()

    def _on_load_finished(self):
        self.html = self.toHtml(self.Callable)
        print('Load finished')

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()


# write things to file
filename = "aznews.csv"
f = open(filename, "w")
headers = "Newspaper Name, Website\n"
f.write(headers)

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
base_url = 'http://www.localmediauk.org/A-Z-Newsbrands?letter=A'

for i in alphabet:
    # get the container of info from the async js
    if __name__ == '__main__':
        next_url = base_url[:-1]
        next_url += i
        url = Client(next_url)
        page_soup = soup(url.html, 'html.parser')
        container = page_soup.findAll("a",{"class": "ql_res_item"})

    # extract name and website from the container
    for i in container:
        newspaper = i.text
        website = i['href']
        f.write(newspaper + "," + str(website) + "\n")
        print("newspaper: " + newspaper + "website: " + website)


# close the file writer
f.close()
