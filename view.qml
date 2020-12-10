import QtQuick.Window 2.2
import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0

ApplicationWindow {
      id: qmlGuiWindow
      visible:true
      title: qsTr("QtQmlTest")
      width:640
      height:280

      Rectangle {
          Switch {
                id: mySwitch
                text: qsTr("This is a switch")
                onClicked: {
                    console.log("switch was clicked")
                    myPythonFunction.TestPrint("This is from QML")        // try calling python function
                }
          }
      }
}
