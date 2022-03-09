from w import Ui_MainWindow
# from widget_11 import widget_11
from PyQt5 import QtCore, QtGui, QtWidgets

class widget_11(Ui_MainWindow):
    i_11 = 1
    lay = ""

    list_of_new_Label_nomer = []
    list_of_new_LineEdits = []
    list_of_new_LineEdits_istocnic = []
    list_of_new_SpinBox = []
    list_of_new_Label_shtuk = []

    outputDATA_from_LE = []
    outputDATA_from_SpinBox = []
    outputDATA_from_LE_ist = []

    def add_new_string(self):
        shift = 32 * widget_11.i_11
        if "добавляем лайбу номера" == "добавляем лайбу номера":
            widget_11.lay = QtWidgets.QLabel(self.frame_11)
            y = 79 + (shift)
            widget_11.lay.setGeometry(QtCore.QRect(10, y, 21, 21))
            widget_11.lay.setObjectName(f"mensale6_lbl_number_{widget_11.i_11 + 2}")
            widget_11.lay.setText(str(widget_11.i_11 + 2))
            widget_11.lay.setStyleSheet("background-color: rgb(177, 127, 66);\n"
                                 "border-radius: 5px;\n"
                                 "color: rgb(0, 0, 0);")
            widget_11.lay.setAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(10)
            font.setItalic(True)
            widget_11.lay.setFont(font)
            widget_11.lay.show()

            widget_11.list_of_new_Label_nomer.append(widget_11.lay)
            print("         widget_11.list_of_new_Label_nomer ", widget_11.list_of_new_Label_nomer)
        if "добавляем LE названия элемента" == "добавляем LE названия элемента":
            widget_11.lay = QtWidgets.QLineEdit(self.frame_11)
            y = 79 + (shift)
            widget_11.lay.setGeometry(QtCore.QRect(40, y, 374, 20))
            p = "mensale6_lbl_elem_" + str(widget_11.i_11 + 2)
            widget_11.lay.setObjectName(p)
            widget_11.lay.setText("")
            widget_11.lay.setAlignment(QtCore.Qt.AlignLeft)
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(10)
            font.setItalic(True)
            widget_11.lay.setFont(font)
            widget_11.lay.setStyleSheet("background-color: rgb(177, 127, 66);\n"
                                 "color: rgb(109, 65, 12);\n"
                                 "border: 1px solid rgb(109, 65, 12);\n"
                                 "border-radius: 5px;")
            widget_11.lay.show()

            widget_11.list_of_new_LineEdits.append(widget_11.lay)
            print("         widget_11.list_of_new_LineEdits ", widget_11.list_of_new_LineEdits)
        iter = widget_11.i_11
        widget_11.lay.returnPressed.connect(lambda: widget_11.HANDLER_NEXT_x(self,iter))
        if "добавляем LE названия элемента" == "добавляем LE названия элемента":
            widget_11.lay = QtWidgets.QLineEdit(self.frame_11)
            y = 79 + (shift)
            widget_11.lay.setGeometry(QtCore.QRect(416, y, 71, 20))
            p = "mensale6_lbl_elem666_" + str(widget_11.i_11 + 2)
            widget_11.lay.setObjectName(p)
            widget_11.lay.setText("")
            widget_11.lay.setAlignment(QtCore.Qt.AlignLeft)
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(10)
            font.setItalic(True)
            widget_11.lay.setFont(font)
            widget_11.lay.setStyleSheet("background-color: rgb(177, 127, 66);\n"
                                 "color: rgb(109, 65, 12);\n"
                                 "border: 1px solid rgb(109, 65, 12);\n"
                                 "border-radius: 5px;")
            widget_11.lay.show()

            widget_11.list_of_new_LineEdits_istocnic.append(widget_11.lay)
            print("         widget_11.list_of_new_LineEdits_istocnic ", widget_11.list_of_new_LineEdits_istocnic)
        widget_11.lay.returnPressed.connect(lambda: widget_11.HANDLER_NEXT_x2(self, iter))
        if "добавляем SB количества" == "добавляем SB количества":
            widget_11.lay = QtWidgets.QSpinBox(self.frame_11)
            y = 79 + shift

            widget_11.lay.setGeometry(QtCore.QRect(490, y, 61, 22))
            widget_11.lay.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                 "color: rgb(109, 65, 12);\n"
                                 "border: 1px solid rgb(109, 65, 12);"
                                 )

            widget_11.lay.setMaximum(10000)

            widget_11.lay.setObjectName(f"mensale6_elem_{widget_11.i_11 + 2}")

            widget_11.lay.setAlignment(QtCore.Qt.AlignLeft)
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(10)
            font.setItalic(True)
            widget_11.lay.setFont(font)
            widget_11.lay.show()

            widget_11.list_of_new_SpinBox.append(widget_11.lay)
            print("         widget_11.list_of_new_SpinBox ", widget_11.list_of_new_SpinBox)
        if "добавляем LBL шт" == "добавляем LBL шт":
            widget_11.lay = QtWidgets.QLabel(self.frame_11)
            y = 79 + (shift)
            widget_11.lay.setGeometry(QtCore.QRect(557, y, 47, 20))
            widget_11.lay.setObjectName(f"mensale6_lbl_sht_{widget_11.i_11 + 2}")
            widget_11.lay.setText("шт.")
            widget_11.lay.setStyleSheet("background-color: None;")
            widget_11.lay.setAlignment(QtCore.Qt.AlignLeft)
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(12)
            font.setItalic(True)
            widget_11.lay.setFont(font)
            widget_11.lay.show()

            widget_11.list_of_new_Label_shtuk.append(widget_11.lay)
            print("         widget_11.list_of_new_Label_shtuk ", widget_11.list_of_new_Label_shtuk)

        buf = 181 + shift
        self.frame_11.setMinimumSize(QtCore.QSize(0, buf))
        buf = 110 + shift
        self.line_35.move(10, buf)
        buf = 138 + shift
        self.pushButton_59.move(280, buf)
        buf = 138 + shift
        self.pushButton_101.move(320, buf)
        widget_11.i_11 += 1

    def del_last_string(self):
        if len(widget_11.list_of_new_Label_nomer) >= 1:
            print("Del last string in the list on widget_11:")
            print("    iteration №: ", widget_11.i_11, " (+2):")
            print("delllllllllllllllllllllllllll",widget_11.i_11)
            len_Label_No = len(widget_11.list_of_new_Label_nomer)
            len_LE = len(widget_11.list_of_new_LineEdits)
            len_SB = len(widget_11.list_of_new_SpinBox)
            len_Label_Sht = len(widget_11.list_of_new_Label_shtuk)

            widget_11.list_of_new_Label_nomer[len_Label_No - 1].deleteLater()
            widget_11.list_of_new_LineEdits[len_LE - 1].deleteLater()
            widget_11.list_of_new_SpinBox[len_SB - 1].deleteLater()
            widget_11.list_of_new_Label_shtuk[len_Label_Sht - 1].deleteLater()

            widget_11.list_of_new_Label_nomer.remove(widget_11.list_of_new_Label_nomer[len_Label_No - 1])
            widget_11.list_of_new_LineEdits.remove(widget_11.list_of_new_LineEdits[len_LE - 1])
            widget_11.list_of_new_SpinBox.remove(widget_11.list_of_new_SpinBox[len_SB - 1])
            widget_11.list_of_new_Label_shtuk.remove(widget_11.list_of_new_Label_shtuk[len_Label_Sht - 1])

            buff = widget_11.i_11 - 1
            widget_11.i_11 = buff
            buff -= 1
            shift = 32 * buff
            buf = 138 + shift

            self.pushButton_59.move(280, buf)
            self.pushButton_101.move(320, buf)
            buf = 110 + shift
            self.line_35.move(10, buf)

            buf = 181 + shift
            self.frame_11.setMinimumSize(QtCore.QSize(0, buf))
            print("dellllllllllllllllllllllllll2", widget_11.i_11)

    def get_inputed_data(self):
        #LE
        print("Ending diagnostics and take all inf. inputed by injiner:")
        widget_11.outputDATA_from_LE = []
        widget_11.outputDATA_from_LE_ist = []
        widget_11.outputDATA_from_SpinBox = []

        widget_11.outputDATA_from_LE.append(self.mensale6_lbl_elem_1.text())
        widget_11.outputDATA_from_LE.append(self.mensale6_lbl_elem_2.text())
        for i in widget_11.list_of_new_LineEdits:
            widget_11.outputDATA_from_LE.append(i.text())
        print('     Get the list from LE on widget_11: ',widget_11.outputDATA_from_LE)

        widget_11.outputDATA_from_LE_ist.append(self.mensale6_lbl_elem_3.text())
        widget_11.outputDATA_from_LE_ist.append(self.mensale6_lbl_elem_4.text())
        for i in widget_11.list_of_new_LineEdits_istocnic:
            widget_11.outputDATA_from_LE_ist.append(i.text())
        print('     Get the list from LE (ist) on widget_11: ', widget_11.outputDATA_from_LE_ist)

        widget_11.outputDATA_from_SpinBox.append(self.mensale6__elem_1.text())
        widget_11.outputDATA_from_SpinBox.append(self.mensale6__elem_2.text())

        for i in widget_11.list_of_new_SpinBox:
            widget_11.outputDATA_from_SpinBox.append(i.text())
        print('     Get the list from SB on widget_11: ',widget_11.outputDATA_from_SpinBox)

    def HANDLER_NEXT_x(self,iter):
        widget_11.list_of_new_LineEdits_istocnic[iter-1].setFocus()
    def HANDLER_NEXT_x2(self,iter):
        try:
            widget_11.list_of_new_LineEdits[iter].setFocus()
        except:
            self.mensale7_le_elem_1.setFocus()

class widget_12(Ui_MainWindow):
    i_12 = 1
    lay = ""

    list_of_new_Label_nomer = []
    list_of_new_LineEdits = []
    list_of_new_LineEdits_ist = []
    list_of_new_SpinBox = []
    list_of_new_LE_edinitsy = []

    outputDATA_from_LE = []
    outputDATA_from_LE_ist = []
    outputDATA_from_SpinBox = []
    outputDATA_from_LE_Edinitsy = []

    def add_new_string(self):
        shift = 32 * widget_12.i_12
        if "добавляем лайбу номера" == "добавляем лайбу номера":
            widget_12.lay = QtWidgets.QLabel(self.frame_12)
            y = 79 + (shift)
            widget_12.lay.setGeometry(QtCore.QRect(10, y, 21, 21))
            widget_12.lay.setObjectName(f"mensale_lbl_number_{widget_12.i_12 + 2}")
            widget_12.lay.setText(str(widget_12.i_12 + 2))
            widget_12.lay.setStyleSheet("background-color: rgb(177, 127, 66);\n"
                                 "border-radius: 5px;\n"
                                 "color: rgb(0, 0, 0);")
            widget_12.lay.setAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(10)
            font.setItalic(True)
            widget_12.lay.setFont(font)
            widget_12.lay.show()

            widget_12.list_of_new_Label_nomer.append(widget_12.lay)
            print("         widget_12.list_of_new_Label_nomer ", widget_12.list_of_new_Label_nomer)
        if "добавляем LE названия элемента" == "добавляем LE названия элемента":
            widget_12.lay = QtWidgets.QLineEdit(self.frame_12)
            y = 79 + (shift)
            widget_12.lay.setGeometry(QtCore.QRect(40, y, 311, 20))
            p = "mensale7_lbl_elem_" + str(widget_12.i_12 + 2)
            widget_12.lay.setObjectName(p)
            widget_12.lay.setText("")
            widget_12.lay.setAlignment(QtCore.Qt.AlignLeft)
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(10)
            font.setItalic(True)
            widget_12.lay.setFont(font)
            widget_12.lay.setStyleSheet("background-color: rgb(177, 127, 66);\n"
                                 "color: rgb(109, 65, 12);\n"
                                 "border: 1px solid rgb(109, 65, 12);\n"
                                 "border-radius: 5px;")
            widget_12.lay.show()

            widget_12.list_of_new_LineEdits.append(widget_12.lay)
            print("         widget_12.list_of_new_LineEdits ", widget_12.list_of_new_LineEdits)
        iterr = widget_12.i_12
        widget_12.lay.returnPressed.connect(lambda: widget_12.HANDLER_NEXT_x(self, iterr))
        if "добавляем LE источника элемента" != "добавляем LE названия элемента":
            widget_12.lay = QtWidgets.QLineEdit(self.frame_12)
            y = 79 + (shift)
            widget_12.lay.setGeometry(QtCore.QRect(353, y, 94, 20))
            p = "mensale7_lbl_elem_" + str(widget_12.i_12 + 2)
            widget_12.lay.setObjectName(p)
            widget_12.lay.setText("")
            widget_12.lay.setAlignment(QtCore.Qt.AlignLeft)
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(10)
            font.setItalic(True)
            widget_12.lay.setFont(font)
            widget_12.lay.setStyleSheet("background-color: rgb(177, 127, 66);\n"
                                 "color: rgb(109, 65, 12);\n"
                                 "border: 1px solid rgb(109, 65, 12);\n"
                                 "border-radius: 5px;")
            widget_12.lay.show()

            widget_12.list_of_new_LineEdits_ist.append(widget_12.lay)
            print("         widget_12.list_of_new_LineEdits_ist ", widget_12.list_of_new_LineEdits_ist)
        widget_12.lay.returnPressed.connect(lambda: widget_12.HANDLER_NEXT_x2(self, iterr))
        if "добавляем SB количества" == "добавляем SB количества":
            widget_12.lay = QtWidgets.QSpinBox(self.frame_12)
            y = 79 + shift

            widget_12.lay.setGeometry(QtCore.QRect(450, y, 61, 22))
            widget_12.lay.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                 "color: rgb(109, 65, 12);\n"
                                 "border: 1px solid rgb(109, 65, 12);"
                                 )

            widget_12.lay.setMaximum(10000)

            widget_12.lay.setObjectName(f"mensale7_elem_{widget_12.i_12 + 2}")

            widget_12.lay.setAlignment(QtCore.Qt.AlignLeft)
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(10)
            font.setItalic(True)
            widget_12.lay.setFont(font)
            widget_12.lay.show()

            widget_12.list_of_new_SpinBox.append(widget_12.lay)
            print("         widget_12.list_of_new_SpinBox ", widget_12.list_of_new_SpinBox)
        if "добавляем LE шт" == "добавляем LE шт":
            widget_12.lay = QtWidgets.QLineEdit(self.frame_12)
            y = 79 + (shift)
            widget_12.lay.setGeometry(QtCore.QRect(520, y, 84, 20))
            widget_12.lay.setObjectName(f"mensale7_lbl_sht_{widget_12.i_12 + 2}")
            widget_12.lay.setText("шт.")
            widget_12.lay.setStyleSheet("background-color: rgb(177, 127, 66);\n"
                                        "color: rgb(109, 65, 12);\n"
                                        "border: 1px solid rgb(109, 65, 12);\n"
                                        "border-radius: 5px;")
            widget_12.lay.setAlignment(QtCore.Qt.AlignLeft)
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(8)
            font.setItalic(True)
            widget_12.lay.setFont(font)
            widget_12.lay.show()

            widget_12.list_of_new_LE_edinitsy.append(widget_12.lay)
            print("         widget_12.list_of_new_LE_edinitsy ", widget_12.list_of_new_LE_edinitsy)
        widget_12.lay.returnPressed.connect(lambda: widget_12.HANDLER_NEXT_x3(self, iterr))

        buf = 181 + shift
        self.frame_12.setMinimumSize(QtCore.QSize(0, buf))
        buf = 110 + shift
        self.line_36.move(10, buf)
        buf = 138 + shift
        self.pushButton_102.move(280, buf)
        buf = 138 + shift
        self.pushButton_103.move(320, buf)
        widget_12.i_12 += 1

    def del_last_string(self):
        if len(widget_12.list_of_new_Label_nomer) >= 1:
            print("Del last string in the list on widget_12:")
            print("    iteration №: ", widget_12.i_12, " (+2):")
            print("delllllllllllllllllllllllllll",widget_12.i_12)
            len_Label_No = len(widget_12.list_of_new_Label_nomer)
            len_LE = len(widget_12.list_of_new_LineEdits)
            len_SB = len(widget_12.list_of_new_SpinBox)
            len_Label_Sht = len(widget_12.list_of_new_LE_edinitsy)

            widget_12.list_of_new_Label_nomer[len_Label_No - 1].deleteLater()
            widget_12.list_of_new_LineEdits[len_LE - 1].deleteLater()
            widget_12.list_of_new_SpinBox[len_SB - 1].deleteLater()
            widget_12.list_of_new_LE_edinitsy[len_Label_Sht - 1].deleteLater()

            widget_12.list_of_new_Label_nomer.remove(widget_12.list_of_new_Label_nomer[len_Label_No - 1])
            widget_12.list_of_new_LineEdits.remove(widget_12.list_of_new_LineEdits[len_LE - 1])
            widget_12.list_of_new_SpinBox.remove(widget_12.list_of_new_SpinBox[len_SB - 1])
            widget_12.list_of_new_LE_edinitsy.remove(widget_12.list_of_new_LE_edinitsy[len_Label_Sht - 1])

            buff = widget_12.i_12 - 1
            widget_12.i_12 = buff
            buff -= 1
            shift = 32 * buff
            buf = 138 + shift

            self.pushButton_102.move(280, buf)
            self.pushButton_103.move(320, buf)
            buf = 110 + shift
            self.line_36.move(10, buf)

            buf = 181 + shift
            self.frame_12.setMinimumSize(QtCore.QSize(0, buf))
            print("dellllllllllllllllllllllllll2", widget_12.i_12)

    def get_inputed_data(self):
        #LE
        widget_12.outputDATA_from_LE = []
        widget_12.outputDATA_from_SpinBox = []

        widget_12.outputDATA_from_LE.append(self.mensale7_le_elem_1.text())
        widget_12.outputDATA_from_LE.append(self.mensale7_le_elem_2.text())
        for i in widget_12.list_of_new_LineEdits:
            widget_12.outputDATA_from_LE.append(i.text())
        print('     Get the list from LE on widget_12: ',widget_12.outputDATA_from_LE)

        widget_12.outputDATA_from_LE_ist = []
        widget_12.outputDATA_from_LE_ist.append(self.mensale7_le_elem_3.text())
        widget_12.outputDATA_from_LE_ist.append(self.mensale7_le_elem_4.text())
        for i in widget_12.list_of_new_LineEdits_ist:
            widget_12.outputDATA_from_LE_ist.append(i.text())
        print('     Get the list from LE (ist.) on widget_12: ', widget_12.outputDATA_from_LE_ist)


        widget_12.outputDATA_from_SpinBox.append(self.mensale7__num_1.text())
        widget_12.outputDATA_from_SpinBox.append(self.mensale7__num_2.text())

        for i in widget_12.list_of_new_SpinBox:
            widget_12.outputDATA_from_SpinBox.append(i.text())
        print('     Get the list from SB on widget_12: ',widget_12.outputDATA_from_SpinBox)

        widget_12.outputDATA_from_LE_Edinitsy = []
        widget_12.outputDATA_from_LE_Edinitsy.append(self.mensale7_le_COL_1.text())
        widget_12.outputDATA_from_LE_Edinitsy.append(self.mensale7_le_COL_2.text())

        for i in widget_12.list_of_new_LE_edinitsy:
            widget_12.outputDATA_from_LE_Edinitsy.append(i.text())
        print('     Get the list from LE (ed.) on widget_12: ', widget_12.outputDATA_from_LE_Edinitsy)

    def HANDLER_NEXT_x(self,iter):
        print("159",iter)
        try:
            widget_12.list_of_new_LineEdits_ist[iter-1].setFocus()
        except:
            pass
    def HANDLER_NEXT_x2(self,iter):
        try:
            widget_12.list_of_new_LE_edinitsy[iter-1].setFocus()
        except:
            pass
    def HANDLER_NEXT_x3(self,iter):
        try:
            widget_12.list_of_new_LineEdits[iter].setFocus()
        except:
            self.mensale6_lbl_elem_5.setFocus()

