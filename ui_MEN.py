from w import Ui_MainWindow
# from widget_11 import widget_11
from PyQt5 import QtCore, QtGui, QtWidgets

class UI_MEN(Ui_MainWindow):
    # внутри заказа: переход к диалогу с заказчиком
    FLAG_nado_li_otpr_otcet_o_vstuplenii = 1
    def HANDLER_MEN_pushButton_52(self):
        #отключаем кнопки, требующие подтвержления
        self.pushButton_119.setDisabled(True)
        self.pushButton_68.setDisabled(True)
        #прячем кнопку ответ пришел, до нажатия на кнопку отправить
        self.pushButton_70.hide()

        self.stackedWidget.setCurrentIndex(7)
        status = ""
        from ui_add_new_elements import widget_begin
        txt = "../pythonProject3/DATABASE/current_project/_" + widget_begin.zakaz_nomer.strip() + ".txt"
        # узнаем статус проекта и имя взявшегося
        mass_of_dats = []

        with open(txt, 'r') as file:
            for index, line in enumerate(file):
                if index == 19:
                    status = line.strip()
                    # break
                if index == 33:
                    print("tr33")
                    all_string = line
                    buf = ""
                    for ik in all_string:
                        if ik != "?":
                            buf += ik
                        else:
                            mass_of_dats.append(buf)
                            buf = ""
                    year = 0
                    for i in range(len(mass_of_dats)):
                        if len(mass_of_dats[i]) < 10:
                            mass_of_dats[i] = "0" + mass_of_dats[i]
                        dat = mass_of_dats[i]
                        if year < int(dat[6:10]):
                            year = int(dat[6:10])
                    years = []
                    for i in range(len(mass_of_dats)):
                        l = mass_of_dats[i]
                        if int(l[6:10]) == year:
                            years.append(mass_of_dats[i])
                    mounth = 0
                    for i in range(len(years)):
                        l = years[i]
                        if int(l[3:5]) > mounth:
                            mounth = int(l[3:5])
                    mounths = []
                    for i in range(len(years)):
                        l = years[i]
                        if int(l[3:5]) == mounth:
                            mounths.append(years[i])
                    day = 0
                    for i in range(len(mounths)):
                        l = mounths[i]
                        if int(l[0:2]) > day:
                            day = int(l[0:2])
                    dayk = str(day) +"."+str(mounth)+"."+str(year)
                    self.mensale3_le_sourse_SUM.setText(dayk)
                    print("y:", year, "m:", mounth, "d:", day)
        print("status", status)
        print("mass_of_dats", mass_of_dats)

        if status == "Ожидание согласования":
            if "Заплняем бланк так, как его заполнял инженер и MEZ"!="":
                txt = "../pythonProject3/DATABASE/current_project/_" + widget_begin.zakaz_nomer.strip() + ".txt"
                #строки диагностики
                textEdit_ = ""
                W11_ = ""
                W12_ = ""
                W14_ = ""
                #строки выяснения цен закупа
                Comm_ = ""
                POST_ = ""
                DaDo_ = ""
                CeDo_ = ""
                CePr_ = ""
                CeSe_ = ""
                DaNe_ = ""
                #строки имён
                ING = ""
                MEZ = ""


                with open(txt, 'r') as file:
                    for index, line in enumerate(file):
                        #инженер
                        if index == 22:
                            textEdit_ = line.strip()
                        if index == 23:
                            W11_ = line.strip()
                        if index == 24:
                            W12_ = line.strip()
                        if index == 25:
                            W14_ = line.strip()
                        #мен. закупа
                        if index == 29:
                            CePr_ = line.strip()
                        if index == 30:
                            POST_ = line.strip()
                        if index == 33:
                            DaDo_ = line.strip()
                        if index == 32:
                            DaNe_ = line.strip()
                        if index == 34:
                            CeDo_ = line.strip()
                        if index == 35:
                            Comm_ = line.strip()
                        if index == 28:
                            CeSe_ = line.strip()
                        # имена
                        if index == 26:
                            MEZ = line.strip()
                        if index == 21:
                            ING = line.strip()
                from translater import TRANSLATE
                TRANSLATE.out_str = ""
                TRANSLATE.into_str = ING
                TRANSLATE.eng_in_rus()
                set_str = "Описание результатов диагностики от польз. " +TRANSLATE.out_str.strip()+":"
                self.label_249.setText(set_str)

                TRANSLATE.out_str = ""
                TRANSLATE.into_str = MEZ
                TRANSLATE.eng_in_rus()
                set_str = "Комментарий выяснения цен закупа от польз. " + TRANSLATE.out_str.strip() + ":"
                self.label_250.setText(set_str)

                print("---------------------------------------------------")
                print("То, что надо будет записать от инженера: (4 строки)")
                print("     textEdit_",textEdit_)
                print("     W11_",W11_)
                print("     W12_",W12_)
                print("     W14_",W14_)
                print("То, что надо будет записать от MEZ-a: (6 строк)")
                print("     Comm_",Comm_ )
                print("     POST_",POST_ )
                print("     DaDo_",DaDo_ )
                print("     CeDo_",CeDo_ )
                print("     CePr_",CePr_ )
                print("     CeSe_", CeSe_)
                print("---------------------------------------------------")
                ######

                textEdit_without_entr = ""
                W11_LE = []
                W11_SB = []
                W11_ist = []

                W12_LE = []
                W12_SB = []
                W12_LE_ed = []
                W12_ist = []

                W14_LE = []
                W14_SB = []
                W14_ist = []

                print("Разбиваем тект инженера по массивам:")
                if "Разбераем текст от инженера по массивам"!="":
                    k = "\ "
                    k = k.strip()
                    buf = ""
                    for i in textEdit_:
                        if i != k:
                            buf += i
                        else:
                            buf += "\n"
                    textEdit_without_entr =buf
                    self.textEdit_10.setText(buf)

                    counter = 0
                    text_BUF = ""
                    try:
                        klk = "?"
                        while True:
                            while True:
                                if W11_[counter] != klk:
                                    text_BUF += W11_[counter]
                                else:
                                    W11_LE.append(text_BUF)
                                    text_BUF = ""
                                    counter += 1
                                    break
                                counter += 1
                            while True:
                                if W11_[counter] != klk:
                                    text_BUF += W11_[counter]
                                else:
                                    W11_ist.append(text_BUF)
                                    text_BUF = ""
                                    counter += 1
                                    break
                                counter += 1
                            # counter += 1
                            while True:
                                if W11_[counter] != klk:
                                    text_BUF += W11_[counter]
                                else:
                                    W11_SB.append(text_BUF)
                                    text_BUF = ""
                                    counter += 1
                                    break
                                counter += 1

                    except:
                        print("     W11_LE ",W11_LE)
                        print("     W11_ist", W11_ist)
                        print("     W11_SB ", W11_SB)
                        print("     ----")
                    counter = 0
                    text_BUF = ""
                    try:
                        klk = "?"
                        while True:
                            while True:
                                if W12_[counter] != klk:
                                    text_BUF += W12_[counter]
                                else:
                                    W12_LE.append(text_BUF)
                                    text_BUF = ""
                                    counter += 1
                                    break
                                counter += 1
                            while True:
                                if W12_[counter] != klk:
                                    text_BUF += W12_[counter]
                                else:
                                    W12_ist.append(text_BUF)
                                    text_BUF = ""
                                    counter += 1
                                    break
                                counter += 1

                            # counter += 1
                            while True:
                                if W12_[counter] != klk:
                                    text_BUF += W12_[counter]
                                else:
                                    W12_SB.append(text_BUF)
                                    text_BUF = ""
                                    counter += 1
                                    break
                                counter += 1
                            while True:
                                if W12_[counter] != klk:
                                    text_BUF += W12_[counter]
                                else:
                                    W12_LE_ed.append(text_BUF)
                                    text_BUF = ""
                                    counter += 1
                                    break
                                counter += 1
                    except:
                        print("     W12_LE", W12_LE)
                        print("     W12_ist", W12_ist)
                        print("     W12_SB", W12_SB)
                        print("     W12_LE_ed", W12_LE_ed)
                        print("     ----")
                    counter = 0
                    text_BUF = ""
                    try:
                        klk = "?"
                        while True:
                            while True:
                                if W14_[counter] != klk:
                                    text_BUF += W14_[counter]
                                else:
                                    W14_LE.append(text_BUF)
                                    text_BUF = ""
                                    counter += 1
                                    break
                                counter += 1
                            while True:
                                if W14_[counter] != klk:
                                    text_BUF += W14_[counter]
                                else:
                                    W14_ist.append(text_BUF)
                                    text_BUF = ""
                                    counter += 1
                                    break
                                counter += 1

                            # counter += 1
                            while True:
                                if W14_[counter] != klk:
                                    text_BUF += W14_[counter]
                                else:
                                    W14_SB.append(text_BUF)
                                    text_BUF = ""
                                    counter += 1
                                    break
                                counter += 1
                    except:
                        print("     W14_LE",W14_LE)
                        print("     W14_ist", W14_ist)
                        print("     W14_SB", W14_SB)

                Comm_s =[]
                POST_s = []
                DaDo_s = []
                CeDo_s = []
                CePr_s = []
                CeSe_s = []
                DaNe_s = []
                print("Разбиваем тект мен. закупа по массивам:")
                if "Разбираем текст от мен. закупа по массивам:"!="":
                    k = "\ "
                    k = k.strip()
                    buf = ""
                    for i in Comm_:
                        if i != k:
                            buf += i
                        else:
                            buf += "\n"
                    TXTi = buf
                    self.textEdit_11.setText(buf)

                    buf = ""
                    for i in POST_:
                        if i != "?":
                            buf += i
                        else:
                            POST_s.append(buf)
                            buf = ""
                    POST_s += buf
                    buf = ""
                    for i in DaDo_:
                        if i != "?":
                            buf += i
                        else:
                            DaDo_s.append(buf)
                            buf = ""
                    DaDo_s += buf
                    buf = ""
                    for i in CeDo_:
                        if i != "?":
                            buf += i
                        else:
                            CeDo_s.append(buf)
                            buf = ""
                    CeDo_s += buf
                    buf = ""
                    for i in CePr_:
                        if i != "?":
                            buf += i
                        else:
                            CePr_s.append(buf)
                            buf = ""
                    CePr_s += buf
                    buf = ""
                    for i in CeSe_:
                        if i != "?":
                            buf += i
                        else:
                            CeSe_s.append(buf)
                            buf = ""
                    CeSe_s += buf

                    buf = ""
                    for i in DaNe_:
                        if i != "?":
                            buf += i
                        else:
                            DaNe_s.append(buf)
                            buf = ""
                    DaNe_s += buf
                print("     Commen",TXTi )
                print("     POST_s",POST_s )
                print("     DaDo_s",DaDo_s )
                print("     CeDo_s",CeDo_s )
                print("     CePr_s",CePr_s )
                print("     CeSe_s", CeSe_s)
                print("     DaNe_s", DaNe_s)
                # self.pushButton_15.setEnabled(True)
                _1 = [] #CeDo_s
                _2 = [] #CePr_s
                _3 = [] #CeSe_s
                _1_ = []
                _2_ = []
                _3_ = []
                for i in range(len(CeDo_s)):
                    int_str = CeDo_s[i]
                    buf = ""
                    for o in int_str:
                        if o != ".":
                            buf += o
                        else:
                            _1.append(buf)
                            buf = ""
                    _1_.append(buf)

                    int_str = CePr_s[i]
                    buf = ""
                    for o in int_str:
                        if o != ".":
                            buf += o
                        else:
                            _2.append(buf)
                            buf = ""
                    _2_.append(buf)

                    int_str = CeSe_s[i]
                    buf = ""
                    for o in int_str:
                        if o != ".":
                            buf += o
                        else:
                            _3.append(buf)
                            buf = ""
                    _3_.append(buf)

                print("_1",_1)
                print("_2", _2)
                print("_3", _3)
                print("_1_", _1_)
                print("_2_", _2_)
                print("_3_", _3_)

                _ITog_Cena = []
                _ITog_Cena_ = []
                #где подчеркивание на конце - копейки. все остальное - рубли
                for i in range(len(_1)):
                    g = int(_1[i]) + int(_2[i])
                    _ITog_Cena.append(str(g))
                    g = int(_1_[i]) + int(_2_[i])
                    _ITog_Cena_.append(str(g))
                print("_ITog_Cena",_ITog_Cena)
                print("_ITog_Cena_", _ITog_Cena_)
                try:
                    for i in range(len(_ITog_Cena_)):
                        if len(str(_ITog_Cena_[i])) > 2:
                            k =_ITog_Cena_[i]
                            _ITog_Cena_[i] = k[1:3]
                            in_rub = k[0]
                            _ITog_Cena[i] = str(int(in_rub) + int(_ITog_Cena[i]))
                        if len(str(_ITog_Cena_[i])) == 1:
                            _ITog_Cena_[i] = "0"+_ITog_Cena_[i]
                except:
                    print(";;;")
                _SUM = 0
                SUM = 0
                SBss = W11_SB + W12_SB + W14_SB
                for i in range(len(_ITog_Cena)):
                    _SUM += int(_ITog_Cena[i]) * int(SBss[i])
                for i in range(len(_ITog_Cena_)):
                    SUM += int(_ITog_Cena_[i]) * int(SBss[i])

                if len(str(SUM)) == 3:
                    SUM = str(SUM)
                    _SUM = int(_SUM) + int(SUM[1]) -1
                    SUM = SUM[1:3]

                tgt = str(_SUM) + "." + str(SUM)
                self.mensale3_le_sum_SUM.setText(tgt)

                print("_ITog_Cena SUM", _ITog_Cena)
                print("_ITog_Cena_", _ITog_Cena_)

                ITOGOVAYA_CENA = []
                for i in range(len(_ITog_Cena)):
                    h =_ITog_Cena[i] + "." + _ITog_Cena_[i]
                    ITOGOVAYA_CENA.append(h)
                print("ITOGOVAYA_CENA до умножения на количество элементов",ITOGOVAYA_CENA)

                counter = 0
                print("1591",W11_SB)
                print("1592", W12_SB)
                print("1593", W14_SB)

                for i in W11_SB:
                    print(ITOGOVAYA_CENA[counter])
                    ITOGOVAYA_CENA[counter] = str(int(i) * float(ITOGOVAYA_CENA[counter]))
                    counter += 1
                print("159")
                for i in W12_SB:
                    ITOGOVAYA_CENA[counter] = str(int(i) * float(ITOGOVAYA_CENA[counter]))
                    counter += 1
                for i in W14_SB:
                    ITOGOVAYA_CENA[counter] = str(int(i) * float(ITOGOVAYA_CENA[counter]))
                    counter += 1
                print("ITOGOVAYA_CENA после умножения на количество элементов", ITOGOVAYA_CENA)
                for i in range(len(ITOGOVAYA_CENA)):
                    cou = 0
                    _buf = ""
                    mass = ITOGOVAYA_CENA[i]
                    while True:
                        if mass[cou] == "." or mass[cou] == ",":
                            break
                        _buf += mass[cou]
                        cou += 1

                    cou += 1
                    buf = ""
                    while True:
                        try:
                            buf += mass[cou]
                            cou += 1
                        except:
                            break
                    if len(buf) < 2:
                        ITOGOVAYA_CENA[i] = _buf + "." + buf + "0"
                print("ITOGOVAYA_CENA c добавлением нулей", ITOGOVAYA_CENA)


                from ui_add_new_elements import widget_soglas
                widget_soglas.del_new_string()
                counter_counter = 0
                for i in range(len(W11_LE)):
                    widget_soglas.add_new_string(self,el = W11_LE[i],post = POST_s[counter_counter], data = DaDo_s[counter_counter], CeDo = CeDo_s[counter_counter], CeIt = ITOGOVAYA_CENA[counter_counter],Dane = DaNe_s[counter_counter])
                    counter_counter += 1
                for i in range(len(W12_LE)):
                    widget_soglas.add_new_string(self,el = W12_LE[i],post = POST_s[counter_counter], data = DaDo_s[counter_counter], CeDo = CeDo_s[counter_counter], CeIt = ITOGOVAYA_CENA[counter_counter],Dane = DaNe_s[counter_counter])
                    counter_counter += 1
                for i in range(len(W14_LE)):
                    widget_soglas.add_new_string(self,el = W14_LE[i],post = POST_s[counter_counter], data = DaDo_s[counter_counter], CeDo = CeDo_s[counter_counter], CeIt = ITOGOVAYA_CENA[counter_counter],Dane = DaNe_s[counter_counter])
                    counter_counter += 1


    # внутри экспорта: кнопка экспорта
    def HANDLER_MEN_pushButton_104(self):
        from export import EXPORT
        from ui_add_new_elements import widget_begin
        from ui import UI
        EXPORT.were_save_2 = self.lineEdit_20.text()
        if UI.ACT == 1:
            EXPORT.were_save_2 += "_Act_otcenki.doc"
            imya_oborudovania = ""
            Nomer_acta = ""
            seriyniy_nomer = ""
            opisanie_neispravnosti = ""
            srok_dostavki = ""
            kategoriya_remonta = ""
            No_intable = ""
            Product_name = ""
            skolko = ""
            Edinitsy = ""
            Cena = ""
            Summa = ""
            Stoyemost_bez_nds = ""
            new_oborudivanie = ""
            txt = "../pythonProject3/DATABASE/current_project/_" + widget_begin.zakaz_nomer.strip() + ".txt"
            with open(txt, 'r') as file:
                for index, line in enumerate(file):
                    if index == 10:
                        imya_oborudovania = line
                    if index == 12:
                        seriyniy_nomer = line
                    if index == 18:
                        opisanie_neispravnosti = line
                    if index == 33:
                        all_string = line
                        mass_of_dats = []
                        buf = ""
                        for ik in all_string:
                            if ik != "?":
                                buf += ik
                            else:
                                mass_of_dats.append(buf)
                                buf = ""
                        year = 0
                        for i in range(len(mass_of_dats)):
                            if len(mass_of_dats[i]) < 10:
                                mass_of_dats[i] = "0" + mass_of_dats[i]
                            dat = mass_of_dats[i]
                            if year < int(dat[6:10]):
                                year = int(dat[6:10])
                        years = []
                        for i in range(len(mass_of_dats)):
                            l = mass_of_dats[i]
                            if int(l[6:10]) == year:
                                years.append(mass_of_dats[i])
                        mounth = 0
                        for i in range(len(years)):
                            l = years[i]
                            if int(l[3:5]) > mounth:
                                mounth = int(l[3:5])
                        mounths = []
                        for i in range(len(years)):
                            l = years[i]
                            if int(l[3:5]) == mounth:
                                mounths.append(years[i])
                        day = 0
                        for i in range(len(mounths)):
                            l = mounths[i]
                            if int(l[0:2]) > day:
                                day = int(l[0:2])

                        print("y:",year,"m:",mounth,"d:",day)
                        print("mass_of_dats",mass_of_dats,)
                        srok_dostavki = str(day) +"."+ str(mounth) +"."+ str(year)
                    if index == 10:
                        kategoriya_remonta = line
                    if index == 10:
                        No_intable = "1"
                    if index == 10:
                        Product_name = line
                    if index == 10:
                        skolko = line
                    if index == 10:
                        Edinitsy = line
                    if index == 10:
                        Cena = line
                    if index == 10:
                        Summa = line
                    if index == 10:
                        Stoyemost_bez_nds = line
                    if index == 10:
                        new_oborudivanie = line
                Nomer_acta = widget_begin.zakaz_nomer

            EXPORT.Act_ocenki_teh_sostoyaniya_oborudovaniya(imya_oborudovania=imya_oborudovania,
                                                            Nomer_acta=Nomer_acta,
                                                            seriyniy_nomer=seriyniy_nomer,
                                                            opisanie_neispravnosti=opisanie_neispravnosti,
                                                            srok_dostavki=srok_dostavki,
                                                            kategoriya_remonta=kategoriya_remonta,
                                                            No_intable=No_intable,
                                                            Product_name=Product_name,
                                                            skolko=skolko,
                                                            Edinitsy=Edinitsy,
                                                            Cena=Cena,
                                                            Summa=Summa,
                                                            Stoyemost_bez_nds=Stoyemost_bez_nds,
                                                            new_oborudivanie=new_oborudivanie,
                                                            )

    # внутри диалога с заказчиком:переход к экспорту
    def HANDLER_MEN_pushButton_67(self):
        self.stackedWidget.setCurrentIndex(6)
    # внутри диалога с заказчиком: подтвердить завершение этапа подготовки к согласованиб
    flag_podtverzdayu_30 = 0
    def HANDLER_MEN_checkBox_30(self):
        if UI_MEN.flag_podtverzdayu_30 == 0:
            UI_MEN.flag_podtverzdayu_30 = 1
            self.pushButton_119.setEnabled(True)
            return
        if UI_MEN.flag_podtverzdayu_30 == 1:
            UI_MEN.flag_podtverzdayu_30 = 0
            self.pushButton_119.setDisabled(True)
    # внутри диалога с заказчиком:завершение этапа подготовки к согласованиб
    def HANDLER_MEN_pushButton_119(self):
        pass
    # внутри диалога с заказчиком: подтвердить отправку мэйла
    flag_podtverzdayu_4 = 0
    def HANDLER_MEN_checkBox_4(self):
        if UI_MEN.flag_podtverzdayu_4 == 0:
            UI_MEN.flag_podtverzdayu_4 = 1
            self.pushButton_68.setEnabled(True)
            return
        if UI_MEN.flag_podtverzdayu_4 == 1:
            UI_MEN.flag_podtverzdayu_4 = 0
            self.pushButton_68.setDisabled(True)
    # внутри диалога с заказчиком: отправить мэйл-письмо
    def HANDLER_MEN_pushButton_68(self):
        self.pushButton_70.show()
    # внутри диалога с заказчиком: ответ пришел
    def HANDLER_MEN_pushButton_70(self):
        pass

