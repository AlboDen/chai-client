from w import Ui_MainWindow
# from widget_11 import widget_11
from PyQt5 import QtCore, QtGui, QtWidgets

class UI_MEZ(Ui_MainWindow):
    # поле узнавания цен:кнопка входа в заказ
    FLAG_nado_li_otpr_otcet_o_vstuplenii = 1

    def HANDLER_MEZ_pushButton_117(self):
        self.label_243.show()
        self.label_244.show()
        self.label_245.show()
        self.scrollArea_16.show()

        self.label_239.hide()
        self.frame_16.setMinimumHeight(1090)
        self.frame_16.setMaximumHeight(1090)
        self.frame_17.setMinimumHeight(480)
        self.frame_17.setMaximumHeight(480)
        self.pushButton_117.setDisabled(True)
        self.checkBox_36.setDisabled(True)
        # 11_widget - для диагностики
        _11_LE_ist = []
        _11_LE = []
        _11_SB = []
        # 12_widget - для диагностики
        _12_LE = []
        _12_LE_ist = []
        _12_SB = []
        _12_LE_ed = []
        # 14_widget - для диагностики
        _14_LE = []
        _14_LE_ist = []
        _14_SB = []

        from ui_add_new_elements import widget_cena, widget_begin
        # достаем из базы все то, что надо для заполнения
        if "достаем инфу, которую предоставил инженер при диагностике" != "":
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
            print("То, что надо будет записать: (4 строки) 117 кнопка")
            print(textEdit_)
            print(W11_)
            print(W12_)
            print(W14_)
            if "Разбераем текст и запихиваем в текстэдит" != "":
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
                print(textEdit_BUF)
            if "Разбераем текст и запихиваем в виджет 11" != "":
                counter = 0
                poleNO = 0  # 0 - LE;  1 - SB; 2 - источник
                LE = []
                LE_buf = ""
                LE_ist = []
                LE_ist_buf = ""
                SB = []
                SB_buf = ""
                if "Разделяем" != "":
                    try:
                        while True:
                            if poleNO == 0:
                                if W11_[counter] != "?":
                                    LE_buf += W11_[counter]
                                else:
                                    LE.append(LE_buf)
                                    LE_buf = ""
                                    poleNO = 1
                                counter += 1
                            else:
                                if poleNO == 2:
                                    if W11_[counter] != "?":
                                        SB_buf += W11_[counter]
                                    else:
                                        SB.append(SB_buf)
                                        SB_buf = ""
                                        poleNO = 0
                                    counter += 1
                                else:
                                    if poleNO == 1:
                                        if W11_[counter] != "?":
                                            LE_ist_buf += W11_[counter]
                                        else:
                                            LE_ist.append(LE_ist_buf)
                                            LE_ist_buf = ""
                                            poleNO = 2
                                        counter += 1
                    except:
                        pass
                    print("Widget 11 :  ", LE, SB,LE_ist)
                    _11_LE_ist = LE_ist
                    _11_LE = LE
                    _11_SB = SB
            if "Разбераем текст и запихиваем в виджет 12" != "":
                counter = 0
                poleNO = 0  # 0 - LE;  1 - SB;
                LE = []
                LE_buf = ""
                SB = []
                SB_buf = ""
                LE_shtuk = []
                LE_shtuk_buf = ""
                LE_ist_sop = []
                if "Разделяем" != "":
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
                                        poleNO = 3
                                    counter += 1
                                else:
                                    if poleNO == 3:
                                        if W12_[counter] != "?":
                                            LE_ist_buf += W12_[counter]
                                        else:
                                            LE_ist_sop.append(LE_ist_buf)
                                            LE_ist_buf = ""
                                            poleNO = 0
                                        counter += 1
                    except:
                        pass
                    print("Widget 12 :  ", LE, SB, LE_shtuk,LE_ist_sop)
                    _12_LE = LE
                    _12_SB = SB
                    _12_LE_ed = LE_shtuk
                    _12_LE_ist = LE_ist_sop
            if "Разбераем текст и запихиваем в виджет 14" != "":
                counter = 0
                poleNO = 0  # 0 - LE;  1 - SB;
                LE = []
                LE_buf = ""
                SB = []
                SB_buf = ""
                LE_ist_rem = []
                if "Разделяем" != "":
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
                                if poleNO == 1:
                                    if W14_[counter] != "?":
                                        SB_buf += W14_[counter]
                                    else:
                                        SB.append(SB_buf)
                                        SB_buf = ""
                                        poleNO = 2
                                    counter += 1
                                else:
                                    if poleNO == 2:
                                        if W14_[counter] != "?":
                                            SB_buf += W14_[counter]
                                        else:
                                            LE_ist_rem.append(SB_buf)
                                            SB_buf = ""
                                            poleNO = 0
                                        counter += 1
                    except:
                        pass
                    print("Widget 14 :  ", LE, SB, LE_ist_rem)
                    _14_LE = LE
                    _14_SB = SB
                    _14_LE_ist = LE_ist_rem
        empt_mass = []
        widget_cena.del_all_strings(self)

        if _11_LE != empt_mass:
            for i in range(len(_11_LE)):
                if len(_11_LE[i]) > 32:
                    widget_cena.FLAG_LowREG = 1

                if len(_11_LE[i]) > 40:
                    o = _11_LE[i]
                    first = o[0:40]
                    first += "\n"
                    counter = 41
                    try:
                        while True:
                            first += o[counter]
                            counter += 1
                    except:
                        pass
                    _11_LE[i] = first
                # widget_cena.del_all_strings(self)

                #меняем > на / для оживления ссылок
                k = "\ "
                k = k.strip()
                buf = ""
                for i in range(len(_11_LE_ist)):
                    for iopt in _11_LE_ist[i]:
                        if iopt == ">" or iopt == k:
                            buf += "/"
                        else:
                            buf += iopt
                    _11_LE_ist[i] = buf
                    buf = ""

            for i in range(len(_11_LE_ist)):
                widget_cena.add_new_string(self, imya_el=_11_LE[i], kolichestvo=_11_SB[i],
                                           tip_rashoda="Эл. для диагностики", ist = _11_LE_ist[i])
        #"""
        if _12_LE != empt_mass:
            for i in range(len(_12_LE)):
                if len(_12_LE[i]) > 32:
                    widget_cena.FLAG_LowREG = 1

                if len(_12_LE[i]) > 40:
                    o = _12_LE[i]
                    first = o[0:40]
                    first += "\n"
                    counter = 41
                    try:
                        while True:
                            first += o[counter]
                            counter += 1
                    except:
                        pass
                    _12_LE[i] = first
                # widget_cena.del_all_strings(self)

                # меняем > на / для оживления ссылок
                k = "\ "
                k = k.strip()
                buf = ""
                for i in range(len(_12_SB)):
                    for iopt in _12_SB[i]:
                        if iopt == ">" or iopt == k:
                            buf += "/"
                        else:
                            buf += iopt
                    _12_SB[i] = buf
                    buf = ""
            for i in range(len(_12_SB)):
                widget_cena.add_new_string(self, imya_el=_12_LE[i], kolichestvo=_12_LE_ist[i],
                                               tip_rashoda="Сопутств. расходы", edinitsy=_12_LE_ed[i], ist = _12_SB[i])
        if _14_LE != empt_mass:
            for i in range(len(_14_LE)):
                if len(_14_LE[i]) > 32:
                    widget_cena.FLAG_LowREG = 1

                if len(_14_LE[i]) > 40:
                    o = _14_LE[i]
                    first = o[0:40]
                    first += "\n"
                    counter = 41
                    try:
                        while True:
                            first += o[counter]
                            counter += 1
                    except:
                        pass
                    _14_LE[i] = first

                # меняем > на / для оживления ссылок
                k = "\ "
                k = k.strip()
                buf = ""
                for i in range(len(_14_SB)):
                    for iopt in _14_SB[i]:
                        if iopt == ">" or iopt == k:
                            buf += "/"
                        else:
                            buf += iopt
                    _14_SB[i] = buf
                    buf = ""
            for i in range(len(_14_SB)):
                widget_cena.add_new_string(self, imya_el=_14_LE[i], kolichestvo=_14_LE_ist[i],
                                               tip_rashoda="Элем. для ремонта", ist = _14_SB[i])

        if UI_MEZ.FLAG_nado_li_otpr_otcet_o_vstuplenii == 1:
            # UI_MEZ.FLAG_nado_li_otpr_otcet_o_vstuplenii = 0
            from ui_add_new_elements import widget_begin
            from client import CLIENT
            CLIENT.nomer_proecta = widget_begin.zakaz_nomer
            CLIENT.MEZ.vstupit_v_uzn_cen()
        #"""
    #внутри проекта:перейти к узнанию цен
    def HANDLER_MEZ_pushButton_57(self):
        #вкл чекбокс подтверждения входа
        self.checkBox_36.setEnabled(True)
        # для того, как заказ не взят мезом
        status = ""
        from ui_add_new_elements import widget_begin
        txt = "../pythonProject3/DATABASE/current_project/_" + widget_begin.zakaz_nomer.strip() + ".txt"
        # узнаем статус проекта и имя взявшегося
        print(txt)
        with open(txt, 'r') as file:
            for index, line in enumerate(file):
                if index == 19:
                    status = line.strip()
                    break
        print(status)
        self.stackedWidget.setCurrentIndex(11)
        if status == "Ожидание цен закупа":
            self.label_243.hide()
            self.label_244.hide()
            self.label_245.hide()
            self.scrollArea_16.hide()

            self.frame_16.setMinimumHeight(480)
            self.frame_16.setMaximumHeight(480)
            self.pushButton_117.setDisabled(True)
        if status == "Цены закупа в процессе":
            imechko = ""
            with open(txt, 'r') as file:
                for index, line in enumerate(file):
                    if index == 26:
                        imechko = line.strip()
            print("imechko", imechko)

            from client import CLIENT
            if imechko == CLIENT.pravilnost_parola:
                print("pp[]cx")
                UI_MEZ.FLAG_nado_li_otpr_otcet_o_vstuplenii = 0
                UI_MEZ.HANDLER_MEZ_pushButton_117(self)
                UI_MEZ.FLAG_nado_li_otpr_otcet_o_vstuplenii = 1

                self.label_243.show()
                self.label_244.show()
                self.label_245.show()
                self.scrollArea_16.show()

                self.frame_16.setMinimumHeight(1091)
                self.frame_16.setMaximumHeight(1091)
                self.pushButton_116.setDisabled(True)
                self.pushButton_117.setDisabled(True)
            else:
                self.label_243.hide()
                self.label_244.hide()
                self.label_245.hide()
                self.scrollArea_16.hide()

                self.frame_16.setMinimumHeight(480)
                self.frame_16.setMaximumHeight(480)
                self.pushButton_117.setDisabled(True)
                self.checkBox_36.setDisabled(True)
        if status == "Ожидание согласования":
            UI_MEZ.FLAG_nado_li_otpr_otcet_o_vstuplenii = 0
            UI_MEZ.HANDLER_MEZ_pushButton_117(self)
            UI_MEZ.FLAG_nado_li_otpr_otcet_o_vstuplenii = 1
            self.label_243.show()
            self.label_244.show()
            self.label_245.show()
            self.label_240.hide()
            self.scrollArea_16.show()

            self.frame_16.setMinimumHeight(1091)
            self.frame_16.setMaximumHeight(1091)
            self.checkBox_36.setDisabled(True)
            self.checkBox_37.setDisabled(True)
            self.pushButton_116.setDisabled(True)
            self.pushButton_117.setDisabled(True)

            from ui_add_new_elements import widget_begin
            txt = "../pythonProject3/DATABASE/current_project/_" + widget_begin.zakaz_nomer.strip() + ".txt"
            # узнаем строки и заполняем бланк так же, как его заполнил бы мен.закупа
            articuls = []
            cens_sebestoy = []
            cens_prodagi = []
            postavshiki = []
            istochnicki = []

            est_li_na_sklades = []
            dats_dostavki = []
            cens_dostavki = []

            articul = ""
            cena_sebestoy = ""
            cena_prodagi = ""
            postavshik = ""
            istochnick = ""

            est_li_na_sklade = ""
            data_dostavki = ""
            cena_dostavki = ""
            TEXT = ""

            with open(txt, 'r') as file:
                for index, line in enumerate(file):
                    if index == 27:
                        articul = line.strip()
                    if index == 28:
                        cena_sebestoy = line.strip()
                    if index == 29:
                        cena_prodagi = line.strip()
                    if index == 30:
                        postavshik = line.strip()
                    if index == 31:
                        istochnick = line.strip()
                    if index == 32:
                        est_li_na_sklade = line.strip()
                    if index == 33:
                        data_dostavki = line.strip()
                    if index == 34:
                        cena_dostavki = line.strip()
                    if index == 35:
                        TEXT = line.strip()

            buf = ""
            #разбераем строки на массивы
            #articul
            for counter in range(len(articul)):
                if articul[counter] != "?":
                    buf += articul[counter]
                else:
                    articuls.append(buf)
                    buf = ""
            # cena_sebestoy
            for counter in range(len(cena_sebestoy)):
                if cena_sebestoy[counter] != "?":
                    buf += cena_sebestoy[counter]
                else:
                    cens_sebestoy.append(buf)
                    buf = ""
            # cena_prodagi
            for counter in range(len(cena_prodagi)):
                if cena_prodagi[counter] != "?":
                    buf += cena_prodagi[counter]
                else:
                    cens_prodagi.append(buf)
                    buf = ""
            # postavshik
            for counter in range(len(postavshik)):
                if postavshik[counter] != "?":
                    buf += postavshik[counter]
                else:
                    postavshiki.append(buf)
                    buf = ""
            # istochnick
            for counter in range(len(istochnick)):
                if istochnick[counter] != "?":
                    buf += istochnick[counter]
                else:
                    istochnicki.append(buf)
                    buf = ""
            # est_li_na_sklade
            for counter in range(len(est_li_na_sklade)):
                if est_li_na_sklade[counter] != "?":
                    buf += est_li_na_sklade[counter]
                else:
                    est_li_na_sklades.append(buf)
                    buf = ""
            # data_dostavki
            for counter in range(len(data_dostavki)):
                if data_dostavki[counter] != "?":
                    buf += data_dostavki[counter]
                else:
                    dats_dostavki.append(buf)
                    buf = ""
            # cena_dostavki
            for counter in range(len(cena_dostavki)):
                if cena_dostavki[counter] != "?":
                    buf += cena_dostavki[counter]
                else:
                    cens_dostavki.append(buf)
                    buf = ""
            print("     Восстанавливаем архивную последовательность данных, введенных мен. закупа:")
            print("         articuls:           ",articuls)
            print("         cens_sebestoy:      ",cens_sebestoy)
            print("         cens_prodagi:       ",cens_prodagi)
            print("         postavshiki:        ",postavshiki)
            print("         istochnicki:        ",istochnicki)
            print("         est_li_na_sklades:  ",est_li_na_sklades)
            print("         dats_dostavki:      ",dats_dostavki)
            print("         cens_dostavki:      ",cens_dostavki)

            from ui_add_new_elements import widget_cena
            buf = ""
            k = "\ "
            k = k.strip()
            for i in TEXT:
                if i == k:
                    buf += "\n"
                else:
                    buf += i

            self.textEdit_9.setText(buf)
            self.textEdit_9.setDisabled(True)
            for i in range(len(articuls)):
                widget_cena.Articul[i].setText(articuls[i])
                widget_cena.Articul[i].setDisabled(True)
                widget_cena.cena_sebestoy[i].setText(cens_sebestoy[i])
                widget_cena.cena_sebestoy[i].setDisabled(True)
                widget_cena.cena_prodagi[i].setText(cens_prodagi[i])
                widget_cena.cena_prodagi[i].setDisabled(True)
                widget_cena.postavshik[i].setText(postavshiki[i])
                widget_cena.postavshik[i].setDisabled(True)
                widget_cena.Istochnic[i].setText(istochnicki[i])
                widget_cena.Istochnic[i].setDisabled(True)
                if est_li_na_sklades[i] == "Da":
                    widget_cena.checkBoxs[i].checkStateSet()
                    widget_cena.checkBoxs[i].setDisabled(True)
                    # self.checkBox_37
                widget_cena.data_dostavki[i].setText(dats_dostavki[i])
                widget_cena.data_dostavki[i].setDisabled(True)
                widget_cena.cena_dostavki[i].setText(cens_dostavki[i])
                widget_cena.cena_dostavki[i].setDisabled(True)


    #поле узнавания цен:чекбокс подтверждения входа в заказ
    # def HANDLER_MEZ_(self):
    # checkBox подтвердить вступление в проект
    flag_podtverzdayu_36 = 0
    def HANDLER_MEN_checkBox_36(self):
        if UI_MEZ.flag_podtverzdayu_36 == 0:
            UI_MEZ.flag_podtverzdayu_36 = 1
            self.pushButton_117.setEnabled(True)
            return
        if UI_MEZ.flag_podtverzdayu_36 == 1:
            UI_MEZ.flag_podtverzdayu_36 = 0
            self.pushButton_117.setDisabled(True)

    # checkBox подтвердить завершение узнавания цен
    flag_podtverzdayu_37 = 0
    def HANDLER_MEN_checkBox_37(self):
        if UI_MEZ.flag_podtverzdayu_37 == 0:
            UI_MEZ.flag_podtverzdayu_37 = 1
            self.pushButton_116.setEnabled(True)
            return
        if UI_MEZ.flag_podtverzdayu_37 == 1:
            UI_MEZ.flag_podtverzdayu_37 = 0
            self.pushButton_116.setDisabled(True)

    def HANDLER_MEZ_pushButton_116(self):
        from ui_add_new_elements import widget_cena
        articuls = []
        cens_sebestoy = []
        cens_prodagi = []
        postavshiki = []
        istochnicki = []

        est_li_na_sklade = []
        dats_dostavki = []
        cens_dostavki = []

        FLAG_chistih_poley = 0
        for i in widget_cena.Articul:
            if i.text() == "":
                i.setFocus()
                i.setStyleSheet(
                    "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
                FLAG_chistih_poley += 1
            else:
                i.setStyleSheet(
                        "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
            articuls.append(i.text())
        for i in widget_cena.cena_sebestoy:
            if i.text() == "":
                i.setFocus()
                i.setStyleSheet(
                    "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
                FLAG_chistih_poley += 1
            else:
                i.setStyleSheet(
                        "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
            cens_sebestoy.append(i.text())
        for i in widget_cena.cena_prodagi:
            if i.text() == "":
                i.setFocus()
                i.setStyleSheet(
                    "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
                FLAG_chistih_poley += 1
            else:
                i.setStyleSheet(
                        "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
            cens_prodagi.append(i.text())
        for i in widget_cena.postavshik:
            if i.text() == "":
                i.setFocus()
                i.setStyleSheet(
                    "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
                FLAG_chistih_poley += 1
            else:
                i.setStyleSheet(
                        "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
            postavshiki.append(i.text())
        for i in widget_cena.Istochnic:
            if i.text() == "":
                i.setFocus()
                i.setStyleSheet(
                    "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
                FLAG_chistih_poley += 1
            else:
                i.setStyleSheet(
                        "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
            istochnicki.append(i.text())
        for i in widget_cena.checkBoxs:
            # self.checkBox_36
            if i.isChecked() == False:
                est_li_na_sklade.append("Net")
            if i.isChecked() == True:
                est_li_na_sklade.append("Da")
        for i in widget_cena.data_dostavki:
            if i.text() == "":
                i.setFocus()
                i.setStyleSheet(
                    "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
                FLAG_chistih_poley += 1
            else:
                i.setStyleSheet(
                        "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
            dats_dostavki.append(i.text())
        for i in widget_cena.cena_dostavki:
            if i.text() == "":
                i.setFocus()
                i.setStyleSheet(
                    "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);\nbackground-color: rgb(220, 54, 20);")
                FLAG_chistih_poley += 1
            else:
                i.setStyleSheet(
                        "border: 1px solid rgb(109, 65, 12);\nborder-radius: 5px;\ncolor: rgb(109, 65, 12);")
            cens_dostavki.append(i.text())
        print("articuls",articuls)
        print("cens_sebestoy",cens_sebestoy)
        print("cens_prodagi",cens_prodagi)
        print("postavshiki",postavshiki)
        print("istochnicki",istochnicki)

        print("est_li_na_sklade",est_li_na_sklade)
        print("dats_dostavki",dats_dostavki)
        print("cens_dostavki",cens_dostavki)

        if FLAG_chistih_poley > 0:
            self.pushButton_116.setStyleSheet("#pushButton_116\n"
                                            "{\n"
                                            "\n"
                                            "    color: rgb(36, 21, 3);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_116:hover\n"
                                            "{\n"
                                            "color: rgb(118, 91, 62);\n"
                                            "background-color: rgb(220, 54, 20);\n"
                                            "border-radius: 5px;\n"
                                            "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                            "border-right: 1px solid rgb(98, 71, 50);\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_116:pressed\n"
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
            self.label_247.show()
            self.label_248.show()
            self.label_248.setText(str(FLAG_chistih_poley))
        else:
            self.pushButton_116.setStyleSheet("#pushButton_116\n"
                                              "{\n"
                                              "color: rgb(98, 71, 42);\n"
                                              "background-color: rgb(197, 147, 86);\n"
                                              "border-radius: 5px;\n"
                                              "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                              "border-right: 1px solid rgb(98, 71, 50);\n"
                                              "}\n"
                                              "\n"
                                              "#pushButton_116:hover\n"
                                              "{\n"
                                              "color: rgb(118, 91, 62);\n"
                                              "background-color: rgb(177, 127, 66);\n"
                                              "border-radius: 5px;\n"
                                              "border-bottom: 3px solid rgb(98, 71, 50);\n"
                                              "border-right: 1px solid rgb(98, 71, 50);\n"
                                              "}\n"
                                              "\n"
                                              "#pushButton_116:pressed\n"
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
            from client import CLIENT
            from ui_add_new_elements import widget_begin
            CLIENT.nomer_proecta = widget_begin.zakaz_nomer
            CLIENT.MEZ.zakonchit_diagnosticu(articuls,cens_sebestoy,cens_prodagi,postavshiki,istochnicki,est_li_na_sklade,dats_dostavki,cens_dostavki,text_comment = self.textEdit_9.toPlainText())
            self.stackedWidget.setCurrentIndex(1)
