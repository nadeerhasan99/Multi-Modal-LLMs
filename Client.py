# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
import requests
import json
import sys  



base_url = "https://478a-35-240-247-214.ngrok-free.app"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1048, 790)
        MainWindow.setStyleSheet("background-color: rgb(85, 170, 255);\n"
                                 "gridline-color: rgb(255, 255, 255);\n"
                                 "border-top-color: rgb(255, 255, 255);\n"
                                 "border-color: rgb(0, 0, 255);\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Add QTabWidget for multiple tabs
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1028, 730))
        self.tabWidget.setObjectName("tabWidget")

        # First Tab: Chat
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.chat = QtWidgets.QTextEdit(self.tab1)
        self.chat.setGeometry(QtCore.QRect(13, 60, 1021, 431))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.chat.setFont(font)
        self.chat.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.chat.setObjectName("chat")
        self.chat.setReadOnly(True)  

        self.label = QtWidgets.QLabel(self.tab1)
        self.label.setGeometry(QtCore.QRect(390, 20, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        self.Question = QtWidgets.QTextEdit(self.tab1)
        self.Question.setGeometry(QtCore.QRect(13, 576, 1021, 60))
        self.Question.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Question.setObjectName("Question")
        
        self.label_2 = QtWidgets.QLabel(self.tab1)
        self.label_2.setGeometry(QtCore.QRect(304, 520, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        
        self.send = QtWidgets.QPushButton(self.tab1)
        self.send.setGeometry(QtCore.QRect(10, 660, 501, 51))  
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.send.setFont(font)
        self.send.setStyleSheet("background-color: rgb(0, 0, 255);\n"
                                "gridline-color: rgb(255, 255, 255);\n"
                                "color: rgb(255, 255, 255);")
        self.send.setObjectName("send")
        self.send.setText("Send")  

        
        self.clear = QtWidgets.QPushButton(self.tab1)
        self.clear.setGeometry(QtCore.QRect(530, 660, 501, 51))  
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.clear.setFont(font)
        self.clear.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                 "color: rgb(255, 255, 255);")
        self.clear.setObjectName("clear")
        self.clear.setText("Clear Chat")  
        
        self.tabWidget.addTab(self.tab1, "Chat")

       
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")

        
        self.uploadButton = QtWidgets.QPushButton(self.tab2)
        self.uploadButton.setGeometry(QtCore.QRect(10, 10, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.uploadButton.setFont(font)
        self.uploadButton.setStyleSheet("background-color: rgb(0, 0, 255);\n"
                                        "color: rgb(255, 255, 255);")
        self.uploadButton.setObjectName("uploadButton")
        self.uploadButton.setText("Upload Image")

        
        self.splitContainer = QtWidgets.QWidget(self.tab2)
        self.splitContainer.setGeometry(QtCore.QRect(10, 60, 1001, 431))
        self.splitContainer.setObjectName("splitContainer")

        # Image Display Area (Left Half)
        self.imageLabel = QtWidgets.QLabel(self.splitContainer)
        self.imageLabel.setGeometry(QtCore.QRect(0, 0, 500, 431))
        self.imageLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.imageLabel.setObjectName("imageLabel")
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)

       
        self.imageAnswer = QtWidgets.QTextEdit(self.splitContainer)
        self.imageAnswer.setGeometry(QtCore.QRect(501, 0, 500, 431))
        self.imageAnswer.setStyleSheet("background-color: rgb(255, 255, 255);")
        font = QtGui.QFont()
        font.setPointSize(8)
        self.imageAnswer.setFont(font)
        self.imageAnswer.setObjectName("imageAnswer")
        self.imageAnswer.setReadOnly(True)

        # Image Question Text Area
        self.imageQuestion = QtWidgets.QTextEdit(self.tab2)
        self.imageQuestion.setGeometry(QtCore.QRect(10, 520, 1001, 60))
        self.imageQuestion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.imageQuestion.setObjectName("imageQuestion")

       
        self.askButton = QtWidgets.QPushButton(self.tab2)
        self.askButton.setGeometry(QtCore.QRect(10, 600, 1001, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.askButton.setFont(font)
        self.askButton.setStyleSheet("background-color: rgb(0, 0, 255);\n"
                                     "color: rgb(255, 255, 255);")
        self.askButton.setObjectName("askButton")
        self.askButton.setText("Ask about the image")

        self.tabWidget.addTab(self.tab2, "Image Upload")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1048, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.actionNew.setFont(font)
        self.actionNew.setObjectName("actionNew")
        self.menuFile.addAction(self.actionNew)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        self.send.clicked.connect(self.handleSendText) 
        self.clear.clicked.connect(self.clearChat)  
        self.uploadButton.clicked.connect(self.openImage)  
        self.askButton.clicked.connect(self.handleSendImageText)  

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " Multi route chat app "))
        self.label.setText(_translate("MainWindow", "Chat"))
        self.label_2.setText(_translate("MainWindow", "Enter your question:"))

    def handleSendText(self):
        question = self.Question.toPlainText().strip()
        if question:
            self.chat.append(f"<b>Question:</b> {question}")  
            self.Question.clear() 
           
            self.generate_text(question)

    def generate_text(self, question):
        endpoint = f"{base_url}/generate_text"
        headers = {"Content-Type": "application/json"}
        payload = {"inputs": question}

        try:
            response = requests.post(endpoint, headers=headers, json=payload)
            if response.status_code == 200:
                result = response.json()
                answer = result.get('generated_text', 'No response from server')
                self.chat.append(f"<b>Answer:</b> {answer}")  
            else:
                self.chat.append(f"Error: {response.status_code}\n{response.text}")
        except Exception as e:
            self.chat.append(f"Request failed: {str(e)}")

    def clearChat(self):
      
        self.chat.clear()

    def openImage(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(None, "Select Image", "",
                                                  "Image Files (*.png *.jpg *.jpeg *.bmp)", options=options)
        if fileName:
            pixmap = QPixmap(fileName)
            self.imageLabel.setPixmap(pixmap.scaled(self.imageLabel.size(), QtCore.Qt.KeepAspectRatio))
            self.imageAnswer.clear()  

    def handleSendImageText(self):
        image_question = self.imageQuestion.toPlainText().strip()
        if image_question and self.imageLabel.pixmap() is not None:
            self.imageQuestion.clear()  
            self.imageAnswer.append(f"<b>Question:</b> {image_question}")  
            
            self.generate_image_text(image_question)

    def generate_image_text(self, image_question):
        endpoint = f"{base_url}/generate_text_image"
        
        pixmap = self.imageLabel.pixmap()
        if pixmap is not None:
            file_name = "temp_image.jpg"
            pixmap.save(file_name)

            files = {'file': open(file_name, 'rb')}
            data = {'prompt': image_question}

            try:
                response = requests.post(endpoint, files=files, data=data)
                if response.status_code == 200:
                    result = response.json()
                    answer = result.get('generated_text', 'No response from server')
                    self.imageAnswer.append(f"<b>Answer:</b> {answer}")  
                else:
                    self.imageAnswer.append(f"Error: {response.status_code}\n{response.text}")
            except Exception as e:
                self.imageAnswer.append(f"Request failed: {str(e)}")


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        
        
        MainWindow.setFixedSize(MainWindow.size())  
        MainWindow.show()
        sys.exit(app.exec_())
    except SystemExit:
        print("Application closed successfully.")
    except Exception as e:
        print(f"Error: {e}")
