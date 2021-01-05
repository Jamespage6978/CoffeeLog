#pyuic5 -x "MainWindow.ui" -o "MainWindow.py"

from MainWindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time
import os
from datetime import datetime
import json



class ApplicationWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,*args,**kwargs):
        super(ApplicationWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.SaveButton.clicked.connect(self.SaveCurrentScreen)
        self.ui.HistoryButton.clicked.connect(ReadLogs)

        self.ui.AdvView.stateChanged.connect(self.AdvViewChanged)
        self.ui.BrewDateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.ui.RoastDate.setDateTime(QtCore.QDateTime.currentDateTime())
        
        self.ui.AromaQualSlide.setVisible(False)
        self.ui.AromaQuantSlide.setVisible(False)
        self.ui.AromaEdit.setVisible(False)
        self.ui.AromaLabel.setVisible(False)
        
        self.ui.AcidQualSlide.setVisible(False)
        self.ui.AcidQuantSlide.setVisible(False)
        self.ui.AcidEdit.setVisible(False)
        self.ui.AcidLabel.setVisible(False)
        
        self.ui.SweetQualSlide.setVisible(False)
        self.ui.SweetQuantSlide.setVisible(False)
        self.ui.SweetEdit.setVisible(False)
        self.ui.SweetLabel.setVisible(False)
        
        self.ui.BodyQualSlide.setVisible(False)
        self.ui.BodyQuantSlide.setVisible(False)
        self.ui.BodyEdit.setVisible(False)
        self.ui.BodyLabel.setVisible(False)
        
        self.ui.FinishQualSlide.setVisible(False)
        self.ui.FinishQuantSlide.setVisible(False)
        self.ui.FinishEdit.setVisible(False)
        self.ui.FinishLabel.setVisible(False)

        self.ui.QualLabel.setVisible(False)
        self.ui.QuantLabel.setVisible(False)
        self.ui.NotesLabel.setVisible(False)

    def AdvViewChanged(self,int):
        if self.ui.AdvView.isChecked():
            self.ui.AromaQualSlide.setVisible(True)
            self.ui.AromaQuantSlide.setVisible(True)
            self.ui.AromaEdit.setVisible(True)
            self.ui.AromaLabel.setVisible(True)
            
            self.ui.AcidQualSlide.setVisible(True)
            self.ui.AcidQuantSlide.setVisible(True)
            self.ui.AcidEdit.setVisible(True)
            self.ui.AcidLabel.setVisible(True)
            
            self.ui.SweetQualSlide.setVisible(True)
            self.ui.SweetQuantSlide.setVisible(True)
            self.ui.SweetEdit.setVisible(True)
            self.ui.SweetLabel.setVisible(True)
            
            self.ui.BodyQualSlide.setVisible(True)
            self.ui.BodyQuantSlide.setVisible(True)
            self.ui.BodyEdit.setVisible(True)
            self.ui.BodyLabel.setVisible(True)
            
            self.ui.FinishQualSlide.setVisible(True)
            self.ui.FinishQuantSlide.setVisible(True)
            self.ui.FinishEdit.setVisible(True)
            self.ui.FinishLabel.setVisible(True)

            self.ui.QualLabel.setVisible(True)
            self.ui.QuantLabel.setVisible(True)
            self.ui.NotesLabel.setVisible(True)
        else:
            self.ui.AromaQualSlide.setVisible(False)
            self.ui.AromaQuantSlide.setVisible(False)
            self.ui.AromaEdit.setVisible(False)
            self.ui.AromaLabel.setVisible(False)
            
            self.ui.AcidQualSlide.setVisible(False)
            self.ui.AcidQuantSlide.setVisible(False)
            self.ui.AcidEdit.setVisible(False)
            self.ui.AcidLabel.setVisible(False)
            
            self.ui.SweetQualSlide.setVisible(False)
            self.ui.SweetQuantSlide.setVisible(False)
            self.ui.SweetEdit.setVisible(False)
            self.ui.SweetLabel.setVisible(False)
            
            self.ui.BodyQualSlide.setVisible(False)
            self.ui.BodyQuantSlide.setVisible(False)
            self.ui.BodyEdit.setVisible(False)
            self.ui.BodyLabel.setVisible(False)
            
            self.ui.FinishQualSlide.setVisible(False)
            self.ui.FinishQuantSlide.setVisible(False)
            self.ui.FinishEdit.setVisible(False)
            self.ui.FinishLabel.setVisible(False)

            self.ui.QualLabel.setVisible(False)
            self.ui.QuantLabel.setVisible(False)
            self.ui.NotesLabel.setVisible(False)
            

        
    def SaveCurrentScreen(self):
        Name = self.ui.NameEdit.text()
        Roaster = self.ui.RoastEdit.text()
        if Name != "":
            dictName = f"{Name}_{Roaster}_{str(int(time.time()))}"
            Data = {dictName:[{
                        "Name" : self.ui.NameEdit.text(),
                        "Roaster" : self.ui.RoastEdit.text(),
                        "RoastDate" : self.ui.RoastDate.text(),
                        "BrewDate" : self.ui.BrewDateEdit.text(),
                        "AromaQualValue" : self.ui.AromaQualSlide.value(),
                        "AromaQuantValue" : self.ui.AromaQuantSlide.value(),
                        "AromaEdit" : self.ui.AromaEdit.toPlainText(),
                        "AcidQualValue" : self.ui.AcidQualSlide.value(),
                        "AcidQuantValue" : self.ui.AcidQuantSlide.value(),
                        "AcidEdit" : self.ui.AcidEdit.toPlainText(),
                        "SweetQualValue" : self.ui.SweetQualSlide.value(),
                        "SweetQuantValue" : self.ui.SweetQuantSlide.value(),
                        "SweetEdit" : self.ui.SweetEdit.toPlainText(),
                        "BodyQualValue" : self.ui.BodyQualSlide.value(),
                        "BodyQuantValue" : self.ui.BodyQuantSlide.value(),
                        "BodyEdit" : self.ui.BodyEdit.toPlainText(),
                        "FinishQualValue" : self.ui.FinishQualSlide.value(),
                        "FinishQuantValue" : self.ui.FinishQuantSlide.value(),
                        "FinishEdit" : self.ui.FinishEdit.toPlainText(),
                        "FlavourEdit" : self.ui.FlavoutEdit.toPlainText(),
                        "OverallScore" : self.ui.ScoreBox.value(),
                        "OverallEdit" : self.ui.OverallEdit.toPlainText()
                        }]
                    }
            with open('Data/CoffeeLogs.txt','r+') as f:
                dataIN = json.load(f)
                dataIN.update(Data)
                json.dump(dataIN,f,indent=4)
        else:
            QtWidgets.QMessageBox.about(self,"No Name", "Please provide a Coffe Name")

def ReadLogs():
    with open('Data/CoffeeLogs.txt') as f:
        data = json.load(f)
    print(data)
def loginit():
    if os.path.exists("Data/CoffeeLogs.txt"):
        #all good
        print("FoundFile")
    else:
        f = open("Data/CoffeeLogs.txt", "w")
        f.write("{}")
        f.close()

def main():
    loginit()
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()