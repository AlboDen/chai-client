import socket

from w import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class UI(Ui_MainWindow):

    #инициализация картинок
    def w_init(self):
        self.pushButton_28.setStyleSheet("#pushButton_28\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/new_proj_prew.png);\n"
                                         "}\n"
                                         "#pushButton_28:hover\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/new_proj_prew_videlenie.png);\n"
                                         "}\n"
                                         "#pushButton_28:pressed\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/new_proj_prew_pres.png);\n"
                                         "}\n"
                                         "")
        self.label_236.setStyleSheet("border-image: url(../pythonProject3/DATABASE/pictures/znak_black.png);")
        self.label_26.setStyleSheet("border-image: url(../pythonProject3/DATABASE/pictures/crest_white.png);")
        #ножницы
        self.label_221.setStyleSheet("border-image: url(../pythonProject3/DATABASE/pictures/knifecut.png);")
        self.label_213.setStyleSheet("border-image: url(../pythonProject3/DATABASE/pictures/knifecut.png);")
        self.label_244.setStyleSheet("border-image: url(../pythonProject3/DATABASE/pictures/knifecut.png);")

        #кресты для выхода на отраслевых бланках
        self.pushButton_53.setStyleSheet("#pushButton_53\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/crest_vihod_white.png);\n"
                                         "}\n"
                                         "#pushButton_53:hover\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/crest_vihod_black.png);\n"
                                         "}\n"
                                         "#pushButton_53:pressed\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/crest_vihod_white.png);\n"
                                         "}\n"
                                         "")
        self.pushButton_53.setStyleSheet("#pushButton_53\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/crest_vihod_white.png);\n"
                                         "}\n"
                                         "#pushButton_53:hover\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/crest_vihod_black.png);\n"
                                         "}\n"
                                         "#pushButton_53:pressed\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/crest_vihod_white.png);\n"
                                         "}\n"
                                         "")
        self.pushButton_56.setStyleSheet("#pushButton_56\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/crest_vihod_white.png);\n"
                                         "}\n"
                                         "#pushButton_56:hover\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/crest_vihod_black.png);\n"
                                         "}\n"
                                         "#pushButton_56:pressed\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/crest_vihod_white.png);\n"
                                         "}\n"
                                         "")
        self.pushButton_60.setStyleSheet("#pushButton_60\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/crest_vihod_white.png);\n"
                                         "}\n"
                                         "#pushButton_60:hover\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/crest_vihod_black.png);\n"
                                         "}\n"
                                         "#pushButton_60:pressed\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/crest_vihod_white.png);\n"
                                         "}\n"
                                         "")
        self.pushButton_62.setStyleSheet("#pushButton_62\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/crest_vihod_white.png);\n"
                                         "}\n"
                                         "#pushButton_62:hover\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/crest_vihod_black.png);\n"
                                         "}\n"
                                         "#pushButton_62:pressed\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/crest_vihod_white.png);\n"
                                         "}\n"
                                         "")
        self.pushButton_63.setStyleSheet("#pushButton_63\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/crest_vihod_white.png);\n"
                                         "}\n"
                                         "#pushButton_63:hover\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/crest_vihod_black.png);\n"
                                         "}\n"
                                         "#pushButton_63:pressed\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/crest_vihod_white.png);\n"
                                         "}\n"
                                         "")
        self.pushButton_65.setStyleSheet("#pushButton_65\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/crest_vihod_white.png);\n"
                                         "}\n"
                                         "#pushButton_65:hover\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/crest_vihod_black.png);\n"
                                         "}\n"
                                         "#pushButton_65:pressed\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/crest_vihod_white.png);\n"
                                         "}\n"
                                         "")
        self.pushButton_128.setStyleSheet("#pushButton_128\n"
                                          "{\n"
                                          "border-image: url(../pythonProject3/DATABASE/pictures/crest_vihod_white.png);\n"
                                          "}\n"
                                          "#pushButton_128:hover\n"
                                          "{\n"
                                          "border-image: url(../pythonProject3/DATABASE/pictures/crest_vihod_black.png);\n"
                                          "}\n"
                                          "#pushButton_128:pressed\n"
                                          "{\n"
                                          "border-image: url(../pythonProject3/DATABASE/pictures/crest_vihod_white.png);\n"
                                          "}\n"
                                          "")
        self.pushButton_130.setStyleSheet("#pushButton_130\n"
                                          "{\n"
                                          "border-image: url(../pythonProject3/DATABASE/pictures/crest_vihod_white.png);\n"
                                          "}\n"
                                          "#pushButton_130:hover\n"
                                          "{\n"
                                          "border-image: url(../pythonProject3/DATABASE/pictures/crest_vihod_black.png);\n"
                                          "}\n"
                                          "#pushButton_130:pressed\n"
                                          "{\n"
                                          "border-image: url(../pythonProject3/DATABASE/pictures/crest_vihod_white.png);\n"
                                          "}\n"
                                          "")
        self.pushButton_131.setStyleSheet("#pushButton_131\n"
                                          "{\n"
                                          "border-image: url(../pythonProject3/DATABASE/pictures/crest_vihod_white.png);\n"
                                          "}\n"
                                          "#pushButton_131:hover\n"
                                          "{\n"
                                          "border-image: url(../pythonProject3/DATABASE/pictures/crest_vihod_black.png);\n"
                                          "}\n"
                                          "#pushButton_131:pressed\n"
                                          "{\n"
                                          "border-image: url(../pythonProject3/DATABASE/pictures/crest_vihod_white.png);\n"
                                          "}\n"
                                          "")

        self.pushButton_127.setStyleSheet("#pushButton_127\n"
                                          "{\n"
                                          "color: rgb(98, 71, 42);\n"
                                          "background-color: rgb(220, 175, 122);\n"
                                          "border-image: url(../pythonProject3/DATABASE/pictures/weel.png);\n"
                                          "border-radius: 5px;\n"
                                          "border: 1px solid rgb(197, 157, 96);\n"
                                          ";\n"
                                          "}\n"
                                          "\n"
                                          "#pushButton_127:hover\n"
                                          "{\n"
                                          "color: rgb(118, 91, 62);\n"
                                          "background-color: rgb(197, 157, 96);\n"
                                          "border-radius: 5px;\n"
                                          "border: 1px solid  rgb(220, 175, 122);\n"
                                          "}\n"
                                          "\n"
                                          "#pushButton_127:pressed\n"
                                          "{\n"
                                          "color: rgb(98, 71, 42);\n"
                                          "    color: rgb(6, 6, 6);\n"
                                          "background-color: rgb(197, 157, 96);\n"
                                          "    border-image: url(../pythonProject3/DATABASE/pictures/weel_red.png);\n"
                                          "border-radius: 5px;\n"
                                          "\n"
                                          "}")
        self.pushButton.setStyleSheet(  "#pushButton\n"
                                        "{\n"
                                        "border-image: url(../pythonProject3/DATABASE/pictures/pbt_strelka_vverh.png);\n"
                                        "}\n"
                                        "#pushButton:pressed\n"
                                        "{\n"
                                        "border-image: url(../pythonProject3/DATABASE/pictures/pbt_strelka_vverh_black.png);\n"
                                        "}")
        self.pushButton_2.setStyleSheet("#pushButton_2\n"
                                        "{\n"
                                        "border-image: url(../pythonProject3/DATABASE/pictures/pbt_strelka_vniz.png);\n"
                                        "}\n"
                                        "#pushButton_2:pressed\n"
                                        "{\n"
                                        "border-image: url(../pythonProject3/DATABASE/pictures/pbt_strelka_vniz_black.png);\n"
                                        "}")
        self.pushButton_52.setStyleSheet("#pushButton_52\n"
                                        "{\n"
                                        "border-image: url(../pythonProject3/DATABASE/pictures/prew_dialog_s_zakazcikom.png);\n"
                                        "}\n"
                                         "#pushButton_52:hover\n"
                                        "{\n"
                                        "border-image: url(../pythonProject3/DATABASE/pictures/prew_dialog_s_zakazcikom_hover.png);\n"
                                        "}"
                                        "#pushButton_52:pressed\n"
                                        "{\n"
                                        "border-image: url(../pythonProject3/DATABASE/pictures/prew_dialog_s_zakazcikom_pressed.png);\n"
                                        "}")
        self.pushButton_14.setStyleSheet("#pushButton_14\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/reload.png);\n"
                                         "border-radius: 5px;\n"
                                         "}\n"
                                         "#pushButton_14:hover\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/reload_hover.png);\n"
                                         "border-radius: 5px;\n"
                                         "}\n"
                                         "#pushButton_14:pressed\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/reload_press.png);\n"
                                         "border-radius: 5px;\n"
                                         "}")
        self.pushButton_133.setStyleSheet("#pushButton_133\n"
                                          "{\n"
                                          "border-image: url(../pythonProject3/DATABASE/pictures/strelca.png);\n"
                                          "}\n"
                                          "#pushButton_133:hover\n"
                                          "{\n"
                                          "border-image: url(../pythonProject3/DATABASE/pictures/strelca_hover.png);\n"
                                          "}")
        self.pushButton_54.setStyleSheet("#pushButton_54\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/prew_remont_ili_diagnostica2.png);\n"
                                         "}\n"
                                         "#pushButton_54:hover\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/prew_remont_ili_diagnostica_hover.png);\n"
                                         "}\n"
                                         "#pushButton_54:pressed\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/prew_remont_ili_diagnostica.png);\n"
                                         "}\n"
                                         "")
        self.pushButton_51.setStyleSheet("#pushButton_51\n"
                                          "{\n"
                                          "border-image: url(../pythonProject3/DATABASE/pictures/prew_export.png);\n"
                                          "}\n"
                                          "#pushButton_51:hover\n"
                                          "{\n"
                                          "border-image: url(../pythonProject3/DATABASE/pictures/prew_export_hover.png);\n"
                                          "}\n"
                                          "#pushButton_51:pressed\n"
                                          "{\n"
                                          "border-image: url(../pythonProject3/DATABASE/pictures/prew_export_pressed.png);\n"
                                          "}\n"
                                          "")
        self.pushButton_64.setStyleSheet("#pushButton_64\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/prew_dannie_dlya_dia.png);\n"
                                         "}\n"
                                         "#pushButton_64:hover\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/prew_dannie_dlya_dia_hover.png);\n"
                                         "}\n"
                                         "#pushButton_64:pressed\n"
                                         "{\n"
                                         "border-image: url(../pythonProject3/DATABASE/pictures/prew_dannie_dlya_dia_pressed.png);\n"
                                         "}\n"
                                         "")

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setItalic(True)
        #инженер:диагностика
        self.textEdit_8.setFont(font)

        self.mensale6_lbl_elem_1.setFont(font)
        self.mensale6_lbl_elem_2.setFont(font)
        self.mensale6__elem_1.setFont(font)
        self.mensale6__elem_2.setFont(font)

        self.mensale7_le_elem_1.setFont(font)
        self.mensale7_le_elem_2.setFont(font)
        self.mensale7__num_1.setFont(font)
        self.mensale7__num_2.setFont(font)
        self.mensale7_le_COL_1.setFont(font)
        self.mensale7_le_COL_2.setFont(font)

        self.mensale6_lbl_elem_5.setFont(font)
        self.mensale6_lbl_elem_6.setFont(font)
        self.mensale6__elem_5.setFont(font)
        self.mensale6__elem_6.setFont(font)
        #мен. закупа
        self.pushButton_57.setStyleSheet("#pushButton_57\n"
                                          "{\n"
                                          "border-image: url(../pythonProject3/DATABASE/pictures/prew_uznat_cenu.png);\n"
                                          "}\n"
                                          "#pushButton_57:hover\n"
                                          "{\n"
                                          "border-image: url(../pythonProject3/DATABASE/pictures/prew_uznat_cenu_hover.png);\n"
                                          "}\n"
                                          "#pushButton_57:pressed\n"
                                          "{\n"
                                          "border-image: url(../pythonProject3/DATABASE/pictures/prew_uznat_cenu_pressed.png);\n"
                                          "}\n"
                                          "")

    #Авторизация
    def HANDLER_MEN_pushButton_29(self):
        try:
            self.widget_5.hide()
            from client import CLIENT
            inp_log = self.lineEdit_18.text()
            inp_par = self.lineEdit_19.text()
            inp_dol = self.comboBox_16.currentText()
            print(inp_dol)
            if inp_dol == "Мен. обслуживания":
                inp_dol = "MEN"
            if inp_dol == "Инженер":
                inp_dol = "ING"
            if inp_dol == "Мен. закупа":
                inp_dol = "MEZ"
            print(inp_dol)

            CLIENT.input_login = inp_log
            CLIENT.input_dol = inp_dol
            CLIENT.input_parol = inp_par
            CLIENT.request_for_server()
            print("prav: ", CLIENT.pravilnost_parola)
            if CLIENT.pravilnost_parola == "bad_parol":
                self.comboBox_16.setCurrentIndex(0)
                print("bad_parolbad_parol")
                self.lineEdit_19.setStyleSheet("background-color: rgb(220, 54, 20);\n"
                                               "border: 2px solid rgb(176, 103, 19);\n"
                                               "border-radius: 5px;")
                self.lineEdit_18.setStyleSheet("background-color: rgb(220, 175, 122);\n"
                                               "border: 2px solid rgb(176, 103, 19);\n"
                                               "border-radius: 5px;")
                self.lineEdit_19.clear()
                self.lineEdit_19.setFocus()

                self.widget_5.show()
                self.label_238.hide()
                self.label_236.hide()
                self.label_274.show()
                self.label_262.show()
                self.label_271.show()
                self.pushButton_129.hide()
                self.label_262.setText("Не правильно введен")
                self.label_271.setText("пароль. Пожалуйста,")

                self.widget_5.move(20, 550)
                self.widget_4.move(400, 60)
                self.widget_3.move(20, 60)
                self.widget_6.move(70, 20)
                self.widget_9.move(450, 20)

            if CLIENT.pravilnost_parola == "acc_does_not":
                self.comboBox_16.setCurrentIndex(0)
                print("acc_does_notacc_does_not")
                self.lineEdit_19.setStyleSheet("background-color: rgb(220, 175, 122);\n"
                                               "border: 2px solid rgb(176, 103, 19);\n"
                                               "border-radius: 5px;")
                self.lineEdit_18.setStyleSheet("background-color: rgb(220, 54, 20);\n"
                                               "border: 2px solid rgb(176, 103, 19);\n"
                                               "border-radius: 5px;")
                self.lineEdit_19.clear()
                self.lineEdit_18.clear()
                self.lineEdit_18.setFocus()

                self.widget_5.show()
                self.label_238.hide()
                self.label_238.hide()
                self.label_274.hide()
                self.pushButton_129.hide()
                self.label_262.show()
                self.label_271.show()

                self.widget_5.move(20,550)
                self.widget_4.move(400,60)
                self.widget_3.move(20,60)
                self.widget_6.move(70, 20)
                self.widget_9.move(450, 20)

                self.label_262.setText("Данного аккаунта")
                self.label_271.setText("не существует.")
                self.pushButton_129.show()
                return

            if CLIENT.pravilnost_parola != "acc_does_not" and CLIENT.pravilnost_parola != "bad_parol":
                UI.w_init(self)

                CLIENT.get_all_files()
                from ui_add_new_elements import widget_begin
                widget_begin.add_new_strings(self)

                # self.lineEdit_19.clear()
                # self.lineEdit_18.clear()
                self.lineEdit_18.setFocus()

                self.widget_5.move(20, 620)
                self.widget_4.move(400, 130)
                self.widget_3.move(20, 130)
                self.widget_6.move(70, 90)
                self.widget_9.move(450, 90)

                self.widget_5.hide()
                self.pushButton_33.hide()
                self.pushButton_34.hide()
                self.pushButton_35.hide()
                self.stackedWidget_3.setCurrentIndex(0)
                self.stackedWidget.setCurrentIndex(1)

                UI.HANDLER_MEN_pushButton_6(self)
                UI.HANDLER_MEN_pushButton_12(self)

                return

        except socket.error:
            self.lineEdit_18.setFocus()
            self.widget_5.show()
            self.label_236.show()
            self.label_238.show()
            self.widget_5.move(20, 550)
            self.widget_4.move(400, 60)
            self.widget_3.move(20, 60)
            self.widget_6.move(70, 20)
            self.widget_9.move(450, 20)
    #смена пользователя
    def HANDLER_MEN_pushButton_25(self):
        self.lineEdit_18.setText("")
        self.lineEdit_19.setText("")
        self.comboBox_16.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(1)
        self.lineEdit_18.setFocus()

    #обработчик крестов
    def HANDLER_MEN_pushButton_53(self):
        self.stackedWidget.setCurrentIndex(1)
        self.lineEdit_23.hide()

        self.pushButton_24.setEnabled(True)
        self.pushButton_25.setEnabled(True)
        if self.comboBox_16.currentText() == "Мен. обслуживания":
            self.pushButton_4.setEnabled(True)
        self.pushButton_14.setEnabled(True)
        self.lineEdit_17.setEnabled(True)
        self.pushButton_15.setEnabled(True)
        self.pushButton_5.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.pushButton_9.setEnabled(True)
        self.pushButton_10.setEnabled(True)
        self.pushButton_11.setEnabled(True)
        self.pushButton_7.setEnabled(True)
        self.pushButton_8.setEnabled(True)
        self.pushButton_12.setEnabled(True)

    #Авторизация по ентеру со второго поля (с поля пароля). То же что и простая
    #авторизация, но для исключения рекурсии
    def HANDLER_MEN_NEXT_lineEdit_19(self):
        if self.lineEdit_19.text() == "":
            self.lineEdit_19.setFocus()
        else:
            self.comboBox_16.showPopup()
    def HANDLER_MEN_NEXT_comboBox_16(self):
        if self.comboBox_16.currentText() =="*****************":
            self.comboBox_16.showPopup()
        else:
            try:
                self.widget_5.hide()
                from client import CLIENT
                inp_log = self.lineEdit_18.text()
                inp_par = self.lineEdit_19.text()
                inp_dol = self.comboBox_16.currentText()
                print(inp_dol)
                if inp_dol == "Мен. обслуживания":
                    inp_dol = "MEN"
                if inp_dol == "Инженер":
                    inp_dol = "ING"
                if inp_dol == "Мен. закупа":
                    inp_dol = "MEZ"
                print(inp_dol)

                CLIENT.input_login = inp_log
                CLIENT.input_dol = inp_dol
                CLIENT.input_parol = inp_par
                CLIENT.request_for_server()
                print("prav: ", CLIENT.pravilnost_parola)
                if CLIENT.pravilnost_parola == "bad_parol":
                    self.comboBox_16.setCurrentIndex(0)
                    self.lineEdit_19.setStyleSheet("background-color: rgb(220, 54, 20);\n"
                                                   "border: 2px solid rgb(176, 103, 19);\n"
                                                   "border-radius: 5px;")
                    self.lineEdit_18.setStyleSheet("background-color: rgb(220, 175, 122);\n"
                                                   "border: 2px solid rgb(176, 103, 19);\n"
                                                   "border-radius: 5px;")
                    self.lineEdit_19.clear()
                    self.lineEdit_19.setFocus()

                    self.widget_5.show()
                    self.label_238.hide()
                    self.label_236.hide()
                    self.label_274.show()
                    self.label_262.show()
                    self.label_271.show()
                    self.pushButton_129.hide()
                    self.label_262.setText("Не правильно введен")
                    self.label_271.setText("пароль. Пожалуйста,")

                    self.widget_5.move(20, 550)
                    self.widget_4.move(400, 60)
                    self.widget_3.move(20, 60)
                    self.widget_6.move(70, 20)
                    self.widget_9.move(450, 20)

                if CLIENT.pravilnost_parola == "acc_does_not":
                    self.comboBox_16.setCurrentIndex(0)
                    print("acc_does_notacc_does_not")
                    self.lineEdit_19.setStyleSheet("background-color: rgb(220, 175, 122);\n"
                                                   "border: 2px solid rgb(176, 103, 19);\n"
                                                   "border-radius: 5px;")
                    self.lineEdit_18.setStyleSheet("background-color: rgb(220, 54, 20);\n"
                                                   "border: 2px solid rgb(176, 103, 19);\n"
                                                   "border-radius: 5px;")
                    self.lineEdit_19.clear()
                    self.lineEdit_18.clear()
                    self.lineEdit_18.setFocus()

                    self.widget_5.show()
                    self.label_238.hide()
                    self.label_238.hide()
                    self.label_274.hide()
                    self.pushButton_129.hide()
                    self.label_262.show()
                    self.label_271.show()

                    self.widget_5.move(20, 550)
                    self.widget_4.move(400, 60)
                    self.widget_3.move(20, 60)
                    self.widget_6.move(70, 20)
                    self.widget_9.move(450, 20)

                    self.label_262.setText("Данного аккаунта")
                    self.label_271.setText("не существует.")
                    self.pushButton_129.show()
                    return

                if CLIENT.pravilnost_parola != "acc_does_not" and CLIENT.pravilnost_parola != "bad_parol":
                    UI.w_init(self)
                    print("OKOKOKOKOKOKOKOKOKOK")
                    CLIENT.get_all_files()
                    from ui_add_new_elements import widget_begin
                    widget_begin.add_new_strings(self)
                    # Активируем кнопки, для каждой отросли индивидуально
                    UI.activated_elem_for_the_changed_path(self)

                    # self.lineEdit_19.clear()
                    # self.lineEdit_18.clear()
                    self.lineEdit_18.setFocus()

                    self.widget_5.move(20, 620)
                    self.widget_4.move(400, 130)
                    self.widget_3.move(20, 130)
                    self.widget_6.move(70, 90)
                    self.widget_9.move(450, 90)

                    self.widget_5.hide()
                    self.pushButton_33.hide()
                    self.pushButton_34.hide()
                    self.pushButton_35.hide()
                    self.stackedWidget_3.setCurrentIndex(0)
                    self.stackedWidget.setCurrentIndex(1)

                    UI.HANDLER_MEN_pushButton_6(self)
                    UI.HANDLER_MEN_pushButton_12(self)


                    return
                    print("3ret")
            except socket.error:
                self.lineEdit_18.setFocus()
                self.widget_5.show()
                self.label_236.show()
                self.label_238.show()
                self.widget_5.move(20, 550)
                self.widget_4.move(400, 60)
                self.widget_3.move(20, 60)
                self.widget_6.move(70, 20)
                self.widget_9.move(450, 20)
    #для быстрого заполнения
    def HANDLER_MEN_NEXT_lineEdit_18(self):
        if self.lineEdit_18.text() == "":
            self.lineEdit_18.setFocus()
        else:
            self.lineEdit_19.setFocus()



    #Регистрация
    def HANDLER_MEN_pushButton_30(self):
        self.lineEdit_30.setFocus()

        self.label_209.hide()

        self.widget_4.show()
        self.widget_9.show()
        self.label_283.hide()
        self.pushButton_29.setDisabled(True)
        self.lineEdit_18.setDisabled(True)
        self.lineEdit_19.setDisabled(True)
        self.comboBox_16.setDisabled(True)
    def HANDLER_MEN_pushButton_133(self):
        self.widget_4.hide()
        self.widget_9.hide()
        self.pushButton_29.setDisabled(False)
        self.lineEdit_18.setDisabled(False)
        self.lineEdit_19.setDisabled(False)
        self.comboBox_16.setDisabled(False)

    g_flaf = 0
    def HANDLER_MEN_pushButton_132(self):
        self.label_209.hide()
        if self.label_283.text() != "Заявка на рассмотрении":
            UI.g_flaf = 1
            print("Запрос на создание нового аккаунта с данными:")
            from client import CLIENT
            CLIENT.FamiliyaImyaOtchestvo = self.lineEdit_30.text().strip() + " " + self.lineEdit_31.text().strip() + " " +self.lineEdit_32.text().strip()
            print("ФИО: ", CLIENT.FamiliyaImyaOtchestvo)
            for bukva in "абвгдеёжзиклмнопрстуфхцшщъыьэюяАБВГДЕЁЖЗИКЛМНОПРСТУФХЦШЩЪЫЬЭЮЯ":
                if bukva in CLIENT.FamiliyaImyaOtchestvo:
                    from translater import TRANSLATE
                    TRANSLATE.out_str = ""
                    TRANSLATE.into_str = CLIENT.FamiliyaImyaOtchestvo
                    TRANSLATE.rus_in_eng()
                    CLIENT.FamiliyaImyaOtchestvo = TRANSLATE.out_str
                    print("CLIENT.FamiliyaImyaOtchestvo ",CLIENT.FamiliyaImyaOtchestvo)

            buuf = self.comboBox_17.currentText()
            print("Должностьь: ",buuf,"]",CLIENT.Dolgnost)
            if buuf == "Мен. обслуживания":
                CLIENT.Dolgnost = "MEN"
            if buuf == "Инженер":
                CLIENT.Dolgnost = "ING"
            if buuf == "Мен. закупа":
                CLIENT.Dolgnost = "MEZ"

            print("Должность: ", buuf,"]",CLIENT.Dolgnost)

            CLIENT.Login = self.lineEdit_36.text().strip()
            print("Логин: ", CLIENT.Login)
            for bukva in "абвгдеёжзиклмнопрстуфхцшщъыьэюяАБВГДЕЁЖЗИКЛМНОПРСТУФХЦШЩЪЫЬЭЮЯ":
                if bukva in CLIENT.Login:
                    self.label_283.show()
                    self.label_283.setText("В логине RU символы!")
                    self.lineEdit_36.setText("")
                    return

            CLIENT.Parol = self.lineEdit_35.text().strip()
            print("Пароль: ", CLIENT.Parol)
            for bukva in "абвгдеёжзиклмнопрстуфхцшщъыьэюяАБВГДЕЁЖЗИКЛМНОПРСТУФХЦШЩЪЫЬЭЮЯ":
                if bukva in CLIENT.Parol:
                    self.label_283.show()
                    self.label_283.setText("В пароле RU символы!")
                    self.lineEdit_35.setText("")
                    return


            CLIENT.request_for_create_acc()
            otvet = CLIENT.zapret_na_sozdanie_acc
            if otvet == "VCE_OK":
                self.label_209.show()
                self.label_283.setAlignment(QtCore.Qt.AlignRight)
                self.label_283.setText("Заявка на рассмотрении")
                self.label_209.setStyleSheet("border-image: url(../pythonProject3/DATABASE/pictures/galochka_black.png);")
                self.label_283.show()
            if otvet == "VCE_BAD":
                self.label_209.show()
                self.label_209.setStyleSheet("border-image: url(../pythonProject3/DATABASE/pictures/crest_black.png);")
                self.label_283.setAlignment(QtCore.Qt.AlignCenter)
                self.label_283.setText("Имя занято")
                self.label_283.show()
            return

        if self.label_283.text() == "Заявка на рассмотрении" and UI.g_flaf == 1:
            UI.g_flaf = 0
            self.label_283.setText("")
            self.widget_4.hide()
            self.widget_9.hide()
            self.pushButton_29.setDisabled(False)
            self.lineEdit_18.setDisabled(False)
            self.lineEdit_19.setDisabled(False)
            self.comboBox_16.setDisabled(False)
            self.widget_3.move(20,130)
            self.widget_5.move(20, 620)
            self.widget_6.move(70, 90)

            self.widget_5.hide()
        #*отсылка*#

    #для быстрого заполнения
    def HANDLER_MEN_NEXT_lineEdit_30(self):
        if self.lineEdit_30.text() == "":
            self.lineEdit_30.setFocus()
        else:
            self.lineEdit_31.setFocus()
    def HANDLER_MEN_NEXT_lineEdit_31(self):
        if self.lineEdit_31.text() == "":
            self.lineEdit_31.setFocus()
        else:
            self.lineEdit_32.setFocus()
    def HANDLER_MEN_NEXT_lineEdit_32(self):
        if self.lineEdit_32.text() == "":
            self.lineEdit_32.setFocus()
        else:
            self.comboBox_17.showPopup()
    def HANDLER_MEN_NEXT_comboBox_17(self):
        if self.comboBox_17.currentText() =="*****************":
            self.comboBox_17.showPopup()
        else:
            self.lineEdit_36.setFocus()
    def HANDLER_MEN_NEXT_lineEdit_36(self):
        if self.lineEdit_36.text() == "":
            self.lineEdit_36.setFocus()
        else:
            self.lineEdit_35.setFocus()
    def HANDLER_MEN_NEXT_lineEdit_35(self):
        if self.lineEdit_35.text() == "":
            self.lineEdit_35.setFocus()
        else:
            self.label_209.hide()
            if self.label_283.text() != "Заявка на рассмотрении":
                UI.g_flaf = 1
                print("Запрос на создание нового аккаунта с данными:")
                from client import CLIENT
                CLIENT.FamiliyaImyaOtchestvo = self.lineEdit_30.text().strip() + " " + self.lineEdit_31.text().strip() + " " + self.lineEdit_32.text().strip()
                print("ФИО: ", CLIENT.FamiliyaImyaOtchestvo)
                for bukva in "абвгдеёжзиклмнопрстуфхцшщъыьэюяАБВГДЕЁЖЗИКЛМНОПРСТУФХЦШЩЪЫЬЭЮЯ":
                    if bukva in CLIENT.FamiliyaImyaOtchestvo:
                        from translater import TRANSLATE
                        TRANSLATE.out_str = ""
                        TRANSLATE.into_str = CLIENT.FamiliyaImyaOtchestvo
                        TRANSLATE.rus_in_eng()
                        CLIENT.FamiliyaImyaOtchestvo = TRANSLATE.out_str
                        print("CLIENT.FamiliyaImyaOtchestvo ", CLIENT.FamiliyaImyaOtchestvo)

                buuf = self.comboBox_17.currentText()
                print("Должность: ",buuf,"[", CLIENT.Dolgnost)
                if buuf == "Мен. обслуживания":
                    CLIENT.Dolgnost = "MEN"
                if buuf == "Инженер":
                    CLIENT.Dolgnost = "ING"
                if buuf == "Мен. закупа":
                    CLIENT.Dolgnost = "MEZ"
                print("Должность: ",buuf,"[", CLIENT.Dolgnost)

                CLIENT.Login = self.lineEdit_36.text().strip()
                print("Логин: ", CLIENT.Login)
                for bukva in "абвгдеёжзиклмнопрстуфхцшщъыьэюяАБВГДЕЁЖЗИКЛМНОПРСТУФХЦШЩЪЫЬЭЮЯ":
                    if bukva in CLIENT.Login:
                        self.label_283.show()
                        self.label_283.setText("В логине RU символы!")
                        self.lineEdit_36.setText("")
                        return

                CLIENT.Parol = self.lineEdit_35.text().strip()
                print("Пароль: ", CLIENT.Parol)
                for bukva in "абвгдеёжзиклмнопрстуфхцшщъыьэюяАБВГДЕЁЖЗИКЛМНОПРСТУФХЦШЩЪЫЬЭЮЯ":
                    if bukva in CLIENT.Parol:
                        self.label_283.show()
                        self.label_283.setText("В пароле RU символы!")
                        self.lineEdit_35.setText("")
                        return

                CLIENT.request_for_create_acc()
                otvet = CLIENT.zapret_na_sozdanie_acc
                if otvet == "VCE_OK":
                    self.label_209.show()
                    self.label_283.setAlignment(QtCore.Qt.AlignRight)
                    self.label_283.setText("Заявка на рассмотрении")
                    self.label_209.setStyleSheet(
                        "border-image: url(../pythonProject3/DATABASE/pictures/galochka_black.png);")
                    self.label_283.show()
                if otvet == "VCE_BAD":
                    self.label_209.show()
                    self.label_209.setStyleSheet(
                        "border-image: url(../pythonProject3/DATABASE/pictures/crest_black.png);")
                    self.label_283.setAlignment(QtCore.Qt.AlignCenter)
                    self.label_283.setText("Имя занято")
                    self.label_283.show()
                return

            if self.label_283.text() == "Заявка на рассмотрении" and UI.g_flaf == 1:
                UI.g_flaf = 0
                self.label_283.setText("")
                self.widget_4.hide()
                self.widget_9.hide()
                self.pushButton_29.setDisabled(False)
                self.lineEdit_18.setDisabled(False)
                self.lineEdit_19.setDisabled(False)
                self.comboBox_16.setDisabled(False)
                self.widget_3.move(20, 130)
                self.widget_5.move(20, 620)
                self.widget_6.move(70, 90)

                self.widget_5.hide()


    # /////////////////////////////////////////////////////////////////////////////////////////////////////////#
    # /////////////////////////////////////////////////////////////////////////////////////////////////////////#
    # /////////////////////////////////////////////////////////////////////////////////////////////////////////#
    # /////////////////////////////////блок менеджера обслуживания/////////////////////////////////////////////#
    # /////////////////////////////////////////////////////////////////////////////////////////////////////////#
    # /////////////////////////////////////////////////////////////////////////////////////////////////////////#
    # /////////////////////////////////////////////////////////////////////////////////////////////////////////#
    # осн настройки
    def HANDLER_MEN_pushButton_31(self):
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)
    # осн настройки:новый проект
    Zanyatie_imena_proectov = []
    def HANDLER_MEN_pushButton_4(self):
        self.lineEdit_21.setEnabled(True)
        self.lineEdit_22.setEnabled(True)
        self.spinBox_2.setEnabled(True)
        self.spinBox_3.setEnabled(True)
        self.spinBox_4.setEnabled(True)
        self.pushButton_36.setEnabled(True)
        self.checkBox_2.setEnabled(True)
        self.comboBox_3.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.checkBox.setEnabled(True)

        self.comboBox_2.setEnabled(True)
        self.lineEdit.setEnabled(True)
        self.lineEdit_16.setEnabled(True)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_5.setEnabled(True)
        print("lll56")
        self.lineEdit_6.setEnabled(True)
        self.lineEdit_7.setEnabled(True)
        self.lineEdit_8.setEnabled(True)
        self.lineEdit_9.setEnabled(True)
        self.lineEdit_10.setEnabled(True)
        self.lineEdit_11.setEnabled(True)
        self.lineEdit_12.setEnabled(True)
        self.lineEdit_13.setEnabled(True)
        self.lineEdit_14.setEnabled(True)
        self.lineEdit_15.setEnabled(True)

        self.textEdit.setEnabled(True)
        self.textEdit_3.setEnabled(True)
        self.textEdit_4.setEnabled(True)

        self.lineEdit_21.setFocus()

        self.label_26.hide()
        self.label_27.hide()
        self.pushButton_27.hide()

        self.label_237.hide()
        self.label_263.hide()
        print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
        if "создание списка занятых имен" != "":
            import os
            names = os.listdir("../pythonProject3/DATABASE/current_project")
            cleated_names = []
            for n in names:
                count = 1
                buf = ""
                while True:
                    if n[count] != ".":
                        buf += n[count]
                    else:
                        cleated_names.append(buf)
                        break
                    count += 1
            UI.Zanyatie_imena_proectov = cleated_names
            print(cleated_names)

        if "возвращаем первозданный цвет" == "возвращаем первозданный цвет":
            self.lineEdit_8.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                          "color: rgb(109, 65, 12);\n"
                                          "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit_21.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                           "color: rgb(109, 65, 12);\n"
                                           "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                        "color: rgb(109, 65, 12);\n"
                                        "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit_16.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                           "color: rgb(109, 65, 12);\n"
                                           "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit_2.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                          "color: rgb(109, 65, 12);\n"
                                          "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit_3.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                          "color: rgb(109, 65, 12);\n"
                                          "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit_4.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                          "color: rgb(109, 65, 12);\n"
                                          "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit_5.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                          "color: rgb(109, 65, 12);\n"
                                          "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit_6.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                          "color: rgb(109, 65, 12);\n"
                                          "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit_7.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                          "color: rgb(109, 65, 12);\n"
                                          "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit_22.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                           "color: rgb(109, 65, 12);\n"
                                           "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit_8.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                          "color: rgb(109, 65, 12);\n"
                                          "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit_9.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                          "color: rgb(109, 65, 12);\n"
                                          "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit_10.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                           "color: rgb(109, 65, 12);\n"
                                           "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit_11.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                           "color: rgb(109, 65, 12);\n"
                                           "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit_12.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                           "color: rgb(109, 65, 12);\n"
                                           "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit_13.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                           "color: rgb(109, 65, 12);\n"
                                           "border: 1px solid rgb(109, 65, 12);")
        self.pushButton_31.setStyleSheet("#pushButton_31\n"
                                         "{\n"
                                         "color: rgb(98, 71, 42);\n"
                                         "background-color: rgb(220, 175, 122);\n"
                                         "border-radius: 5px;\n"
                                         "border: 1px solid rgb(197, 157, 96);\n"
                                         ";\n"
                                         "}\n"
                                         "\n"
                                         "#pushButton_31:hover\n"
                                         "{\n"
                                         "color: rgb(118, 91, 62);\n"
                                         "background-color: rgb(197, 157, 96);\n"
                                         "border-radius: 5px;\n"
                                         "border: 1px solid  rgb(220, 175, 122);\n"
                                         "}\n"
                                         "\n"
                                         "#pushButton_31:pressed\n"
                                         "{\n"
                                         "color: rgb(98, 71, 42);\n"
                                         "    color: rgb(6, 6, 6);\n"
                                         "background-color: rgb(197, 157, 96);\n"
                                         "border-radius: 5px;\n"
                                         "\n"
                                         "}")

        import datetime
        now = str(datetime.datetime.now())
        self.spinBox_2.setSpecialValueText(now[8:10])
        self.spinBox_3.setSpecialValueText(now[5:7])
        self.spinBox_4.setSpecialValueText(now[0:4])

        from client import CLIENT
        from translater import TRANSLATE
        TRANSLATE.out_str = ""
        TRANSLATE.into_str = CLIENT.imya_menedgera
        TRANSLATE.eng_in_rus()
        u = "Имя менеджера: "+TRANSLATE.out_str
        self.label_19.setText(u)

        self.pushButton_3.setDisabled(True)
        self.pushButton_32.show()
        self.pushButton_33.hide()
        self.stackedWidget_2.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(0)
        UI.write_colichestvo_dney_na_remont_plus(self)

        with open("..\pythonProject3\DATABASE\oll_project.txt", 'r') as file:
            for index, line in enumerate(file):
                if line == "sboy" and index == 0:
                    print("Проектов нет.")
                    self.lineEdit_21.setText("1")
                    break
                else:
                    pass#превращаем проекты в визуалку 968
    # осн настройки:cогласование БД с сервером
    def HANDLER_MEN_pushButton_14(self):
        from client import CLIENT
        CLIENT.get_all_files()

        with open("..\pythonProject3\DATABASE\oll_project.txt", 'r') as file:
            for index, line in enumerate(file):
                if line == "sboy" and index == 0:
                    print("Проектов нет.")
                    self.lineEdit_21.setText("1")
                    break
        from ui_add_new_elements import widget_begin
        widget_begin.del_all_strings(self)
        print("{159}")
        UI.MASSIVE_FILE_with_posledovat = []
        widget_begin.add_new_strings(self)

    FLAG_TOLKO = "VCE"
    # осн настройки: отсеивание
    # осн настройки:кнопка только срочные заказы
    counter_push = 0
    def HANDLER_MEN_pushButton_11(self):
        # зеленая, активная

        # обычная, не активная
        self.pushButton_7.setStyleSheet("#pushButton_7\n"
                                        "{\n"
                                        "color: rgb(98, 71, 42);\n"
                                        "background-color: rgb(197, 157, 96);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_7:hover\n"
                                        "{\n"
                                        "color: rgb(118, 91, 62);\n"
                                        "background-color: rgb(177, 127, 66);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_7:pressed\n"
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
        self.pushButton_8.setStyleSheet("#pushButton_8\n"
                                        "{\n"
                                        "color: rgb(98, 71, 42);\n"
                                        "background-color: rgb(197, 147, 86);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_8:hover\n"
                                        "{\n"
                                        "color: rgb(118, 91, 62);\n"
                                        "background-color: rgb(177, 127, 66);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_8:pressed\n"
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
        self.pushButton_12.setStyleSheet("#pushButton_12\n"
                                         "{\n"
                                         "color: rgb(98, 71, 42);\n"
                                         "background-color: rgb(197, 157, 96);\n"
                                         "border-radius: 5px;\n"
                                         "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                         "border-right: 1px solid rgb(98, 71, 50);\n"
                                         "}\n"
                                         "\n"
                                         "#pushButton_12:hover\n"
                                         "{\n"
                                         "color: rgb(118, 91, 62);\n"
                                         "background-color: rgb(177, 127, 66);\n"
                                         "border-radius: 5px;\n"
                                         "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                         "border-right: 1px solid rgb(98, 71, 50);\n"
                                         "}\n"
                                         "\n"
                                         "#pushButton_12:pressed\n"
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

        if UI.counter_push == 0:
            self.pushButton_11.setStyleSheet("#pushButton_11\n"
                                             "{\n"
                                             "color: rgb(98, 71, 42);\n"
                                             "background-color: rgb(197, 147, 86);\n"
                                             "border-radius: 5px;\n"
                                             "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                             "border-right: 1px solid rgb(98, 71, 50);\n"
                                             "	background-color: rgb(209, 59, 13);}\n"
                                             "\n"
                                             "#pushButton_11:hover\n"
                                             "{\n"
                                             "color: rgb(118, 91, 62);\n"
                                             "	background-color: rgb(199, 49, 3);\n"
                                             "border-radius: 5px;\n"
                                             "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                             "border-right: 1px solid rgb(98, 71, 50);\n"
                                             "}\n"
                                             "\n"
                                             "#pushButton_11:pressed\n"
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
            UI.counter_push+=1
            self.pushButton_11.setText("Только срочные заказы")
            UI.FLAG_TOLKO = "KRA"
        else:
            if UI.counter_push == 1:
                self.pushButton_11.setStyleSheet("#pushButton_11\n"
                                                 "{\n"
                                                 "color: rgb(98, 71, 42);\n"
                                                 "background-color: rgb(197, 147, 86);\n"
                                                 "border-radius: 5px;\n"
                                                 "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                                 "border-right: 1px solid rgb(98, 71, 50);\n"
                                                 "	background-color: rgb(255, 205, 24);}\n"
                                                 "\n"
                                                 "#pushButton_11:hover\n"
                                                 "{\n"
                                                 "color: rgb(118, 91, 62);\n"
                                                 "background-color: rgb(255, 176, 17);\n"
                                                 "border-radius: 5px;\n"
                                                 "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                                 "border-right: 1px solid rgb(98, 71, 50);\n"
                                                 "}\n"
                                                 "\n"
                                                 "#pushButton_11:pressed\n"
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
                UI.counter_push += 1
                self.pushButton_11.setText("Только ср. по сроч. заказы")
                UI.FLAG_TOLKO = "JEL"
            else:
                if UI.counter_push == 2:
                    self.pushButton_11.setStyleSheet("#pushButton_11\n"
                                                     "{\n"
                                                     "color: rgb(98, 71, 42);\n"
                                                     "background-color: rgb(197, 147, 86);\n"
                                                     "border-radius: 5px;\n"
                                                     "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                                     "border-right: 1px solid rgb(98, 71, 50);\n"
                                                     "	background-color: rgb(151, 177, 34);}\n"
                                                     "\n"
                                                     "#pushButton_11:hover\n"
                                                     "{\n"
                                                     "color: rgb(118, 91, 62);\n"
                                                     "background-color: rgb(131, 157, 14);\n"
                                                     "border-radius: 5px;\n"
                                                     "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                                     "border-right: 1px solid rgb(98, 71, 50);\n"
                                                     "}\n"
                                                     "\n"
                                                     "#pushButton_11:pressed\n"
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
                    UI.counter_push = 0
                    self.pushButton_11.setText("Только не срочные заказы")
                    UI.FLAG_TOLKO = "ZEL"

        from ui_add_new_elements import widget_begin
        widget_begin.del_all_strings(self)
        widget_begin.add_new_strings(self)
    # осн настройки:кнопка только активные заказы
    def HANDLER_MEN_pushButton_7(self):
        # обычная, не активная
        self.pushButton_11.setStyleSheet("#pushButton_11\n"
                                         "{\n"
                                         "color: rgb(98, 71, 42);\n"
                                         "background-color: rgb(197, 147, 86);\n"
                                         "border-radius: 5px;\n"
                                         "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                         "border-right: 1px solid rgb(98, 71, 50);\n"
                                         "}\n"
                                         "\n"
                                         "#pushButton_11:hover\n"
                                         "{\n"
                                         "color: rgb(118, 91, 62);\n"
                                         "background-color: rgb(177, 127, 66);\n"
                                         "border-radius: 5px;\n"
                                         "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                         "border-right: 1px solid rgb(98, 71, 50);\n"
                                         "}\n"
                                         "\n"
                                         "#pushButton_11:pressed\n"
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
        self.pushButton_12.setStyleSheet("#pushButton_12\n"
                                         "{\n"
                                         "color: rgb(98, 71, 42);\n"
                                         "background-color: rgb(197, 157, 96);\n"
                                         "border-radius: 5px;\n"
                                         "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                         "border-right: 1px solid rgb(98, 71, 50);\n"
                                         "}\n"
                                         "\n"
                                         "#pushButton_12:hover\n"
                                         "{\n"
                                         "color: rgb(118, 91, 62);\n"
                                         "background-color: rgb(177, 127, 66);\n"
                                         "border-radius: 5px;\n"
                                         "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                         "border-right: 1px solid rgb(98, 71, 50);\n"
                                         "}\n"
                                         "\n"
                                         "#pushButton_12:pressed\n"
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
        self.pushButton_8.setStyleSheet("#pushButton_8\n"
                                        "{\n"
                                        "color: rgb(98, 71, 42);\n"
                                        "background-color: rgb(197, 147, 86);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_8:hover\n"
                                        "{\n"
                                        "color: rgb(118, 91, 62);\n"
                                        "background-color: rgb(177, 127, 66);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_8:pressed\n"
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

        self.pushButton_7.setStyleSheet("#pushButton_7\n"
                                        "{\n"
                                        "color: rgb(98, 71, 42);\n"
                                        "background-color: rgb(197, 147, 86);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "	background-color: rgb(151, 177, 34);}\n"
                                        "\n"
                                        "#pushButton_7:hover\n"
                                        "{\n"
                                        "color: rgb(118, 91, 62);\n"
                                        "background-color: rgb(131, 157, 14);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_7:pressed\n"
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

        UI.FLAG_TOLKO = "NET_CONEC"
        from ui_add_new_elements import widget_begin
        widget_begin.del_all_strings(self)
        widget_begin.add_new_strings(self)
    # осн настройки:кнопка только завершенные заказы
    def HANDLER_MEN_pushButton_8(self):
        # обычная, не активная
        self.pushButton_11.setStyleSheet("#pushButton_11\n"
                                         "{\n"
                                         "color: rgb(98, 71, 42);\n"
                                         "background-color: rgb(197, 147, 86);\n"
                                         "border-radius: 5px;\n"
                                         "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                         "border-right: 1px solid rgb(98, 71, 50);\n"
                                         "}\n"
                                         "\n"
                                         "#pushButton_11:hover\n"
                                         "{\n"
                                         "color: rgb(118, 91, 62);\n"
                                         "background-color: rgb(177, 127, 66);\n"
                                         "border-radius: 5px;\n"
                                         "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                         "border-right: 1px solid rgb(98, 71, 50);\n"
                                         "}\n"
                                         "\n"
                                         "#pushButton_11:pressed\n"
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
        self.pushButton_12.setStyleSheet("#pushButton_12\n"
                                         "{\n"
                                         "color: rgb(98, 71, 42);\n"
                                         "background-color: rgb(197, 147, 86);\n"
                                         "border-radius: 5px;\n"
                                         "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                         "border-right: 1px solid rgb(98, 71, 50);\n"
                                         "}\n"
                                         "\n"
                                         "#pushButton_12:hover\n"
                                         "{\n"
                                         "color: rgb(118, 91, 62);\n"
                                         "background-color: rgb(177, 127, 66);\n"
                                         "border-radius: 5px;\n"
                                         "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                         "border-right: 1px solid rgb(98, 71, 50);\n"
                                         "}\n"
                                         "\n"
                                         "#pushButton_12:pressed\n"
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
        self.pushButton_7.setStyleSheet("#pushButton_7\n"
                                        "{\n"
                                        "color: rgb(98, 71, 42);\n"
                                        "background-color: rgb(197, 157, 96);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_7:hover\n"
                                        "{\n"
                                        "color: rgb(118, 91, 62);\n"
                                        "background-color: rgb(177, 127, 66);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_7:pressed\n"
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

        # кнопка активная
        self.pushButton_8.setStyleSheet("#pushButton_8\n"
                                        "{\n"
                                        "color: rgb(98, 71, 42);\n"
                                        "background-color: rgb(197, 147, 86);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "	background-color: rgb(151, 177, 34);}\n"
                                        "\n"
                                        "#pushButton_8:hover\n"
                                        "{\n"
                                        "color: rgb(118, 91, 62);\n"
                                        "background-color: rgb(131, 157, 14);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_8:pressed\n"
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

        UI.FLAG_TOLKO = "EST_CONEC"
        from ui_add_new_elements import widget_begin
        widget_begin.del_all_strings(self)
        widget_begin.add_new_strings(self)
    # осн настройки:все заказы
    def HANDLER_MEN_pushButton_12(self):
        # обычная, не активная
        self.pushButton_11.setStyleSheet("#pushButton_11\n"
                                         "{\n"
                                         "color: rgb(98, 71, 42);\n"
                                         "background-color: rgb(197, 147, 86);\n"
                                         "border-radius: 5px;\n"
                                         "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                         "border-right: 1px solid rgb(98, 71, 50);\n"
                                         "}\n"
                                         "\n"
                                         "#pushButton_11:hover\n"
                                         "{\n"
                                         "color: rgb(118, 91, 62);\n"
                                         "background-color: rgb(177, 127, 66);\n"
                                         "border-radius: 5px;\n"
                                         "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                         "border-right: 1px solid rgb(98, 71, 50);\n"
                                         "}\n"
                                         "\n"
                                         "#pushButton_11:pressed\n"
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
        self.pushButton_7.setStyleSheet("#pushButton_7\n"
                                        "{\n"
                                        "color: rgb(98, 71, 42);\n"
                                        "background-color: rgb(197, 157, 96);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_7:hover\n"
                                        "{\n"
                                        "color: rgb(118, 91, 62);\n"
                                        "background-color: rgb(177, 127, 66);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_7:pressed\n"
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
        self.pushButton_8.setStyleSheet("#pushButton_8\n"
                                        "{\n"
                                        "color: rgb(98, 71, 42);\n"
                                        "background-color: rgb(197, 147, 86);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_8:hover\n"
                                        "{\n"
                                        "color: rgb(118, 91, 62);\n"
                                        "background-color: rgb(177, 127, 66);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_8:pressed\n"
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
        # кнопка активная
        self.pushButton_12.setStyleSheet("#pushButton_12\n"
                                         "{\n"
                                         "color: rgb(98, 71, 42);\n"
                                         "background-color: rgb(197, 147, 86);\n"
                                         "border-radius: 5px;\n"
                                         "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                         "border-right: 1px solid rgb(98, 71, 50);\n"
                                         "	background-color: rgb(151, 177, 34);}\n"
                                         "\n"
                                         "#pushButton_12:hover\n"
                                         "{\n"
                                         "color: rgb(118, 91, 62);\n"
                                         "background-color: rgb(131, 157, 14);\n"
                                         "border-radius: 5px;\n"
                                         "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                         "border-right: 1px solid rgb(98, 71, 50);\n"
                                         "}\n"
                                         "\n"
                                         "#pushButton_12:pressed\n"
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

        UI.FLAG_TOLKO = "VCE"
        from ui_add_new_elements import widget_begin
        widget_begin.del_all_strings(self)
        widget_begin.add_new_strings(self)

    MASSIVE_FILE_with_posledovat = []

    # осн настройки: сортировка
    # осн настройки: сортировки по срочности
    def HANDLER_MEN_pushButton_5(self):
        # зеленая, активная
        self.pushButton_5.setStyleSheet("#pushButton_5\n"
                                        "{\n"
                                        "color: rgb(98, 71, 42);\n"
                                        "background-color: rgb(197, 147, 86);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "	background-color: rgb(151, 177, 34);}\n"
                                        "\n"
                                        "#pushButton_5:hover\n"
                                        "{\n"
                                        "color: rgb(118, 91, 62);\n"
                                        "background-color: rgb(141, 167, 24);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_5:pressed\n"
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
        # обычная, не активная
        self.pushButton_6.setStyleSheet("#pushButton_6\n"
                                        "{\n"
                                        "color: rgb(98, 71, 42);\n"
                                        "background-color: rgb(197, 157, 96);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_6:hover\n"
                                        "{\n"
                                        "color: rgb(118, 91, 62);\n"
                                        "background-color: rgb(177, 127, 66);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_6:pressed\n"
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
        self.pushButton_9.setStyleSheet("#pushButton_9\n"
                                        "{\n"
                                        "color: rgb(98, 71, 42);\n"
                                        "background-color: rgb(197, 147, 86);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_9:hover\n"
                                        "{\n"
                                        "color: rgb(118, 91, 62);\n"
                                        "background-color: rgb(177, 127, 66);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_9:pressed\n"
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
        self.pushButton_10.setStyleSheet("#pushButton_10\n"
                                         "{\n"
                                         "color: rgb(98, 71, 42);\n"
                                         "background-color: rgb(197, 157, 96);\n"
                                         "border-radius: 5px;\n"
                                         "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                         "border-right: 1px solid rgb(98, 71, 50);\n"
                                         "}\n"
                                         "\n"
                                         "#pushButton_10:hover\n"
                                         "{\n"
                                         "color: rgb(118, 91, 62);\n"
                                         "background-color: rgb(177, 127, 66);\n"
                                         "border-radius: 5px;\n"
                                         "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                         "border-right: 1px solid rgb(98, 71, 50);\n"
                                         "}\n"
                                         "\n"
                                         "#pushButton_10:pressed\n"
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
        file_nomer = 1

        file_KRA = []
        file_JEL = []
        file_ZEL = []
        file_BLC = []

        name = ""
        if "достоем информацию из файла всех заказов" != "и составаляем список в нужном порядке":
            if "" == "":
                import os
                name = os.listdir("../pythonProject3/DATABASE/current_project")
            for iks in name:
                txt = f"../pythonProject3/DATABASE/current_project/" + (name[file_nomer - 1])
                path_to_current_file = txt
                print(txt)
                with open(txt, 'r') as file:
                    nomer_proecta = name[file_nomer - 1]
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
                        if index == 4:
                            data_konca = line.strip()

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
                                print("data_konca[counter]", data_konca[counter])
                                day_end += data_konca[counter]
                            else:
                                break
                            counter += 1
                        mounth_end = ""
                        counter += 1
                        while True:
                            if data_konca[counter] != ".":
                                print("data_konca[counter]", data_konca[counter])
                                mounth_end += data_konca[counter]
                            else:
                                break
                            counter += 1
                        year_end = ""
                        counter += 1
                        try:
                            while True:
                                if data_konca[counter] != ".":
                                    print("data_konca[counter]", data_konca[counter])
                                    year_end += data_konca[counter]
                                else:
                                    break
                                counter += 1
                        except:
                            pass

                    raznitsa = int(day_end) - day

                    DAYindex_plus = 0
                    # if raznitsa < 0:
                    while True:
                        if (year_now + 2) == year:
                            DAYindex_plus = -100
                            break
                        if int(day_end) == int(day) and int(mounth_end) == int(mounth) and int(year) == int(
                                year_end):
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
                    # else:
                    #     DAYindex_plus = raznitsa

                    if DAYindex_plus > 5 and DAYindex_plus>0:
                        file_ZEL.append(name[file_nomer - 1])
                    else:
                        if (DAYindex_plus <= 5 and DAYindex_plus > 2):
                            file_JEL.append(name[file_nomer - 1])
                        else:
                            if (DAYindex_plus <= 2 and DAYindex_plus >= 0):
                                file_KRA.append(name[file_nomer - 1])
                            else:
                                if DAYindex_plus < 0:
                                    file_BLC.append(name[file_nomer - 1])

                    # except:
                    #     raznitsa = int(data_konca[0:1]) - int(day)
                    #     print("raznitsa ", data_konca[0:1], " - ", day, " = ", raznitsa)
                file_nomer += 1
        name = []
        print("file_ZEL",file_ZEL,file_JEL,file_KRA,file_BLC)
        name += file_BLC
        name += file_KRA
        name += file_JEL
        name += file_ZEL

        UI.MASSIVE_FILE_with_posledovat = name
        from ui_add_new_elements import widget_begin
        widget_begin.del_all_strings(self)
        widget_begin.add_new_strings(self)
    # осн настройки: сортировки по номеру
    def HANDLER_MEN_pushButton_6(self):
        # зеленая, активная
        self.pushButton_6.setStyleSheet("#pushButton_6\n"
                                        "{\n"
                                        "color: rgb(98, 71, 42);\n"
                                        "background-color: rgb(197, 147, 86);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "	background-color: rgb(151, 177, 34);}\n"
                                        "\n"
                                        "#pushButton_6:hover\n"
                                        "{\n"
                                        "color: rgb(118, 91, 62);\n"
                                        "background-color: rgb(141, 167, 24);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_6:pressed\n"
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
        # обычная, не активная
        self.pushButton_5.setStyleSheet("#pushButton_5\n"
                                        "{\n"
                                        "color: rgb(98, 71, 42);\n"
                                        "background-color: rgb(197, 147, 86);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_5:hover\n"
                                        "{\n"
                                        "color: rgb(118, 91, 62);\n"
                                        "background-color: rgb(177, 127, 66);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_5:pressed\n"
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
        self.pushButton_9.setStyleSheet("#pushButton_9\n"
                                        "{\n"
                                        "color: rgb(98, 71, 42);\n"
                                        "background-color: rgb(197, 147, 86);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_9:hover\n"
                                        "{\n"
                                        "color: rgb(118, 91, 62);\n"
                                        "background-color: rgb(177, 127, 66);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_9:pressed\n"
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
        self.pushButton_10.setStyleSheet("#pushButton_10\n"
                                         "{\n"
                                         "color: rgb(98, 71, 42);\n"
                                         "background-color: rgb(197, 157, 96);\n"
                                         "border-radius: 5px;\n"
                                         "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                         "border-right: 1px solid rgb(98, 71, 50);\n"
                                         "}\n"
                                         "\n"
                                         "#pushButton_10:hover\n"
                                         "{\n"
                                         "color: rgb(118, 91, 62);\n"
                                         "background-color: rgb(177, 127, 66);\n"
                                         "border-radius: 5px;\n"
                                         "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                         "border-right: 1px solid rgb(98, 71, 50);\n"
                                         "}\n"
                                         "\n"
                                         "#pushButton_10:pressed\n"
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

        import os
        name = os.listdir("../pythonProject3/DATABASE/current_project")
        UI.MASSIVE_FILE_with_posledovat = name

        from ui_add_new_elements import widget_begin
        widget_begin.del_all_strings(self)
        widget_begin.add_new_strings(self)
    # осн настройки: сортировки по алфавиту в оборудование
    def HANDLER_MEN_pushButton_9(self):
        # зеленая, активная
        self.pushButton_9.setStyleSheet("#pushButton_9\n"
                                        "{\n"
                                        "color: rgb(98, 71, 42);\n"
                                        "background-color: rgb(197, 147, 86);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "	background-color: rgb(151, 177, 34);}\n"
                                        "\n"
                                        "#pushButton_9:hover\n"
                                        "{\n"
                                        "color: rgb(118, 91, 62);\n"
                                        "background-color: rgb(141, 167, 24);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_9:pressed\n"
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
        # обычная, не активная
        self.pushButton_5.setStyleSheet("#pushButton_5\n"
                                        "{\n"
                                        "color: rgb(98, 71, 42);\n"
                                        "background-color: rgb(197, 147, 86);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_5:hover\n"
                                        "{\n"
                                        "color: rgb(118, 91, 62);\n"
                                        "background-color: rgb(177, 127, 66);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_5:pressed\n"
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
        self.pushButton_6.setStyleSheet("#pushButton_6\n"
                                        "{\n"
                                        "color: rgb(98, 71, 42);\n"
                                        "background-color: rgb(197, 157, 96);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_6:hover\n"
                                        "{\n"
                                        "color: rgb(118, 91, 62);\n"
                                        "background-color: rgb(177, 127, 66);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_6:pressed\n"
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
        self.pushButton_10.setStyleSheet("#pushButton_10\n"
                                         "{\n"
                                         "color: rgb(98, 71, 42);\n"
                                         "background-color: rgb(197, 157, 96);\n"
                                         "border-radius: 5px;\n"
                                         "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                         "border-right: 1px solid rgb(98, 71, 50);\n"
                                         "}\n"
                                         "\n"
                                         "#pushButton_10:hover\n"
                                         "{\n"
                                         "color: rgb(118, 91, 62);\n"
                                         "background-color: rgb(177, 127, 66);\n"
                                         "border-radius: 5px;\n"
                                         "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                         "border-right: 1px solid rgb(98, 71, 50);\n"
                                         "}\n"
                                         "\n"
                                         "#pushButton_10:pressed\n"
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

        file_nomer = 1

        file_A = []
        file_B = []
        file_V = []
        file_G = []
        file_D = []
        file_YE = []
        file_YO = []
        file_J = []
        file_Z = []
        file_YI = []
        file_Y = []
        file_K = []
        file_L = []
        file_M = []
        file_N = []
        file_O = []
        file_P = []
        file_R = []
        file_S = []
        file_T = []
        file_U = []
        file_F = []
        file_H = []
        file_C = []
        file_SH = []
        file_SHY = []
        file_E = []
        file_YU = []
        file_YA = []
        # file_V = []

        name = ""
        oborudovanie = ""
        zakazchic = ""
        if "достоем информацию из файла всех заказов" != "и составаляем список в нужном порядке":
            import os
            name = os.listdir("../pythonProject3/DATABASE/current_project")
            for iks in name:
                txt = f"../pythonProject3/DATABASE/current_project/" + (name[file_nomer - 1])
                path_to_current_file = txt
                with open(txt, 'r') as file:
                    nomer_proecta = name[file_nomer - 1]
                    counter = 1
                    buf = ""

                    for index, line in enumerate(file):
                        if index == 10:
                            oborudovanie = " " + line.strip()
                            break

                    if "раскидываем по алфавиту" != "":
                        if oborudovanie[1] == "А" or oborudovanie[1] == "а":
                            file_A.append(name[file_nomer - 1])
                        if oborudovanie[1] == "Б" or oborudovanie[1] == "б":
                            file_B.append(name[file_nomer - 1])
                        if oborudovanie[1] == "В" or oborudovanie[1] == "в":
                            file_V.append(name[file_nomer - 1])
                        if oborudovanie[1] == "Г" or oborudovanie[1] == "г":
                            file_G.append(name[file_nomer - 1])
                        if oborudovanie[1] == "Д" or oborudovanie[1] == "д":
                            file_D.append(name[file_nomer - 1])
                        if oborudovanie[1] == "Е" or oborudovanie[1] == "е":
                            file_YE.append(name[file_nomer - 1])
                        if oborudovanie[1] == "Ё" or oborudovanie[1] == "ё":
                            file_YO.append(name[file_nomer - 1])
                        if oborudovanie[1] == "Ж" or oborudovanie[1] == "ж":
                            file_J.append(name[file_nomer - 1])
                        if oborudovanie[1] == "З" or oborudovanie[1] == "з":
                            file_Z.append(name[file_nomer - 1])
                        if oborudovanie[1] == "И" or oborudovanie[1] == "и":
                            file_YI.append(name[file_nomer - 1])
                        if oborudovanie[1] == "Й" or oborudovanie[1] == "й":
                            file_Y.append(name[file_nomer - 1])
                        if oborudovanie[1] == "К" or oborudovanie[1] == "к":
                            file_K.append(name[file_nomer - 1])
                        if oborudovanie[1] == "Л" or oborudovanie[1] == "л":
                            file_L.append(name[file_nomer - 1])
                        if oborudovanie[1] == "М" or oborudovanie[1] == "м":
                            file_M.append(name[file_nomer - 1])
                        if oborudovanie[1] == "Н" or oborudovanie[1] == "н":
                            file_N.append(name[file_nomer - 1])
                        if oborudovanie[1] == "О" or oborudovanie[1] == "о":
                            file_O.append(name[file_nomer - 1])
                        if oborudovanie[1] == "П" or oborudovanie[1] == "п":
                            file_P.append(name[file_nomer - 1])
                        if oborudovanie[1] == "Р" or oborudovanie[1] == "р":
                            file_R.append(name[file_nomer - 1])
                        if oborudovanie[1] == "С" or oborudovanie[1] == "с":
                            file_S.append(name[file_nomer - 1])
                        if oborudovanie[1] == "Т" or oborudovanie[1] == "т":
                            file_T.append(name[file_nomer - 1])
                        if oborudovanie[1] == "У" or oborudovanie[1] == "у":
                            file_U.append(name[file_nomer - 1])
                        if oborudovanie[1] == "Ф" or oborudovanie[1] == "ф":
                            file_F.append(name[file_nomer - 1])
                        if oborudovanie[1] == "Х" or oborudovanie[1] == "х":
                            file_H.append(name[file_nomer - 1])
                        if oborudovanie[1] == "Ц" or oborudovanie[1] == "ц":
                            file_C.append(name[file_nomer - 1])
                        if oborudovanie[1] == "Ш" or oborudovanie[1] == "ш":
                            file_SH.append(name[file_nomer - 1])
                        if oborudovanie[1] == "Щ" or oborudovanie[1] == "щ":
                            file_SHY.append(name[file_nomer - 1])
                        if oborudovanie[1] == "Э" or oborudovanie[1] == "э":
                            file_E.append(name[file_nomer - 1])
                        if oborudovanie[1] == "Ю" or oborudovanie[1] == "ю":
                            file_YU.append(name[file_nomer - 1])
                        if oborudovanie[1] == "Я" or oborudovanie[1] == "я":
                            file_YA.append(name[file_nomer - 1])
                        FLAG_ne_bukva = 1
                        for qui in "ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ":
                            if qui == oborudovanie[1]:
                                FLAG_ne_bukva = 0
                        if FLAG_ne_bukva == 1:
                            file_YA.append(name[file_nomer - 1])


                file_nomer += 1
            print("file_A: ", file_A)
        UI.MASSIVE_FILE_with_posledovat = []
        UI.MASSIVE_FILE_with_posledovat = file_A + file_B + file_V + file_G + file_D + file_YE + file_YO + file_J + file_Z + file_YI + file_Y + file_K + file_L + file_M + file_N + file_O + file_P + file_R + file_S + file_T + file_U + file_F + file_H + file_C + file_SH + file_SHY + file_E + file_YU + file_YA
        print("UI.UI.MASSIVE_FILE_with_posledovat", UI.MASSIVE_FILE_with_posledovat)
        from ui_add_new_elements import widget_begin
        widget_begin.del_all_strings(self)
        widget_begin.add_new_strings(self)
    # осн настройки: сортировки по алфавиту в заказчиках
    def HANDLER_MEN_pushButton_10(self):
        # зеленая, активная
        self.pushButton_10.setStyleSheet("#pushButton_10\n"
                                         "{\n"
                                         "color: rgb(98, 71, 42);\n"
                                         "background-color: rgb(197, 147, 86);\n"
                                         "border-radius: 5px;\n"
                                         "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                         "border-right: 1px solid rgb(98, 71, 50);\n"
                                         "	background-color: rgb(151, 177, 34);}\n"
                                         "\n"
                                         "#pushButton_10:hover\n"
                                         "{\n"
                                         "color: rgb(118, 91, 62);\n"
                                         "background-color: rgb(141, 167, 24);\n"
                                         "border-radius: 5px;\n"
                                         "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                         "border-right: 1px solid rgb(98, 71, 50);\n"
                                         "}\n"
                                         "\n"
                                         "#pushButton_10:pressed\n"
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
        # обычная, не активная
        self.pushButton_5.setStyleSheet("#pushButton_5\n"
                                        "{\n"
                                        "color: rgb(98, 71, 42);\n"
                                        "background-color: rgb(197, 147, 86);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_5:hover\n"
                                        "{\n"
                                        "color: rgb(118, 91, 62);\n"
                                        "background-color: rgb(177, 127, 66);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_5:pressed\n"
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
        self.pushButton_9.setStyleSheet("#pushButton_9\n"
                                        "{\n"
                                        "color: rgb(98, 71, 42);\n"
                                        "background-color: rgb(197, 147, 86);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_9:hover\n"
                                        "{\n"
                                        "color: rgb(118, 91, 62);\n"
                                        "background-color: rgb(177, 127, 66);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_9:pressed\n"
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
        self.pushButton_6.setStyleSheet("#pushButton_6\n"
                                        "{\n"
                                        "color: rgb(98, 71, 42);\n"
                                        "background-color: rgb(197, 157, 96);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_6:hover\n"
                                        "{\n"
                                        "color: rgb(118, 91, 62);\n"
                                        "background-color: rgb(177, 127, 66);\n"
                                        "border-radius: 5px;\n"
                                        "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                        "border-right: 1px solid rgb(98, 71, 50);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_6:pressed\n"
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

        file_nomer = 1

        file_A = []
        file_B = []
        file_V = []
        file_G = []
        file_D = []
        file_YE = []
        file_YO = []
        file_J = []
        file_Z = []
        file_YI = []
        file_Y = []
        file_K = []
        file_L = []
        file_M = []
        file_N = []
        file_O = []
        file_P = []
        file_R = []
        file_S = []
        file_T = []
        file_U = []
        file_F = []
        file_H = []
        file_C = []
        file_SH = []
        file_SHY = []
        file_E = []
        file_YU = []
        file_YA = []
        # file_V = []

        name = ""
        oborudovanie = ""
        zakazchic = ""
        if "достоем информацию из файла всех заказов" != "и составаляем список в нужном порядке":
            import os
            name = os.listdir("../pythonProject3/DATABASE/current_project")
            for iks in name:
                txt = f"../pythonProject3/DATABASE/current_project/" + (name[file_nomer - 1])
                path_to_current_file = txt
                with open(txt, 'r') as file:
                    nomer_proecta = name[file_nomer - 1]
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
                    if "" == "":
                        for index, line in enumerate(file):
                            if index == 2:
                                zakazchic = " " + line.strip()

                    print("zakazchic!!! ", name[file_nomer - 1], zakazchic, ": ", zakazchic[6])
                    if "раскидываем по алфавиту" != "":
                        if zakazchic[6] == "А" or zakazchic[6] == "а":
                            file_A.append(name[file_nomer - 1])
                        if zakazchic[6] == "Б" or zakazchic[6] == "б":
                            file_B.append(name[file_nomer - 1])
                        if zakazchic[6] == "В" or zakazchic[6] == "в":
                            file_V.append(name[file_nomer - 1])
                        if zakazchic[6] == "Г" or zakazchic[6] == "г":
                            file_G.append(name[file_nomer - 1])
                        if zakazchic[6] == "Д" or zakazchic[6] == "д":
                            file_D.append(name[file_nomer - 1])
                        if zakazchic[6] == "Е" or zakazchic[6] == "е":
                            file_YE.append(name[file_nomer - 1])
                        if zakazchic[6] == "Ё" or zakazchic[6] == "ё":
                            file_YO.append(name[file_nomer - 1])
                        if zakazchic[6] == "Ж" or zakazchic[6] == "ж":
                            file_J.append(name[file_nomer - 1])
                        if zakazchic[6] == "З" or zakazchic[6] == "з":
                            file_Z.append(name[file_nomer - 1])
                        if zakazchic[6] == "И" or zakazchic[6] == "и":
                            file_YI.append(name[file_nomer - 1])
                        if zakazchic[6] == "Й" or zakazchic[6] == "й":
                            file_Y.append(name[file_nomer - 1])
                        if zakazchic[6] == "К" or zakazchic[6] == "к":
                            file_K.append(name[file_nomer - 1])
                        if zakazchic[6] == "Л" or zakazchic[6] == "л":
                            file_L.append(name[file_nomer - 1])
                        if zakazchic[6] == "М" or zakazchic[6] == "м":
                            file_M.append(name[file_nomer - 1])
                        if zakazchic[6] == "Н" or zakazchic[6] == "н":
                            file_N.append(name[file_nomer - 1])
                        if zakazchic[6] == "О" or zakazchic[6] == "о":
                            file_O.append(name[file_nomer - 1])
                        if zakazchic[6] == "П" or zakazchic[6] == "п":
                            file_P.append(name[file_nomer - 1])
                        if zakazchic[6] == "Р" or zakazchic[6] == "р":
                            file_R.append(name[file_nomer - 1])
                        if zakazchic[6] == "С" or zakazchic[6] == "с":
                            file_S.append(name[file_nomer - 1])
                        if zakazchic[6] == "Т" or zakazchic[6] == "т":
                            file_T.append(name[file_nomer - 1])
                        print("zakazchic!", zakazchic)
                        if zakazchic[6] == "У" or zakazchic[6] == "у":
                            print("zakazchic!", zakazchic)
                            file_U.append(name[file_nomer - 1])
                        if zakazchic[6] == "Ф" or zakazchic[6] == "ф":
                            file_F.append(name[file_nomer - 1])
                        if zakazchic[6] == "Х" or zakazchic[6] == "х":
                            file_H.append(name[file_nomer - 1])
                        if zakazchic[6] == "Ц" or zakazchic[6] == "ц":
                            file_C.append(name[file_nomer - 1])
                        if zakazchic[6] == "Ш" or zakazchic[6] == "ш":
                            file_SH.append(name[file_nomer - 1])
                        if zakazchic[6] == "Щ" or zakazchic[6] == "щ":
                            file_SHY.append(name[file_nomer - 1])
                        if zakazchic[6] == "Э" or zakazchic[6] == "э":
                            file_E.append(name[file_nomer - 1])
                        if zakazchic[6] == "Ю" or zakazchic[6] == "ю":
                            file_YU.append(name[file_nomer - 1])
                        if zakazchic[6] == "Я" or zakazchic[6] == "я":
                            file_YA.append(name[file_nomer - 1])

                        FLAG_ne_bukva = 1
                        for qui in "ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ":
                            if qui == zakazchic[6]:
                                FLAG_ne_bukva = 0
                        if FLAG_ne_bukva == 1:
                            file_YA.append(name[file_nomer - 1])
                    # except:
                    #     raznitsa = int(data_konca[0:1]) - int(day)
                    #     print("raznitsa ", data_konca[0:1], " - ", day, " = ", raznitsa)
                file_nomer += 1
            print("file_A: ", file_A)
        UI.MASSIVE_FILE_with_posledovat = []
        UI.MASSIVE_FILE_with_posledovat = file_A + file_B + file_V + file_G + file_D + file_YE + file_YO + file_J + file_Z + file_YI + file_Y + file_K + file_L + file_M + file_N + file_O + file_P + file_R + file_S + file_T + file_U + file_F + file_H + file_C + file_SH + file_SHY + file_E + file_YU + file_YA
        print("UI.UI.MASSIVE_FILE_with_posledovat", UI.MASSIVE_FILE_with_posledovat)
        from ui_add_new_elements import widget_begin
        widget_begin.del_all_strings(self)
        widget_begin.add_new_strings(self)


    #cоздания настройки
    def HANDLER_MEN_pushButton_32(self):
        self.stackedWidget_2.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(0)
    # cоздания настройки:отмена создания
    def HANDLER_MEN_pushButton_40(self):
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)
        self.pushButton_32.hide()

        self.lineEdit.clear()
        self.lineEdit_16.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()
        self.lineEdit_9.clear()
        self.lineEdit_10.clear()
        self.lineEdit_11.clear()
        self.lineEdit_12.clear()
        self.lineEdit_13.clear()
        self.lineEdit_14.clear()
        self.lineEdit_15.clear()
        self.textEdit.clear()
        self.textEdit_3.clear()
        self.textEdit_4.clear()
        self.lineEdit.clear()
        self.lineEdit.clear()
        self.lineEdit.clear()
        self.lineEdit.clear()

    #поле создания
    # поле создания:повысить срок выполнения проекта на 1 день
    pushButton_DAYindex = 7
    pushButton_DAYindex_plus = 7
    pushButton_MOUNTHindex_plus = 0
    pushButton_YEARindex_plus = 0
    def HANDLER_MEN_pushButton(self):
        UI.pushButton_DAYindex += 1
        UI.pushButton_DAYindex_plus += 1
        UI.write_colichestvo_dney_na_remont_plus(self)
    def HANDLER_MEN_pushButton_2(self):
        UI.pushButton_DAYindex -= 1
        UI.pushButton_DAYindex_plus -= 1
        UI.write_colichestvo_dney_na_remont_minus(self)
    # на поле начинания:кнопка отменить создание проекта/заполнить бланк пятерккми
    def HANDLER_MEN_pushButton_13(self):
        UI.HANDLER_MEN_pushButton_40(self)

        self.pushButton_24.setEnabled(True)
        self.pushButton_25.setEnabled(True)
        if self.comboBox_16.currentText() == "Мен. обслуживания":
            self.pushButton_4.setEnabled(True)
        self.pushButton_14.setEnabled(True)
        self.lineEdit_17.setEnabled(True)
        self.pushButton_15.setEnabled(True)
        self.pushButton_5.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.pushButton_9.setEnabled(True)
        self.pushButton_10.setEnabled(True)
        self.pushButton_11.setEnabled(True)
        self.pushButton_7.setEnabled(True)
        self.pushButton_8.setEnabled(True)
        self.pushButton_12.setEnabled(True)
        #для быстрого заполнения для проверки кода
        # self.lineEdit_21.setText("111")
        # self.lineEdit.setText("112")
        # self.lineEdit_2.setText("113")
        # self.lineEdit_16.setText("114")
        # self.lineEdit_3.setText("115")
        # self.lineEdit_4.setText("116")
        # self.lineEdit_10.setText("117")
        # self.lineEdit_11.setText("118")
        # self.lineEdit_12.setText("119")
        # self.lineEdit_13.setText("120")
        # self.lineEdit_14.setText("121")
        # self.lineEdit_15.setText("122")
        # self.textEdit.setText("123")
        # self.textEdit_3.setText("124")
        # self.textEdit_4.setText("125")




    flag_get_SYStime = 1
    year = ""
    mounth = ""
    day = ""
    def write_colichestvo_dney_na_remont_plus(self):
        if UI.flag_get_SYStime == 1:
            UI.flag_get_SYStime = 0
            import datetime
            now = str(datetime.datetime.now())
            UI.year = int(now[0:4])
            UI.mounth = int(now[5:7])
            UI.day = int(now[8:10])
            # UI.pushButton_DAYindex_plus = UI.day

            # print("UI.day ", UI.day)
            UI.day += UI.pushButton_DAYindex_plus
            # print("UI.day ",UI.day)
        else:
            UI.day += 1
        print("UI.day 2159", UI.day)
        if 31 == 31:
            if UI.mounth == 1 and UI.day > 31:
                print("UI.year ",UI.year," UI.mounth ",UI.mounth," UI.day ",UI.day)
                UI.day = UI.day - 32
                UI.mounth += 1
                UI.pushButton_DAYindex_plus = 0
            if UI.mounth == 3 and UI.day > 31:
                print("UI.year ", UI.year, " UI.mounth ", UI.mounth, " UI.day ", UI.day)
                UI.day = UI.day - 32
                UI.mounth += 1
                UI.pushButton_DAYindex_plus = 0
            if UI.mounth == 5 and UI.day > 31:
                print("UI.year ", UI.year, " UI.mounth ", UI.mounth, " UI.day ", UI.day)
                UI.day = UI.day - 32
                UI.mounth += 1
                UI.pushButton_DAYindex_plus = 0
            if UI.mounth == 7 and UI.day > 31:
                print("UI.year ", UI.year, " UI.mounth ", UI.mounth, " UI.day ", UI.day)
                UI.day = 1
                UI.mounth += 1
                UI.pushButton_DAYindex_plus = 0
            if UI.mounth == 8 and UI.day > 31:
                print("UI.year ", UI.year, " UI.mounth ", UI.mounth, " UI.day ", UI.day)
                UI.day = UI.day - 32
                UI.mounth += 1
                UI.pushButton_DAYindex_plus = 0
            if UI.mounth == 10 and UI.day > 31:
                print("UI.year ", UI.year, " UI.mounth ", UI.mounth, " UI.day ", UI.day)
                UI.day = UI.day - 32
                UI.mounth += 1
                UI.pushButton_DAYindex_plus = 0
            if UI.mounth == 12 and UI.day > 31:
                print("UI.year ", UI.year, " UI.mounth ", UI.mounth, " UI.day ", UI.day)
                UI.day = UI.day - 31
                UI.mounth += 1
                UI.pushButton_DAYindex_plus = 0
        if 30 == 30:
            if UI.mounth == 4 and UI.day > 30:
                print("UI.year ", UI.year, " UI.mounth ", UI.mounth, " UI.day ", UI.day)
                UI.day = UI.day - 31
                UI.mounth += 1
                UI.pushButton_DAYindex_plus = 0
            if UI.mounth == 6 and UI.day > 30:
                print("UI.year ", UI.year, " UI.mounth ", UI.mounth, " UI.day ", UI.day)
                UI.day = UI.day - 31
                UI.mounth += 1
                UI.pushButton_DAYindex_plus = 0
            if UI.mounth == 9 and UI.day > 30:
                print("UI.year ", UI.year, " UI.mounth ", UI.mounth, " UI.day ", UI.day)
                UI.day = UI.day - 31
                UI.mounth += 1
                UI.pushButton_DAYindex_plus = 0
            if UI.mounth == 11 and UI.day > 30:
                print("UI.year ", UI.year, " UI.mounth ", UI.mounth, " UI.day ", UI.day)
                UI.day = UI.day - 30
                UI.mounth += 1
                UI.pushButton_DAYindex_plus = 0
        if 29 == 29 or 28 == 28:
            for i in [2020,2024,2028,2032,2036,2040,2044,2048,2052,2056,2060,2064,2068,2072,2076,2080]:
                if UI.mounth == 2 and UI.day > 29 and UI.year == i:
                    print("UI.year ", UI.year, " UI.mounth ", UI.mounth, " UI.day ", UI.day)
                    UI.day = UI.day - 30
                    UI.mounth += 1
                    UI.pushButton_DAYindex_plus = 0
                else:
                    if UI.mounth == 2 and UI.day > 28 and UI.year != i:
                        print("UI.year ", UI.year, " UI.mounth ", UI.mounth, " UI.day ", UI.day)
                        UI.day = UI.day - 29
                        UI.mounth += 1
                        UI.pushButton_DAYindex_plus = 0

        if 12 == 12:
            if UI.mounth > 12:
                UI.mounth = 0
                UI.mounth = 1
                UI.year +=1

        self.label_4.setText(f"Дата выполнения проекта: {UI.day}.{UI.mounth}.{UI.year}  ({UI.pushButton_DAYindex} дней)")
    def write_colichestvo_dney_na_remont_minus(self):
        UI.day -= 1
        print("UI.day -", UI.day)

        if UI.mounth == 1 and UI.day < 1:
            print("UI.year ",UI.year," UI.mounth ",UI.mounth," UI.day ",UI.day)
            UI.day = 31
            UI.mounth = 12
            UI.year -= 1
            UI.pushButton_DAYindex_plus = 0
        if UI.mounth == 2 and UI.day < 1:
            print("UI.year ", UI.year, " UI.mounth ", UI.mounth, " UI.day ", UI.day)
            UI.day = 31
            UI.mounth -= 1
            UI.pushButton_DAYindex_plus = 0
        if UI.mounth == 3 and UI.day < 1:
            UI.mounth -= 1
            if 29 == 29 or 28 == 28:
                for i in [2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068, 2072, 2076,
                          2080]:
                    if UI.mounth == 2 and UI.year == i:
                        print("UI.year ", UI.year, " UI.mounth ", UI.mounth, " UI.day ", UI.day)
                        UI.day = 29
                        UI.pushButton_DAYindex_plus = 0
                    else:
                        if UI.mounth == 2 and UI.year != i:
                            print("UI.year ", UI.year, " UI.mounth ", UI.mounth, " UI.day ", UI.day)
                            UI.day = 28
                            UI.pushButton_DAYindex_plus = 0
        if UI.mounth == 4 and UI.day < 1:
            print("UI.year ", UI.year, " UI.mounth ", UI.mounth, " UI.day ", UI.day)
            UI.day = 31
            UI.mounth -= 1
            UI.pushButton_DAYindex_plus = 0
        if UI.mounth == 5 and UI.day < 1:
            print("UI.year ", UI.year, " UI.mounth ", UI.mounth, " UI.day ", UI.day)
            UI.day = 30
            UI.mounth -= 1
            UI.pushButton_DAYindex_plus = 0
        if UI.mounth == 6 and UI.day < 1:
            print("UI.year ", UI.year, " UI.mounth ", UI.mounth, " UI.day ", UI.day)
            UI.day = 31
            UI.mounth -= 1
            UI.pushButton_DAYindex_plus = 0
        if UI.mounth == 7 and UI.day < 1:
            print("UI.year ", UI.year, " UI.mounth ", UI.mounth, " UI.day ", UI.day)
            UI.day = 30
            UI.mounth -= 1
            UI.pushButton_DAYindex_plus = 0
        if UI.mounth == 8 and UI.day < 1:
            print("UI.year ", UI.year, " UI.mounth ", UI.mounth, " UI.day ", UI.day)
            UI.day = 31
            UI.mounth -= 1
            UI.pushButton_DAYindex_plus = 0
        if UI.mounth == 9 and UI.day < 1:
            print("UI.year ", UI.year, " UI.mounth ", UI.mounth, " UI.day ", UI.day)
            UI.day = 31
            UI.mounth -= 1
            UI.pushButton_DAYindex_plus = 0
        if UI.mounth == 10 and UI.day < 1:
            print("UI.year ", UI.year, " UI.mounth ", UI.mounth, " UI.day ", UI.day)
            UI.day = 30
            UI.mounth -= 1
            UI.pushButton_DAYindex_plus = 0
        if UI.mounth == 11 and UI.day < 1:
            print("UI.year ", UI.year, " UI.mounth ", UI.mounth, " UI.day ", UI.day)
            UI.day = 31
            UI.mounth -= 1
            UI.pushButton_DAYindex_plus = 0
        if UI.mounth == 12 and UI.day < 1:
            print("UI.year ", UI.year, " UI.mounth ", UI.mounth, " UI.day ", UI.day)
            UI.day = 30
            UI.mounth -= 1
            UI.pushButton_DAYindex_plus = 0
        self.label_4.setText(f"Дата выполнения проекта: {UI.day}.{UI.mounth}.{UI.year}  ({UI.pushButton_DAYindex} дней)")
    #Поле создания:создать заказ
    def HANDLER_MEN_pushButton_3(self):


        from client import CLIENT
        CLIENT.nomer_proecta = ""
        CLIENT.data_sozdaniya_proecta = ""

        CLIENT.imya_menedgera = ""

        CLIENT.name_of_organisation = ""
        CLIENT.elect_pochta_of_contact_face = ""
        CLIENT.number_time_for_end = ""

        CLIENT.INN = ""
        CLIENT.KPP = ""
        CLIENT.number_of_contact_face = ""
        CLIENT.name_of_contact_face = ""

        CLIENT.adress_of_organisation = ""
        CLIENT.oborudovanie = ""
        CLIENT.seriyniy_nomer = ""
        CLIENT.kodovoye_nazvanie = ""
        CLIENT.kolichestvo = ""
        CLIENT.edinitsy = ""
        CLIENT.nomer_sticker_plomby = ""
        CLIENT.komplektatia = ""
        CLIENT.opisanie_neispravnosti_ot_zakazchika = ""
        CLIENT.input_meh_destroy = ""

        CLIENT.status_remonta = ""
        CLIENT.dogovor_podpisan = ""

        CLIENT.otvet_na_zapros_sozdaniya = ""

        if "возвращаем первозданный цвет" == "возвращаем первозданный цвет":
            self.lineEdit_8.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                          "color: rgb(109, 65, 12);\n"
                                          "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit_21.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                           "color: rgb(109, 65, 12);\n"
                                           "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                        "color: rgb(109, 65, 12);\n"
                                        "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit_16.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                           "color: rgb(109, 65, 12);\n"
                                           "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit_2.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                          "color: rgb(109, 65, 12);\n"
                                          "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit_3.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                          "color: rgb(109, 65, 12);\n"
                                          "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit_4.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                          "color: rgb(109, 65, 12);\n"
                                          "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit_5.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                          "color: rgb(109, 65, 12);\n"
                                          "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit_6.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                          "color: rgb(109, 65, 12);\n"
                                          "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit_7.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                          "color: rgb(109, 65, 12);\n"
                                          "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit_22.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                           "color: rgb(109, 65, 12);\n"
                                           "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit_8.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                          "color: rgb(109, 65, 12);\n"
                                          "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit_9.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                          "color: rgb(109, 65, 12);\n"
                                          "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit_10.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                           "color: rgb(109, 65, 12);\n"
                                           "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit_11.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                           "color: rgb(109, 65, 12);\n"
                                           "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit_12.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                           "color: rgb(109, 65, 12);\n"
                                           "border: 1px solid rgb(109, 65, 12);")
            self.lineEdit_13.setStyleSheet("background-color: rgb(197, 147, 86);\n"
                                           "color: rgb(109, 65, 12);\n"
                                           "border: 1px solid rgb(109, 65, 12);")

        if self.lineEdit_21.text() == "":
            self.lineEdit_21.setFocus()
            self.lineEdit_21.setStyleSheet("background-color: rgb(220, 54, 20);\n"
                                           "color: rgb(109, 65, 12);\n"
                                           "border: 1px solid rgb(109, 65, 12);")
            self.pushButton_3.setStyleSheet("#pushButton_3\n"
                                            "{\n"
                                            "\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:hover\n"
                                            "{\n"
                                            "color: rgb(118, 91, 62);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:pressed\n"
                                            "{\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(197, 147, 86);\n"
                                            "border-radius: 5px;\n"
                                            "\n"
                                            "border-bottom: None;\n"
                                            "border-right: None;\n"
                                            "\n"
                                            "border-top: 3px solid rgb(98, 71, 50);\n"
                                            "border-left: 1px solid rgb(98, 71, 50);\n"
                                            "}    color: rgb(36, 21, 3);")
            return

        try:
            int(self.lineEdit_21.text())
            for n in UI.Zanyatie_imena_proectov:
                if int(self.lineEdit_21.text()) == int(n):
                    self.label_26.setText("")
                    self.label_26.show()
                    self.label_27.show()
                    self.pushButton_27.show()
                    font = QtGui.QFont()
                    font.setFamily("Arial")
                    font.setPointSize(6)
                    font.setItalic(True)
                    self.pushButton_27.setFont(font)
                    self.pushButton_27.setText("ИЗМЕНИТЬ")
                    self.pushButton_27.setStyleSheet("#pushButton_27\n"
                                                     "{\n"
                                                     "border: 1px solid rgb(109, 65, 12);\n"
                                                     "background-color: rgb(200, 155, 102);\n"
                                                     "}\n"
                                                     "#pushButton_27:hover\n"
                                                     "{\n"
                                                     "border: 1px solid rgb(109, 65, 12);\n"
                                                     "background-color: rgb(180, 135, 82);\n"
                                                     "}\n"
                                                     "#pushButton_27:pressed\n"
                                                     "{\n"
                                                     "border: 1px solid rgb(109, 65, 12);\n"
                                                     "background-color: rgb(200, 155, 102);\n"
                                                     "}\n"
                                                     )
                    self.pushButton_3.setStyleSheet("#pushButton_3\n"
                                                    "{\n"
                                                    "\n"
                                                    "    color: rgb(36, 21, 3);\n"
                                                    "background-color: rgb(220, 54, 20);\n"
                                                    "border-radius: 5px;\n"
                                                    "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                                    "border-right: 1px solid rgb(98, 71, 50);\n"
                                                    "}\n"
                                                    "\n"
                                                    "#pushButton_3:hover\n"
                                                    "{\n"
                                                    "color: rgb(118, 91, 62);\n"
                                                    "background-color: rgb(220, 54, 20);\n"
                                                    "border-radius: 5px;\n"
                                                    "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                                    "border-right: 1px solid rgb(98, 71, 50);\n"
                                                    "}\n"
                                                    "\n"
                                                    "#pushButton_3:pressed\n"
                                                    "{\n"
                                                    "    color: rgb(36, 21, 3);\n"
                                                    "background-color: rgb(197, 147, 86);\n"
                                                    "border-radius: 5px;\n"
                                                    "\n"
                                                    "border-bottom: None;\n"
                                                    "border-right: None;\n"
                                                    "\n"
                                                    "border-top: 3px solid rgb(98, 71, 50);\n"
                                                    "border-left: 1px solid rgb(98, 71, 50);\n"
                                                    "}    color: rgb(36, 21, 3);")
                    print("Имя занятоооооооооооооооооо")
                    return
        except:
            print("Не целочисленныйййййййййййййййййййй")
            self.label_26.show()
            self.label_27.show()
            self.pushButton_27.setText("ИЗМЕНИТЬ")
            self.label_27.setText("Не целочисленное число")
            self.label_26.setText("")
            self.pushButton_27.show()
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(8)
            font.setItalic(True)
            self.pushButton_27.setFont(font)
            self.pushButton_27.setStyleSheet("#pushButton_27\n"
                                             "{\n"
                                             "border: 1px solid rgb(109, 65, 12);\n"
                                             "background-color: rgb(200, 155, 102);\n"
                                             "}\n"
                                             "#pushButton_27:hover\n"
                                             "{\n"
                                             "border: 1px solid rgb(109, 65, 12);\n"
                                             "background-color: rgb(180, 135, 82);\n"
                                             "}\n"
                                             "#pushButton_27:pressed\n"
                                             "{\n"
                                             "border: 1px solid rgb(109, 65, 12);\n"
                                             "background-color: rgb(200, 155, 102);\n"
                                             "}\n"
                                             )
            self.pushButton_3.setStyleSheet("#pushButton_3\n"
                                            "{\n"
                                            "\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:hover\n"
                                            "{\n"
                                            "color: rgb(118, 91, 62);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:pressed\n"
                                            "{\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(197, 147, 86);\n"
                                            "border-radius: 5px;\n"
                                            "\n"
                                            "border-bottom: None;\n"
                                            "border-right: None;\n"
                                            "\n"
                                            "border-top: 3px solid rgb(98, 71, 50);\n"
                                            "border-left: 1px solid rgb(98, 71, 50);\n"
                                            "}    color: rgb(36, 21, 3);")
            return
        if self.lineEdit.text() == "":
            self.lineEdit.setFocus()
            self.lineEdit.setStyleSheet("background-color: rgb(220, 54, 20);\n"
                                        "color: rgb(109, 65, 12);\n"
                                        "border: 1px solid rgb(109, 65, 12);")
            self.pushButton_3.setStyleSheet("#pushButton_3\n"
                                            "{\n"
                                            "\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:hover\n"
                                            "{\n"
                                            "color: rgb(118, 91, 62);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:pressed\n"
                                            "{\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(197, 147, 86);\n"
                                            "border-radius: 5px;\n"
                                            "\n"
                                            "border-bottom: None;\n"
                                            "border-right: None;\n"
                                            "\n"
                                            "border-top: 3px solid rgb(98, 71, 50);\n"
                                            "border-left: 1px solid rgb(98, 71, 50);\n"
                                            "}    color: rgb(36, 21, 3);")
            return
        if self.lineEdit_16.text() == "":
            self.lineEdit_16.setFocus()
            self.lineEdit_16.setStyleSheet("background-color: rgb(220, 54, 20);\n"
                                           "color: rgb(109, 65, 12);\n"
                                           "border: 1px solid rgb(109, 65, 12);")
            self.pushButton_3.setStyleSheet("#pushButton_3\n"
                                            "{\n"
                                            "\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:hover\n"
                                            "{\n"
                                            "color: rgb(118, 91, 62);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:pressed\n"
                                            "{\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(197, 147, 86);\n"
                                            "border-radius: 5px;\n"
                                            "\n"
                                            "border-bottom: None;\n"
                                            "border-right: None;\n"
                                            "\n"
                                            "border-top: 3px solid rgb(98, 71, 50);\n"
                                            "border-left: 1px solid rgb(98, 71, 50);\n"
                                            "}    color: rgb(36, 21, 3);")
            return
        if self.lineEdit_2.text() == "":
            self.lineEdit_2.setFocus()
            self.lineEdit_2.setStyleSheet("background-color: rgb(220, 54, 20);\n"
                                          "color: rgb(109, 65, 12);\n"
                                          "border: 1px solid rgb(109, 65, 12);")
            self.pushButton_3.setStyleSheet("#pushButton_3\n"
                                            "{\n"
                                            "\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:hover\n"
                                            "{\n"
                                            "color: rgb(118, 91, 62);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:pressed\n"
                                            "{\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(197, 147, 86);\n"
                                            "border-radius: 5px;\n"
                                            "\n"
                                            "border-bottom: None;\n"
                                            "border-right: None;\n"
                                            "\n"
                                            "border-top: 3px solid rgb(98, 71, 50);\n"
                                            "border-left: 1px solid rgb(98, 71, 50);\n"
                                            "}    color: rgb(36, 21, 3);")
            return
        if self.lineEdit_3.text() == "":
            self.lineEdit_3.setFocus()
            self.lineEdit_3.setStyleSheet("background-color: rgb(220, 54, 20);\n"
                                          "color: rgb(109, 65, 12);\n"
                                          "border: 1px solid rgb(109, 65, 12);")
            self.pushButton_3.setStyleSheet("#pushButton_3\n"
                                            "{\n"
                                            "\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:hover\n"
                                            "{\n"
                                            "color: rgb(118, 91, 62);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:pressed\n"
                                            "{\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(197, 147, 86);\n"
                                            "border-radius: 5px;\n"
                                            "\n"
                                            "border-bottom: None;\n"
                                            "border-right: None;\n"
                                            "\n"
                                            "border-top: 3px solid rgb(98, 71, 50);\n"
                                            "border-left: 1px solid rgb(98, 71, 50);\n"
                                            "}    color: rgb(36, 21, 3);")
            return
        if self.lineEdit_4.text() == "":
            self.lineEdit_4.setFocus()
            self.lineEdit_4.setStyleSheet("background-color: rgb(220, 54, 20);\n"
                                          "color: rgb(109, 65, 12);\n"
                                          "border: 1px solid rgb(109, 65, 12);")
            self.pushButton_3.setStyleSheet("#pushButton_3\n"
                                            "{\n"
                                            "\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:hover\n"
                                            "{\n"
                                            "color: rgb(118, 91, 62);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:pressed\n"
                                            "{\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(197, 147, 86);\n"
                                            "border-radius: 5px;\n"
                                            "\n"
                                            "border-bottom: None;\n"
                                            "border-right: None;\n"
                                            "\n"
                                            "border-top: 3px solid rgb(98, 71, 50);\n"
                                            "border-left: 1px solid rgb(98, 71, 50);\n"
                                            "}    color: rgb(36, 21, 3);")
            return
        if self.lineEdit_5.text() == "Как обращаться" or self.lineEdit_5.text() == "":
            self.lineEdit_5.setFocus()
            self.lineEdit_5.setStyleSheet("background-color: rgb(220, 54, 20);\n"
                                          "color: rgb(109, 65, 12);\n"
                                          "border: 1px solid rgb(109, 65, 12);")
            self.pushButton_3.setStyleSheet("#pushButton_3\n"
                                            "{\n"
                                            "\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:hover\n"
                                            "{\n"
                                            "color: rgb(118, 91, 62);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:pressed\n"
                                            "{\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(197, 147, 86);\n"
                                            "border-radius: 5px;\n"
                                            "\n"
                                            "border-bottom: None;\n"
                                            "border-right: None;\n"
                                            "\n"
                                            "border-top: 3px solid rgb(98, 71, 50);\n"
                                            "border-left: 1px solid rgb(98, 71, 50);\n"
                                            "}    color: rgb(36, 21, 3);")
            return
        if self.lineEdit_6.text() == "Страна" or self.lineEdit_6.text() == "":
            self.lineEdit_6.setFocus()
            self.lineEdit_6.setStyleSheet("background-color: rgb(220, 54, 20);\n"
                                          "color: rgb(109, 65, 12);\n"
                                          "border: 1px solid rgb(109, 65, 12);")
            self.pushButton_3.setStyleSheet("#pushButton_3\n"
                                            "{\n"
                                            "\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:hover\n"
                                            "{\n"
                                            "color: rgb(118, 91, 62);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:pressed\n"
                                            "{\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(197, 147, 86);\n"
                                            "border-radius: 5px;\n"
                                            "\n"
                                            "border-bottom: None;\n"
                                            "border-right: None;\n"
                                            "\n"
                                            "border-top: 3px solid rgb(98, 71, 50);\n"
                                            "border-left: 1px solid rgb(98, 71, 50);\n"
                                            "}    color: rgb(36, 21, 3);")
            return
        if self.lineEdit_7.text() == "Город" or self.lineEdit_7.text() == "":
            self.lineEdit_7.setFocus()
            self.lineEdit_7.setStyleSheet("background-color: rgb(220, 54, 20);\n"
                                          "color: rgb(109, 65, 12);\n"
                                          "border: 1px solid rgb(109, 65, 12);")
            self.pushButton_3.setStyleSheet("#pushButton_3\n"
                                            "{\n"
                                            "\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:hover\n"
                                            "{\n"
                                            "color: rgb(118, 91, 62);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:pressed\n"
                                            "{\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(197, 147, 86);\n"
                                            "border-radius: 5px;\n"
                                            "\n"
                                            "border-bottom: None;\n"
                                            "border-right: None;\n"
                                            "\n"
                                            "border-top: 3px solid rgb(98, 71, 50);\n"
                                            "border-left: 1px solid rgb(98, 71, 50);\n"
                                            "}    color: rgb(36, 21, 3);")
            return
        if self.lineEdit_22.text() == "Улица" or self.lineEdit_22.text() == "":
            self.lineEdit_22.setFocus()
            self.lineEdit_22.setStyleSheet("background-color: rgb(220, 54, 20);\n"
                                           "color: rgb(109, 65, 12);\n"
                                           "border: 1px solid rgb(109, 65, 12);")
            self.pushButton_3.setStyleSheet("#pushButton_3\n"
                                            "{\n"
                                            "\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:hover\n"
                                            "{\n"
                                            "color: rgb(118, 91, 62);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:pressed\n"
                                            "{\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(197, 147, 86);\n"
                                            "border-radius: 5px;\n"
                                            "\n"
                                            "border-bottom: None;\n"
                                            "border-right: None;\n"
                                            "\n"
                                            "border-top: 3px solid rgb(98, 71, 50);\n"
                                            "border-left: 1px solid rgb(98, 71, 50);\n"
                                            "}    color: rgb(36, 21, 3);")
            return
        if self.lineEdit_8.text() == "Дом" or self.lineEdit_8.text() == "":
            self.lineEdit_8.setFocus()
            self.lineEdit_8.setStyleSheet("background-color: rgb(220, 54, 20);\n"
                                          "color: rgb(109, 65, 12);\n"
                                          "border: 1px solid rgb(109, 65, 12);")
            self.pushButton_3.setStyleSheet("#pushButton_3\n"
                                            "{\n"
                                            "\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:hover\n"
                                            "{\n"
                                            "color: rgb(118, 91, 62);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:pressed\n"
                                            "{\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(197, 147, 86);\n"
                                            "border-radius: 5px;\n"
                                            "\n"
                                            "border-bottom: None;\n"
                                            "border-right: None;\n"
                                            "\n"
                                            "border-top: 3px solid rgb(98, 71, 50);\n"
                                            "border-left: 1px solid rgb(98, 71, 50);\n"
                                            "}    color: rgb(36, 21, 3);"
                                            )
            return
        if self.lineEdit_9.text() == "№" or self.lineEdit_9.text() == "":
            self.lineEdit_9.setFocus()
            self.lineEdit_9.setStyleSheet("background-color: rgb(220, 54, 20);\n"
                                          "color: rgb(109, 65, 12);\n"
                                          "border: 1px solid rgb(109, 65, 12);")
            self.pushButton_3.setStyleSheet("#pushButton_3\n"
                                            "{\n"
                                            "\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:hover\n"
                                            "{\n"
                                            "color: rgb(118, 91, 62);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:pressed\n"
                                            "{\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(197, 147, 86);\n"
                                            "border-radius: 5px;\n"
                                            "\n"
                                            "border-bottom: None;\n"
                                            "border-right: None;\n"
                                            "\n"
                                            "border-top: 3px solid rgb(98, 71, 50);\n"
                                            "border-left: 1px solid rgb(98, 71, 50);\n"
                                            "}    color: rgb(36, 21, 3);")
            return
        if self.lineEdit_10.text() == "":
            self.lineEdit_10.setFocus()
            self.lineEdit_10.setStyleSheet("background-color: rgb(220, 54, 20);\n"
                                           "color: rgb(109, 65, 12);\n"
                                           "border: 1px solid rgb(109, 65, 12);")
            self.pushButton_3.setStyleSheet("#pushButton_3\n"
                                            "{\n"
                                            "\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:hover\n"
                                            "{\n"
                                            "color: rgb(118, 91, 62);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:pressed\n"
                                            "{\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(197, 147, 86);\n"
                                            "border-radius: 5px;\n"
                                            "\n"
                                            "border-bottom: None;\n"
                                            "border-right: None;\n"
                                            "\n"
                                            "border-top: 3px solid rgb(98, 71, 50);\n"
                                            "border-left: 1px solid rgb(98, 71, 50);\n"
                                            "}    color: rgb(36, 21, 3);")
            return
        if self.lineEdit_11.text() == "":
            self.lineEdit_11.setFocus()
            self.lineEdit_11.setStyleSheet("background-color: rgb(220, 54, 20);\n"
                                           "color: rgb(109, 65, 12);\n"
                                           "border: 1px solid rgb(109, 65, 12);")
            self.pushButton_3.setStyleSheet("#pushButton_3\n"
                                            "{\n"
                                            "\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:hover\n"
                                            "{\n"
                                            "color: rgb(118, 91, 62);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:pressed\n"
                                            "{\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(197, 147, 86);\n"
                                            "border-radius: 5px;\n"
                                            "\n"
                                            "border-bottom: None;\n"
                                            "border-right: None;\n"
                                            "\n"
                                            "border-top: 3px solid rgb(98, 71, 50);\n"
                                            "border-left: 1px solid rgb(98, 71, 50);\n"
                                            "}    color: rgb(36, 21, 3);")
            return
        if self.lineEdit_13.text() == "":
            self.lineEdit_13.setFocus()
            self.lineEdit_13.setStyleSheet("background-color: rgb(220, 54, 20);\n"
                                           "color: rgb(109, 65, 12);\n"
                                           "border: 1px solid rgb(109, 65, 12);")
            self.pushButton_3.setStyleSheet("#pushButton_3\n"
                                            "{\n"
                                            "\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:hover\n"
                                            "{\n"
                                            "color: rgb(118, 91, 62);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:pressed\n"
                                            "{\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(197, 147, 86);\n"
                                            "border-radius: 5px;\n"
                                            "\n"
                                            "border-bottom: None;\n"
                                            "border-right: None;\n"
                                            "\n"
                                            "border-top: 3px solid rgb(98, 71, 50);\n"
                                            "border-left: 1px solid rgb(98, 71, 50);\n"
                                            "}    color: rgb(36, 21, 3);")
            return
        if self.lineEdit_14.text() == "":
            self.lineEdit_14.setFocus()
            self.lineEdit_14.setStyleSheet("background-color: rgb(220, 54, 20);\n"
                                           "color: rgb(109, 65, 12);\n"
                                           "border: 1px solid rgb(109, 65, 12);")
            self.pushButton_3.setStyleSheet("#pushButton_3\n"
                                            "{\n"
                                            "\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:hover\n"
                                            "{\n"
                                            "color: rgb(118, 91, 62);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:pressed\n"
                                            "{\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(197, 147, 86);\n"
                                            "border-radius: 5px;\n"
                                            "\n"
                                            "border-bottom: None;\n"
                                            "border-right: None;\n"
                                            "\n"
                                            "border-top: 3px solid rgb(98, 71, 50);\n"
                                            "border-left: 1px solid rgb(98, 71, 50);\n"
                                            "}    color: rgb(36, 21, 3);")
            return
        if self.textEdit.toPlainText() == "":
            self.textEdit.setFocus()
            self.textEdit.setStyleSheet("background-color: rgb(220, 54, 20);\n"
                                        "color: rgb(109, 65, 12);\n"
                                        "border: 1px solid rgb(109, 65, 12);")
            self.pushButton_3.setStyleSheet("#pushButton_3\n"
                                            "{\n"
                                            "\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:hover\n"
                                            "{\n"
                                            "color: rgb(118, 91, 62);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:pressed\n"
                                            "{\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(197, 147, 86);\n"
                                            "border-radius: 5px;\n"
                                            "\n"
                                            "border-bottom: None;\n"
                                            "border-right: None;\n"
                                            "\n"
                                            "border-top: 3px solid rgb(98, 71, 50);\n"
                                            "border-left: 1px solid rgb(98, 71, 50);\n"
                                            "}    color: rgb(36, 21, 3);")
            return
        if self.textEdit_3.toPlainText() == "":
            self.textEdit_3.setFocus()
            self.textEdit_3.setStyleSheet("background-color: rgb(220, 54, 20);\n"
                                          "color: rgb(109, 65, 12);\n"
                                          "border: 1px solid rgb(109, 65, 12);")
            self.pushButton_3.setStyleSheet("#pushButton_3\n"
                                            "{\n"
                                            "\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:hover\n"
                                            "{\n"
                                            "color: rgb(118, 91, 62);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:pressed\n"
                                            "{\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(197, 147, 86);\n"
                                            "border-radius: 5px;\n"
                                            "\n"
                                            "border-bottom: None;\n"
                                            "border-right: None;\n"
                                            "\n"
                                            "border-top: 3px solid rgb(98, 71, 50);\n"
                                            "border-left: 1px solid rgb(98, 71, 50);\n"
                                            "}    color: rgb(36, 21, 3);")
            return
        if self.textEdit_4.toPlainText() == "":
            self.textEdit_4.setFocus()
            self.textEdit_4.setStyleSheet("background-color: rgb(220, 54, 20);\n"
                                          "color: rgb(109, 65, 12);\n"
                                          "border: 1px solid rgb(109, 65, 12);")
            self.pushButton_3.setStyleSheet("#pushButton_3\n"
                                            "{\n"
                                            "\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:hover\n"
                                            "{\n"
                                            "color: rgb(118, 91, 62);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_3:pressed\n"
                                            "{\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(197, 147, 86);\n"
                                            "border-radius: 5px;\n"
                                            "\n"
                                            "border-bottom: None;\n"
                                            "border-right: None;\n"
                                            "\n"
                                            "border-top: 3px solid rgb(98, 71, 50);\n"
                                            "border-left: 1px solid rgb(98, 71, 50);\n"
                                            "}    color: rgb(36, 21, 3);")
            return

        print("Begin save new project...")

        from client import CLIENT
        lend = len(str(self.lineEdit_21.text()))
        text = ""
        if lend == 1:
            text = "00000" + str(self.lineEdit_21.text())
            self.lineEdit_21.setText(text)
        if lend == 2:
            text = "0000" + str(self.lineEdit_21.text())
            self.lineEdit_21.setText(text)
        if lend == 3:
            text = "000" + str(self.lineEdit_21.text())
            self.lineEdit_21.setText(text)
        if lend == 4:
            text = "00" + str(self.lineEdit_21.text())
            self.lineEdit_21.setText(text)
        if lend == 5:
            text = "0" + str(self.lineEdit_21.text())
            self.lineEdit_21.setText(text)

        CLIENT.nomer_proecta = self.lineEdit_21.text()


        d = self.spinBox_2.text()
        m = self.spinBox_3.text()
        y = self.spinBox_4.text()
        if str(d) == "0":
            import datetime
            now = str(datetime.datetime.now())
            d = now[8:10]
        if str(m) == "0":
            import datetime
            now = str(datetime.datetime.now())
            m = now[5:7]
        if str(y) == "0":
            import datetime
            now = str(datetime.datetime.now())
            y = now[0:4]
        CLIENT.data_sozdaniya_proecta = d +"."+m+"."+y

        CLIENT.imya_menedgera = CLIENT.pravilnost_parola

        CLIENT.name_of_organisation = self.comboBox.currentText() +' "'+self.lineEdit.text()+'"'

        # if "checkBox_3 == 1"=="checkBox_3 == 1":
        if self.checkBox_3.checkState():
            CLIENT.elect_pochta_of_contact_face = self.lineEdit_16.text() + self.comboBox_4.currentText()
        else:
            CLIENT.elect_pochta_of_contact_face = self.lineEdit_16.text()


        CLIENT.number_time_for_end = str(UI.day) + "." + str(UI.mounth) + "." + str(UI.year)

        CLIENT.INN = self.lineEdit_2.text()
        CLIENT.KPP = self.lineEdit_3.text()
        CLIENT.number_of_contact_face = self.lineEdit_4.text()
        if self.lineEdit_5.text() == "Как обращаться":
            self.lineEdit_5.setText("")
        CLIENT.name_of_contact_face = self.lineEdit_5.text()
        CLIENT.adress_of_organisation = \
            "с."+self.lineEdit_6.text()+ \
            " г."+self.lineEdit_7.text()+" ул."+self.lineEdit_22.text()+" "+self.comboBox_2.currentText()+self.lineEdit_9.text()
        from translater import TRANSLATE
        TRANSLATE.into_str = CLIENT.adress_of_organisation
        TRANSLATE.out_str = ""
        TRANSLATE.rus_in_eng()
        CLIENT.adress_of_organisation = TRANSLATE.out_str
        CLIENT.oborudovanie = self.lineEdit_10.text()
        CLIENT.seriyniy_nomer = self.lineEdit_11.text()
        CLIENT.kodovoye_nazvanie = self.lineEdit_12.text()
        CLIENT.kolichestvo = self.lineEdit_13.text()
        CLIENT.edinitsy = self.lineEdit_14.text()
        CLIENT.nomer_sticker_plomby = self.lineEdit_15.text()
        CLIENT.komplektatia = self.textEdit.toPlainText()
        # CLIENT.komplektatia.replace("\n", "?", 1000)

        input_text = CLIENT.komplektatia
        output_text = ""
        output_text_mas = []
        output_text_mas2 = []
        output_text_buf = ""
        div_el = "\n"
        counter = 0
        try:
            output_text += "-  "
            while True:
                print("input_text[counter].в аписывателе в переменную", input_text[counter])
                if input_text[counter] != div_el:
                    output_text_buf += input_text[counter]
                else:
                    output_text_mas.append(output_text_buf)
                    output_text_buf = ""
                    # counter += 1
                counter += 1
        except:
            output_text_mas.append(output_text_buf)
            output_text_buf = ""
            print("FFFFuck.в аписывателе в переменную")
        print("output_text_mas:.в аписывателе в переменную ", output_text_mas)
        CLIENT.komplektatia = ""
        for ij in output_text_mas:
            CLIENT.komplektatia += ij
            CLIENT.komplektatia += ";"

        CLIENT.opisanie_neispravnosti_ot_zakazchika = self.textEdit_3.toPlainText()
        input_text = CLIENT.opisanie_neispravnosti_ot_zakazchika
        output_text = ""
        output_text_mas = []
        output_text_mas2 = []
        output_text_buf = ""
        div_el = "\n"
        counter = 0
        try:
            output_text += "-  "
            while True:
                print("input_text[counter].в аписывателе в переменную", input_text[counter])
                if input_text[counter] != div_el:
                    output_text_buf += input_text[counter]
                else:
                    output_text_mas.append(output_text_buf)
                    output_text_buf = ""
                    # counter += 1
                counter += 1
        except:
            output_text_mas.append(output_text_buf)
            output_text_buf = ""
            print("FFFFuck.в аписывателе в переменную")
        print("output_text_mas:.в аписывателе в переменную ", output_text_mas)
        CLIENT.opisanie_neispravnosti_ot_zakazchika = ""
        for ij in output_text_mas:
            CLIENT.opisanie_neispravnosti_ot_zakazchika += ij
            CLIENT.opisanie_neispravnosti_ot_zakazchika += ";"

        CLIENT.input_meh_destroy = self.textEdit_4.toPlainText()
        input_text = CLIENT.input_meh_destroy
        output_text = ""
        output_text_mas = []
        output_text_mas2 = []
        output_text_buf = ""
        div_el = "\n"
        counter = 0
        try:
            output_text += "-  "
            while True:
                print("input_text[counter].в аписывателе в переменную", input_text[counter])
                if input_text[counter] != div_el:
                    output_text_buf += input_text[counter]
                else:
                    output_text_mas.append(output_text_buf)
                    output_text_buf = ""
                    # counter += 1
                counter += 1
        except:
            output_text_mas.append(output_text_buf)

            output_text_buf = ""
            print("FFFFuck.в аписывателе в переменную")
        print("output_text_mas:.в аписывателе в переменную ", output_text_mas)
        CLIENT.input_meh_destroy = ""
        for ij in output_text_mas:
            CLIENT.input_meh_destroy += ij
            CLIENT.input_meh_destroy += ";"

        CLIENT.status_remonta = self.comboBox_3.currentText()
        if self.checkBox_2.checkState():
            CLIENT.dogovor_podpisan = "Da"
        else:
            CLIENT.dogovor_podpisan = "Net"
        print("New proj")
        try:
            CLIENT.create_new_project()
        except:
            print("что-то пошло не так")
        if CLIENT.otvet_na_zapros_sozdaniya == "okok":
            print("Проект удачно создан")
            self.pushButton_32.hide()
            self.stackedWidget.setCurrentIndex(1)
            self.stackedWidget_2.setCurrentIndex(0)
        if CLIENT.otvet_na_zapros_sozdaniya == "non_full_pocket":
            print("Проект не создан: Не полная посылка")

    def HANDLER_MEN_pushButton_27(self):
        self.label_26.hide()
        self.label_27.hide()
        self.pushButton_27.hide()
        i = 1
        flagss = 0
        while True:
            print("i: ",i)
            len_mas_of_fileName = len(UI.Zanyatie_imena_proectov)
            counter_sovpadeniy = 0
            for n in UI.Zanyatie_imena_proectov:
                print("int(n) ",int(n))
                if i == int(n):
                    counter_sovpadeniy += 1
            if counter_sovpadeniy == 0:
                lend = len(str(i))
                text = ""
                if lend == 1:
                    text = "00000"+str(i)
                if lend == 2:
                    text = "0000"+str(i)
                if lend == 3:
                    text = "000"+str(i)
                if lend == 4:
                    text = "00"+str(i)
                if lend == 5:
                    text = "0"+str(i)

                self.lineEdit_21.setText(text)
                return
            i +=1



    #Поле создания: добавить к комплектации "штуки"
    p = []
    def HANDLER_MEN_pushButton_36(self):
        input_text = self.textEdit.toPlainText()
        output_text = ""
        print("99999999999999999999999999999999999999999999")
        print("UI.p begin:", UI.p)
        output_text_mas = UI.p
        output_text_mas2 = []
        output_text_buf = ""
        div_el = "\n"
        counter = 0
        try:
            output_text += "-  "
            while True:
                print("input_text[counter]",input_text[counter])
                if input_text[counter] != div_el:
                    output_text_buf += input_text[counter]
                else:
                    output_text_mas.append(output_text_buf)
                    output_text_buf = ""
                    # counter += 1
                counter += 1
        except:
            output_text_mas.append(output_text_buf)
            output_text_buf = ""
            print("FFFFuck")
        print("output_text_mas:", output_text_mas)

        for i in output_text_mas:
            if i !="":
                if i[0] != "-":
                    output_text_buf = ""
                    output_text_buf += "- "
                    output_text_buf += i
                    output_text_buf += " 1 шт."
                    output_text_mas2.append(output_text_buf)
                else:
                    print(i," - loaded str")
        print("output_text_mas2:", output_text_mas2)
        str = ""
        for i in output_text_mas2:
            str += i
            str += "\n"
        UI.p += output_text_mas2
        print("UI.p end:", UI.p)
        self.textEdit.setText(str.strip())

    #Элементы для диагностики
    # plus
    def HANDLER_MEN_pushButton_59(self):
        from ui_add_new_elements import widget_11
        widget_11.add_new_string(self)
    # minus
    def HANDLER_MEN_pushButton_101(self):
        from ui_add_new_elements import widget_11
        widget_11.del_last_string(self)

    #Сопутствующие расходы (транспорт и тп)
    #plus
    def HANDLER_MEN_pushButton_102(self):
        from ui_add_new_elements import widget_12
        widget_12.add_new_string(self)
    # minus
    def HANDLER_MEN_pushButton_103(self):
        from ui_add_new_elements import widget_12
        widget_12.del_last_string(self)

    # Элементы для ремонта
    # plus
    def HANDLER_MEN_pushButton_106(self):
        from ui_add_new_elements import widget_14
        widget_14.add_new_string(self)
    # minus
    def HANDLER_MEN_pushButton_107(self):
        from ui_add_new_elements import widget_14
        widget_14.del_last_string(self)

    # Незапланированные расходы
    # plus
    def HANDLER_MEN_pushButton_108(self):
        from ui_add_new_elements import widget_15
        widget_15.add_new_string(self)
    # minus
    def HANDLER_MEN_pushButton_112(self):
        from ui_add_new_elements import widget_15
        widget_15.del_last_string(self)

    def HANDLER_MEN_pushButton_39(self):
        print(self.pushButton_50.text())
        if self.pushButton_50.text() == "ПОДТВЕРДИТЬ":
            self.pushButton_50.setEnabled(True)
            self.pushButton_50.setText("Подтверждаю")
            self.pushButton_50.setStyleSheet("#pushButton_50\n"
                                             "{\n"
                                             "color: rgb(98, 71, 42);\n"
                                             # "    color: rgb(183, 143, 97);\n"
                                             "background-color: rgb(197, 147, 86);\n"
                                             "border-radius: 5px;\n"
                                             "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                             "border-right: 1px solid rgb(98, 71, 50);\n"
                                             "}\n"
                                             "\n"
                                             "#pushButton_50:hover\n"
                                             "{\n"
                                             "color: rgb(118, 91, 62);\n"
                                             "background-color: rgb(177, 127, 66);\n"
                                             "border-radius: 5px;\n"
                                             "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                             "border-right: 1px solid rgb(98, 71, 50);\n"
                                             "}\n"
                                             "\n"
                                             "#pushButton_50:pressed\n"
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
        else:
            self.pushButton_50.setDisabled(False)
            self.pushButton_50.setText("ПОДТВЕРДИТЬ")
            self.pushButton_50.setStyleSheet("#pushButton_50\n"
                                             "{\n"
                                             # "color: rgb(98, 71, 42);\n"
                                             "    color: rgb(183, 143, 97);\n"
                                             "background-color: rgb(197, 147, 86);\n"
                                             "border-radius: 5px;\n"
                                             "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                             "border-right: 1px solid rgb(98, 71, 50);\n"
                                             "}\n"
                                             "\n"
                                             "#pushButton_50:hover\n"
                                             "{\n"
                                             "color: rgb(118, 91, 62);\n"
                                             "background-color: rgb(177, 127, 66);\n"
                                             "border-radius: 5px;\n"
                                             "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                             "border-right: 1px solid rgb(98, 71, 50);\n"
                                             "}\n"
                                             "\n"
                                             "#pushButton_50:pressed\n"
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

    def HANDLER_MEN_pushButton_50(self):
        self.lineEdit.clear()
        self.lineEdit_16.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()
        self.lineEdit_9.clear()
        self.lineEdit_10.clear()
        self.lineEdit_11.clear()
        self.lineEdit_12.clear()
        self.lineEdit_13.clear()
        self.lineEdit_14.clear()
        self.lineEdit_15.clear()

        self.textEdit.clear()
        self.textEdit_3.clear()
        self.textEdit_4.clear()


        # self.checkBox.click()
        # self.checkBox_2.clear()
        # self.checkBox_3.clear()

        # self.checkBox.
        self.lineEdit.clear()
        self.lineEdit.clear()
        self.lineEdit.clear()
        self.lineEdit.clear()



        self.stackedWidget.setCurrentIndex(0)
        self.pushButton_50.setText("ПОДТВЕРДИТЬ")
        self.pushButton_50.setDisabled(True)
        self.pushButton_50.setStyleSheet("#pushButton_50\n"
                                         "{\n"
                                         # "color: rgb(98, 71, 42);\n"
                                         "    color: rgb(183, 143, 97);\n"
                                         "background-color: rgb(197, 147, 86);\n"
                                         "border-radius: 5px;\n"
                                         "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                         "border-right: 1px solid rgb(98, 71, 50);\n"
                                         "}\n"
                                         "\n"
                                         "#pushButton_50:hover\n"
                                         "{\n"
                                         "    color: rgb(183, 143, 97);\n"
                                         "background-color: rgb(197, 147, 86);\n"
                                         "border-radius: 5px;\n"
                                         "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                         "border-right: 1px solid rgb(98, 71, 50);\n"
                                         "}\n"
                                         "\n"
                                         "#pushButton_50:pressed\n"
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
    # внутри проекта: кнопка акнкеты прокета
    def HANDLER_MEN_pushButton_28(self):
        self.pushButton_27.hide()
        self.label_26.hide()
        self.label_27.hide()
        self.label_263.hide()
        self.label_237.hide()

        from ui_add_new_elements import widget_begin
        txt = f"../pythonProject3/DATABASE/current_project/_" + widget_begin.zakaz_nomer.strip() +".txt"
        self.lineEdit_21.setText(widget_begin.zakaz_nomer.strip())
        with open(txt, 'r') as file:
            for index, line in enumerate(file):
                # print("123",type(index), index, line)
                if index == 0:
                    k = line.strip()
                    self.spinBox_2.setSpecialValueText(k[0:2])
                    self.spinBox_3.setSpecialValueText(k[3:5])
                    self.spinBox_4.setSpecialValueText(k[6:10])
                if index == 1:
                    k = "Имя менеджера: "+ line.strip()
                    self.label_19.setText(k)
                if index == 2:
                    self.lineEdit.setText(line.strip())
                if index == 3:
                    self.lineEdit_16.setText(line.strip())
                if index == 4:
                    data_konca = "Дата выполнения проекта: "+line.strip()
                    self.label_4.setText(data_konca)
                if index == 5:
                    self.lineEdit_2.setText(line.strip())
                if index == 6:
                    self.lineEdit_3.setText(line.strip())
                if index == 7:
                    self.lineEdit_4.setText(line.strip())
                if index == 8:
                    self.lineEdit_5.setText(line.strip())
                if index == 9:
                    self.lineEdit_23.show()
                    from translater import TRANSLATE
                    TRANSLATE.out_str = ""
                    TRANSLATE.into_str = line.strip()
                    TRANSLATE.eng_in_rus()
                    self.lineEdit_23.setText(TRANSLATE.out_str)
                if index == 10:
                    self.lineEdit_10.setText(line.strip())
                if index == 11:
                    self.lineEdit_11.setText(line.strip())
                if index == 12:
                    self.lineEdit_12.setText(line.strip())
                if index == 13:
                    self.lineEdit_13.setText(line.strip())
                if index == 14:
                    self.lineEdit_14.setText(line.strip())
                if index == 15:
                    self.lineEdit_15.setText(line.strip())
                if index == 16:
                    #комплектация
                    f = ""
                    for i in line.strip():
                        if i != ";":
                            f += i
                        else:
                            f+= i
                            f += '\n'
                    self.textEdit.setText(f)
                if index == 17:
                    # комплектация
                    f = ""
                    for i in line.strip():
                        if i != ";":
                            f += i
                        else:
                            f += i
                            f += '\n'
                    self.textEdit_3.setText(f)
                if index == 18:
                    # комплектация
                    f = ""
                    for i in line.strip():
                        if i != ";":
                            f += i
                        else:
                            f += i
                            f += '\n'
                    self.textEdit_4.setText(f)
                if index == 19:
                    self.comboBox_3.addItem(line.strip())
                    self.comboBox_3.setCurrentText(line.strip())
                if index == 20:
                    print("aaxy",line.strip(),self.checkBox_2.isChecked())
                    if line.strip() == "Da":
                        self.checkBox_2.click()
                    else:
                        self.checkBox_2.isChecked(False)
                    print("aaxy")
                if index == 21:
                    from translater import TRANSLATE
                    TRANSLATE.out_str = ""
                    TRANSLATE.into_str = line.strip()
                    TRANSLATE.eng_in_rus()
                    llop = "Имя менеджера: " + TRANSLATE.out_str
                    self.label_19.setText(llop)
        self.lineEdit_21.setDisabled(True)
        self.lineEdit_22.setDisabled(True)
        self.spinBox_2.setDisabled(True)
        self.spinBox_3.setDisabled(True)
        self.spinBox_4.setDisabled(True)
        self.pushButton_36.setDisabled(True)
        self.checkBox_2.setDisabled(True)
        self.comboBox_3.setDisabled(True)
        self.pushButton_3.setDisabled(True)
        self.checkBox.setDisabled(True)
        print("159-456")
        self.comboBox_2.setDisabled(True)
        self.comboBox_2.hide()

        self.lineEdit.setDisabled(True)
        self.lineEdit_16.setDisabled(True)
        self.lineEdit_2.setDisabled(True)
        self.lineEdit_3.setDisabled(True)
        self.lineEdit_4.setDisabled(True)
        self.lineEdit_5.setDisabled(True)
        print("lll56")
        self.lineEdit_6.setDisabled(True)
        self.lineEdit_7.setDisabled(True)
        self.lineEdit_8.setDisabled(True)
        self.lineEdit_9.setDisabled(True)
        self.lineEdit_10.setDisabled(True)
        self.lineEdit_11.setDisabled(True)
        self.lineEdit_12.setDisabled(True)
        self.lineEdit_13.setDisabled(True)
        self.lineEdit_14.setDisabled(True)
        self.lineEdit_15.setDisabled(True)

        self.textEdit.setDisabled(True)
        self.textEdit_3.setDisabled(True)
        self.textEdit_4.setDisabled(True)

        self.lineEdit_21.setDisabled(True)
        self.lineEdit_22.setDisabled(True)
        self.spinBox_2.setDisabled(True)
        self.spinBox_3.setDisabled(True)
        self.spinBox_4.setDisabled(True)
        self.pushButton_36.setDisabled(True)
        self.checkBox_2.setDisabled(True)
        self.comboBox_3.setDisabled(True)
        self.pushButton_3.setDisabled(True)
        self.checkBox.setDisabled(True)

        self.comboBox_2.setDisabled(True)
        self.lineEdit.setDisabled(True)
        self.lineEdit_16.setDisabled(True)
        self.lineEdit_2.setDisabled(True)
        self.lineEdit_3.setDisabled(True)
        self.lineEdit_4.setDisabled(True)
        self.lineEdit_5.setDisabled(True)
        print("lll56")
        self.lineEdit_6.setDisabled(True)
        self.lineEdit_7.setDisabled(True)
        self.lineEdit_8.setDisabled(True)
        self.lineEdit_9.setDisabled(True)
        self.lineEdit_10.setDisabled(True)
        self.lineEdit_11.setDisabled(True)
        self.lineEdit_12.setDisabled(True)
        self.lineEdit_13.setDisabled(True)
        self.lineEdit_14.setDisabled(True)
        self.lineEdit_15.setDisabled(True)

        self.textEdit.setDisabled(True)
        self.textEdit_3.setDisabled(True)
        self.textEdit_4.setDisabled(True)
        # self.checkBox.set
        self.stackedWidget.setCurrentIndex(0)
    # внутри проекта: кнопка экспорта проета
    def HANDLER_MEN_pushButton_51(self):
        self.lineEdit_20.hide()
        self.label_319.hide()

        self.checkBox_22.hide()
        self.checkBox_27.hide()
        self.checkBox_29.hide()

        self.pushButton_104.move(190,400)
        self.pushButton_115.move(540,400)
        self.pushButton_104.setDisabled(True)
        p = "C:/Users/user/Desktop/ "
        from ui_add_new_elements import  widget_begin
        p = p.strip() + widget_begin.zakaz_nomer
        self.lineEdit_20.setText(p.strip())

        self.stackedWidget.setCurrentIndex(6)
    #экспорт проекта: чекбокс  подтверждения эекспорта
    flag_podtverzdayu_28 = 0
    def HANDLER_MEN_checkBox_28(self):
        if UI.flag_podtverzdayu_28 == 0:
            UI.flag_podtverzdayu_28 = 1
            self.pushButton_104.setEnabled(True)
            self.lineEdit_20.show()
            self.label_319.show()

            self.checkBox_22.show()
            self.checkBox_27.show()
            self.checkBox_29.show()

            self.pushButton_104.move(190, 480)
            self.pushButton_115.move(540, 480)
            return
        if UI.flag_podtverzdayu_28 == 1:
            UI.flag_podtverzdayu_28 = 0
            self.pushButton_104.setDisabled(True)
            self.lineEdit_20.hide()
            self.label_319.hide()

            self.checkBox_22.hide()
            self.checkBox_27.hide()
            self.checkBox_29.hide()

            self.pushButton_104.move(190, 400)
            self.pushButton_115.move(540, 400)
            return
    # Экспорт проекта:выбрать экспорт акта
    ACT = 0
    def HANDLER_MEN_pushButton_105(self):
        if UI.ACT == 0:
            UI.ACT = 1
            self.pushButton_105.setStyleSheet("#pushButton_105\n"
                                              "{\n"
                                              "color: rgb(98, 71, 42);\n"
                                              "background-color: rgb(151, 177, 34);\n"
                                              "border-radius: 5px;\n"
                                              "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                              "border-right: 1px solid rgb(98, 71, 50);\n"
                                              "}\n"
                                              "\n"
                                              "#pushButton_105:hover\n"
                                              "{\n"
                                              "color: rgb(118, 91, 62);\n"
                                              "background-color: rgb(131, 157, 14);\n"
                                              "border-radius: 5px;\n"
                                              "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                              "border-right: 1px solid rgb(98, 71, 50);\n"
                                              "}\n"
                                              "\n"
                                              "#pushButton_105:pressed\n"
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
            return
        if UI.ACT == 1:
            UI.ACT = 0
            self.pushButton_105.setStyleSheet("#pushButton_105\n"
                                              "{\n"
                                              "color: rgb(98, 71, 42);\n"
                                              "background-color: rgb(197, 147, 86);\n"
                                              "border-radius: 5px;\n"
                                              "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                              "border-right: 1px solid rgb(98, 71, 50);\n"
                                              "}\n"
                                              "\n"
                                              "#pushButton_105:hover\n"
                                              "{\n"
                                              "color: rgb(118, 91, 62);\n"
                                              "background-color: rgb(177, 127, 66);\n"
                                              "border-radius: 5px;\n"
                                              "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                              "border-right: 1px solid rgb(98, 71, 50);\n"
                                              "}\n"
                                              "\n"
                                              "#pushButton_105:pressed\n"
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

    # Экспорт проекта:выбрать экспорт счета
    SCHOT = 0
    def HANDLER_MEN_pushButton_114(self):
        if UI.SCHOT == 0:
            UI.SCHOT = 1
            self.pushButton_114.setStyleSheet("#pushButton_114\n"
                                              "{\n"
                                              "color: rgb(98, 71, 42);\n"
                                              "background-color: rgb(151, 177, 34);\n"
                                              "border-radius: 5px;\n"
                                              "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                              "border-right: 1px solid rgb(98, 71, 50);\n"
                                              "}\n"
                                              "\n"
                                              "#pushButton_114:hover\n"
                                              "{\n"
                                              "color: rgb(118, 91, 62);\n"
                                              "background-color: rgb(131, 157, 14);\n"
                                              "border-radius: 5px;\n"
                                              "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                              "border-right: 1px solid rgb(98, 71, 50);\n"
                                              "}\n"
                                              "\n"
                                              "#pushButton_114:pressed\n"
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
            return
        if UI.SCHOT == 1:
            UI.SCHOT = 0
            self.pushButton_114.setStyleSheet("#pushButton_114\n"
                                                  "{\n"
                                                  "color: rgb(98, 71, 42);\n"
                                                  "background-color: rgb(197, 147, 86);\n"
                                                  "border-radius: 5px;\n"
                                                  "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                                  "border-right: 1px solid rgb(98, 71, 50);\n"
                                                  "}\n"
                                                  "\n"
                                                  "#pushButton_114:hover\n"
                                                  "{\n"
                                                  "color: rgb(118, 91, 62);\n"
                                                  "background-color: rgb(177, 127, 66);\n"
                                                  "border-radius: 5px;\n"
                                                  "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                                  "border-right: 1px solid rgb(98, 71, 50);\n"
                                                  "}\n"
                                                  "\n"
                                                  "#pushButton_114:pressed\n"
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
    # Экспорт проекта:выбрать экспорт квитанции
    KVITANTIA = 0
    def HANDLER_MEN_pushButton_126(self):
        if UI.KVITANTIA == 0:
            UI.KVITANTIA = 1
            self.pushButton_126.setStyleSheet("#pushButton_126\n"
                                              "{\n"
                                              "color: rgb(98, 71, 42);\n"
                                              "background-color: rgb(151, 177, 34);\n"
                                              "border-radius: 5px;\n"
                                              "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                              "border-right: 1px solid rgb(98, 71, 50);\n"
                                              "}\n"
                                              "\n"
                                              "#pushButton_126:hover\n"
                                              "{\n"
                                              "color: rgb(118, 91, 62);\n"
                                              "background-color: rgb(131, 157, 14);\n"
                                              "border-radius: 5px;\n"
                                              "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                              "border-right: 1px solid rgb(98, 71, 50);\n"
                                              "}\n"
                                              "\n"
                                              "#pushButton_126:pressed\n"
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
            return
        if UI.KVITANTIA == 1:
            UI.KVITANTIA = 0
            self.pushButton_126.setStyleSheet("#pushButton_126\n"
                                                  "{\n"
                                                  "color: rgb(98, 71, 42);\n"
                                                  "background-color: rgb(197, 147, 86);\n"
                                                  "border-radius: 5px;\n"
                                                  "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                                  "border-right: 1px solid rgb(98, 71, 50);\n"
                                                  "}\n"
                                                  "\n"
                                                  "#pushButton_126:hover\n"
                                                  "{\n"
                                                  "color: rgb(118, 91, 62);\n"
                                                  "background-color: rgb(177, 127, 66);\n"
                                                  "border-radius: 5px;\n"
                                                  "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                                  "border-right: 1px solid rgb(98, 71, 50);\n"
                                                  "}\n"
                                                  "\n"
                                                  "#pushButton_126:pressed\n"
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
    # Экспорт проекта:кнопка экспорт
    def HANDLER_MEN_pushButton_104(self):
        from ui_MEN import UI_MEN
        UI_MEN.HANDLER_MEN_pushButton_104(self)



    flag_podtverzdayu = 0
    def HANDLER_MEN_checkBox(self):
        if UI.flag_podtverzdayu == 0:
            UI.flag_podtverzdayu = 1
            self.pushButton_3.setEnabled(True)
            return
        if UI.flag_podtverzdayu == 1:
            UI.flag_podtverzdayu = 0
            self.pushButton_3.setDisabled(True)

    flag_rasreshenie_redachit = 1

    # на поле начинания:обработчики для быстрого заполнения анкеты нового заказа
    def HANDLER_MEN_NEXT_lineEdit_21(self):
        self.lineEdit.setFocus()
    def HANDLER_MEN_NEXT_lineEdit(self):
        self.lineEdit_16.setFocus()
    def HANDLER_MEN_NEXT_lineEdit_16(self):
        self.comboBox_4.showPopup()
    def HANDLER_MEN_NEXT_comboBox_4(self):
        self.lineEdit_2.setFocus()
    def HANDLER_MEN_NEXT_lineEdit_2(self):
        self.lineEdit_3.setFocus()
    def HANDLER_MEN_NEXT_lineEdit_3(self):
        self.lineEdit_4.setFocus()
    def HANDLER_MEN_NEXT_lineEdit_4(self):
        self.lineEdit_5.setFocus()
    def HANDLER_MEN_NEXT_lineEdit_5(self):
        self.lineEdit_6.setFocus()
    def HANDLER_MEN_NEXT_lineEdit_6(self):
        self.lineEdit_7.setFocus()
    def HANDLER_MEN_NEXT_lineEdit_7(self):
        self.lineEdit_22.setFocus()
    def HANDLER_MEN_NEXT_lineEdit_22(self):
        self.lineEdit_8.setFocus()
    def HANDLER_MEN_NEXT_lineEdit_8(self):
        self.lineEdit_9.setFocus()
    def HANDLER_MEN_NEXT_lineEdit_9(self):
        self.lineEdit_10.setFocus()
    def HANDLER_MEN_NEXT_lineEdit_10(self):
        self.lineEdit_11.setFocus()
    def HANDLER_MEN_NEXT_lineEdit_11(self):
        self.lineEdit_12.setFocus()
    def HANDLER_MEN_NEXT_lineEdit_12(self):
        self.lineEdit_13.setFocus()
    def HANDLER_MEN_NEXT_lineEdit_13(self):
        self.lineEdit_14.setFocus()
    def HANDLER_MEN_NEXT_lineEdit_14(self):
        self.lineEdit_15.setFocus()
    def HANDLER_MEN_NEXT_lineEdit_15(self):
        self.textEdit.setFocus()

    # на поле начинания:обработчики для быстрого заполнения анкеты нового заказа:удаление контекстных подсказок
    FLAG_HANDLER_MEN_NEXT_DEL_lineEdit_5 = 1
    def HANDLER_MEN_NEXT_DEL_lineEdit_5(self):
        if UI.FLAG_HANDLER_MEN_NEXT_DEL_lineEdit_5 == 1:
            UI.FLAG_HANDLER_MEN_NEXT_DEL_lineEdit_5 = 0
            self.lineEdit_5.clear()
    FLAG_HANDLER_MEN_NEXT_DEL_lineEdit_6 = 1
    def HANDLER_MEN_NEXT_DEL_lineEdit_6(self):
        if UI.FLAG_HANDLER_MEN_NEXT_DEL_lineEdit_6 == 1:
            UI.FLAG_HANDLER_MEN_NEXT_DEL_lineEdit_6 = 0
            self.lineEdit_6.clear()

    FLAG_HANDLER_MEN_NEXT_DEL_lineEdit_7 = 1
    def HANDLER_MEN_NEXT_DEL_lineEdit_7(self):
        if UI.FLAG_HANDLER_MEN_NEXT_DEL_lineEdit_7 == 1:
            UI.FLAG_HANDLER_MEN_NEXT_DEL_lineEdit_7 = 0
            self.lineEdit_7.clear()

    FLAG_HANDLER_MEN_NEXT_DEL_lineEdit_22 = 1
    def HANDLER_MEN_NEXT_DEL_lineEdit_22(self):
        if UI.FLAG_HANDLER_MEN_NEXT_DEL_lineEdit_22 == 1:
            UI.FLAG_HANDLER_MEN_NEXT_DEL_lineEdit_22 = 0
            self.lineEdit_22.clear()

    FLAG_HANDLER_MEN_NEXT_DEL_lineEdit_8 = 1
    def HANDLER_MEN_NEXT_DEL_lineEdit_8(self):
        if UI.FLAG_HANDLER_MEN_NEXT_DEL_lineEdit_8 == 1:
            UI.FLAG_HANDLER_MEN_NEXT_DEL_lineEdit_8 = 0
            self.lineEdit_8.clear()
    FLAG_HANDLER_MEN_NEXT_DEL_lineEdit_9 = 1
    def HANDLER_MEN_NEXT_DEL_lineEdit_9(self):
        if UI.FLAG_HANDLER_MEN_NEXT_DEL_lineEdit_9 == 1:
            UI.FLAG_HANDLER_MEN_NEXT_DEL_lineEdit_9 = 0
            self.lineEdit_9.clear()
###########################СОГЛАСОВАНИЕ
    def HANDLER_MEN_pushButton_52(self):
        from ui_MEN import UI_MEN
        UI_MEN.HANDLER_MEN_pushButton_52(self)
    # /////////////////////////////////////////////////////////////////////////////////////////////////////////#
    # /////////////////////////////////////////////////////////////////////////////////////////////////////////#
    # /////////////////////////////////////////////////////////////////////////////////////////////////////////#
    # ///////////////////////////////////////////блок инженера/////////////////////////////////////////////////#
    # /////////////////////////////////////////////////////////////////////////////////////////////////////////#
    # /////////////////////////////////////////////////////////////////////////////////////////////////////////#
    # /////////////////////////////////////////////////////////////////////////////////////////////////////////#
    # внутри проекта:большая кнопка с гаячным ключем и молоткоам
    def HANDLER_INJ_pushButton_54(self):


        status = ""
        from ui_add_new_elements import widget_begin
        txt = "../pythonProject3/DATABASE/current_project/_" + widget_begin.zakaz_nomer.strip() + ".txt"
        #узнаем статус проекта и имя взявшегося
        with open(txt, 'r') as file:
            for index, line in enumerate(file):
                if index == 19:
                    status = line.strip()
                    break
        print("status",status)
        from client import CLIENT
        from ui_add_new_elements import widget_11,widget_12,widget_14,widget_begin
        if status == "Ожидание диагностики":
            self.frame_10.setMinimumHeight(480)
            self.frame_10.setMaximumHeight(480)
            self.label_220.hide()
            self.label_221.hide()
            self.label_211.hide()
            self.textEdit_8.hide()
            self.label_222.hide()
            self.label_213.hide()

            self.scrollArea_11.hide()
        if status.strip() == "Диагностика в процессе":
            self.pushButton_110.setDisabled(True)
            self.label_213.hide()
            imechko = ""
            with open(txt, 'r') as file:
                    for index, line in enumerate(file):
                        if index == 21:
                            imechko = line.strip()
            print("imechko",imechko)
            if CLIENT.pravilnost_parola != imechko:
                self.frame_10.setMinimumHeight(480)
                self.frame_10.setMaximumHeight(480)
                self.label_220.hide()

                from translater import TRANSLATE
                TRANSLATE.out_str = ""
                TRANSLATE.into_str = imechko
                TRANSLATE.eng_in_rus()
                imechko = "Имя инженера: " + TRANSLATE.out_str
                self.label_219.setText(imechko)

                self.label_221.hide()
                self.label_211.hide()
                self.textEdit_8.hide()
                self.label_222.hide()
                self.scrollArea_11.hide()
                self.pushButton_110.setDisabled(True)
                self.checkBox_32.setDisabled(True)

            else:
                UI.FLAG_pushButton_110_communicate_with_serv = 0
                UI.HANDLER_INJ_pushButton_110(self)

                from translater import TRANSLATE
                TRANSLATE.out_str = ""
                TRANSLATE.into_str = imechko
                TRANSLATE.eng_in_rus()
                imechko = "Имя инженера: " + TRANSLATE.out_str
                self.label_219.setText(imechko)
                self.label_220.show()
                # self.pushButton_109

                self.label_221.show()
                self.label_211.show()
                self.textEdit_8.show()
                self.label_222.show()
                self.scrollArea_11.show()
                # self.pushButton_110.setEnabled(True)
                self.checkBox_32.setDisabled(True)
                self.frame_10.setMinimumHeight(1200)
                self.frame_10.setMaximumHeight(1200)
                self.label_213.show()
        if status.strip() == "Ожидание согласования":
            self.label_213.hide()
            UI.FLAG_pushButton_110_communicate_with_serv = 0
            UI.HANDLER_INJ_pushButton_110(self)

            if "отключаем все, что можно"!= "":
                self.checkBox_32.setDisabled(True)
                self.pushButton_110.setDisabled(True)
                self.textEdit_8.setDisabled(True)
                #11 виджет
                self.pushButton_59.setDisabled(True)
                self.pushButton_101.setDisabled(True)
                self.mensale6_lbl_elem_1.setDisabled(True)
                self.mensale6_lbl_elem_2.setDisabled(True)
                for o in widget_11.list_of_new_LineEdits:
                    o.setDisabled(True)
                self.mensale6__elem_1.setDisabled(True)
                self.mensale6__elem_2.setDisabled(True)
                for o in widget_11.list_of_new_SpinBox:
                    o.setDisabled(True)
                # 12 виджет
                self.pushButton_102.setDisabled(True)
                self.pushButton_103.setDisabled(True)
                self.mensale7_le_elem_1.setDisabled(True)
                self.mensale7_le_elem_2.setDisabled(True)
                for o in widget_12.list_of_new_LineEdits:
                    o.setDisabled(True)
                self.mensale7__num_1.setDisabled(True)
                self.mensale7__num_2.setDisabled(True)
                for o in widget_12.list_of_new_SpinBox:
                    o.setDisabled(True)
                self.mensale7_le_COL_1.setDisabled(True)
                self.mensale7_le_COL_2.setDisabled(True)
                for o in widget_12.list_of_new_LE_edinitsy:
                    o.setDisabled(True)
                # 14 виджет
                self.pushButton_106.setDisabled(True)
                self.pushButton_107.setDisabled(True)
                self.mensale6_lbl_elem_5.setDisabled(True)
                self.mensale6_lbl_elem_6.setDisabled(True)
                for o in widget_14.list_of_new_LineEdits:
                    o.setDisabled(True)
                self.mensale6__elem_5.setDisabled(True)
                self.mensale6__elem_6.setDisabled(True)
                for o in widget_14.list_of_new_SpinBox:
                    o.setDisabled(True)
                #дальше
                self.checkBox_33.setDisabled(True)
                self.pushButton_109.setDisabled(True)
            if "Узнаем имя менеджера, заполнявшего бланк"!="":
                txt = "../pythonProject3/DATABASE/current_project/_" + widget_begin.zakaz_nomer.strip() + ".txt"
                #имя взявшегося
                imechko = ""
                with open(txt, 'r') as file:
                    for index, line in enumerate(file):
                        if index == 21:
                            imechko = line.strip()
                print("imechko", imechko)
                from translater import TRANSLATE
                TRANSLATE.out_str = ""
                TRANSLATE.into_str = imechko
                TRANSLATE.eng_in_rus()
                imechko = "Имя инженера: " + TRANSLATE.out_str
                self.label_218.setText(imechko)
                self.label_219.setText(imechko)
            if "Заплняем бланк так, как его заполнил инженер"!="":
                txt = "../pythonProject3/DATABASE/current_project/_" + widget_begin.zakaz_nomer.strip() + ".txt"
                textEdit_ = ""
                W11_ = ""
                W12_ = ""
                W14_ = ""
                with open(txt, 'r') as file:
                    for index, line in enumerate(file):
                        if index == 22:
                            textEdit_ = line.strip()
                        if index == 23:
                            W11_ = line.strip()
                        if index == 24:
                            W12_ = line.strip()
                        if index == 25:
                            W14_ = line.strip()
                print("То, что надо будет записать: (4 строкаки) 54 кнопка")
                print("textEdit_",textEdit_)
                print("W11_",W11_)
                print("W12_",W12_)
                print("W14_",W14_)
                print("156")

                if "Разбераем текст и запихиваем в текстэдит"!="":
                    counter = 0
                    textEdit_BUF = ""
                    try:
                        klk = "\ "
                        klk = klk.strip()
                        while True:
                            if textEdit_[counter] != klk:
                                textEdit_BUF += textEdit_[counter]
                            else:
                                textEdit_BUF += "\n"
                            counter += 1
                    except:
                        pass
                    # print(textEdit_BUF)
                    self.textEdit_8.setText(textEdit_BUF)
                if "Разбераем текст и запихиваем в виджет 11"!="":
                    counter = 0
                    poleNO = 0 #0 - LE;  1 - SB; 2 - LE_ist;
                    LE = []
                    LE_buf = ""
                    LE_ist = []
                    LE_istbuf = ""
                    SB = []
                    SB_buf = ""
                    if "Разделяем"!="":
                        try:
                            while True:
                                print("poleNO",poleNO)
                                if poleNO == 0:
                                    if W11_[counter] != "?":
                                        LE_buf += W11_[counter]
                                    else:
                                        LE.append(LE_buf)
                                        LE_buf = ""
                                        poleNO = 1
                                        counter += 1
                                else:
                                    if poleNO == 1:
                                        if W11_[counter] != "?":
                                            SB_buf += W11_[counter]
                                        else:
                                            SB.append(SB_buf)
                                            SB_buf = ""
                                            poleNO = 2
                                            counter += 1
                                    else:
                                        if poleNO == 2:
                                            if W11_[counter] != "?":
                                                LE_istbuf += W11_[counter]
                                                print("LE_istbuf ",LE_istbuf)
                                            else:
                                                LE_ist.append(LE_istbuf)
                                                print("LE_ist ", LE_ist)
                                                LE_istbuf = ""
                                                poleNO = 0
                                                counter += 1

                        except:
                            pass
                        print("Widget 11 :  ",LE,SB,LE_ist)

                    if "Влавствуем" != "":
                        try:
                            from ui_add_new_elements import widget_11
                            self.mensale6_lbl_elem_1.setText(LE[0])
                            self.mensale6__elem_1.setSpecialValueText(SB[0])
                            self.mensale6_lbl_elem_2.setText(LE[1])
                            self.mensale6__elem_2.setSpecialValueText(SB[1])
                            if (len(LE) - 2) !=0:
                                for i in range(len(widget_11.list_of_new_LineEdits)):#очищаем на всякий
                                    UI.HANDLER_MEN_pushButton_101(self)
                                widget_11.list_of_new_LineEdits =[]
                                widget_11.list_of_new_SpinBox = []
                                for i in range(len(LE)-2):#раздвигаем на столько позиций, на сколько надо
                                    UI.HANDLER_MEN_pushButton_59(self)
                                for i in range(len(widget_11.list_of_new_LineEdits)):#очищаем на всякий
                                    widget_11.list_of_new_LineEdits[i].setText(LE[i-1])
                                for i in range(len(widget_11.list_of_new_LineEdits)):#очищаем на всякий
                                    widget_11.list_of_new_SpinBox[i].setSpecialValueText(SB[i-1])

                        except:
                            print("UUUu")
                if "Разбераем текст и запихиваем в виджет 12"!="":
                    counter = 0
                    poleNO = 0 #0 - LE;  1 - SB;
                    LE = []
                    LE_buf = ""
                    SB = []
                    SB_buf = ""
                    LE_shtuk = []
                    LE_shtuk_buf = ""
                    if "Разделяем"!="":
                        try:
                            while True:
                                if poleNO == 0:
                                    if W12_[counter] != "?":
                                        LE_buf += W12_[counter]
                                    else:
                                        LE.append(LE_buf)
                                        LE_buf = ""
                                        poleNO = 1
                                    counter += 1
                                else:
                                    if poleNO == 1:
                                        if W12_[counter] != "?":
                                            SB_buf += W12_[counter]
                                        else:
                                            SB.append(SB_buf)
                                            SB_buf = ""
                                            poleNO = 2
                                        counter += 1
                                    if poleNO == 2:
                                        if W12_[counter] != "?":
                                            LE_shtuk_buf += W12_[counter]
                                        else:
                                            LE_shtuk.append(LE_shtuk_buf)
                                            LE_shtuk_buf = ""
                                            poleNO = 0
                                        counter += 1
                        except:
                            pass
                        print("Widget 12 :  ",LE,SB,LE_shtuk)

                    if "Влавствуем" != "":
                        try:
                            from ui_add_new_elements import widget_12
                            print("VLAST")
                            self.mensale7_le_elem_1.setText(LE[0])
                            self.mensale7__num_1.setSpecialValueText(SB[0])
                            self.mensale7_le_COL_1.setText(LE_shtuk[0])
                            self.mensale7_le_elem_2.setText(LE[1])
                            self.mensale7__num_2.setSpecialValueText(SB[1])
                            self.mensale7_le_COL_2.setText(LE_shtuk[1])
                            if (len(LE) - 2) !=0:
                                for i in range(len(widget_12.list_of_new_LineEdits)):#очищаем на всякий
                                    UI.HANDLER_MEN_pushButton_103(self)
                                widget_14.list_of_new_LineEdits =[]
                                widget_12.list_of_new_SpinBox = []
                                widget_12.list_of_new_LE_edinitsy = []
                                for i in range(len(LE)-2):#раздвигаем на столько позиций, на сколько надо
                                    UI.HANDLER_MEN_pushButton_102(self)
                                for i in range(len(widget_12.list_of_new_LineEdits)):#очищаем на всякий
                                    widget_12.list_of_new_LineEdits[i].setText(LE[i-1])
                                for i in range(len(widget_12.list_of_new_LineEdits)):#очищаем на всякий
                                    widget_12.list_of_new_SpinBox[i].setSpecialValueText(SB[i-1])
                                for i in range(len(widget_12.list_of_new_LE_edinitsy)):#очищаем на всякий
                                    widget_12.list_of_new_LE_edinitsy[i].setSpecialValueText(LE_shtuk[i-1])

                        except:
                            print("UUUu")
                if "Разбераем текст и запихиваем в виджет 14"!="":
                    counter = 0
                    poleNO = 0 #0 - LE;  1 - SB;
                    LE = []
                    LE_buf = ""
                    SB = []
                    SB_buf = ""
                    if "Разделяем"!="":
                        try:
                            while True:
                                if poleNO == 0:
                                    if W14_[counter] != "?":
                                        LE_buf += W14_[counter]
                                    else:
                                        LE.append(LE_buf)
                                        LE_buf = ""
                                        poleNO = 1
                                    counter += 1
                                else:
                                    if W14_[counter] != "?":
                                        SB_buf += W14_[counter]
                                    else:
                                        SB.append(SB_buf)
                                        SB_buf = ""
                                        poleNO = 0
                                    counter += 1
                        except:
                            pass
                        print("Widget 14 :  ",LE,SB)

                    if "Влавствуем" != "":
                        try:
                            from ui_add_new_elements import widget_14
                            self.mensale6_lbl_elem_5.setText(LE[0])
                            self.mensale6__elem_5.setSpecialValueText(SB[0])

                            self.mensale6__elem_6.setSpecialValueText(SB[1])
                            self.mensale6_lbl_elem_6.setText(LE[1])
                            if (len(LE) - 2) !=0:
                                for i in range(len(widget_14.list_of_new_LineEdits)):#очищаем на всякий
                                    UI.HANDLER_MEN_pushButton_107(self)
                                widget_14.list_of_new_LineEdits =[]
                                widget_14.list_of_new_SpinBox = []
                                for i in range(len(LE)-2):#раздвигаем на столько позиций, на сколько надо
                                    UI.HANDLER_MEN_pushButton_106(self)
                                for i in range(len(widget_14.list_of_new_LineEdits)):#очищаем на всякий
                                    widget_14.list_of_new_LineEdits[i].setText(LE[i-1])
                                for i in range(len(widget_14.list_of_new_LineEdits)):#очищаем на всякий
                                    widget_14.list_of_new_SpinBox[i].setSpecialValueText(SB[i-1])

                        except:
                            print("UUUu")
        self.stackedWidget.setCurrentIndex(10)

    # внутри проекта: кнопка возврата к прокетам
    def HANDLER_INJ_pushButton_53(self):
        self.stackedWidget.setCurrentIndex(1)

    #кнопка вступить в диагностику
    FLAG_pushButton_110_communicate_with_serv = 1
    def HANDLER_INJ_pushButton_110(self):
        self.pushButton_24.setEnabled(True)
        self.pushButton_25.setEnabled(True)
        self.pushButton_4.setEnabled(True)
        self.pushButton_14.setEnabled(True)
        self.lineEdit_17.setEnabled(True)
        self.pushButton_15.setEnabled(True)
        self.pushButton_5.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.pushButton_9.setEnabled(True)
        self.pushButton_10.setEnabled(True)
        self.pushButton_11.setEnabled(True)
        self.pushButton_7.setEnabled(True)
        self.pushButton_8.setEnabled(True)
        self.pushButton_12.setEnabled(True)
        if UI.FLAG_pushButton_110_communicate_with_serv == 1:
            from ui_add_new_elements import widget_begin
            from client import CLIENT
            CLIENT.nomer_proecta = widget_begin.zakaz_nomer
            CLIENT.INJ.vstupit_v_diagnosticu()

        self.frame_10.setMinimumHeight(1200)
        self.frame_10.setMaximumHeight(1200)
        self.label_213.hide()

        self.label_220.show()
        self.label_221.show()
        self.label_211.show()
        self.textEdit_8.show()
        self.label_222.show()
        self.scrollArea_11.show()
    #checkBox подтвердить вступление в проект
    flag_podtverzdayu_32 = 0
    def HANDLER_MEN_checkBox_32(self):
        if UI.flag_podtverzdayu_32 == 0:
            UI.flag_podtverzdayu_32 = 1
            self.pushButton_110.setEnabled(True)
            return
        if UI.flag_podtverzdayu_32 == 1:
            UI.flag_podtverzdayu_32 = 0
            self.pushButton_110.setDisabled(True)

    def HANDLER_MEN_pushButton_109(self):
        from ui_add_new_elements import widget_11,widget_12,widget_14,widget_begin
        widget_11.get_inputed_data(self)
        widget_12.get_inputed_data(self)
        widget_14.get_inputed_data(self)
        from client import  CLIENT
        CLIENT.INJ.text_textEdit_8 = self.textEdit_8.toPlainText()
        CLIENT.nomer_proecta = widget_begin.zakaz_nomer
        try:
            CLIENT.INJ.zakonchit_diagnosticu()
        except socket.error:
            pass

        self.stackedWidget.setCurrentIndex(1)


    flag_podtverzdayu_33 = 0
    def HANDLER_MEN_checkBox_33(self):
        if UI.flag_podtverzdayu_33 == 0:
            UI.flag_podtverzdayu_33 = 1
            self.pushButton_109.setEnabled(True)
            return
        if UI.flag_podtverzdayu_33 == 1:
            UI.flag_podtverzdayu_33 = 0
            self.pushButton_109.setDisabled(True)

    def HANDLER_MEN_pushButton_111(self):
        pass
    flag_podtverzdayu_34 = 0
    def HANDLER_MEN_checkBox_34(self):
        if UI.flag_podtverzdayu_34 == 0:
            UI.flag_podtverzdayu_34 = 1
            self.pushButton_111.setEnabled(True)
            return
        if UI.flag_podtverzdayu_34 == 1:
            UI.flag_podtverzdayu_34 = 0
            self.pushButton_111.setDisabled(True)

    def HANDLER_MEN_pushButton_113(self):
        pass
    flag_podtverzdayu_35 = 0
    def HANDLER_MEN_checkBox_35(self):
        if UI.flag_podtverzdayu_35 == 0:
            UI.flag_podtverzdayu_35 = 1
            self.pushButton_113.setEnabled(True)
            return
        if UI.flag_podtverzdayu_35 == 1:
            UI.flag_podtverzdayu_35 = 0
            self.pushButton_113.setDisabled(True)

# на бланке диагностики:11 виджет
    def HANDLER_NEXT_w11_1(self):#mensale6_lbl_elem_1
        self.mensale6_lbl_elem_3.setFocus()
    def HANDLER_NEXT_w11_2(self):#mensale6_lbl_elem_3
        self.mensale6_lbl_elem_4.setFocus()
    def HANDLER_NEXT_w11_3(self):#mensale6_lbl_elem_2
        self.mensale6_lbl_elem_2.setFocus()
    def HANDLER_NEXT_w11_4(self):#mensale6_lbl_elem_4
        try:
            from ui_add_new_elements import widget_11
            widget_11.list_of_new_LineEdits[0].setFocus()
        except:
            self.mensale7_le_elem_1.setFocus()

    # на бланке диагностики:12 виджет
    def HANDLER_NEXT_w12_1(self):  # mensale6_lbl_elem_1
        self.mensale7_le_elem_3.setFocus()
    def HANDLER_NEXT_w12_2(self):  # mensale6_lbl_elem_3
        self.mensale7_le_COL_1.setFocus()
    def HANDLER_NEXT_w12_3(self):  # mensale6_lbl_elem_2
        self.mensale7_le_elem_2.setFocus()
    def HANDLER_NEXT_w12_4(self):  # mensale6_lbl_elem_2
        self.mensale7_le_elem_4.setFocus()
    def HANDLER_NEXT_w12_5(self):  # mensale6_lbl_elem_2
        self.mensale7_le_COL_2.setFocus()

    def HANDLER_NEXT_w12_6(self):  # mensale7_le_COL_1
        try:
            from ui_add_new_elements import widget_12
            widget_12.list_of_new_LineEdits[0].setFocus()
        except:
            self.mensale6_lbl_elem_5.setFocus()
#на бланке диагностики:14 виджет
    def HANDLER_NEXT_w14_1(self):#mensale6_lbl_elem_5
        self.mensale6_lbl_elem_7.setFocus()
    def HANDLER_NEXT_w14_2(self):#mensale6_lbl_elem_7
        self.mensale6_lbl_elem_6.setFocus()
    def HANDLER_NEXT_w14_3(self):#mensale6_lbl_elem_6
        self.mensale6_lbl_elem_8.setFocus()
    def HANDLER_NEXT_w14_4(self):#mensale6_lbl_elem_8
        try:
            from ui_add_new_elements import widget_14
            widget_14.list_of_new_LineEdits[0].setFocus()
        except:
            pass



    def activated_elem_for_the_changed_path(self):
        print("В силу вступает...")
        if self.comboBox_16.currentText() == "Мен. обслуживания":
            print("В силу вступает Менеджер общения")
            self.stackedWidget_3.setCurrentIndex(1)
            self.stackedWidget_2.setCurrentIndex(0)
            self.widget_4.hide()
            self.widget_5.hide()
            self.widget_9.hide()
            self.pushButton_32.hide()
            self.pushButton_129.hide()
            self.label_262.hide()
            self.label_271.hide()
            self.label_274.hide()

            #заглавье настроек
            self.pushButton_31.clicked.connect(self.HANDLER_MEN_pushButton_31)
            self.pushButton_32.clicked.connect(self.HANDLER_MEN_pushButton_32)

            #На основных настройках:новый проект
            self.pushButton_4.clicked.connect(self.HANDLER_MEN_pushButton_4)



            #на натройках начинания:очистить
            self.pushButton_39.clicked.connect(self.HANDLER_MEN_pushButton_39)
            # на натройках начинания:подтвердить очистку
            self.pushButton_50.clicked.connect(self.HANDLER_MEN_pushButton_50)
            # на натройках начинания:закрыть редактор нового проекта
            self.pushButton_40.clicked.connect(self.HANDLER_MEN_pushButton_40)


            # на поле начинания:кнопка повысить количество исполнительных дней
            self.pushButton.clicked.connect(self.HANDLER_MEN_pushButton)
            # на поле начинания:кнопка понизить количество исполнительных дней
            self.pushButton_2.clicked.connect(self.HANDLER_MEN_pushButton_2)
            # на поле начинания:кнопка создать проект
            self.pushButton_3.clicked.connect(self.HANDLER_MEN_pushButton_3)
            # на поле начинания:кнопка изменения номера
            self.pushButton_27.clicked.connect(self.HANDLER_MEN_pushButton_27)
            self.pushButton_36.clicked.connect(self.HANDLER_MEN_pushButton_36)
            # на поле начинания:кнопка отменить создание проекта/заполнить бланк пятерккми
            self.pushButton_13.clicked.connect(self.HANDLER_MEN_pushButton_13)
            # на поле начинания:обработчики для быстрого заполнения анкеты нового заказа
            self.lineEdit_21.returnPressed.connect(self.HANDLER_MEN_NEXT_lineEdit_21)
            self.lineEdit.returnPressed.connect(self.HANDLER_MEN_NEXT_lineEdit)
            self.lineEdit_16.returnPressed.connect(self.HANDLER_MEN_NEXT_lineEdit_16)
            self.comboBox_4.currentTextChanged.connect(self.HANDLER_MEN_NEXT_comboBox_4)
            self.lineEdit_2.returnPressed.connect(self.HANDLER_MEN_NEXT_lineEdit_2)
            self.lineEdit_3.returnPressed.connect(self.HANDLER_MEN_NEXT_lineEdit_3)
            self.lineEdit_4.returnPressed.connect(self.HANDLER_MEN_NEXT_lineEdit_4)
            self.lineEdit_5.returnPressed.connect(self.HANDLER_MEN_NEXT_lineEdit_5)
            self.lineEdit_6.returnPressed.connect(self.HANDLER_MEN_NEXT_lineEdit_6)
            self.lineEdit_7.returnPressed.connect(self.HANDLER_MEN_NEXT_lineEdit_7)
            self.lineEdit_22.returnPressed.connect(self.HANDLER_MEN_NEXT_lineEdit_22)
            self.lineEdit_8.returnPressed.connect(self.HANDLER_MEN_NEXT_lineEdit_8)
            self.lineEdit_9.returnPressed.connect(self.HANDLER_MEN_NEXT_lineEdit_9)
            self.lineEdit_10.returnPressed.connect(self.HANDLER_MEN_NEXT_lineEdit_10)
            self.lineEdit_11.returnPressed.connect(self.HANDLER_MEN_NEXT_lineEdit_11)
            self.lineEdit_12.returnPressed.connect(self.HANDLER_MEN_NEXT_lineEdit_12)
            self.lineEdit_13.returnPressed.connect(self.HANDLER_MEN_NEXT_lineEdit_13)
            self.lineEdit_14.returnPressed.connect(self.HANDLER_MEN_NEXT_lineEdit_14)
            self.lineEdit_15.returnPressed.connect(self.HANDLER_MEN_NEXT_lineEdit_15)
            # на поле начинания:обработчики для быстрого заполнения анкеты нового заказа:удаление контекстных подсказок
            self.lineEdit_5.textEdited.connect(self.HANDLER_MEN_NEXT_DEL_lineEdit_5)
            self.lineEdit_6.textEdited.connect(self.HANDLER_MEN_NEXT_DEL_lineEdit_6)
            self.lineEdit_7.textEdited.connect(self.HANDLER_MEN_NEXT_DEL_lineEdit_7)
            self.lineEdit_22.textEdited.connect(self.HANDLER_MEN_NEXT_DEL_lineEdit_22)
            self.lineEdit_8.textEdited.connect(self.HANDLER_MEN_NEXT_DEL_lineEdit_8)
            self.lineEdit_9.textEdited.connect(self.HANDLER_MEN_NEXT_DEL_lineEdit_9)
            self.lineEdit_9.textEdited.connect(self.HANDLER_MEN_NEXT_DEL_lineEdit_9)



            self.pushButton_108.clicked.connect(self.HANDLER_MEN_pushButton_108)
            self.pushButton_112.clicked.connect(self.HANDLER_MEN_pushButton_112)

            self.checkBox.clicked.connect(self.HANDLER_MEN_checkBox)

            #внутри заказа:к анкете
            self.pushButton_28.clicked.connect(self.HANDLER_MEN_pushButton_28)
            self.pushButton_51.clicked.connect(self.HANDLER_MEN_pushButton_51)

            # внутри экспорта: отмена
            self.pushButton_115.clicked.connect(self.HANDLER_MEN_pushButton_53)
            # кнопка экспорта
            self.pushButton_104.clicked.connect(self.HANDLER_MEN_pushButton_104)
            # подтверждение экспорта
            self.checkBox_28.clicked.connect(self.HANDLER_MEN_checkBox_28)
            #кнопка экспорта акта оценки ТС оборудования
            self.pushButton_105.clicked.connect(self.HANDLER_MEN_pushButton_105)
            # кнопка экспорта счёта
            self.pushButton_114.clicked.connect(self.HANDLER_MEN_pushButton_114)
            # кнопка экспорта квитанции
            self.pushButton_126.clicked.connect(self.HANDLER_MEN_pushButton_126)
            ####################этап согласования
            # кнопка перехода к диалогу с заказчиком
            self.pushButton_52.clicked.connect(self.HANDLER_MEN_pushButton_52)

        if self.comboBox_16.currentText() == "Инженер":
            print("В силу вступает Инженер")
            self.pushButton_4.setText("")
            self.stackedWidget_3.setCurrentIndex(1)
            self.stackedWidget_2.setCurrentIndex(0)
            self.widget_4.hide()
            self.widget_5.hide()
            self.widget_9.hide()
            self.pushButton_32.hide()
            self.pushButton_129.hide()
            self.label_262.hide()
            self.label_271.hide()
            self.label_274.hide()
            self.pushButton_110.setDisabled(True)
            self.pushButton_109.setDisabled(True)
            self.pushButton_111.setDisabled(True)
            self.pushButton_113.setDisabled(True)


            #заглавье настроек
            self.pushButton_31.clicked.connect(self.HANDLER_MEN_pushButton_31)
            self.pushButton_32.hide()#кнопка нового проекта

            #На основных настройках:новый проект
            self.pushButton_4.setDisabled(True)

            #внутри заказа: проход к данным менеджера
            self.pushButton_64.clicked.connect(self.HANDLER_INJ_pushButton_64)

            #на поле диагностики: вступить в проект
            self.pushButton_110.clicked.connect(self.HANDLER_INJ_pushButton_110)
            # на поле диагностики: подтвердить вступление
            self.checkBox_32.clicked.connect(self.HANDLER_MEN_checkBox_32)
            # на поле диагностики :: 11 виджет : быстрый переход
            self.mensale6_lbl_elem_1.returnPressed.connect(self.HANDLER_NEXT_w11_1)
            self.mensale6_lbl_elem_2.returnPressed.connect(self.HANDLER_NEXT_w11_2)
            self.mensale6_lbl_elem_3.returnPressed.connect(self.HANDLER_NEXT_w11_3)
            self.mensale6_lbl_elem_4.returnPressed.connect(self.HANDLER_NEXT_w11_4)
            # на поле диагностики :: 12 виджет : быстрый переход
            self.mensale7_le_elem_1.returnPressed.connect(self.HANDLER_NEXT_w12_1)
            self.mensale7_le_elem_3.returnPressed.connect(self.HANDLER_NEXT_w12_2)
            self.mensale7_le_COL_1.returnPressed.connect(self.HANDLER_NEXT_w12_3)
            self.mensale7_le_elem_2.returnPressed.connect(self.HANDLER_NEXT_w12_4)
            self.mensale7_le_elem_4.returnPressed.connect(self.HANDLER_NEXT_w12_5)
            self.mensale7_le_COL_2.returnPressed.connect(self.HANDLER_NEXT_w12_6)
            # на поле диагностики :: 14 виджет : быстрый переход
            self.mensale6_lbl_elem_5.returnPressed.connect(self.HANDLER_NEXT_w14_1)
            self.mensale6_lbl_elem_6.returnPressed.connect(self.HANDLER_NEXT_w14_3)
            self.mensale6_lbl_elem_7.returnPressed.connect(self.HANDLER_NEXT_w14_2)
            self.mensale6_lbl_elem_8.returnPressed.connect(self.HANDLER_NEXT_w14_4)


            #на поле диагностики: вступить в проект
            self.pushButton_109.clicked.connect(self.HANDLER_MEN_pushButton_109)
            # на поле диагностики: подтвердить вступление
            self.checkBox_33.clicked.connect(self.HANDLER_MEN_checkBox_33)
            self.pushButton_111.clicked.connect(self.HANDLER_MEN_pushButton_111)
            self.checkBox_34.clicked.connect(self.HANDLER_MEN_checkBox_34)

            self.pushButton_113.clicked.connect(self.HANDLER_MEN_pushButton_113)
            self.checkBox_35.clicked.connect(self.HANDLER_MEN_checkBox_35)


            # поле диагностики: кнопки +- (ниже они расположены по порядку)
            self.pushButton_59.clicked.connect(self.HANDLER_MEN_pushButton_59)
            self.pushButton_101.clicked.connect(self.HANDLER_MEN_pushButton_101)
            self.pushButton_102.clicked.connect(self.HANDLER_MEN_pushButton_102)
            self.pushButton_103.clicked.connect(self.HANDLER_MEN_pushButton_103)
            self.pushButton_106.clicked.connect(self.HANDLER_MEN_pushButton_106)
            self.pushButton_107.clicked.connect(self.HANDLER_MEN_pushButton_107)


            # поле ремонта: кнопки +- (ниже они расположены по порядку)
            self.pushButton_108.clicked.connect(self.HANDLER_MEN_pushButton_108)
            self.pushButton_112.clicked.connect(self.HANDLER_MEN_pushButton_112)


            self.checkBox.clicked.connect(self.HANDLER_MEN_checkBox)
            #внутри проекта:кнопка с молотком
            self.pushButton_54.clicked.connect(self.HANDLER_INJ_pushButton_54)
            # внутри проекта: возврат к проектам
            self.pushButton_53.clicked.connect(self.HANDLER_INJ_pushButton_53)

        if self.comboBox_16.currentText() == "Мен. закупа":
            self.pushButton_57.clicked.connect(self.HANDLER_MEZ_pushButton_57)
            #на поле узнавания цен:подтвердить вступление в заказ
            self.checkBox_36.clicked.connect(self.HANDLER_MEZ_checkBox_36)
            # на поле узнавания цен:кнопка вступить в заказ
            self.pushButton_117.clicked.connect(self.HANDLER_MEZ_pushButton_117)
            # на поле узнавания цен:подтвердить завершение узнавания цен
            self.checkBox_37.clicked.connect(self.HANDLER_MEZ_checkBox_37)
            # на поле узнавания цен: завершить указываение цен
            self.pushButton_116.clicked.connect(self.HANDLER_MEZ_pushButton_116)




    def __init__(self, MainWindow):
        Ui_MainWindow.__init__(self)
        self.setupUi(MainWindow)

        print('__Begin Client programm:')



        self.stackedWidget_3.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(0)
        self.widget_4.hide()
        self.widget_5.hide()
        self.widget_9.hide()
        self.pushButton_32.hide()
        self.pushButton_129.hide()
        self.label_262.hide()
        self.label_271.hide()
        self.label_274.hide()
        self.lineEdit_23.hide()

        self.pushButton_33.show()
        #кнопка войти
        self.pushButton_29.clicked.connect(self.HANDLER_MEN_pushButton_29)
        #для быстрого перехода по энтеру
        self.lineEdit_18.returnPressed.connect(self.HANDLER_MEN_NEXT_lineEdit_18)
        self.lineEdit_19.returnPressed.connect(self.HANDLER_MEN_NEXT_lineEdit_19)
        self.comboBox_16.currentTextChanged.connect(self.HANDLER_MEN_NEXT_comboBox_16)

        #кнопки решистрации
        self.pushButton_30.clicked.connect(self.HANDLER_MEN_pushButton_30)
        self.pushButton_37.clicked.connect(self.HANDLER_MEN_pushButton_30)
        self.pushButton_38.clicked.connect(self.HANDLER_MEN_pushButton_30)
        self.pushButton_129.clicked.connect(self.HANDLER_MEN_pushButton_30)
        #для быстрого заполнения окна
        self.lineEdit_30.returnPressed.connect(self.HANDLER_MEN_NEXT_lineEdit_30)
        self.lineEdit_31.returnPressed.connect(self.HANDLER_MEN_NEXT_lineEdit_31)
        self.lineEdit_32.returnPressed.connect(self.HANDLER_MEN_NEXT_lineEdit_32)
        self.comboBox_17.currentTextChanged.connect(self.HANDLER_MEN_NEXT_comboBox_17)
        self.lineEdit_36.returnPressed.connect(self.HANDLER_MEN_NEXT_lineEdit_36)
        self.lineEdit_35.returnPressed.connect(self.HANDLER_MEN_NEXT_lineEdit_35)

        #закрытие окна регистрации
        self.pushButton_133.clicked.connect(self.HANDLER_MEN_pushButton_133)
        self.pushButton_132.clicked.connect(self.HANDLER_MEN_pushButton_132)

        self.pushButton_5.clicked.connect(self.HANDLER_MEN_pushButton_5)
        self.pushButton_6.clicked.connect(self.HANDLER_MEN_pushButton_6)
        self.pushButton_9.clicked.connect(self.HANDLER_MEN_pushButton_9)
        self.pushButton_10.clicked.connect(self.HANDLER_MEN_pushButton_10)

        self.pushButton_11.clicked.connect(self.HANDLER_MEN_pushButton_11)
        self.pushButton_7.clicked.connect(self.HANDLER_MEN_pushButton_7)
        self.pushButton_8.clicked.connect(self.HANDLER_MEN_pushButton_8)
        self.pushButton_12.clicked.connect(self.HANDLER_MEN_pushButton_12)

        self.pushButton_25.clicked.connect(self.HANDLER_MEN_pushButton_25)

        #кресты
        self.pushButton_53.clicked.connect(self.HANDLER_MEN_pushButton_53)
        self.pushButton_56.clicked.connect(self.HANDLER_MEN_pushButton_53)
        self.pushButton_60.clicked.connect(self.HANDLER_MEN_pushButton_53)
        self.pushButton_62.clicked.connect(self.HANDLER_MEN_pushButton_53)
        self.pushButton_63.clicked.connect(self.HANDLER_MEN_pushButton_53)
        self.pushButton_65.clicked.connect(self.HANDLER_MEN_pushButton_53)
        self.pushButton_128.clicked.connect(self.HANDLER_MEN_pushButton_53)
        self.pushButton_130.clicked.connect(self.HANDLER_MEN_pushButton_53)
        self.pushButton_131.clicked.connect(self.HANDLER_MEN_pushButton_53)

        # на натройках основныз:обновление БД
        self.pushButton_14.clicked.connect(self.HANDLER_MEN_pushButton_14)
        # на натройках начинания:обновление БД
        ################
        self.pushButton_15.clicked.connect(self.HANDLER_MEZ_pushButton_15)
        #НАСТРОЕЧНЫЕ КНОПКИ
        #MEZ
        #MEX:для заполнения узнавания цен
        self.pushButton_118.clicked.connect(self.HANDLER_MEN_pushButton_118)

    def HANDLER_MEZ_pushButton_57(self):
        #прячем найдено незак. полей
        self.label_247.hide()
        self.label_248.hide()
        #отключаем кнопку завершения
        self.pushButton_116.setDisabled(True)
        from ui_MEZ import UI_MEZ
        UI_MEZ.HANDLER_MEZ_pushButton_57(self)
    def HANDLER_MEZ_checkBox_36(self):
        from ui_MEZ import UI_MEZ
        UI_MEZ.HANDLER_MEN_checkBox_36(self)
    def HANDLER_MEZ_pushButton_117(self):
        self.pushButton_15.setEnabled(True)
        from ui_MEZ import UI_MEZ
        UI_MEZ.HANDLER_MEZ_pushButton_117(self)
    def HANDLER_MEZ_pushButton_15(self):
        from ui_add_new_elements import widget_11,widget_12,widget_14
        widget_11.get_inputed_data(self)
        widget_12.get_inputed_data(self)
        widget_14.get_inputed_data(self)

    def HANDLER_MEZ_checkBox_37(self):
        from ui_MEZ import UI_MEZ
        UI_MEZ.HANDLER_MEN_checkBox_37(self)
    def HANDLER_MEZ_pushButton_116(self):
        from ui_MEZ import UI_MEZ
        UI_MEZ.HANDLER_MEZ_pushButton_116(self)
    def HANDLER_MEN_pushButton_118(self):
        from ui_add_new_elements import widget_cena
        counter = 0
        for i in widget_cena.Articul:
            i.setText(f"ACKL_mamapomogi_{counter}")
            counter += 1
        counter = 0
        for i in widget_cena.cena_sebestoy:
            i.setText(f"{counter}.00")
            counter += 1
        counter = 0
        for i in widget_cena.cena_prodagi:
            i.setText(f"{counter+2}.00")
            counter += 1
        counter = 0
        for i in widget_cena.postavshik:
            i.setText(f"ВИКТОР {counter}-ныч")
            counter += 1
        counter = 0
        for i in widget_cena.Istochnic:
            i.setText(f"https://jio_{counter}.com")
            counter += 1
        counter = 0
        for i in widget_cena.data_dostavki:
            i.setText(f"{counter}.01.2021")
            counter += 1
        counter = 0
        for i in widget_cena.cena_dostavki:
            i.setText(f"{counter}.00")
            counter += 1

    def HANDLER_INJ_pushButton_64(self):
        try:
            UI.HANDLER_MEN_pushButton_28(self)
        except:
            print("Press F to pay respect")