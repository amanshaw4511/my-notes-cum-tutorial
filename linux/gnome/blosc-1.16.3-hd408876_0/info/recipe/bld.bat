import QtQuick.tooling 1.1

// This file describes the plugin-supplied types contained in the library.
// It is used for QML tooling purposes only.
//
// This file was auto-generated with the command 'qmlplugindump -noinstantiate -nonrelocatable QtWebKit 3.0'.

Module {
    Component {
        name: "QIODevice"
        prototype: "QObject"
        Signal { name: "readyRead" }
        Signal {
            name: "bytesWritten"
            Parameter { name: "bytes"; type: "qlonglong" }
        }
        Signal { name: "aboutToClose" }
        Signal { name: "readChannelFinished" }
    }
    Component {
        name: "QNetworkReply"
        prototype: "QIODevice"
        exports: ["QtWebKit/NetworkReply 3.0"]
        exportMetaObjectRevisions: [0]
        Enum {
            name: "NetworkError"
            values: {
                "NoError": 0,
                "ConnectionRefusedError": 1,
                "RemoteHostClosedError": 2,
                "HostNotFoundE