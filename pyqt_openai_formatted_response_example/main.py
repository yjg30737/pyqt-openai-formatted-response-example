import pyperclip

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextBrowser, QApplication, QHBoxLayout, QSpacerItem, \
    QSizePolicy
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import guess_lexer

from pyqt_openai_formatted_response_example.svgButton import SvgButton


class SourceBrowser(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        menuWidget = QWidget()
        lay = QHBoxLayout()

        self.__langLbl = QLabel()
        fnt = self.__langLbl.font()
        fnt.setBold(True)
        self.__langLbl.setFont(fnt)

        # SvgButton is supposed to be used like "copyBtn = SvgButton(self)" but it makes GUI broken so i won't give "self" argument to SvgButton
        copyBtn = SvgButton()
        copyBtn.setIcon('ico/copy.svg')
        copyBtn.clicked.connect(self.__copy)

        lay.addWidget(self.__langLbl)
        lay.addSpacerItem(QSpacerItem(10, 10, QSizePolicy.MinimumExpanding))
        lay.addWidget(copyBtn)
        lay.setAlignment(Qt.AlignRight)
        lay.setContentsMargins(2, 2, 2, 2)
        lay.setSpacing(1)

        menuWidget.setLayout(lay)
        menuWidget.setMaximumHeight(menuWidget.sizeHint().height())
        menuWidget.setStyleSheet('QWidget { background-color: #BBB }')

        self.__browser = QTextBrowser()
        lay = QVBoxLayout()
        lay.addWidget(menuWidget)
        lay.addWidget(self.__browser)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)
        self.setLayout(lay)

    def setText(self, lexer, text):
        self.__langLbl.setText(lexer.name)
        self.__browser.setText(text)

    def __copy(self):
        pyperclip.copy(self.__browser.toPlainText())


class LblWithQTextBrowser(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        lay = QVBoxLayout()
        lay.setSpacing(0)

        self.setLayout(lay)

    def setText(self, text):
        chunks = text.split('```')
        for i in range(len(chunks)):
            if i % 2 == 0:
                self.layout().addWidget(QLabel(chunks[i]))
            else:
                browser = SourceBrowser()

                # get the guessed language based on given code
                lexer = guess_lexer(chunks[i])
                print(lexer)
                formatter = HtmlFormatter(style='colorful')

                css_styles = formatter.get_style_defs('.highlight')

                SourceBrowser()

                html_code = f"""
                <html>
                    <head>
                        <style>
                            {css_styles}
                        </style>
                    </head>
                    <body>
                        {highlight(chunks[i], lexer, formatter)}
                    </body>
                </html>
                """
                browser.setText(lexer, html_code)
                self.layout().addWidget(browser)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = LblWithQTextBrowser()
    w.setText(
    '''
Sure! Here are five random two-line basic Python code snippets:

1. Generate a random number between 1 and 10:
```
import random
random_number = random.randint(1, 10)
print(random_number)
```

2. Check if a number is even or odd:
```
number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

3. Swap the values of two variables:
```
a = 5
b = 10
a, b = b, a
print("a =", a)
print("b =", b)
```

4. Find the maximum value in a list:
```
numbers = [3, 7, 1, 9, 2]
max_value = max(numbers)
print(max_value)
```

5. Calculate the factorial of a number:
```
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result)
```

Please note that these snippets are randomly selected and may not necessarily be related to each other.
    '''
    )
    w.show()
    sys.exit(app.exec())