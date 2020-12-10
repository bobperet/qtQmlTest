# Test code to understand calling a python method from QML

from PySide2.QtCore  import QObject, Signal, Slot
from PyQt5.QtQml     import QQmlApplicationEngine, qmlRegisterType, QQmlComponent, QQmlEngine
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick   import QQuickView
import sys

class Test(QObject):
    # something to call from QML to see if it works
    @Slot(str)
    def TestPrint(self, passedInString):
        print(passedInString)

#
# MAIN
#
if __name__ == '__main__':
    test = Test()
    testApp = QApplication(sys.argv)  # manages the GUI application's control flow and main settings

    engine.rootContext()->setContextProperty("Receiver", & rcvr);
    engine.load(QUrl(QStringLiteral("qrc:/main.qml")));

    engine = QQmlApplicationEngine()  # loads an application from a single QML file
    engine.load(QUrl(QStringLiteral('view.qml')));

    if not engine.rootObjects():
        qDebug("*** No root object!")  # (QML probably has syntax error)

    context = engine.rootContext()  # add to context for QML to see it
    context.setContextProperty("myPythonFunction", test)
    testApp.exec_()
    print("Application done")   # application has exited