class widget_14(Ui_MainWindow):
    i_13 = 1
    lay = ""

    list_of_new_Label_nomer = []
    list_of_new_LineEdits = []
    list_of_new_LineEdits_ist = []
    list_of_new_SpinBox = []
    list_of_new_Label_shtuk = []

    outputDATA_from_LE = []
    outputDATA_from_LE_ist = []
    outputDATA_from_SpinBox = []

    def add_new_string(self):
        shift = 32 * widget_14.i_13

        if "добавляем лайбу номера" == "добавляем лайбу номера":
            widget_14.lay = QtWidgets.QLabel(self.frame_14)
            y = 79 + (shift)
            widget_14.lay.setGeometry(QtCore.QRect(10, y, 21, 21))

            widget_14.lay.setObjectName(f"mensale6_lbl_number_{widget_14.i_13 + 2}")
            widget_14.lay.setText(str(widget_14.i_13 + 2))
            widget_14.lay.setStyleSheet("background-color: rgb(177, 127, 66);\n"
                                 "border-radius: 5px;\n"
                                 "color: rgb(0, 0, 0);")
            widget_14.lay.setAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(10)
            font.setItalic(True)
            widget_14.lay.setFont(font)
            widget_14.lay.show()

            widget_14.list_of_new_Label_nomer.append(widget_14.lay)
            print("         widget_14.list_of_new_Label_nomer ", widget_14.list_of_new_Label_nomer)
        if "добавляем LE названия элемента" == "добавляем LE названия элемента":
            widget_14.lay = QtWidgets.QLineEdit(self.frame_14)
            y = 79 + (shift)
            widget_14.lay.setGeometry(QtCore.QRect(40, y, 370, 20))
            p = "mensale6_lbl_elem_" + str(widget_14.i_13 + 2)
            widget_14.lay.setObjectName(p)
            widget_14.lay.setText("")
            widget_14.lay.setAlignment(QtCore.Qt.AlignLeft)
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(10)
            font.setItalic(True)
            widget_14.lay.setFont(font)
            widget_14.lay.setStyleSheet("background-color: rgb(177, 127, 66);\n"
                                 "color: rgb(109, 65, 12);\n"
                                 "border: 1px solid rgb(109, 65, 12);\n"
                                 "border-radius: 5px;")
            widget_14.lay.show()

            widget_14.list_of_new_LineEdits.append(widget_14.lay)
            print("         widget_14.list_of_new_LineEdits ", widget_14.list_of_new_LineEdits)
        iter = widget_14.i_13
        widget_14.lay.returnPressed.connect(lambda: widget_14.HANDLER_NEXT_w14_x(self, iter))
        if "добавляем LE источника элемента" != "добавляем LE названия элемента":
            widget_14.lay = QtWidgets.QLineEdit(self.frame_14)
            y = 79 + (shift)
            widget_14.lay.setGeometry(QtCore.QRect(412, y, 75, 20))
            p = "mensale6_lbl_elem_" + str(widget_14.i_13 + 2)
            widget_14.lay.setObjectName(p)
            widget_14.lay.setText("")
            widget_14.lay.setAlignment(QtCore.Qt.AlignLeft)
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(10)
            font.setItalic(True)
            widget_14.lay.setFont(font)
            widget_14.lay.setStyleSheet("background-color: rgb(177, 127, 66);\n"
                                 "color: rgb(109, 65, 12);\n"
                                 "border: 1px solid rgb(109, 65, 12);\n"
                                 "border-radius: 5px;")
            widget_14.lay.show()

            widget_14.list_of_new_LineEdits_ist.append(widget_14.lay)
            print("         widget_14.list_of_new_LineEdits ", widget_14.list_of_new_LineEdits)
        widget_14.lay.returnPressed.connect(lambda: widget_14.HANDLER_NEXT_w14_x2(self,iter))
        if "добавляем SB количества" == "добавляем SB количества":
            widget_14.lay = QtWidgets.QSpinBox(self.frame_14)
            y = 79 + shift

            widget_14.lay.setGeometry(QtCore.QRect(490, y, 61, 22))
            widget_14.lay.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                 "color: rgb(109, 65, 12);\n"
                                 "border: 1px solid rgb(109, 65, 12);"
                                 )

            widget_14.lay.setMaximum(10000)

            widget_14.lay.setObjectName(f"mensale6_elem_{widget_14.i_13 + 2}")

            widget_14.lay.setAlignment(QtCore.Qt.AlignLeft)
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(10)
            font.setItalic(True)
            widget_14.lay.setFont(font)
            widget_14.lay.show()

            widget_14.list_of_new_SpinBox.append(widget_14.lay)
            print("         widget_14.list_of_new_SpinBox ", widget_14.list_of_new_SpinBox)
        if "добавляем LBL шт" == "добавляем LBL шт":
            widget_14.lay = QtWidgets.QLabel(self.frame_14)
            y = 79 + (shift)
            widget_14.lay.setGeometry(QtCore.QRect(557, y, 47, 20))
            widget_14.lay.setObjectName(f"mensale6_lbl_sht_{widget_14.i_13 + 2}")
            widget_14.lay.setText("шт.")
            widget_14.lay.setStyleSheet("background-color: None;")
            widget_14.lay.setAlignment(QtCore.Qt.AlignLeft)
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(12)
            font.setItalic(True)
            widget_14.lay.setFont(font)
            widget_14.lay.show()

            widget_14.list_of_new_Label_shtuk.append(widget_14.lay)
            print("         widget_14.list_of_new_Label_shtuk ", widget_14.list_of_new_Label_shtuk)

        buf = 181 + shift
        self.frame_14.setMinimumSize(QtCore.QSize(0, buf))
        buf = 110 + shift
        self.line_38.move(10, buf)
        buf = 138 + shift
        self.pushButton_106.move(280, buf)
        buf = 138 + shift
        self.pushButton_107.move(320, buf)
        widget_14.i_13 += 1

    def del_last_string(self):
        if len(widget_14.list_of_new_Label_nomer) >= 1:
            len_Label_No = len(widget_14.list_of_new_Label_nomer)
            len_LE = len(widget_14.list_of_new_LineEdits)
            len_SB = len(widget_14.list_of_new_SpinBox)
            len_Label_Sht = len(widget_14.list_of_new_Label_shtuk)

            widget_14.list_of_new_Label_nomer[len_Label_No - 1].deleteLater()
            widget_14.list_of_new_LineEdits[len_LE - 1].deleteLater()
            widget_14.list_of_new_SpinBox[len_SB - 1].deleteLater()
            widget_14.list_of_new_Label_shtuk[len_Label_Sht - 1].deleteLater()

            widget_14.list_of_new_Label_nomer.remove(widget_14.list_of_new_Label_nomer[len_Label_No - 1])
            widget_14.list_of_new_LineEdits.remove(widget_14.list_of_new_LineEdits[len_LE - 1])
            widget_14.list_of_new_SpinBox.remove(widget_14.list_of_new_SpinBox[len_SB - 1])
            widget_14.list_of_new_Label_shtuk.remove(widget_14.list_of_new_Label_shtuk[len_Label_Sht - 1])

            buff = widget_14.i_13 - 1
            widget_14.i_13 = buff
            buff -= 1
            shift = 32 * buff
            buf = 138 + shift

            self.pushButton_106.move(280, buf)
            self.pushButton_107.move(320, buf)
            buf = 110 + shift
            self.line_38.move(10, buf)

            buf = 181 + shift
            self.frame_14.setMinimumSize(QtCore.QSize(0, buf))
            print("dellllllllllllllllllllllllll2", widget_14.i_13)

    def get_inputed_data(self):
        #LE
        widget_14.outputDATA_from_LE = []
        widget_14.outputDATA_from_SpinBox = []

        widget_14.outputDATA_from_LE.append(self.mensale6_lbl_elem_5.text())
        widget_14.outputDATA_from_LE.append(self.mensale6_lbl_elem_6.text())
        for i in widget_14.list_of_new_LineEdits:
            widget_14.outputDATA_from_LE.append(i.text())
        print('     Get the list from LE on widget_14: ',widget_14.outputDATA_from_LE)

        widget_14.outputDATA_from_LE_ist = []
        widget_14.outputDATA_from_LE_ist.append(self.mensale6_lbl_elem_7.text())
        widget_14.outputDATA_from_LE_ist.append(self.mensale6_lbl_elem_8.text())
        for i in widget_14.list_of_new_LineEdits_ist:
            widget_14.outputDATA_from_LE_ist.append(i.text())
        print('     Get the list from LE (ist.) on widget_14: ', widget_14.outputDATA_from_LE_ist)

        widget_14.outputDATA_from_SpinBox.append(self.mensale6__elem_5.text())
        widget_14.outputDATA_from_SpinBox.append(self.mensale6__elem_6.text())

        for i in widget_14.list_of_new_SpinBox:
            widget_14.outputDATA_from_SpinBox.append(i.text())
        print('     Get the list from SB on widget_14: ',widget_14.outputDATA_from_SpinBox)

    def HANDLER_NEXT_w14_1(self,iter):#mensale6_lbl_elem_5
        self.mensale6_lbl_elem_7.setFocus()
    def HANDLER_NEXT_w14_2(self,iter):#mensale6_lbl_elem_7
        self.mensale6_lbl_elem_6.setFocus()
    def HANDLER_NEXT_w14_3(self,iter):#mensale6_lbl_elem_6
        self.mensale6_lbl_elem_8.setFocus()
    def HANDLER_NEXT_w14_4(self,iter):#mensale6_lbl_elem_8
        try:
            widget_14.list_of_new_LineEdits[0].setFocus()
        except:
            pass

    def HANDLER_NEXT_w14_x(self,iter):#mensale6_lbl_elem_5
        print("x",iter)
        try:
            widget_14.list_of_new_LineEdits_ist[iter-1].setFocus()
        except:
            pass
    def HANDLER_NEXT_w14_x2(self,iter):#mensale6_lbl_elem_5
        print("x2",iter)
        try:
            widget_14.list_of_new_LineEdits[iter].setFocus()
        except:
            pass

