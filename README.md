# pyqt-openai-formatted-response-example
Implementing response of ChatGPT(plain text and source) as desktop application with Python (PyQt)

This simple app demonstrates how to create a John-like response using PyQt, which includes both plain text and source code.

For instance, consider the following response:

`````
To print "Hello, World!" 10 times in Python, you can use a loop. Here's an example:

```
for _ in range(10):
    print("Hello, World!")
```

In this code snippet, the `for` loop iterates 10 times. During each iteration, it executes the `print("Hello, World!")` statement, which will output "Hello, World!" to the console.
``````

This app utilizes a `QLabel` widget for the plain text portion and a `QTextBrowser` widget for the source code section. menu which includes a copy button is attached to the source code section.

## Requirements
* PyQt5 >= 5.14
* pyperclip - for "copy" feature
* pygments - to highlight the source

## How to Run
1. git clone ~
2. cd pyqt-openai-formatted-response-example
3. pip install -r requirements.txt
4. cd pyqt_openai_formatted_response_example
5. go to the main.py and give the text you want to give. If you want to include the source in text, you have to wrap it with "```".
```python
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = LblWithQTextBrowser()
    w.setText(
    [YOUR TEXT] # change this part
    )
    w.show()
    sys.exit(app.exec())
```
6. python main.py

## Result
![image](https://github.com/yjg30737/pyqt-openai-formatted-response-example/assets/55078043/89f440fb-2aa0-43f3-aaf9-8381c3fd8cec)
