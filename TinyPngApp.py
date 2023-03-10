
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from ui import Ui_TinyPngApp
import os
import tinify
import json


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.jsonfile = None
        self.ui = Ui_TinyPngApp()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('tinypng.ico'))
        if os.path.exists("./config.json"):
            with open("./config.json", "r") as openfile:
                self.jsonfile = json.load(openfile)
                if self.jsonfile["api"] != None:
                    self.ui.apiText.setText(self.jsonfile["api"])
                openfile.close()
        self.ui.srcBrowseBtn.clicked.connect(self.readSrc)
        self.ui.dstBrowseBtn.clicked.connect(self.readDst)
        self.ui.startBtn.clicked.connect(self.startCompress)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:

        return super().closeEvent(a0)

    def readSrc(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Source Path")
        if path != "":
            self.ui.srcText.setText(path)

    def readDst(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Distination Path")
        if path != "":
            self.ui.dstText.setText(path)

    def startCompress(self):
        rootDir = self.ui.srcText.text()
        dstDir = self.ui.dstText.text()
        if dstDir == "":
            dstDir = rootDir+"_Slim"
            os.makedirs(dstDir, exist_ok=True)
        apiKy = self.ui.apiText.text()
        with open("config.json", "w") as outfile:
            json.dump({"api": apiKy}, outfile)
        self.compress(rootDir, dstDir, apiKy)

    def compress(self, rootdir, dstdir, keyStr):
        self.ui.statusLabel.setText("Start")
        tinify.key = keyStr
        dirs = []
        for root, subdirs, files in os.walk(rootdir):
            for file in files:
                
                print(file)
                if "meta" not in file:
                    if ("png" in file.lower() or "jpg" in file.lower()):
                        filePath = os.path.join(root, file)
                        dstPath = root.replace(rootdir, dstdir)
                        outFilePath = os.path.join(dstPath, file)
                        if os.path.exists(outFilePath) and self.ui.skipCB.isChecked():
                            self.ui.statusLabel.setText("Exist Skipped:"+file)
                            continue
                        dirs.append((filePath, outFilePath, dstPath))
                        
        index = 0
        for (filePath, outFilePath, dstPath) in dirs:
            QtWidgets.QApplication.processEvents()
            self.ui.statusLabel.setText("Processing:"+file)
            source = tinify.from_file(filePath)
            os.makedirs(dstPath, exist_ok=True)
            source.to_file(outFilePath)
            index += 1
            self.ui.progressBar.setValue(int(index/len(dirs)*100))

        self.ui.statusLabel.setText("Image Compressing Completed")
        print("Image Compressing Completed")


def main():

    # Handle high resolution displays:
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(
            QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(
            QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