class widget_15(Ui_MainWindow):
    i_12 = 1
    lay = ""

    list_of_new_Label_nomer = []
    list_of_new_LineEdits = []
    list_of_new_SpinBox = []
    list_of_new_LE_edinitsy = []

    outputDATA_from_LE = []
    outputDATA_from_SpinBox = []
    outputDATA_from_LE_Edinitsy = []

    def add_new_string(self):
        shift = 32 * widget_15.i_12
        if "добавляем лайбу номера" == "добавляем лайбу номера":
            widget_15.lay = QtWidgets.QLabel(self.frame_15)
            y = 79 + (shift)
            widget_15.lay.setGeometry(QtCore.QRect(10, y, 21, 21))
            widget_15.lay.setObjectName(f"mensale_lbl_number_{widget_15.i_12 + 2}")
            widget_15.lay.setText(str(widget_15.i_12 + 2))
            widget_15.lay.setStyleSheet("background-color: rgb(177, 127, 66);\n"
                                 "border-radius: 5px;\n"
                                 "color: rgb(0, 0, 0);")
            widget_15.lay.setAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(10)
            font.setItalic(True)
            widget_15.lay.setFont(font)
            widget_15.lay.show()

            widget_15.list_of_new_Label_nomer.append(widget_15.lay)
            print("         widget_15.list_of_new_Label_nomer ", widget_15.list_of_new_Label_nomer)
        if "добавляем LE названия элемента" == "добавляем LE названия элемента":
            widget_15.lay = QtWidgets.QLineEdit(self.frame_15)
            y = 79 + (shift)
            widget_15.lay.setGeometry(QtCore.QRect(40, y, 401, 20))
            p = "mensale8_lbl_elem_" + str(widget_15.i_12 + 2)
            widget_15.lay.setObjectName(p)
            widget_15.lay.setText("")
            widget_15.lay.setAlignment(QtCore.Qt.AlignLeft)
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(10)
            font.setItalic(True)
            widget_15.lay.setFont(font)
            widget_15.lay.setStyleSheet("background-color: rgb(177, 127, 66);\n"
                                 "color: rgb(109, 65, 12);\n"
                                 "border: 1px solid rgb(109, 65, 12);\n"
                                 "border-radius: 5px;")
            widget_15.lay.show()

            widget_15.list_of_new_LineEdits.append(widget_15.lay)
            print("         widget_15.list_of_new_LineEdits ", widget_15.list_of_new_LineEdits)
        if "добавляем SB количества" == "добавляем SB количества":
            widget_15.lay = QtWidgets.QSpinBox(self.frame_15)
            y = 79 + shift

            widget_15.lay.setGeometry(QtCore.QRect(450, y, 61, 22))
            widget_15.lay.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                 "color: rgb(109, 65, 12);\n"
                                 "border: 1px solid rgb(109, 65, 12);"
                                 )

            widget_15.lay.setMaximum(10000)

            widget_15.lay.setObjectName(f"mensale7_elem_{widget_15.i_12 + 2}")

            widget_15.lay.setAlignment(QtCore.Qt.AlignLeft)
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(10)
            font.setItalic(True)
            widget_15.lay.setFont(font)
            widget_15.lay.show()

            widget_15.list_of_new_SpinBox.append(widget_15.lay)
            print("         widget_15.list_of_new_SpinBox ", widget_15.list_of_new_SpinBox)
        if "добавляем LE шт" == "добавляем LE шт":
            widget_15.lay = QtWidgets.QLineEdit(self.frame_15)
            y = 79 + (shift)
            widget_15.lay.setGeometry(QtCore.QRect(520, y, 84, 20))
            widget_15.lay.setObjectName(f"mensale7_lbl_sht_{widget_15.i_12 + 2}")
            widget_15.lay.setText("шт.")
            widget_15.lay.setStyleSheet("background-color: rgb(177, 127, 66);\n"
                                        "color: rgb(109, 65, 12);\n"
                                        "border: 1px solid rgb(109, 65, 12);\n"
                                        "border-radius: 5px;")
            widget_15.lay.setAlignment(QtCore.Qt.AlignLeft)
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(8)
            font.setItalic(True)
            widget_15.lay.setFont(font)
            widget_15.lay.show()

            widget_15.list_of_new_LE_edinitsy.append(widget_15.lay)
            print("         widget_15.list_of_new_LE_edinitsy ", widget_15.list_of_new_LE_edinitsy)

        buf = 181 + shift
        self.frame_15.setMinimumSize(QtCore.QSize(0, buf))
        buf = 110 + shift
        self.line_39.move(10, buf)
        buf = 138 + shift
        self.pushButton_108.move(280, buf)
        buf = 138 + shift
        self.pushButton_112.move(320, buf)
        widget_15.i_12 += 1

    def del_last_string(self):
        if len(widget_15.list_of_new_Label_nomer) >= 1:
            print("Del last string in the list on widget_15:")
            print("    iteration №: ", widget_15.i_12, " (+2):")
            print("delllllllllllllllllllllllllll",widget_15.i_12)
            len_Label_No = len(widget_15.list_of_new_Label_nomer)
            len_LE = len(widget_15.list_of_new_LineEdits)
            len_SB = len(widget_15.list_of_new_SpinBox)
            len_Label_Sht = len(widget_15.list_of_new_LE_edinitsy)

            widget_15.list_of_new_Label_nomer[len_Label_No - 1].deleteLater()
            widget_15.list_of_new_LineEdits[len_LE - 1].deleteLater()
            widget_15.list_of_new_SpinBox[len_SB - 1].deleteLater()
            widget_15.list_of_new_LE_edinitsy[len_Label_Sht - 1].deleteLater()

            widget_15.list_of_new_Label_nomer.remove(widget_15.list_of_new_Label_nomer[len_Label_No - 1])
            widget_15.list_of_new_LineEdits.remove(widget_15.list_of_new_LineEdits[len_LE - 1])
            widget_15.list_of_new_SpinBox.remove(widget_15.list_of_new_SpinBox[len_SB - 1])
            widget_15.list_of_new_LE_edinitsy.remove(widget_15.list_of_new_LE_edinitsy[len_Label_Sht - 1])

            buff = widget_15.i_12 - 1
            widget_15.i_12 = buff
            buff -= 1
            shift = 32 * buff
            buf = 138 + shift

            self.pushButton_108.move(280, buf)
            self.pushButton_112.move(320, buf)
            buf = 110 + shift
            self.line_39.move(10, buf)

            buf = 181 + shift
            self.frame_15.setMinimumSize(QtCore.QSize(0, buf))
            print("dellllllllllllllllllllllllll2", widget_15.i_12)

    def get_inputed_data(self):
        #LE
        widget_15.outputDATA_from_LE = []
        widget_15.outputDATA_from_SpinBox = []

        widget_15.outputDATA_from_LE.append(self.mensale8_le_elem_1.text())
        widget_15.outputDATA_from_LE.append(self.mensale8_le_elem_2.text())
        for i in widget_15.list_of_new_LineEdits:
            widget_15.outputDATA_from_LE.append(i.text())
        print('     Get the list from LE on widget_15: ',widget_15.outputDATA_from_LE)

        widget_15.outputDATA_from_SpinBox.append(self.mensale8__num_1.text())
        widget_15.outputDATA_from_SpinBox.append(self.mensale8__num_2.text())

        for i in widget_15.list_of_new_SpinBox:
            widget_15.outputDATA_from_SpinBox.append(i.text())
        print('     Get the list from SB on widget_15: ',widget_15.outputDATA_from_SpinBox)

        widget_15.outputDATA_from_LE_Edinitsy.append(self.mensale8_le_COL_1.text())
        widget_15.outputDATA_from_LE_Edinitsy.append(self.mensale8_le_COL_2.text())

        for i in widget_15.list_of_new_LE_edinitsy:
            widget_15.outputDATA_from_LE_Edinitsy.append(i.text())
        print('     Get the list from LE (ed.) on widget_15: ', widget_15.outputDATA_from_LE_Edinitsy)

