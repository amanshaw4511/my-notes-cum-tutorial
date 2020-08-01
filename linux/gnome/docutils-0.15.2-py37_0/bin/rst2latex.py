          name: "setY"
            Parameter { name: "arg"; type: "int" }
        }
        Method {
            name: "setWidth"
            Parameter { name: "arg"; type: "int" }
        }
        Method {
            name: "setHeight"
            Parameter { name: "arg"; type: "int" }
        }
    }
    Component {
        name: "QQuickAbstractFileDialog"
        prototype: "QQuickAbstractDialog"
        Property { name: "selectExisting"; type: "bool" }
        Property { name: "selectMultiple"; type: "bool" }
        Property { name: "selectFolder"; type: "bool" }
        Property { name: "folder"; type: "QUrl" }
        Property { name: "nameFilters"; type: "QStringList" }
        Property { name: "selectedNameFilter"; type: "string" }
        Property { name: "selectedNameFilterE