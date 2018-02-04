import QtQuick 2.9
import QtQuick.Controls 2.2
import QtQuick.Window 2.3

Item{
    Rectangle{
        id: mainWindow
        objectName: "mainWindow"
        visible: true
        width: 400
        height: 400
        color: "#000000"

        MouseArea {
            anchors.fill: parent
            onClicked: {
                console.log("Mouse clicked!", parent.color)
                if (parent.color == "#000000")
                    parent.color = 'blue';
                else
                    parent.color = 'black';
            }
        }
    }
}