#начальное окно отображение заказов
class widget_begin(Ui_MainWindow):
    i_1 = 1 #количество
    i_1_name = 1 #номер файла
    lay = ""
    lay_nomer = ""

    list_of_new_widgets = []

    list_of_new_pbt_k_proectu = []
    list_of_new_pbt_export = []
    def add_new_strings(self):
        widget_begin.i_1 = 1
        widget_begin.i_1_name = 1
        import os
        # for i in range(0,len(os.listdir("../pythonProject3/DATABASE/current_project"))-1):
        # try:
        print("odissey")
        # while True:
        daty = os.listdir("../pythonProject3/DATABASE/current_project")
        for i in range(len(os.listdir("../pythonProject3/DATABASE/current_project"))):
            print("iter file",daty[i])
            # widget_begin.i_1 = i
            widget_begin.add_new_string(self)
            # break
        # except:
        #     pass

    def del_all_strings(self):
        widget_begin.i_1 = 1
        widget_begin.i_1_name = 1
        for i in range(len(widget_begin.list_of_new_widgets)):
            widget_begin.list_of_new_widgets[i].deleteLater()
        widget_begin.list_of_new_widgets = []
        widget_begin.list_of_new_pbt_k_proectu = []
        widget_begin.list_of_new_pbt_export = []
    def add_new_string(self):
        nomer_proecta = ""
        oborudovanie = ""
        zakazchic = ""
        Etap_proecta = ""
        data_konca = ""
        srochnost = ""
        tel = ""
        mail = ""

        path_to_current_file = ""
        if "достоем информацию из файла всех заказов" == "достоем информацию из файла всех заказов":
            import os
            name = os.listdir("../pythonProject3/DATABASE/current_project")
            # name = []

            from ui import UI
            k = []
            print("159 UI.MASSIVE_FILE_with_posledovat", UI.MASSIVE_FILE_with_posledovat)

            if UI.MASSIVE_FILE_with_posledovat != k:
                name = UI.MASSIVE_FILE_with_posledovat
            else:
                import os
                name = os.listdir("../pythonProject3/DATABASE/current_project")
                print("159")


            txt = f"../pythonProject3/DATABASE/current_project/" + (name[widget_begin.i_1_name - 1])
            path_to_current_file = txt
            print(";;;;;;;;;;;;;;;;;;;;;;",name[widget_begin.i_1_name - 1])

            with open(txt, 'r') as file:
                nomer_proecta = name[widget_begin.i_1_name - 1]
                counter = 1
                buf = ""
                try:
                    while True:
                        if nomer_proecta[counter] != ".":
                            buf += nomer_proecta[counter]
                        else:
                            nomer_proecta = " " + buf
                            break
                        counter += 1
                except:
                    pass
                for index, line in enumerate(file):
                    # print("123",type(index), index, line)
                    if index == 4:
                        data_konca = line.strip()
                    if index == 10:
                        oborudovanie = " " + line.strip()
                    if index == 2:
                        zakazchic = " " + line.strip()
                    if index == 19:
                        Etap_proecta = " " + line.strip()
                    if index == 7:
                        tel = line.strip()
                        buf = ''
                        if len(tel) == 7:
                            buf = ""
                            buf += tel[0]
                            buf += " "
                            buf += tel[1]
                            buf += tel[2]
                            buf += "-"
                            buf += tel[3]
                            buf += tel[4]
                            buf += "-"
                            buf += tel[5]
                            buf += tel[6]
                            tel = buf
                        if len(tel) == 11:
                            buf += " "
                            buf += tel[0]
                            buf += " "
                            buf += "("
                            buf += tel[1]
                            buf += tel[2]
                            buf += tel[3]
                            buf += ")"
                            buf += " "
                            buf += tel[4]
                            buf += tel[5]
                            buf += tel[6]
                            buf += "-"
                            buf += tel[7]
                            buf += tel[8]
                            buf += "-"
                            buf += tel[9]
                            buf += tel[10]
                            tel = buf
                    if index == 3:
                        mail = " " + line.strip()

                import datetime

                now = str(datetime.datetime.now())
                # 2021-08-06 22:45:02.522446
                year = int(now[0:4])
                year_now = year
                mounth = int(now[5:7])
                day = int(now[8:10])

                if "" == "":
                    day_end = ""
                    counter = 0
                    while True:
                        if data_konca[counter] != ".":
                            day_end += data_konca[counter]
                        else:
                            break
                        counter += 1
                    mounth_end = ""
                    counter += 1
                    while True:
                        if data_konca[counter] != ".":
                            mounth_end += data_konca[counter]
                        else:
                            break
                        counter += 1
                    year_end = ""
                    counter += 1
                    try:
                        while True:
                            if data_konca[counter] != ".":
                                year_end += data_konca[counter]
                            else:
                                break
                            counter += 1
                    except:
                        pass
                # try:
                raznitsa = int(day_end) - day

                DAYindex_plus = 0
                if raznitsa < 0:
                    while True:
                        if (year_now + 5) == year:
                            DAYindex_plus = -100
                            break
                        if int(day_end) == int(day) and int(mounth_end) == int(mounth) and int(year) == int(year_end):
                            break
                        else:
                            DAYindex_plus += 1
                            day += 1
                        if 31 == 31:
                            if mounth == 1 and day > 31:
                                day = 1
                                mounth += 1
                            if mounth == 3 and day > 31:
                                day = 1
                                mounth += 1
                            if mounth == 5 and day > 31:
                                day = 1
                                mounth += 1
                            if mounth == 7 and day > 31:
                                day = 1
                                mounth += 1
                            if mounth == 8 and day > 31:
                                day = 1
                                mounth += 1
                            if mounth == 10 and day > 31:
                                day = 1
                                mounth += 1
                            if mounth == 12 and day > 31:
                                day = 1
                                mounth += 1
                        if 30 == 30:
                            if mounth == 4 and day > 30:
                                day = 1
                                mounth += 1
                            if mounth == 6 and day > 30:
                                day = 1
                                mounth += 1
                            if mounth == 9 and day > 30:
                                day = 1
                                mounth += 1
                            if mounth == 11 and day > 30:
                                day = 1
                                mounth += 1
                        if 29 == 29 or 28 == 28:
                            for i in [2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068,
                                      2072, 2076, 2080]:
                                if mounth == 2 and day > 29 and year == i:
                                    day = 1
                                    mounth += 1
                                else:
                                    if mounth == 2 and day > 28 and year != i:
                                        day = 1
                                        mounth += 1
                        if 12 == 12:
                            if mounth >= 12:
                                mounth = 1
                                year += 1
                else:
                    DAYindex_plus = raznitsa
                # except:
                #     raznitsa = int(data_konca[0:1]) - int(day)
                #     print("raznitsa ", data_konca[0:1], " - ", day, " = ", raznitsa)
        FLAG_yest_li_conec = 0
        # path_to_current_file
        from ui import UI
        if "Если включер нежим сортировки 'только неоконченные' или 'только законченные', проверяем наличае конца" != "":
            if UI.FLAG_TOLKO == "EST_CONEC" or UI.FLAG_TOLKO == "NET_CONEC":
                with open(path_to_current_file, 'r') as file:
                    for index,line in enumerate(file):
                        print("line:::",path_to_current_file,line)
                        if line.strip() == "^^^THE_END":
                            FLAG_yest_li_conec = 1
                            print("ESLIIIIIIIIIIIIIII")
                            break
                        else:
                            FLAG_yest_li_conec = 0

        # UI.FLAG_TOLKO = "ZEL"
        print("DAYindex_plus666",oborudovanie, DAYindex_plus, raznitsa)

        try:
            if (DAYindex_plus >5 and UI.FLAG_TOLKO == "ZEL") or ((DAYindex_plus <=5 and DAYindex_plus>2) and UI.FLAG_TOLKO == "JEL") or ((DAYindex_plus <=2 and DAYindex_plus>=0)and UI.FLAG_TOLKO == "KRA") or UI.FLAG_TOLKO == "VCE" or \
                    (FLAG_yest_li_conec == 1 and UI.FLAG_TOLKO == "EST_CONEC") or (FLAG_yest_li_conec == 0 and UI.FLAG_TOLKO == "NET_CONEC")or (DAYindex_plus < 0 and UI.FLAG_TOLKO == "KRA"):
                shift = 117 * (widget_begin.i_1 - 1)

                if widget_begin.i_1 >= 5:
                    self.frame_2.setMinimumHeight(478 + (117*(widget_begin.i_1 - 4)))

                if "добавляем фоновый виджет заказа" == "добавляем фоновый виджет заказа":
                    widget_begin.lay = QtWidgets.QWidget(self.frame_2)
                    y = 10 + shift
                    widget_begin.lay.setGeometry(QtCore.QRect(10, y, 711, 108))
                    widget_begin.lay.setObjectName(f"widget_begin_{widget_begin.i_1 + 1}")
                    widget_begin.lay.setStyleSheet(f"#widget_begin_{widget_begin.i_1 + 1}\n"
                                                   "{\n"
                                                   "background-color: rgb(214, 176, 110);\n"
                                                   "border-radius: 10px;\n"
                                                   "\n"
                                                   "border: 1px solid  rgb(202, 144, 85);\n"
                                                   "border-color: rgb(202, 144, 85);\n"
                                                   "}")
                    widget_begin.list_of_new_widgets.append(widget_begin.lay)
                    widget_begin.lay.show()

                if "не изменяемые элементы" == "не изменяемые элементы":
                    if "добавляем лэйбл 'заказ№'" == "добавляем лэйбл 'заказ№'":
                        widget_begin.lay = QtWidgets.QLabel(widget_begin.list_of_new_widgets[int(widget_begin.i_1) - 1])
                        widget_begin.lay.setGeometry(QtCore.QRect(10, 10, 71, 16))
                        widget_begin.lay.setObjectName(f"label_zakaz{widget_begin.i_1 + 2}")
                        widget_begin.lay.setText("Заказ №")
                        widget_begin.lay.setStyleSheet("background-color: rgb(214, 176, 110);")
                        font = QtGui.QFont()
                        font.setFamily("Arial")
                        font.setPointSize(12)
                        font.setItalic(True)
                        widget_begin.lay.setFont(font)
                        widget_begin.lay.show()
                    if "добавляем лэйбл 'срочность'" == "добавляем лэйбл 'срочность'":
                        widget_begin.lay = QtWidgets.QLabel(widget_begin.list_of_new_widgets[widget_begin.i_1 - 1])
                        widget_begin.lay.setGeometry(QtCore.QRect(260, 10, 91, 16))
                        widget_begin.lay.setObjectName(f"label_crochnost{widget_begin.i_1 + 2}")
                        widget_begin.lay.setText("Срочность:")
                        widget_begin.lay.setStyleSheet("background-color: rgb(214, 176, 110);")
                        font = QtGui.QFont()
                        font.setFamily("Arial")
                        font.setPointSize(12)
                        font.setItalic(True)
                        widget_begin.lay.setFont(font)
                        widget_begin.lay.show()
                    if "добавляем лэйбл 'Оборудование:'" == "добавляем лэйбл 'Оборудование:'":
                        widget_begin.lay = QtWidgets.QLabel(widget_begin.list_of_new_widgets[widget_begin.i_1 - 1])
                        widget_begin.lay.setGeometry(QtCore.QRect(10, 40, 91, 16))
                        widget_begin.lay.setObjectName(f"label_oborud{widget_begin.i_1 + 2}")
                        widget_begin.lay.setText("Оборудование:")
                        widget_begin.lay.setStyleSheet("background-color: rgb(214, 176, 110);")
                        font = QtGui.QFont()
                        font.setFamily("Arial")
                        font.setPointSize(10)
                        font.setItalic(False)
                        widget_begin.lay.setFont(font)
                        widget_begin.lay.show()
                    if "добавляем лэйбл 'Заказчик:'" == "добавляем лэйбл 'Заказчик:'":
                        widget_begin.lay = QtWidgets.QLabel(widget_begin.list_of_new_widgets[widget_begin.i_1 - 1])
                        widget_begin.lay.setGeometry(QtCore.QRect(10, 60, 91, 16))
                        widget_begin.lay.setObjectName(f"label_zakazchik{widget_begin.i_1 + 2}")
                        widget_begin.lay.setText("Заказчик:")
                        widget_begin.lay.setStyleSheet("background-color: rgb(214, 176, 110);")
                        font = QtGui.QFont()
                        font.setFamily("Arial")
                        font.setPointSize(10)
                        font.setItalic(False)
                        widget_begin.lay.setFont(font)
                        widget_begin.lay.show()
                    if "добавляем лэйбл 'ЭтапПроекта:'" == "добавляем лэйбл 'ЭтапПроекта:'":
                        widget_begin.lay = QtWidgets.QLabel(widget_begin.list_of_new_widgets[widget_begin.i_1 - 1])
                        widget_begin.lay.setGeometry(QtCore.QRect(10, 81, 141, 16))
                        widget_begin.lay.setObjectName(f"label_etap_proecta{widget_begin.i_1 + 2}")
                        widget_begin.lay.setText("Этап проекта:")
                        widget_begin.lay.setStyleSheet("background-color: rgb(214, 176, 110);")
                        font = QtGui.QFont()
                        font.setFamily("Arial")
                        font.setPointSize(10)
                        font.setItalic(False)
                        widget_begin.lay.setFont(font)
                        widget_begin.lay.show()
                    if "добавляем лэйбл 'телефон:'" == "добавляем лэйбл 'телефон:'":
                        widget_begin.lay = QtWidgets.QLabel(widget_begin.list_of_new_widgets[widget_begin.i_1 - 1])
                        widget_begin.lay.setGeometry(QtCore.QRect(340, 60, 91, 16))
                        widget_begin.lay.setObjectName(f"label_tel{widget_begin.i_1 + 2}")
                        widget_begin.lay.setText("Телефон:")
                        widget_begin.lay.setStyleSheet("background-color: rgb(214, 176, 110);")
                        font = QtGui.QFont()
                        font.setFamily("Arial")
                        font.setPointSize(10)
                        font.setItalic(False)
                        widget_begin.lay.setFont(font)
                        widget_begin.lay.show()
                    if "добавляем лэйбл 'EMail:'" == "добавляем лэйбл 'EMail:'":
                        widget_begin.lay = QtWidgets.QLabel(widget_begin.list_of_new_widgets[widget_begin.i_1 - 1])
                        widget_begin.lay.setGeometry(QtCore.QRect(290, 82, 41, 16))
                        widget_begin.lay.setObjectName(f"label_tel{widget_begin.i_1 + 2}")
                        widget_begin.lay.setText("EMail:")
                        widget_begin.lay.setStyleSheet("background-color: rgb(214, 176, 110);")
                        font = QtGui.QFont()
                        font.setFamily("Arial")
                        font.setPointSize(10)
                        font.setItalic(False)
                        widget_begin.lay.setFont(font)
                        widget_begin.lay.show()

                if "изменяемые элементы" == "изменяемые элементы":
                    if "добавляем номер заказа" == "добавляем номер заказа":
                        widget_begin.lay_nomer = QtWidgets.QLabel(widget_begin.list_of_new_widgets[widget_begin.i_1 - 1])
                        widget_begin.lay_nomer.setGeometry(QtCore.QRect(80, 10, 141, 21))
                        widget_begin.lay_nomer.setObjectName(f"label_zakazNomer{widget_begin.i_1 + 2}")
                        widget_begin.lay_nomer.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                             "color: rgb(154, 113, 67);\n"
                                                             "background-color: rgb(197, 147, 86);\n"
                                                             "border-radius: 5px;")
                        font = QtGui.QFont()
                        font.setFamily("Arial")
                        font.setPointSize(11)
                        font.setItalic(False)
                        widget_begin.lay_nomer.setFont(font)
                        widget_begin.lay_nomer.show()
                    widget_begin.lay_nomer.setText(str(nomer_proecta))
                    if "добавляем имя оборудование" == "добавляем имя оборудование":
                        widget_begin.lay = QtWidgets.QLabel(widget_begin.list_of_new_widgets[widget_begin.i_1 - 1])
                        widget_begin.lay.setGeometry(QtCore.QRect(110, 40, 421, 21))
                        widget_begin.lay.setObjectName(f"label_oborud_imya{widget_begin.i_1 + 2}")
                        widget_begin.lay.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                       "color: rgb(154, 113, 67);\n"
                                                       "background-color: rgb(197, 147, 86);\n"
                                                       "border-radius: 5px;\n"
                                                       "border: 1px solid rgb(214, 176, 110);")
                        font = QtGui.QFont()
                        font.setFamily("Arial")
                        font.setPointSize(11)
                        font.setItalic(False)
                        widget_begin.lay.setFont(font)
                        widget_begin.lay.show()
                    widget_begin.lay.setText(str(oborudovanie))

                    if "добавляем 1 элемент срочности" == "добавляем 1 элемент срочности":
                        widget_begin.lay = QtWidgets.QLabel(widget_begin.list_of_new_widgets[widget_begin.i_1 - 1])
                        widget_begin.lay.setGeometry(QtCore.QRect(360, 10, 51, 21))
                        widget_begin.lay.setObjectName(f"label_crochnostLVL1{widget_begin.i_1 + 2}")
                        widget_begin.lay.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                       "color: rgb(154, 113, 67);\n"
                                                       "background-color: rgb(197, 147, 86);\n"
                                                       "border-radius: 5px;")
                        font = QtGui.QFont()
                        font.setFamily("Arial")
                        font.setPointSize(11)
                        font.setItalic(False)
                        widget_begin.lay.setFont(font)
                        widget_begin.lay.show()
                    if DAYindex_plus >5:
                        widget_begin.lay.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                       "color: rgb(154, 113, 67);\n"
                                                       "border: 1px solid  rgb(202, 144, 85);\n"
                                                       "background-color: rgb(126, 197, 67);\n"
                                                       "border-radius: 5px;")
                    if DAYindex_plus <=5 and DAYindex_plus>2:
                        widget_begin.lay.setStyleSheet("background-color: rgb(213, 216, 27);\n"
                                                       "color: rgb(154, 113, 67);\n"
                                                       "border: 1px solid  rgb(202, 144, 85);\n"
                                                       "border-radius: 5px;")
                    if DAYindex_plus <=2 and DAYindex_plus>=0:
                        print("OXUUUUUUUUUUUUUU")
                        widget_begin.lay.setStyleSheet("background-color: rgb(197, 33, 18);\n"
                                                       "color: rgb(154, 113, 67);\n"
                                                       "border: 1px solid  rgb(202, 144, 85);\n"
                                                       "border-radius: 5px;")
                    if DAYindex_plus < 0:
                        widget_begin.lay.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                                       "color: rgb(154, 113, 67);\n"
                                                       "border: 1px solid  rgb(202, 144, 85);\n"
                                                       "border-radius: 5px;")
                    # widget_begin.lay.setText(str(DAYindex_plus)) #важная строка
                    if "добавляем 2 элемент срочности" == "добавляем 2 элемент срочности":
                        widget_begin.lay = QtWidgets.QLabel(widget_begin.list_of_new_widgets[widget_begin.i_1 - 1])
                        widget_begin.lay.setGeometry(QtCore.QRect(420, 10, 51, 21))
                        widget_begin.lay.setObjectName(f"label_crochnostLVL2{widget_begin.i_1 + 2}")
                        widget_begin.lay.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                       "color: rgb(154, 113, 67);\n"
                                                       "background-color: rgb(197, 147, 86);\n"
                                                       "border-radius: 5px;")
                        font = QtGui.QFont()
                        font.setFamily("Arial")
                        font.setPointSize(11)
                        font.setItalic(False)
                        widget_begin.lay.setFont(font)
                        widget_begin.lay.show()
                    if DAYindex_plus <=5 and DAYindex_plus>2:
                        widget_begin.lay.setStyleSheet("background-color: rgb(213, 216, 27);\n"
                                                       "color: rgb(154, 113, 67);\n"
                                                       "border: 1px solid  rgb(202, 144, 85);\n"
                                                       "border-radius: 5px;")
                    if DAYindex_plus <=2 and DAYindex_plus>=0:
                        widget_begin.lay.setStyleSheet("background-color: rgb(197, 33, 18);\n"
                                                       "color: rgb(154, 113, 67);\n"
                                                       "border: 1px solid  rgb(202, 144, 85);\n"
                                                       "border-radius: 5px;")
                    if DAYindex_plus < 0:
                        widget_begin.lay.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                                       "color: rgb(154, 113, 67);\n"
                                                       "border: 1px solid  rgb(202, 144, 85);\n"
                                                       "border-radius: 5px;")
                    if "добавляем 3 элемент срочности" == "добавляем 3 элемент срочности":
                        widget_begin.lay = QtWidgets.QLabel(widget_begin.list_of_new_widgets[widget_begin.i_1 - 1])
                        widget_begin.lay.setGeometry(QtCore.QRect(480, 10, 51, 21))
                        widget_begin.lay.setObjectName(f"label_crochnostLVL3{widget_begin.i_1 + 2}")
                        widget_begin.lay.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                       "color: rgb(154, 113, 67);\n"
                                                       "background-color: rgb(197, 147, 86);\n"
                                                       "border-radius: 5px;")
                        font = QtGui.QFont()
                        font.setFamily("Arial")
                        font.setPointSize(11)
                        font.setItalic(False)
                        widget_begin.lay.setFont(font)
                        widget_begin.lay.show()
                    if DAYindex_plus <=2 and DAYindex_plus>=0:
                        widget_begin.lay.setStyleSheet("background-color: rgb(197, 33, 18);\n"
                                                       "color: rgb(154, 113, 67);\n"
                                                       "border: 1px solid  rgb(202, 144, 85);\n"
                                                       "border-radius: 5px;")
                    if DAYindex_plus < 0:
                        widget_begin.lay.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                                       "color: rgb(154, 113, 67);\n"
                                                       "border: 1px solid  rgb(202, 144, 85);\n"
                                                       "border-radius: 5px;")

                    if "добавляем заказчик" == "добавляем заказчик":
                        widget_begin.lay = QtWidgets.QLabel(widget_begin.list_of_new_widgets[widget_begin.i_1 - 1])
                        widget_begin.lay.setGeometry(QtCore.QRect(70, 60, 261, 21))
                        widget_begin.lay.setObjectName(f"label_zakazchik_imya{widget_begin.i_1 + 2}")
                        widget_begin.lay.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                       "color: rgb(154, 113, 67);\n"
                                                       "background-color: rgb(197, 147, 86);\n"
                                                       "border-radius: 5px;\n"
                                                       "border: 1px solid rgb(214, 176, 110);")
                        font = QtGui.QFont()
                        font.setFamily("Arial")
                        font.setPointSize(11)
                        font.setItalic(False)
                        widget_begin.lay.setFont(font)
                        widget_begin.lay.show()
                    widget_begin.lay.setText(zakazchic)
                    if "добавляем этап" == "добавляем этап":
                        widget_begin.lay = QtWidgets.QLabel(widget_begin.list_of_new_widgets[widget_begin.i_1 - 1])
                        widget_begin.lay.setGeometry(QtCore.QRect(90, 80, 191, 21))
                        widget_begin.lay.setObjectName(f"label_etap_proecta_imya{widget_begin.i_1 + 2}")
                        widget_begin.lay.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                       "color: rgb(154, 113, 67);\n"
                                                       "background-color: rgb(197, 147, 86);\n"
                                                       "border-radius: 5px;\n"
                                                       "border: 1px solid rgb(214, 176, 110);")
                        font = QtGui.QFont()
                        font.setFamily("Arial")
                        font.setPointSize(11)
                        font.setItalic(False)
                        widget_begin.lay.setFont(font)
                        widget_begin.lay.show()
                    widget_begin.lay.setText(Etap_proecta)
                    if "добавляем телефон" == "добавляем телефон":
                        widget_begin.lay = QtWidgets.QLabel(widget_begin.list_of_new_widgets[widget_begin.i_1 - 1])
                        widget_begin.lay.setGeometry(QtCore.QRect(400, 60, 131, 21))
                        widget_begin.lay.setObjectName(f"label_tel_no{widget_begin.i_1 + 2}")
                        widget_begin.lay.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                       "color: rgb(154, 113, 67);\n"
                                                       "background-color: rgb(197, 147, 86);\n"
                                                       "border-radius: 5px;\n"
                                                       "border: 1px solid rgb(214, 176, 110);")
                        font = QtGui.QFont()
                        font.setFamily("Arial")
                        font.setPointSize(11)
                        font.setItalic(False)
                        widget_begin.lay.setFont(font)
                        widget_begin.lay.show()
                    widget_begin.lay.setText(tel)
                    if "добавляем мэйл" == "добавляем мэйл":
                        widget_begin.lay = QtWidgets.QLabel(widget_begin.list_of_new_widgets[widget_begin.i_1 - 1])
                        widget_begin.lay.setGeometry(QtCore.QRect(330, 80, 201, 21))
                        widget_begin.lay.setObjectName(f"label_mail_2{widget_begin.i_1 + 2}")
                        widget_begin.lay.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                       "color: rgb(154, 113, 67);\n"
                                                       "background-color: rgb(197, 147, 86);\n"
                                                       "border-radius: 5px;\n"
                                                       "border: 1px solid rgb(214, 176, 110);")
                        font = QtGui.QFont()
                        font.setFamily("Arial")
                        font.setPointSize(11)
                        font.setItalic(False)
                        widget_begin.lay.setFont(font)
                        widget_begin.lay.show()
                    widget_begin.lay.setText(mail)

                if "кнопки" == "кнопки":
                    if "к проекту" == "к проекту":
                        widget_begin.lay = QtWidgets.QPushButton(widget_begin.list_of_new_widgets[widget_begin.i_1 - 1])
                        widget_begin.lay.setGeometry(QtCore.QRect(540, 10, 161, 41))
                        font = QtGui.QFont()
                        font.setFamily("Arial")
                        font.setPointSize(10)
                        font.setBold(True)
                        font.setItalic(True)
                        font.setWeight(75)
                        widget_begin.lay.setFont(font)
                        widget_begin.lay.setText("К ПРОЕКТУ")
                        widget_begin.lay.setStyleSheet(f"#pushButton_k_proektu{widget_begin.i_1 + 2}\n"
                                                       "{\n"
                                                       "color: rgb(98, 71, 42);\n"
                                                       "background-color: rgb(197, 147, 86);\n"
                                                       "border-radius: 5px;\n"
                                                       "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                                       "border-right: 1px solid rgb(98, 71, 50);\n"
                                                       "}\n"
                                                       "\n"
                                                       f"#pushButton_k_proektu{widget_begin.i_1 + 2}:hover\n"
                                                       "{\n"
                                                       "color: rgb(118, 91, 62);\n"
                                                       "background-color: rgb(177, 127, 66);\n"
                                                       "border-radius: 5px;\n"
                                                       "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                                       "border-right: 1px solid rgb(98, 71, 50);\n"
                                                       "}\n"
                                                       "\n"
                                                       f"#pushButton_k_proektu{widget_begin.i_1 + 2}:pressed\n"
                                                       "{\n"
                                                       "color: rgb(98, 71, 42);\n"
                                                       "background-color: rgb(197, 147, 86);\n"
                                                       "border-radius: 5px;\n"
                                                       "\n"
                                                       "border-bottom: None;\n"
                                                       "border-right: None;\n"
                                                       "\n"
                                                       "border-top: 3px solid rgb(98, 71, 50);\n"
                                                       "border-left: 1px solid rgb(98, 71, 50);\n"
                                                       "}")
                        widget_begin.lay.setObjectName(f"pushButton_k_proektu{widget_begin.i_1 + 2}")
                        widget_begin.lay.show()
                    widget_begin.list_of_new_pbt_k_proectu.append(widget_begin.lay)
                    zakaz = widget_begin.lay_nomer.text()
                    widget_begin.lay.clicked.connect(lambda: widget_begin.Handler_k_proectu(self, zakaz))
                    if "к экспорту" == "к экспорту":
                        widget_begin.lay = QtWidgets.QPushButton(widget_begin.list_of_new_widgets[widget_begin.i_1 - 1])
                        widget_begin.lay.setGeometry(QtCore.QRect(540, 60, 161, 41))
                        font = QtGui.QFont()
                        font.setFamily("Arial")
                        font.setPointSize(10)
                        font.setBold(True)
                        font.setItalic(True)
                        font.setWeight(75)
                        widget_begin.lay.setFont(font)
                        widget_begin.lay.setText("")
                        widget_begin.lay.setStyleSheet(f"#pushButton_EXPORT_DOCX{widget_begin.i_1 + 2}\n"
                                                       "{\n"
                                                       "color: rgb(98, 71, 42);\n"
                                                       "background-color: rgb(197, 147, 86);\n"
                                                       "border-radius: 5px;\n"
                                                       "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                                       "border-right: 1px solid rgb(98, 71, 50);\n"
                                                       "}\n"
                                                       "\n"
                                                       f"#pushButton_EXPORT_DOCX{widget_begin.i_1 + 2}:hover\n"
                                                       "{\n"
                                                       "color: rgb(118, 91, 62);\n"
                                                       "background-color: rgb(177, 127, 66);\n"
                                                       "border-radius: 5px;\n"
                                                       "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                                       "border-right: 1px solid rgb(98, 71, 50);\n"
                                                       "}\n"
                                                       "\n"
                                                       f"#pushButton_EXPORT_DOCX{widget_begin.i_1 + 2}:pressed\n"
                                                       "{\n"
                                                       "color: rgb(98, 71, 42);\n"
                                                       "background-color: rgb(197, 147, 86);\n"
                                                       "border-radius: 5px;\n"
                                                       "\n"
                                                       "border-bottom: None;\n"
                                                       "border-right: None;\n"
                                                       "\n"
                                                       "border-top: 3px solid rgb(98, 71, 50);\n"
                                                       "border-left: 1px solid rgb(98, 71, 50);\n"
                                                       "}")
                        widget_begin.lay.setObjectName(f"pushButton_EXPORT_DOCX{widget_begin.i_1 + 2}")
                        widget_begin.lay.show()
                    widget_begin.list_of_new_pbt_export.append(widget_begin.lay)
                    widget_begin.lay.clicked.connect(lambda: widget_begin.Handler_export(self))
                widget_begin.i_1 += 1
            widget_begin.i_1_name+=1
        except:
            pass

    zakaz_nomer = ""
    def Handler_k_proectu(self, zakaz):
        widget_begin.zakaz_nomer = zakaz
        txt = "../pythonProject3/DATABASE/current_project/_" +zakaz.strip()+".txt"
        p = "Заказ №: " + zakaz

        self.pushButton_24.setDisabled(True)
        self.pushButton_25.setDisabled(True)
        self.pushButton_4.setDisabled(True)
        self.pushButton_14.setDisabled(True)
        self.lineEdit_17.setDisabled(True)
        self.pushButton_15.setDisabled(True)
        self.pushButton_5.setDisabled(True)
        self.pushButton_6.setDisabled(True)
        self.pushButton_9.setDisabled(True)
        self.pushButton_10.setDisabled(True)
        self.pushButton_11.setDisabled(True)
        self.pushButton_7.setDisabled(True)
        self.pushButton_8.setDisabled(True)
        self.pushButton_12.setDisabled(True)

        #имя человека, заполняющего бланк
        from client import CLIENT
        men = "Имя менеджера: "
        from translater import TRANSLATE
        if self.comboBox_16.currentIndex() == 1:
            self.label_43.setText(p)
            self.label_265.setText(p)
            import datetime
            now = str(datetime.datetime.now())
            # 2021-08-06 22:45:02.522446
            year = now[0:4]
            mounth = now[5:7]
            day = now[8:10]
            if len(day) == 1:
                day = "0"+day
            if len(mounth) == 1:
                mounth = "0"+mounth
            self.spinBox_20.setSpecialValueText(str(day))
            self.spinBox_18.setSpecialValueText(str(mounth))
            self.spinBox_19.setSpecialValueText(str(year))
            tdt = "Экспорт Акта оценки технического состояния оборудования\n№ "+zakaz
            self.pushButton_105.setText(tdt)
            tdt = "Экспорт счёта на оплату №"+zakaz+" \nот № " + str(day)+"."+str(mounth)+"."+str(year)
            self.pushButton_114.setText(tdt)
            tdt = "Экспорт Акта оценки технического состояния оборудования\n№ " + zakaz
            self.pushButton_126.setText(tdt)
            self.label_86.setText(p)
            self.label_147.setText(p)
            self.label_24.setText(p)

            TRANSLATE.into_str = CLIENT.pravilnost_parola
            TRANSLATE.out_str = ""
            TRANSLATE.eng_in_rus()
            men += TRANSLATE.out_str
            self.label_267.setText(men)
        # menZ = "Имя менеджера закупа: " + CLIENT.pravilnost_parola
        if self.comboBox_16.currentIndex() == 2:
            self.label_30.setText(p)
            self.label_177.setText(p)

            ing = "Имя инженера: "
            TRANSLATE.into_str = CLIENT.pravilnost_parola
            TRANSLATE.out_str = ""
            TRANSLATE.eng_in_rus()
            ing += TRANSLATE.out_str
            self.label_219.setText(ing)
            self.label_218.setText(ing)
        #закупа менеджер
        if self.comboBox_16.currentIndex() == 3:
            self.label_34.setText(p)
            self.label_194.setText(p)

            pass
        # коммерческий менеджер
        if self.comboBox_16.currentIndex() == 4:
            self.label_32.setText(p)

            pass


        with open(txt, 'r') as file:
            for index,line in enumerate(file):
                if index == 2:
                    print("Заказчик в кнопке", line)
                    self.label_296.setText(line.strip())
                    self.label_268.setText(line.strip())
                    self.label_306.setText(line.strip())
                    self.label_316.setText(line.strip())
                    self.label_66.setText(line.strip())
                    self.label_150.setText(line.strip())
                    self.label_89.setText(line.strip())
                    self.label_180.setText(line.strip())
                    self.label_197.setText(line.strip())
                if index == 10:
                    self.label_291.setText(line.strip())
                    self.label_269.setText(line.strip())
                    self.label_301.setText(line.strip())
                    self.label_311.setText(line.strip())
                    self.label_64.setText(line.strip())
                    self.label_153.setText(line.strip())
                    self.label_92.setText(line.strip())
                    self.label_189.setText(line.strip())
                    self.label_200.setText(line.strip())
                if index == 19:
                    self.label_292.setText(line.strip())
                    self.label_266.setText(line.strip())
                    self.label_302.setText(line.strip())
                    self.label_312.setText(line.strip())
                    self.label_53.setText(line.strip())
                    self.label_154.setText(line.strip())
                    self.label_93.setText(line.strip())
                    self.label_190.setText(line.strip())
                    self.label_231.setText(line.strip())

                if index == 7:
                    tel = line.strip()
                    buf = ''
                    if len(tel) == 7:
                        buf = ""
                        buf += tel[0]
                        buf += " "
                        buf += tel[1]
                        buf += tel[2]
                        buf += "-"
                        buf += tel[3]
                        buf += tel[4]
                        buf += "-"
                        buf += tel[5]
                        buf += tel[6]
                        tel = buf
                    if len(tel) == 11:
                        buf += " "
                        buf += tel[0]
                        buf += " "
                        buf += "("
                        buf += tel[1]
                        buf += tel[2]
                        buf += tel[3]
                        buf += ")"
                        buf += " "
                        buf += tel[4]
                        buf += tel[5]
                        buf += tel[6]
                        buf += "-"
                        buf += tel[7]
                        buf += tel[8]
                        buf += "-"
                        buf += tel[9]
                        buf += tel[10]
                        tel = buf
                    o = " "+tel
                    self.label_289.setText(o)
                    self.label_270.setText(o)
                    self.label_299.setText(o)
                    self.label_309.setText(o)
                    self.label_55.setText(o)
                    self.label_157.setText(o)
                    self.label_96.setText(o)
                    self.label_193.setText(o)
                    self.label_234.setText(o)


                if index == 3:
                    mail = " " + line.strip()
                    self.label_295.setText(mail)
                    self.label_273.setText(mail)
                    self.label_305.setText(mail)
                    self.label_315.setText(mail)
                    self.label_56.setText(mail)
                    self.label_156.setText(mail)
                    self.label_95.setText(mail)
                    self.label_192.setText(mail)
                    self.label_233.setText(mail)



        if self.comboBox_16.currentText() == "Мен. обслуживания":
            self.stackedWidget.setCurrentIndex(2)
        if self.comboBox_16.currentText() == "Инженер":
            self.stackedWidget.setCurrentIndex(3)
        if self.comboBox_16.currentText() == "Мен. закупа":
            self.stackedWidget.setCurrentIndex(4)

    def Handler_export(self):
        pass

