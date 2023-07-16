
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from ui import Ui_TinyPngApp
import os
import tinify
import json
from multiprocessing import cpu_count
from PyQt5.QtCore import QRunnable, QThreadPool, QObject, pyqtSignal
import time

os.environ['REQUESTS_CA_BUNDLE'] = os.path.join(os.path.dirname(sys.argv[0]),'cacert.pem')
class Task(QRunnable):
    def __init__(self, filePath, outFilePath, dstPath, cb, errcb):
        super().__init__()
        self.filePath = filePath
        self.dstPath = dstPath
        self.outFilePath = outFilePath
        self.cb = cb
        self.errorCb = errcb

    def run(self):
        try:
            source = tinify.from_file(self.filePath)
            os.makedirs(self.dstPath, exist_ok=True)
            source.to_file(self.outFilePath)
            self.cb(self.outFilePath)
        except Exception as e:
            self.errorCb(Exception(self.outFilePath + " " + str(e)))


class CallbackHandler(QObject):
    task_completed = pyqtSignal(str)
    task_failed = pyqtSignal(Exception)

    def callback(self, path):
        self.task_completed.emit(path)

    def error_handler(self, error):
        self.task_failed.emit(error)


class ApplicationWindow(QtWidgets.QMainWindow):

    count = 0
    max = 0
    startTime = None

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
        try:
            rootDir = self.ui.srcText.text()
            dstDir = self.ui.dstText.text()
            if not os.path.exists(rootDir):
                self.ui.srcText.setText("")
                raise Exception("Source Path Not Found!")

            if dstDir == "":
                dstDir = rootDir+"_Slim"

                os.makedirs(dstDir, exist_ok=True)
            else:
                if not os.path.exists(dstDir):
                    self.ui.dstText.setText("")
                    raise Exception("Destination Path Not Found!")
            apiKy = self.ui.apiText.text()
            with open("config.json", "w") as outfile:
                json.dump({"api": apiKy}, outfile)
            self.compress(rootDir, dstDir, apiKy)
        except Exception as e:
            print(str(e))
            self.ui.statusLabel.setText(str(e))

    def onTinfyCompleted(self, path: str):
        print(path)
        self.count += 1
        self.ui.progressBar.setValue(self.count)
        self.ui.statusLabel.setText(
            "Compressing {0} of {1}.".format(self.count, self.max))

        if(self.count == self.max):
            totalTime = time.time() - self.startTime
            showS = "s"
            if self.max==1:
                showS = ""
            self.ui.statusLabel.setText(
                "{:d} image{} compressing completed,total process time: {:.2f} secs.".format(self.max, showS, totalTime))
            self.ui.startBtn.setEnabled(True)

    def onTinifyError(self, err: Exception):
        print(str(err))
        self.ui.statusLabel.setText(str(err))

    def compress(self, rootdir, dstdir, keyStr):
        self.ui.statusLabel.setText("Start")
        self.startTime = time.time()
        tinify.key = keyStr
        dirs = []
        for root, subdirs, files in os.walk(rootdir):
            for file in files:
                filename = file.lower()
                if filename.endswith(".png") or filename.endswith(".jpg"):
                    filePath = os.path.join(root, file)
                    dstPath = root.replace(rootdir, dstdir)
                    outFilePath = os.path.join(dstPath, file)
                    if os.path.exists(outFilePath) and self.ui.skipCB.isChecked():
                        self.ui.statusLabel.setText("Exist Skipped:"+file)
                        continue
                    dirs.append((filePath, outFilePath, dstPath))
        if len(dirs) == 0:
            self.ui.statusLabel.setText("No PNG Image found in the folder.")
            return
        self.count = 0
        self.ui.progressBar.setMaximum(len(dirs))
        self.ui.startBtn.setEnabled(False)
        self.ui.statusLabel.setText("Processing...")
        self.max = len(dirs)
        threadpool = QThreadPool.globalInstance()
        threadpool.setMaxThreadCount(cpu_count())
        callback_handler = CallbackHandler()
        callback_handler.task_completed.connect(self.onTinfyCompleted)
        callback_handler.task_failed.connect(self.onTinifyError)

        for (filePath, outFilePath, dstPath) in dirs:
            task = Task(filePath, outFilePath, dstPath,
                        callback_handler.callback, callback_handler.error_handler)
            threadpool.start(task)


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