#окно цен мен. расценки: добавление цен элементов
class widget_cena(Ui_MainWindow):
    i_1 = 1  # количество
    i_1_name = 1  # номер файла
    lay = ""
    lay_nomer = ""

    list_of_new_widgets = [] #фоновые виджеты

    #LE для ввода мен. закупа
    Articul = []
    cena_sebestoy = []
    valuta_1 = [] #SB

    cena_prodagi = []
    valuta_2 = [] #SB

    postavshik = []
    Istochnic = []

    nalichaye_na_sklade = [] #CB

    data_dostavki = []
    data_post = [] #LBL
    cena_dostavki = []
    cena_post = []  # LBL
    valuta_3 = []

    checkBoxs = []

    KNOPKA_IMEA_el = []
    #ДЛЯ ИНФОРМАЦИИ
    # FLAG_CB = [] -состояние чекбоксов



    def del_all_strings(self):
        for i in widget_cena.list_of_new_widgets:
            i.deleteLater()
        widget_cena.i_1 = 1
        widget_cena.list_of_new_widgets = []

    FLAG_LowREG = 0
    def add_new_string(self,imya_el,tip_rashoda,kolichestvo,edinitsy = "шт.",ist = ""):
        nomer_proecta = ""
        oborudovanie = ""
        zakazchic = ""
        Etap_proecta = ""
        data_konca = ""
        srochnost = ""
        tel = ""
        mail = ""

        shift = (widget_cena.i_1-1) * 205

        try:
            if widget_cena.i_1 > 2:
                self.frame_17.setMaximumHeight(420 + (205 * (widget_cena.i_1 - 2)))
                self.frame_17.setMinimumHeight(420 + (205 * (widget_cena.i_1 - 2)))

            if "добавляем фоновый виджет заказа" == "добавляем фоновый виджет заказа":
                widget_cena.lay = QtWidgets.QWidget(self.frame_17)
                y = 10 + shift
                # widget_cena.lay.setGeometry(QtCore.QRect(9, y, 711, 108))
                widget_cena.lay.setGeometry(QtCore.QRect(9, y, 597, 195))
                widget_cena.lay.setObjectName(f"widget_chena_{widget_cena.i_1 + 1}")  # №№№№№№№№
                widget_cena.lay.setStyleSheet(f"#widget_chena_{widget_cena.i_1 + 1}\n"
                                                  "{\n"
                                                  "background-color: rgb(177, 127, 66);\n"
                                                  "color: rgb(109, 65, 12);\n"
                                                  "border: 1px solid rgb(109, 65, 12);\n"
                                                  "border-radius: 10px;\n"
                                                  "}")
                widget_cena.list_of_new_widgets.append(widget_cena.lay)
                widget_cena.lay.show()
            if "не изменяемые элементы" == "не изменяемые элементы":
                if "добавляем лэйбл 'заказ№'" == "добавляем лэйбл 'заказ№'":
                    widget_cena.lay = QtWidgets.QLabel(widget_cena.list_of_new_widgets[int(widget_cena.i_1) - 1])
                    widget_cena.lay.setGeometry(QtCore.QRect(10, 10, 131, 18))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(12)
                    font.setItalic(True)
                    widget_cena.lay.setFont(font)
                    txt = " Элемент №" + str(widget_cena.i_1)
                    widget_cena.lay.setText(txt)
                    widget_cena.lay.setStyleSheet("border-radius: 5px;")
                    widget_cena.lay.setAlignment(QtCore.Qt.AlignCenter)
                    widget_cena.lay.setObjectName(f"mensale9_lbl_elNO_{widget_cena.i_1 + 1}")
                    widget_cena.lay.show()
                if "добавляем лэйбл 'рублей'" != "":
                    widget_cena.lay = QtWidgets.QLabel(widget_cena.list_of_new_widgets[int(widget_cena.i_1) - 1])
                    widget_cena.lay.setGeometry(QtCore.QRect(286, 91, 51, 20))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(12)
                    font.setItalic(True)
                    widget_cena.lay.setFont(font)
                    txt = "₽ (рус.)"
                    widget_cena.lay.setText(txt)
                    widget_cena.lay.setStyleSheet("background: None;")
                    widget_cena.lay.setAlignment(QtCore.Qt.AlignCenter)
                    widget_cena.lay.setObjectName(f"mensale9_lbl_el15NO_{widget_cena.i_1 + 1}")
                    widget_cena.lay.show()
                if "добавляем лэйбл 'рублей'" != "":
                    widget_cena.lay = QtWidgets.QLabel(widget_cena.list_of_new_widgets[int(widget_cena.i_1) - 1])
                    widget_cena.lay.setGeometry(QtCore.QRect(286, 112, 51, 20))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(12)
                    font.setItalic(True)
                    widget_cena.lay.setFont(font)
                    txt = "₽ (рус.)"
                    widget_cena.lay.setText(txt)
                    widget_cena.lay.setStyleSheet("background: None;")
                    widget_cena.lay.setAlignment(QtCore.Qt.AlignCenter)
                    widget_cena.lay.setObjectName(f"mensale9_lbl_el115NO_{widget_cena.i_1 + 1}")
                    widget_cena.lay.show()
                if "добавляем лэйбл 'рублей'" != "":
                    widget_cena.lay = QtWidgets.QLabel(widget_cena.list_of_new_widgets[int(widget_cena.i_1) - 1])
                    widget_cena.lay.setGeometry(QtCore.QRect(540, 166, 51, 20))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(12)
                    font.setItalic(True)
                    widget_cena.lay.setFont(font)
                    txt = "₽ (рус.)"
                    widget_cena.lay.setText(txt)
                    widget_cena.lay.setStyleSheet("background: None;")
                    widget_cena.lay.setAlignment(QtCore.Qt.AlignCenter)
                    widget_cena.lay.setObjectName(f"mensale9_lbl_el155NO_{widget_cena.i_1 + 1}")
                    widget_cena.lay.show()
                if "имя расходной единицы"!="":
                    widget_cena.lay = QtWidgets.QLabel(widget_cena.list_of_new_widgets[int(widget_cena.i_1) - 1])
                    widget_cena.lay.setGeometry(QtCore.QRect(160, 10, 191, 16))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(12)
                    font.setItalic(True)
                    widget_cena.lay.setFont(font)
                    txt = "Имя расх. единицы:"
                    widget_cena.lay.setText(txt)
                    widget_cena.lay.setStyleSheet("background: None;")
                    widget_cena.lay.setAlignment(QtCore.Qt.AlignLeft)
                    widget_cena.lay.setObjectName(f"mensale9_lbl_nameED_{widget_cena.i_1 + 1}")
                    widget_cena.lay.show()
                if "тип расхода" != "":
                    widget_cena.lay = QtWidgets.QLabel(widget_cena.list_of_new_widgets[int(widget_cena.i_1) - 1])
                    widget_cena.lay.setGeometry(QtCore.QRect(10, 35, 101, 18))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(12)
                    font.setItalic(True)
                    widget_cena.lay.setFont(font)
                    txt = "Тип расхода:"
                    widget_cena.lay.setText(txt)
                    widget_cena.lay.setStyleSheet("background: None;")
                    widget_cena.lay.setAlignment(QtCore.Qt.AlignLeft)
                    widget_cena.lay.setObjectName(f"mensale9_lbl_TypeED_{widget_cena.i_1 + 1}")
                    widget_cena.lay.show()
                if "количество"!="":
                    widget_cena.lay = QtWidgets.QLabel(widget_cena.list_of_new_widgets[int(widget_cena.i_1) - 1])
                    widget_cena.lay.setGeometry(QtCore.QRect(300, 41, 101, 18))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(12)
                    font.setItalic(True)
                    widget_cena.lay.setFont(font)
                    txt = "Количество:"
                    widget_cena.lay.setText(txt)
                    widget_cena.lay.setStyleSheet("background: None;")
                    widget_cena.lay.setAlignment(QtCore.Qt.AlignLeft)
                    widget_cena.lay.setObjectName(f"mensale9_lbl_articulED_3{widget_cena.i_1 + 1}")
                    widget_cena.lay.show()
                if "единицы"!="":
                    widget_cena.lay = QtWidgets.QLabel(widget_cena.list_of_new_widgets[int(widget_cena.i_1) - 1])
                    widget_cena.lay.setGeometry(QtCore.QRect(320, 66, 81, 18))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(12)
                    font.setItalic(True)
                    widget_cena.lay.setFont(font)
                    txt = "Единицы:"
                    widget_cena.lay.setText(txt)
                    widget_cena.lay.setStyleSheet("background: None;")
                    widget_cena.lay.setAlignment(QtCore.Qt.AlignLeft)
                    widget_cena.lay.setObjectName(f"mensale9_lbl_articulED_3{widget_cena.i_1 + 1}")
                    widget_cena.lay.show()
                if "артикул"!="":
                    widget_cena.lay = QtWidgets.QLabel(widget_cena.list_of_new_widgets[int(widget_cena.i_1) - 1])
                    widget_cena.lay.setGeometry(QtCore.QRect(11, 63, 101, 18))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(12)
                    font.setItalic(True)
                    widget_cena.lay.setFont(font)
                    txt = "Артикул:"
                    widget_cena.lay.setText(txt)
                    widget_cena.lay.setStyleSheet("background: None;")
                    widget_cena.lay.setAlignment(QtCore.Qt.AlignLeft)
                    widget_cena.lay.setObjectName(f"mensale9_lbl_articulED_1{widget_cena.i_1 + 1}")
                    widget_cena.lay.show()
                if "Цена себестой"!="":
                    widget_cena.lay = QtWidgets.QLabel(widget_cena.list_of_new_widgets[int(widget_cena.i_1) - 1])
                    widget_cena.lay.setGeometry(QtCore.QRect(10, 93, 181, 18))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(12)
                    font.setItalic(True)
                    widget_cena.lay.setFont(font)
                    txt = "Цена себестоимости:"
                    widget_cena.lay.setText(txt)
                    widget_cena.lay.setStyleSheet("background: None;")
                    widget_cena.lay.setAlignment(QtCore.Qt.AlignLeft)
                    widget_cena.lay.setObjectName(f"mensale9_lbl_Sebest_1{widget_cena.i_1 + 1}")
                    widget_cena.lay.show()
                if "Цена продажи"!="":
                    widget_cena.lay = QtWidgets.QLabel(widget_cena.list_of_new_widgets[int(widget_cena.i_1) - 1])
                    widget_cena.lay.setGeometry(QtCore.QRect(10, 116, 181, 18))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(12)
                    font.setItalic(True)
                    widget_cena.lay.setFont(font)
                    txt = "Цена продажи:"
                    widget_cena.lay.setText(txt)
                    widget_cena.lay.setStyleSheet("background: None;")
                    widget_cena.lay.setAlignment(QtCore.Qt.AlignLeft)
                    widget_cena.lay.setObjectName(f"mensale9_lbl_Sale_1{widget_cena.i_1 + 1}")
                    widget_cena.lay.show()
                if "поставщик"!="":
                    widget_cena.lay = QtWidgets.QLabel(widget_cena.list_of_new_widgets[int(widget_cena.i_1) - 1])
                    widget_cena.lay.setGeometry(QtCore.QRect(352, 92, 104, 18))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(12)
                    font.setItalic(True)
                    widget_cena.lay.setFont(font)
                    txt = "Поставщик:"
                    widget_cena.lay.setText(txt)
                    widget_cena.lay.setStyleSheet("background: None;")
                    widget_cena.lay.setAlignment(QtCore.Qt.AlignLeft)
                    widget_cena.lay.setObjectName(f"mensale9_lbl_saler_1{widget_cena.i_1 + 1}")
                    widget_cena.lay.show()
                if "источник"!="":
                    widget_cena.lay = QtWidgets.QLabel(widget_cena.list_of_new_widgets[int(widget_cena.i_1) - 1])
                    widget_cena.lay.setGeometry(QtCore.QRect(352, 112, 104, 18))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(12)
                    font.setItalic(True)
                    widget_cena.lay.setFont(font)
                    txt = "Источник:"
                    widget_cena.lay.setText(txt)
                    widget_cena.lay.setStyleSheet("background: None;")
                    widget_cena.lay.setAlignment(QtCore.Qt.AlignLeft)
                    widget_cena.lay.setObjectName(f"mensale9_lbl_sourse_1{widget_cena.i_1 + 1}")
                    widget_cena.lay.show()
                if "Дата доставки"!="":
                    widget_cena.lay = QtWidgets.QLabel(widget_cena.list_of_new_widgets[int(widget_cena.i_1) - 1])
                    widget_cena.lay.setGeometry(QtCore.QRect(300, 145, 128, 18))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(12)
                    font.setItalic(True)
                    widget_cena.lay.setFont(font)
                    txt = "Дата доставки:"
                    widget_cena.lay.setText(txt)
                    widget_cena.lay.setStyleSheet("background: None;")
                    widget_cena.lay.setAlignment(QtCore.Qt.AlignLeft)
                    widget_cena.lay.setObjectName(f"mensale9_lbl_DATAdelivery_1{widget_cena.i_1 + 1}")
                    widget_cena.lay.show()
                widget_cena.data_post.append(widget_cena.lay)
                if "Цена доставки"!="":
                    widget_cena.lay = QtWidgets.QLabel(widget_cena.list_of_new_widgets[int(widget_cena.i_1) - 1])
                    widget_cena.lay.setGeometry(QtCore.QRect(300, 168, 128, 18))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(12)
                    font.setItalic(True)
                    widget_cena.lay.setFont(font)
                    txt = "Цена доставки:"
                    widget_cena.lay.setText(txt)
                    widget_cena.lay.setStyleSheet("background: None;")
                    widget_cena.lay.setAlignment(QtCore.Qt.AlignLeft)
                    widget_cena.lay.setObjectName(f"mensale9_lbl_delivery_1{widget_cena.i_1 + 1}")
                    widget_cena.lay.show()
                widget_cena.cena_post.append(widget_cena.lay)
            if "элементы, которые заполнил инженер"!="":
                if "имя расх единицы"!="":
                    widget_cena.lay = QtWidgets.QPushButton(widget_cena.list_of_new_widgets[int(widget_cena.i_1) - 1])
                    widget_cena.lay.setGeometry(QtCore.QRect(310, 7, 281, 30))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    if widget_cena.FLAG_LowREG == 1:
                        widget_cena.FLAG_LowREG = 0
                        font.setPointSize(10)
                    else:
                        font.setPointSize(12)
                    font.setItalic(True)
                    widget_cena.lay.setFont(font)
                    widget_cena.lay.setObjectName(f"pushButton_135_{widget_cena.i_1 + 1}_")
                    widget_cena.lay.setStyleSheet(f"#pushButton_135_{widget_cena.i_1 + 1}_\n"
                                                  "{\n"
                                                  "border-radius: 5px;\n"
                                                  "color: rgb(109, 65, 12);\n"
                                                  "background-color: rgb(197, 147, 86);\n"
                                                  "}\n"
                                                  f"#pushButton_135_{widget_cena.i_1 + 1}_:hover\n"
                                                  "{\n"
                                                  "border: 1px solid rgb(109, 65, 12);\n"
                                                  "border-radius: 1px;\n"
                                                  "color: rgb(119, 75, 22);\n"
                                                  "background-color: rgb(177, 127, 66);\n"
                                                  "}\n"
                                                  f"#pushButton_135_{widget_cena.i_1 + 1}_:pressed\n"
                                                  "{\n"
                                                  "border: 1px solid rgb(109, 65, 12);\n"
                                                  "border-radius: 1px;\n"
                                                  "color: rgb(119, 75, 22);\n"
                                                  "background-color: rgb(197, 147, 86);\n"
                                                  "}")
                    # widget_cena.lay.setAlignment(QtCore.Qt.AlignLeft)
                    widget_cena.lay.show()
                    widget_cena.KNOPKA_IMEA_el.append(widget_cena.lay)
                widget_cena.lay.clicked.connect(lambda: widget_cena.HANDLER_PBT_copy(self,imya_el))
                widget_cena.lay.setText(imya_el)
                if "тип расхода"!="":
                    widget_cena.lay = QtWidgets.QLabel(widget_cena.list_of_new_widgets[int(widget_cena.i_1) - 1])
                    widget_cena.lay.setGeometry(QtCore.QRect(112, 34, 171, 18))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(12)
                    font.setItalic(True)
                    widget_cena.lay.setFont(font)
                    widget_cena.lay.setStyleSheet("border-radius: 5px;\ncolor: rgb(109, 65, 12);")
                    widget_cena.lay.setAlignment(QtCore.Qt.AlignCenter)
                    widget_cena.lay.setObjectName(f"mensale9_lbl_TypeTypeED_1{widget_cena.i_1 + 1}")
                    widget_cena.lay.show()
                widget_cena.lay.setText(tip_rashoda)
                if "Количество"!="":
                    widget_cena.lay = QtWidgets.QLabel(widget_cena.list_of_new_widgets[int(widget_cena.i_1) - 1])
                    widget_cena.lay.setGeometry(QtCore.QRect(400, 40, 191, 18))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(12)
                    font.setItalic(True)
                    widget_cena.lay.setFont(font)
                    widget_cena.lay.setStyleSheet("border-radius: 5px;\ncolor: rgb(109, 65, 12);")
                    widget_cena.lay.setAlignment(QtCore.Qt.AlignCenter)
                    widget_cena.lay.setObjectName(f"mensale9_lbl_TypeTypeED_3{widget_cena.i_1 + 1}")
                    widget_cena.lay.show()
                widget_cena.lay.setText(kolichestvo)
                if "Единицы"!="":
                    widget_cena.lay = QtWidgets.QLabel(widget_cena.list_of_new_widgets[int(widget_cena.i_1) - 1])
                    widget_cena.lay.setGeometry(QtCore.QRect(400, 66, 191, 18))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(12)
                    font.setItalic(True)
                    widget_cena.lay.setFont(font)
                    widget_cena.lay.setStyleSheet("border-radius: 5px;\ncolor: rgb(109, 65, 12);")
                    widget_cena.lay.setAlignment(QtCore.Qt.AlignCenter)
                    widget_cena.lay.setObjectName(f"mensale9_lbl_TypeTypeED_3{widget_cena.i_1 + 1}")
                    widget_cena.lay.show()
                widget_cena.lay.setText(edinitsy)

            if "изменяемые элементы" == "изменяемые элементы":
                if "Артикул"!="LE":
                    widget_cena.lay = QtWidgets.QLineEdit(widget_cena.list_of_new_widgets[int(widget_cena.i_1) - 1])
                    widget_cena.lay.setGeometry(QtCore.QRect(93, 60, 191, 20))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(12)
                    font.setItalic(True)
                    widget_cena.lay.setFont(font)
                    widget_cena.lay.setStyleSheet("border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
                    widget_cena.lay.setAlignment(QtCore.Qt.AlignCenter)
                    widget_cena.lay.setObjectName(f"mensale9_lbl_articulArticulED_1{widget_cena.i_1 + 1}")
                    widget_cena.lay.show()
                iter = widget_cena.i_1-1
                widget_cena.lay.returnPressed.connect(lambda: widget_cena.HANDLER_NEXT_ARTIKUL(self,iter))
                widget_cena.Articul.append(widget_cena.lay)
                if "Цена себестой"!="LE":
                    widget_cena.lay = QtWidgets.QLineEdit(widget_cena.list_of_new_widgets[int(widget_cena.i_1) - 1])
                    widget_cena.lay.setGeometry(QtCore.QRect(190, 91, 91, 20))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(12)
                    font.setItalic(True)
                    widget_cena.lay.setFont(font)
                    widget_cena.lay.setStyleSheet("border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
                    widget_cena.lay.setAlignment(QtCore.Qt.AlignCenter)
                    widget_cena.lay.setObjectName(f"mensale9_le_Sebest_1{widget_cena.i_1 + 1}")
                    widget_cena.lay.show()
                widget_cena.lay.returnPressed.connect(lambda: widget_cena.HANDLER_NEXT_SEBESTOY(self,iter))
                widget_cena.cena_sebestoy.append(widget_cena.lay)
                if "Цена продажи"!="LE":
                    widget_cena.lay = QtWidgets.QLineEdit(widget_cena.list_of_new_widgets[int(widget_cena.i_1) - 1])
                    widget_cena.lay.setGeometry(QtCore.QRect(190, 114, 91, 20))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(12)
                    font.setItalic(True)
                    widget_cena.lay.setFont(font)
                    widget_cena.lay.setStyleSheet("border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
                    widget_cena.lay.setAlignment(QtCore.Qt.AlignCenter)
                    widget_cena.lay.setObjectName(f"mensale9_le_Sale_1{widget_cena.i_1 + 1}")
                    widget_cena.lay.show()
                widget_cena.lay.returnPressed.connect(lambda: widget_cena.HANDLER_NEXT_PRODAGI(self,iter))
                widget_cena.cena_prodagi.append(widget_cena.lay)
                if "поставщик"!="LE":
                    widget_cena.lay = QtWidgets.QLineEdit(widget_cena.list_of_new_widgets[int(widget_cena.i_1) - 1])
                    widget_cena.lay.setGeometry(QtCore.QRect(450, 91, 141, 20))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(12)
                    font.setItalic(True)
                    widget_cena.lay.setFont(font)
                    widget_cena.lay.setStyleSheet("border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
                    widget_cena.lay.setAlignment(QtCore.Qt.AlignCenter)
                    widget_cena.lay.setObjectName(f"mensale9_le_saler_1{widget_cena.i_1 + 1}")
                    widget_cena.lay.show()
                widget_cena.lay.returnPressed.connect(lambda: widget_cena.HANDLER_NEXT_POSTAVSHIK(self,iter))
                widget_cena.postavshik.append(widget_cena.lay)
                if "источик"!="LE":
                    widget_cena.lay = QtWidgets.QLineEdit(widget_cena.list_of_new_widgets[int(widget_cena.i_1) - 1])
                    widget_cena.lay.setGeometry(QtCore.QRect(440, 113, 151, 20))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(12)
                    font.setItalic(True)
                    widget_cena.lay.setFont(font)
                    widget_cena.lay.setStyleSheet("border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
                    widget_cena.lay.setAlignment(QtCore.Qt.AlignCenter)
                    widget_cena.lay.setObjectName(f"mensale9_le_sourse_1{widget_cena.i_1 + 1}")
                    widget_cena.lay.show()
                widget_cena.lay.setText(ist)
                widget_cena.lay.returnPressed.connect(lambda: widget_cena.HANDLER_NEXT_ISTOCHNIK(self,iter))
                widget_cena.Istochnic.append(widget_cena.lay)
                if "дата доставки" != "LE":
                    widget_cena.lay = QtWidgets.QLineEdit(widget_cena.list_of_new_widgets[int(widget_cena.i_1) - 1])
                    widget_cena.lay.setGeometry(QtCore.QRect(440, 145, 151, 20))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(12)
                    font.setItalic(True)
                    widget_cena.lay.setFont(font)
                    widget_cena.lay.setStyleSheet(
                        "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
                    widget_cena.lay.setAlignment(QtCore.Qt.AlignCenter)
                    widget_cena.lay.setObjectName(f"mensale9_le_DATAdelivery_1{widget_cena.i_1 + 1}")
                    widget_cena.lay.show()
                widget_cena.lay.returnPressed.connect(lambda: widget_cena.HANDLER_NEXT_DATA_DOST(self,iter))
                widget_cena.data_dostavki.append(widget_cena.lay)
                if "цена доставки" != "LE":
                    widget_cena.lay = QtWidgets.QLineEdit(widget_cena.list_of_new_widgets[int(widget_cena.i_1) - 1])
                    widget_cena.lay.setGeometry(QtCore.QRect(440, 168, 98, 20))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(12)
                    font.setItalic(True)
                    widget_cena.lay.setFont(font)
                    widget_cena.lay.setStyleSheet(
                        "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
                    widget_cena.lay.setAlignment(QtCore.Qt.AlignCenter)
                    widget_cena.lay.setObjectName(f"mensale9_le_delivery_1{widget_cena.i_1 + 1}")
                    widget_cena.lay.show()
                widget_cena.lay.returnPressed.connect(lambda: widget_cena.HANDLER_NEXT_CENA_DOST(self,iter))
                widget_cena.cena_dostavki.append(widget_cena.lay)
            if "чекбокс и линии" == "чекбокс и линии":
                if "Чекбокс" !="":
                    widget_cena.lay = QtWidgets.QCheckBox(widget_cena.list_of_new_widgets[int(widget_cena.i_1) - 1])
                    widget_cena.lay.setGeometry(QtCore.QRect(70, 158, 171, 17))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(12)
                    font.setItalic(True)
                    widget_cena.lay.setFont(font)
                    widget_cena.lay.setText("Наличае на складе")
                    widget_cena.lay.setStyleSheet("background-color: None;")
                    widget_cena.lay.setObjectName(f"mensale9_CheckBox_delivery_1{widget_cena.i_1 + 1}")
                    widget_cena.lay.show()
                widget_cena.checkBoxs.append(widget_cena.lay)
                widget_cena.lay.clicked.connect(lambda: widget_cena.HANDLER_CheckBox(self,iter))
                widget_cena.FLAG_CB.append(0)
                if "line1"!="":
                    widget_cena.lay = QtWidgets.QFrame(widget_cena.list_of_new_widgets[int(widget_cena.i_1) - 1])
                    widget_cena.lay.setGeometry(QtCore.QRect(290, 30, 3, 51))
                    widget_cena.lay.setFrameShape(QtWidgets.QFrame.VLine)
                    widget_cena.lay.setFrameShadow(QtWidgets.QFrame.Sunken)
                    widget_cena.lay.setObjectName(f"mensale9_line1_3{widget_cena.i_1 + 1}")
                    widget_cena.lay.show()
                if "line2" != "":
                    widget_cena.lay = QtWidgets.QFrame(widget_cena.list_of_new_widgets[int(widget_cena.i_1) - 1])
                    widget_cena.lay.setGeometry(QtCore.QRect(342, 88, 3, 51))
                    widget_cena.lay.setFrameShape(QtWidgets.QFrame.VLine)
                    widget_cena.lay.setFrameShadow(QtWidgets.QFrame.Sunken)
                    widget_cena.lay.setObjectName(f"mensale9_line1_3{widget_cena.i_1 + 1}")
                    widget_cena.lay.show()
                if "line3" != "":
                    widget_cena.lay = QtWidgets.QFrame(widget_cena.list_of_new_widgets[int(widget_cena.i_1) - 1])
                    widget_cena.lay.setGeometry(QtCore.QRect(290, 144, 3, 47))
                    widget_cena.lay.setFrameShape(QtWidgets.QFrame.VLine)
                    widget_cena.lay.setFrameShadow(QtWidgets.QFrame.Sunken)
                    widget_cena.lay.setObjectName(f"mensale9_line1_3{widget_cena.i_1 + 1}")
                    widget_cena.lay.show()

            widget_cena.i_1 += 1
            widget_cena.i_1_name += 1
        except:
            print("zak")
    def HANDLER_PBT_copy(self, nomer_iteracii):
        import pyperclip
        pyperclip.copy(widget_cena.KNOPKA_IMEA_el[nomer_iteracii - 1].text())

    def HANDLER_NEXT_ARTIKUL(self,iteration):
        if "?" in widget_cena.Articul[iteration].text():
            widget_cena.Articul[iteration].clear()
            widget_cena.Articul[iteration].setFocus()
            widget_cena.Articul[iteration].setStyleSheet(
                "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
        else:
            widget_cena.Articul[iteration].setStyleSheet(
                "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
            widget_cena.cena_sebestoy[iteration].setFocus()
    def HANDLER_NEXT_SEBESTOY(self,iteration):
        if "?" in widget_cena.cena_sebestoy[iteration].text():
            widget_cena.cena_sebestoy[iteration].clear()
            widget_cena.cena_sebestoy[iteration].setFocus()
            widget_cena.cena_sebestoy[iteration].setStyleSheet(
                "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
        else:
            widget_cena.cena_sebestoy[iteration].setStyleSheet(
                "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
            widget_cena.cena_prodagi[iteration].setFocus()

        if "," in widget_cena.cena_sebestoy[iteration].text():
            txt = widget_cena.cena_sebestoy[iteration].text()
            counter = 0
            buf = ""
            buf_2 = ""
            try:
                while True:
                    if txt[counter] != ",":
                        buf += txt[counter]
                    else:
                        break
                    counter += 1
                counter += 1
                while True:
                    if txt[counter] != ",":
                        buf_2 += txt[counter]
                    else:
                        break
                    counter += 1
            except:
                pass

            try:
                k = int(buf)
                k = int(buf_2)
            except:
                widget_cena.cena_sebestoy[iteration].clear()
                widget_cena.cena_sebestoy[iteration].setFocus()
                widget_cena.cena_sebestoy[iteration].setStyleSheet(
                    "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
                return
            else:
                widget_cena.cena_sebestoy[iteration].setStyleSheet(
                    "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
                # widget_cena.cena_sebestoy[iteration].setFocus()

            if len(buf_2) > 2:
                widget_cena.cena_sebestoy[iteration].clear()
                widget_cena.cena_sebestoy[iteration].setFocus()
                widget_cena.cena_sebestoy[iteration].setStyleSheet(
                    "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
                return
            else:
                widget_cena.cena_sebestoy[iteration].setStyleSheet(
                    "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")

            if len(buf_2) == 1:
                buf_2 = buf_2 + "0"
            if len(buf_2) == 0:
                buf_2 = "00"
            end_buf = buf + "." + buf_2
            widget_cena.cena_sebestoy[iteration].setText(end_buf)



        if "." not in widget_cena.cena_sebestoy[iteration].text():
            h = widget_cena.cena_sebestoy[iteration].text()
            h += ".00"
            widget_cena.cena_sebestoy[iteration].setText(h)

        txt = widget_cena.cena_sebestoy[iteration].text()
        counter = 0
        buf = ""
        buf_2 = ""
        try:
            while True:
                if txt[counter] != ".":
                    buf += txt[counter]
                else:
                    break
                counter += 1
            counter += 1
            while True:
                if txt[counter] != ".":
                    buf_2 += txt[counter]
                else:
                    break
                counter += 1
        except:
            pass

        try:
            k = int(buf)
            k = int(buf_2)
        except:
            widget_cena.cena_sebestoy[iteration].clear()
            widget_cena.cena_sebestoy[iteration].setFocus()
            widget_cena.cena_sebestoy[iteration].setStyleSheet(
                "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
            return
        else:
            widget_cena.cena_sebestoy[iteration].setStyleSheet(
                "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
        if len(buf_2) > 2:
            widget_cena.cena_sebestoy[iteration].clear()
            widget_cena.cena_sebestoy[iteration].setFocus()
            widget_cena.cena_sebestoy[iteration].setStyleSheet(
                "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
            return
        else:
            widget_cena.cena_sebestoy[iteration].setStyleSheet(
                "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
            # widget_cena.cena_sebestoy[iteration].setFocus()
        widget_cena.cena_prodagi[iteration].setFocus()

    def HANDLER_NEXT_PRODAGI(self,iteration):
        if "?" in widget_cena.cena_prodagi[iteration].text():
            widget_cena.cena_prodagi[iteration].clear()
            widget_cena.cena_prodagi[iteration].setFocus()
            widget_cena.cena_prodagi[iteration].setStyleSheet(
                "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
        else:
            widget_cena.cena_prodagi[iteration].setStyleSheet(
                "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
            widget_cena.cena_prodagi[iteration].setFocus()

        if "," in widget_cena.cena_prodagi[iteration].text():
            txt = widget_cena.cena_prodagi[iteration].text()
            counter = 0
            buf = ""
            buf_2 = ""
            try:
                while True:
                    if txt[counter] != ",":
                        buf += txt[counter]
                    else:
                        break
                    counter += 1
                counter += 1
                while True:
                    if txt[counter] != ",":
                        buf_2 += txt[counter]
                    else:
                        break
                    counter += 1
            except:
                pass

            try:
                k = int(buf)
                k = int(buf_2)
            except:
                widget_cena.cena_prodagi[iteration].clear()
                widget_cena.cena_prodagi[iteration].setFocus()
                widget_cena.cena_prodagi[iteration].setStyleSheet(
                    "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
                return
            else:
                widget_cena.cena_prodagi[iteration].setStyleSheet(
                    "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
                # widget_cena.cena_prodagi[iteration].setFocus()

            if len(buf_2) > 2:
                widget_cena.cena_prodagi[iteration].clear()
                widget_cena.cena_prodagi[iteration].setFocus()
                widget_cena.cena_prodagi[iteration].setStyleSheet(
                    "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
                return
            else:
                widget_cena.cena_prodagi[iteration].setStyleSheet(
                    "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")

            if len(buf_2) == 1:
                buf_2 = buf_2 + "0"
            if len(buf_2) == 0:
                buf_2 = "00"
            end_buf = buf + "." + buf_2
            widget_cena.cena_prodagi[iteration].setText(end_buf)

        if "." not in widget_cena.cena_prodagi[iteration].text():
            h = widget_cena.cena_prodagi[iteration].text()
            h += ".00"
            widget_cena.cena_prodagi[iteration].setText(h)

        txt = widget_cena.cena_prodagi[iteration].text()
        counter = 0
        buf = ""
        buf_2 = ""
        try:
            while True:
                if txt[counter] != ".":
                    buf += txt[counter]
                else:
                    break
                counter += 1
            counter += 1
            while True:
                if txt[counter] != ".":
                    buf_2 += txt[counter]
                else:
                    break
                counter += 1
        except:
            pass

        try:
            k = int(buf)
            k = int(buf_2)
        except:
            widget_cena.cena_prodagi[iteration].clear()
            widget_cena.cena_prodagi[iteration].setFocus()
            widget_cena.cena_prodagi[iteration].setStyleSheet(
                "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
            return
        else:
            widget_cena.cena_prodagi[iteration].setStyleSheet(
                "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
        if len(buf_2) > 2:
            widget_cena.cena_prodagi[iteration].clear()
            widget_cena.cena_prodagi[iteration].setFocus()
            widget_cena.cena_prodagi[iteration].setStyleSheet(
                "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
            return
        else:
            widget_cena.cena_prodagi[iteration].setStyleSheet(
                "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
            # widget_cena.cena_prodagi[iteration].setFocus()
        widget_cena.postavshik[iteration].setFocus()
    def HANDLER_NEXT_POSTAVSHIK(self,iteration):
        if "?" in widget_cena.postavshik[iteration].text():
            widget_cena.postavshik[iteration].clear()
            widget_cena.postavshik[iteration].setFocus()
            widget_cena.postavshik[iteration].setStyleSheet(
                "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
        else:
            widget_cena.postavshik[iteration].setStyleSheet(
                "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
            widget_cena.Istochnic[iteration].setFocus()

    FLAG_CB = []
    def HANDLER_CheckBox(self, iteration):
        print(iteration)
        if widget_cena.FLAG_CB[iteration] == 0:
            widget_cena.FLAG_CB[iteration] = 1
            widget_cena.data_dostavki[iteration].hide()
            widget_cena.cena_dostavki[iteration].hide()
            widget_cena.data_post[iteration].hide()
            widget_cena.cena_post[iteration].hide()
            return
        if widget_cena.FLAG_CB[iteration] == 1:
            widget_cena.FLAG_CB[iteration] = 0
            widget_cena.data_dostavki[iteration].show()
            widget_cena.cena_dostavki[iteration].show()
            widget_cena.data_post[iteration].show()
            widget_cena.cena_post[iteration].show()

    def HANDLER_NEXT_ISTOCHNIK(self,iteration):
        if "?" in widget_cena.Istochnic[iteration].text():
            widget_cena.Istochnic[iteration].clear()
            widget_cena.Istochnic[iteration].setFocus()
            widget_cena.Istochnic[iteration].setStyleSheet(
                "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
        else:
            widget_cena.Istochnic[iteration].setStyleSheet(
                "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
            if widget_cena.FLAG_CB[iteration] == 0:
                widget_cena.data_dostavki[iteration].setFocus()
            else:
                try:
                    widget_cena.Articul[iteration + 1].setFocus()
                    # iteration += 1
                except:
                    pass

    def HANDLER_NEXT_DATA_DOST(self,iteration):
        buf = widget_cena.data_dostavki[iteration].text()
        buf_2 = ""
        if "." not in buf and "," not in buf:
            if len(buf) == 4:
                print("four")
                buf_2 += "0"
                buf_2 += buf[0]
                try:
                    k = int(buf[0])
                except:
                    widget_cena.data_dostavki[iteration].clear()
                    widget_cena.data_dostavki[iteration].setFocus()
                    widget_cena.data_dostavki[iteration].setStyleSheet(
                        "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
                    return
                buf_2 += "."
                buf_2 += "0"
                buf_2 += buf[1]
                try:
                    k = int(buf[1])
                except:
                    widget_cena.data_dostavki[iteration].clear()
                    widget_cena.data_dostavki[iteration].setFocus()
                    widget_cena.data_dostavki[iteration].setStyleSheet(
                        "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
                    return
                buf_2 += "."
                buf_2 += "20"
                buf_2 += buf[2:4]
                try:
                    k = int(buf[2:4])
                except:
                    widget_cena.data_dostavki[iteration].clear()
                    widget_cena.data_dostavki[iteration].setFocus()
                    widget_cena.data_dostavki[iteration].setStyleSheet(
                        "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
                    return
                widget_cena.data_dostavki[iteration].setText(buf_2)
                widget_cena.data_dostavki[iteration].setStyleSheet(
                    "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
            else:
                if len(buf) == 6:
                    buf_2 += buf[0:2]
                    try:
                        k = int(buf[0:2])
                    except:
                        widget_cena.data_dostavki[iteration].clear()
                        widget_cena.data_dostavki[iteration].setFocus()
                        widget_cena.data_dostavki[iteration].setStyleSheet(
                            "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
                        return
                    buf_2 += "."
                    buf_2 += buf[2:4]
                    try:
                        k = int(buf[2:4])
                    except:
                        widget_cena.data_dostavki[iteration].clear()
                        widget_cena.data_dostavki[iteration].setFocus()
                        widget_cena.data_dostavki[iteration].setStyleSheet(
                            "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
                        return
                    buf_2 += "."
                    buf_2 += "20"
                    buf_2 += buf[4:6]
                    try:
                        k = int(buf[4:6])
                    except:
                        widget_cena.data_dostavki[iteration].clear()
                        widget_cena.data_dostavki[iteration].setFocus()
                        widget_cena.data_dostavki[iteration].setStyleSheet(
                            "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
                        return
                    widget_cena.data_dostavki[iteration].setText(buf_2)
                    widget_cena.data_dostavki[iteration].setStyleSheet(
                        "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
                else:
                    if len(buf) == 8:
                        buf_2 += buf[0:2]
                        try:
                            k = int(buf[0:2])
                        except:
                            widget_cena.data_dostavki[iteration].clear()
                            widget_cena.data_dostavki[iteration].setFocus()
                            widget_cena.data_dostavki[iteration].setStyleSheet(
                                "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
                            return
                        buf_2 += "."
                        buf_2 += buf[2:4]
                        try:
                            k = int(buf[2:4])
                        except:
                            widget_cena.data_dostavki[iteration].clear()
                            widget_cena.data_dostavki[iteration].setFocus()
                            widget_cena.data_dostavki[iteration].setStyleSheet(
                                "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
                            return
                        buf_2 += "."
                        buf_2 += buf[4:9]
                        try:
                            k = int(buf[4:9])
                        except:
                            widget_cena.data_dostavki[iteration].clear()
                            widget_cena.data_dostavki[iteration].setFocus()
                            widget_cena.data_dostavki[iteration].setStyleSheet(
                                "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
                            return
                        widget_cena.data_dostavki[iteration].setText(buf_2)
                        widget_cena.data_dostavki[iteration].setStyleSheet(
                            "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
                    else:
                        widget_cena.data_dostavki[iteration].clear()
                        widget_cena.data_dostavki[iteration].setFocus()
                        widget_cena.data_dostavki[iteration].setStyleSheet(
                            "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
                        return
        else:
            if len(buf) < 10 or len(buf) > 10:
                widget_cena.data_dostavki[iteration].clear()
                widget_cena.data_dostavki[iteration].setFocus()
                widget_cena.data_dostavki[iteration].setStyleSheet(
                    "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
                return

            print("00000111")
            counter_div_chars = 0
            int_ch = ""
            for i in buf:
                if i == ".":
                    try:
                        y = int(int_ch)
                    except:
                        widget_cena.data_dostavki[iteration].clear()
                        widget_cena.data_dostavki[iteration].setFocus()
                        widget_cena.data_dostavki[iteration].setStyleSheet(
                            "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
                        return
                    else:
                        int_ch = ""
                    counter_div_chars+=1
                else:
                    int_ch += i
            if counter_div_chars > 2 or (counter_div_chars< 2 and counter_div_chars > 0):
                widget_cena.data_dostavki[iteration].clear()
                widget_cena.data_dostavki[iteration].setFocus()
                widget_cena.data_dostavki[iteration].setStyleSheet(
                    "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
                return
            if counter_div_chars == 0:
                k = ""
                int_ch = ""
                for i in buf:
                    if i == "," or i == ",":
                        try:
                            y = int(int_ch)
                        except:
                            widget_cena.data_dostavki[iteration].clear()
                            widget_cena.data_dostavki[iteration].setFocus()
                            widget_cena.data_dostavki[iteration].setStyleSheet(
                                "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
                            return
                        else:
                            int_ch = ""

                        counter_div_chars += 1
                        k += "."
                    else:
                        int_ch += i
                        k += i
                    buf = k
                print("counter_div_chars",counter_div_chars)
                if counter_div_chars > 2 or counter_div_chars < 2:
                    print("blin")
                    widget_cena.data_dostavki[iteration].clear()
                    widget_cena.data_dostavki[iteration].setFocus()
                    widget_cena.data_dostavki[iteration].setStyleSheet(
                        "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
                    return
                else:
                    if len(buf) < 10 or len(buf) > 10:
                        widget_cena.data_dostavki[iteration].clear()
                        widget_cena.data_dostavki[iteration].setFocus()
                        widget_cena.data_dostavki[iteration].setStyleSheet(
                            "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
                        return
                    else:
                        widget_cena.data_dostavki[iteration].setText(buf)
        widget_cena.data_dostavki[iteration].setStyleSheet(
            "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
        widget_cena.cena_dostavki[iteration].setFocus()
    def HANDLER_NEXT_CENA_DOST(self,iteration):
        if "?" in widget_cena.cena_dostavki[iteration].text():
            widget_cena.cena_dostavki[iteration].clear()
            widget_cena.cena_dostavki[iteration].setFocus()
            widget_cena.cena_dostavki[iteration].setStyleSheet(
                "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
        else:
            widget_cena.cena_dostavki[iteration].setStyleSheet(
                "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
            widget_cena.cena_dostavki[iteration].setFocus()

        if "," in widget_cena.cena_dostavki[iteration].text():
            txt = widget_cena.cena_dostavki[iteration].text()
            counter = 0
            buf = ""
            buf_2 = ""
            try:
                while True:
                    if txt[counter] != ",":
                        buf += txt[counter]
                    else:
                        break
                    counter += 1
                counter += 1
                while True:
                    if txt[counter] != ",":
                        buf_2 += txt[counter]
                    else:
                        break
                    counter += 1
            except:
                pass

            try:
                k = int(buf)
                k = int(buf_2)
            except:
                widget_cena.cena_dostavki[iteration].clear()
                widget_cena.cena_dostavki[iteration].setFocus()
                widget_cena.cena_dostavki[iteration].setStyleSheet(
                    "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
                return
            else:
                widget_cena.cena_dostavki[iteration].setStyleSheet(
                    "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
                # widget_cena.cena_dostavki[iteration].setFocus()

            if len(buf_2) > 2:
                widget_cena.cena_dostavki[iteration].clear()
                widget_cena.cena_dostavki[iteration].setFocus()
                widget_cena.cena_dostavki[iteration].setStyleSheet(
                    "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
                return
            else:
                widget_cena.cena_dostavki[iteration].setStyleSheet(
                    "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")

            if len(buf_2) == 1:
                buf_2 = buf_2 + "0"
            if len(buf_2) == 0:
                buf_2 = "00"
            end_buf = buf + "." + buf_2
            widget_cena.cena_dostavki[iteration].setText(end_buf)

        if "." not in widget_cena.cena_dostavki[iteration].text():
            h = widget_cena.cena_dostavki[iteration].text()
            h += ".00"
            widget_cena.cena_dostavki[iteration].setText(h)

        txt = widget_cena.cena_dostavki[iteration].text()
        counter = 0
        buf = ""
        buf_2 = ""
        try:
            while True:
                if txt[counter] != ".":
                    buf += txt[counter]
                else:
                    break
                counter += 1
            counter += 1
            while True:
                if txt[counter] != ".":
                    buf_2 += txt[counter]
                else:
                    break
                counter += 1
        except:
            pass

        try:
            k = int(buf)
            k = int(buf_2)
        except:
            widget_cena.cena_dostavki[iteration].clear()
            widget_cena.cena_dostavki[iteration].setFocus()
            widget_cena.cena_dostavki[iteration].setStyleSheet(
                "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
            return
        else:
            widget_cena.cena_dostavki[iteration].setStyleSheet(
                "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
        if len(buf_2) > 2:
            widget_cena.cena_dostavki[iteration].clear()
            widget_cena.cena_dostavki[iteration].setFocus()
            widget_cena.cena_dostavki[iteration].setStyleSheet(
                "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
            return
        else:
            widget_cena.cena_dostavki[iteration].setStyleSheet(
                "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
            # widget_cena.cena_dostavki[iteration].setFocus()




        try:
            widget_cena.Articul[iteration+1].setFocus()
        except:
            pass

#окно диалога с заказчиком мен. обслуж.: добавление все иинфы об эл-х для менеджера
class widget_soglas(Ui_MainWindow):
    i_1 = 1  # количество
    i_1_name = 1  # номер файла
    lay = ""
    lay_nomer = ""

    list_of_new_widgets = []  # фоновые виджеты

    # LE для ввода мен. закупа
    cena_sebestoy = []
    cena_prodagi = []
    postavshik = []
    data_dostavki = []
    cena_dostavki = []

    KNOPKA_Imya_el = []
    KNOPKA_Postavshik = []

    VCE_EL = []
    def del_new_string():
        for i in widget_soglas.VCE_EL:
            i.deleteLater()
        widget_soglas.i_1 = 1
        widget_soglas.VCE_EL = []
    def add_new_string(self, el, post, data, CeDo, CeIt,Dane):
        # , el, post, data, CeDo, CeIt
        shift = (widget_soglas.i_1-1) * 31

        try:
            if widget_soglas.i_1 >= 8:
                self.frame_4.setMaximumHeight(345 + (31 * (widget_soglas.i_1-8)))
                self.frame_4.setMinimumHeight(345 + (31 * (widget_soglas.i_1-8)))

            y = 47+shift
            if "не изменяемые элементы" == "не изменяемые элементы":
                if "добавляем лэйбл 'эл'№'" != "":
                    widget_soglas.lay = QtWidgets.QLabel(self.frame_4)
                    widget_soglas.lay.setGeometry(QtCore.QRect(10, y, 21, 21))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(10)
                    font.setItalic(True)
                    widget_soglas.lay.setFont(font)
                    txt = str(widget_soglas.i_1)
                    widget_soglas.lay.setText(txt)
                    widget_soglas.lay.setStyleSheet("background-color: rgb(177, 127, 66);\nborder-radius: 5px;\ncolor: rgb(0, 0, 0);")
                    widget_soglas.lay.setAlignment(QtCore.Qt.AlignCenter)
                    widget_soglas.lay.setObjectName(f"mensale9_lbl_elNO_{widget_soglas.i_1 + 1}")
                    widget_soglas.lay.show()
                widget_soglas.VCE_EL.append(widget_soglas.lay)
                if"кнопка названия элемента"!="":
                    # self.mensale3_pbt_name_1
                    widget_soglas.lay = QtWidgets.QPushButton(self.frame_4)
                    widget_soglas.lay.setGeometry(QtCore.QRect(34, y, 271, 21))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(10)
                    font.setItalic(True)
                    widget_soglas.lay.setFont(font)
                    txt = str(widget_soglas.i_1)
                    widget_soglas.lay.setText(txt)
                    widget_soglas.lay.setObjectName(f"mensale3_pbt_name_1{widget_soglas.i_1-1}")
                    widget_soglas.lay.setStyleSheet(f"#mensale3_pbt_name_1{widget_soglas.i_1-1}\n"
                                                           "{\n"
                                                           "color: rgb(0, 0, 0);\n"
                                                           "background-color: rgb(177, 127, 66);\n"
                                                           "border-radius: 5px;\n"
                                                           "}\n"
                                                           "\n"
                                                           f"#mensale3_pbt_name_1{widget_soglas.i_1-1}:hover\n"
                                                           "{\n"
                                                           "color: rgb(0, 0, 0);\n"
                                                           "background-color: rgb(177, 127, 66);\n"
                                                           "border-radius: 5px;\n"
                                                           "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                                           "border-right: 1px solid rgb(98, 71, 50);\n"
                                                           "}\n"
                                                           "\n"
                                                           f"#mensale3_pbt_name_1{widget_soglas.i_1-1}:pressed\n"
                                                           "{\n"
                                                           "color: rgb(0, 0, 0);\n"
                                                           "background-color: rgb(197, 147, 86);\n"
                                                           "border-radius: 5px;\n"
                                                           "\n"
                                                           "border-bottom: None;\n"
                                                           "border-right: None;\n"
                                                           "\n"
                                                           "border-top: 3px solid rgb(98, 71, 50);\n"
                                                           "border-left: 1px solid rgb(98, 71, 50);\n"
                                                           "}")
                    widget_soglas.lay.show()
                    widget_soglas.KNOPKA_Imya_el.append(widget_soglas.lay)
                    # pass
                widget_soglas.VCE_EL.append(widget_soglas.lay)
                txt = str(el)
                widget_soglas.lay.setText(txt)
                iterr = widget_soglas.i_1
                widget_soglas.lay.clicked.connect(lambda: widget_soglas.HANDLER_IMYA_COPy(self,iterr))
                if "кнопка поставщик" != "":
                    # self.mensale3_pbt_name_1
                    widget_soglas.lay = QtWidgets.QPushButton(self.frame_4)
                    widget_soglas.lay.setGeometry(QtCore.QRect(308, y, 90, 21))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(10)
                    font.setItalic(True)
                    widget_soglas.lay.setFont(font)

                    # self.mensale3_pbt_name_3
                    widget_soglas.lay.setObjectName(f"mensale3_pbt_name_1{widget_soglas.i_1 - 1}")
                    widget_soglas.lay.setStyleSheet(f"#mensale3_pbt_name_1{widget_soglas.i_1 - 1}\n"
                                                           "{\n"
                                                           "background-color: rgb(197, 147, 86);\n"
                                                           "color: rgb(136, 85, 48);\n"
                                                           "border: 1px solid rgb(109, 65, 12);\n"
                                                           "border-radius: 5px;\n"
                                                           "}\n"
                                                           "\n"
                                                           f"#mensale3_pbt_name_1{widget_soglas.i_1 - 1}:hover\n"
                                                           "{\n"
                                                           "background-color: rgb(197, 147, 86);\n"
                                                           "color: rgb(0, 0, 0);\n"
                                                           "border: 1px solid rgb(89, 45, 0);\n"
                                                           "border-radius: 5px;\n"
                                                           "}\n"
                                                           "\n"
                                                           f"#mensale3_pbt_name_1{widget_soglas.i_1 - 1}:pressed\n"
                                                           "{\n"
                                                           "background-color: rgb(177, 127, 66);\n"
                                                           "color: rgb(136, 85, 48);\n"
                                                           "border: 1px solid rgb(109, 65, 12);\n"
                                                           "border-radius: 5px;\n"
                                                           "}")
                    widget_soglas.lay.show()
                    txt = str(widget_soglas.i_1)
                    widget_soglas.lay.setText(txt)
                    # pass
                widget_soglas.VCE_EL.append(widget_soglas.lay)
                widget_soglas.KNOPKA_Postavshik.append(widget_soglas.lay)
                widget_soglas.lay.clicked.connect(lambda: widget_soglas.HANDLER_POST_COPy(self, iterr))
                txt = str(post)
                widget_soglas.lay.setText(txt)

                if "дата доставки" != "":
                    # self.mensale3_pbt_name_1
                    widget_soglas.lay = QtWidgets.QLabel(self.frame_4)
                    widget_soglas.lay.setGeometry(QtCore.QRect(400, y, 67, 21))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(8)
                    font.setItalic(True)
                    widget_soglas.lay.setFont(font)
                    widget_soglas.lay.setAlignment(QtCore.Qt.AlignCenter)
                    # self.mensale3_pbt_name_3
                    widget_soglas.lay.setObjectName(f"mensale3_pbt_name_112{widget_soglas.i_1 - 1}")
                    widget_soglas.lay.setStyleSheet(f"#mensale3_pbt_name_112{widget_soglas.i_1 - 1}\n"
                                                           "{\n"
                                                           "background-color: rgb(197, 147, 86);\n"
                                                           "color: rgb(136, 85, 48);\n"
                                                           "border: 1px solid rgb(109, 65, 12);\n"
                                                           "border-radius: 5px;\n"
                                                           "}\n"
                                                           "\n")
                    widget_soglas.lay.show()
                    txt = str(widget_soglas.i_1)
                    widget_soglas.lay.setText(txt)
                    # pass
                widget_soglas.VCE_EL.append(widget_soglas.lay)
                if Dane.strip() == "Net":
                    txt = str(data)
                    widget_soglas.lay.setText(txt)
                else:
                    if Dane.strip() == "Da":
                        widget_soglas.lay.setText("на складе")
                if "цена доставки" != "":
                    # self.mensale3_pbt_name_1
                    widget_soglas.lay = QtWidgets.QLabel(self.frame_4)
                    widget_soglas.lay.setGeometry(QtCore.QRect(469, y, 50, 21))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(8)
                    font.setItalic(True)
                    widget_soglas.lay.setFont(font)
                    widget_soglas.lay.setAlignment(QtCore.Qt.AlignCenter)

                    # self.mensale3_pbt_name_3
                    widget_soglas.lay.setObjectName(f"mensale3_pbt_name_112{widget_soglas.i_1 - 1}")
                    widget_soglas.lay.setStyleSheet(f"#mensale3_pbt_name_112{widget_soglas.i_1 - 1}\n"
                                                           "{\n"
                                                           "background-color: rgb(197, 147, 86);\n"
                                                           "color: rgb(136, 85, 48);\n"
                                                           "border: 1px solid rgb(109, 65, 12);\n"
                                                           "border-radius: 5px;\n"
                                                           "}\n"
                                                           "\n")
                    widget_soglas.lay.show()
                    txt = str(widget_soglas.i_1)
                    widget_soglas.lay.setText(txt)
                    # pass
                widget_soglas.VCE_EL.append(widget_soglas.lay)
                if Dane.strip() == "Net":
                    txt = str(CeDo)
                    widget_soglas.lay.setText(txt)
                else:
                    if Dane.strip() == "Da":
                        widget_soglas.lay.setText("- - - - -")
                widget_soglas.lay.setText(txt)
                if "Итоговая цена" != "":
                    # self.mensale3_pbt_name_1
                    widget_soglas.lay = QtWidgets.QLabel(self.frame_4)
                    widget_soglas.lay.setGeometry(QtCore.QRect(523, y, 61, 21))
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(8)
                    font.setItalic(True)
                    widget_soglas.lay.setFont(font)

                    # self.mensale3_pbt_name_3
                    widget_soglas.lay.setObjectName(f"mensale3_pbt_name_112{widget_soglas.i_1 - 1}")
                    widget_soglas.lay.setStyleSheet(f"#mensale3_pbt_name_112{widget_soglas.i_1 - 1}\n"
                                                           "{\n"
                                                           "background-color: rgb(197, 147, 86);\n"
                                                           "color: rgb(136, 85, 48);\n"
                                                           "border: 1px solid rgb(109, 65, 12);\n"
                                                           "border-radius: 5px;\n"
                                                           "}\n"
                                                           "\n")
                    widget_soglas.lay.show()
                    txt = str(widget_soglas.i_1)
                    widget_soglas.lay.setText(txt)
                    # pass
                widget_soglas.VCE_EL.append(widget_soglas.lay)
                txt = str(CeIt)
                widget_soglas.lay.setText(txt)
                if "лэйба 'рублей'" != "":
                    # self.mensale3_pbt_name_1
                    widget_soglas.lay = QtWidgets.QLabel(self.frame_4)
                    widget_soglas.lay.setGeometry(QtCore.QRect(587, y, 61, 21))
                    font = QtGui.QFont()
                    font.setFamily("Segoe Print")
                    font.setPointSize(10)
                    # font.setItalic(True)
                    widget_soglas.lay.setFont(font)

                    # self.mensale3_pbt_name_3
                    widget_soglas.lay.setObjectName(f"mensale3_pbt_name_1132{widget_soglas.i_1 - 1}")
                    # widget_soglas.lay.setStyleSheet(f"")
                    widget_soglas.lay.show()
                    # pass
                    txt = "руб."
                    widget_soglas.lay.setText(txt)
                widget_soglas.VCE_EL.append(widget_soglas.lay)
            y = shift + 70
            self.line_16.move(390,y)
            y = shift + 87
            self.label_49.move(360, y)
            y = shift + 91
            self.mensale3_le_sourse_SUM.move(450, y)
            y = shift + 91
            self.mensale3_le_sum_SUM.move(523, y)
            y = shift + 91
            self.label_36.move(587, y)


            widget_soglas.i_1 += 1
            widget_soglas.i_1_name += 1

        except:
            pass

    def HANDLER_IMYA_COPy(self,iteration):
        print("iteration",iteration)
        import pyperclip
        pyperclip.copy(widget_soglas.KNOPKA_Imya_el[iteration-1].text())

    def HANDLER_POST_COPy(self,iteration):
        import pyperclip
        pyperclip.copy(widget_soglas.KNOPKA_Postavshik[iteration-1].text())