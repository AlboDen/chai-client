import socket

class CLIENT():
    adr = ('127.0.0.1', 8889)


    pravilnost_parola = ""
    input_login = ""
    input_dol = ""
    input_parol = ""
    def request_for_server():

        # login1 = input("Imput Your login:   ")
        login1 = CLIENT.input_login
        login = login1.strip()

        # parol1 = input("Imput Your parol:   ")
        parol1 = CLIENT.input_parol
        parol = parol1.strip()

        # dol1 = input("Imput Your dol:   ")
        dol1 = CLIENT.input_dol
        dol = dol1.strip()

        import datetime
        now = str(datetime.datetime.now())
        # 2021-08-06 22:45:02.522446
        year = now[0:4]
        mounth = now[5:7]
        day = now[8:10]
        hour = now[11:13]
        minut = now[14:16]

        time_request = day + "." + mounth + "." + year + hour + ":" + minut + "1234567890123456_PAROL"

        impute = time_request + f"_{login}_{parol}_{dol}_"
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(CLIENT.adr)
            s.sendall(impute.encode())
            print("1 answer ",s.recv(1024).decode())
            CLIENT.pravilnost_parola = s.recv(1024).decode()

            print("2 answer name of client ",CLIENT.pravilnost_parola)
            CLIENT.imya_menedgera = CLIENT.pravilnost_parola

            # impute = 02.01.202020:00_03.01.202012:00_PAROL   32:37

    ##################INPUT DATA#####################
    FamiliyaImyaOtchestvo = "Petrischenko Fyodor Yuryevich"
    Dolgnost = "MEN"
    Login = "popa"
    Parol = "dopa"
    zapret_na_sozdanie_acc = ""

    def request_for_create_acc():

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(CLIENT.adr)
            port = s.getsockname()[1]
            ip = s.getsockname()[0]

            FamiliyaImyaOtchestvo = CLIENT.FamiliyaImyaOtchestvo
            Dolgnost = CLIENT.Dolgnost
            Login = CLIENT.Login
            Parol = CLIENT.Parol

            import datetime
            now = str(datetime.datetime.now())
            #2021-08-06 22:45:02.522446
            year = now[0:4]
            mounth = now[5:7]
            day = now[8:10]
            hour = now[11:13]
            minut = now[14:16]

            time_request = day+"."+mounth+"."+year+" "+hour+":"+minut
            print("time_request",time_request)
                        #   16        1       3        1              x
            send_str = time_request +"?" + Dolgnost + "?" +"xxxxxxxxxxxADDAC_"+FamiliyaImyaOtchestvo + "?" + Login +"?"+ Parol +"?"
            
            print("Sending pocket:  ",send_str)
            s.sendall(send_str.encode())

            CLIENT.zapret_na_sozdanie_acc = s.recv(1024).decode()
            CLIENT.zapret_na_sozdanie_acc = s.recv(1024).decode()
            print("Разрешение на создание от системы списков: ",CLIENT.zapret_na_sozdanie_acc)

    ##GETFL
    def get_all_files():
        print("GEtting files...")
        string_of_all_files = ""

        import datetime
        now = str(datetime.datetime.now())
        # 2021-08-06 22:45:02.522446
        year = now[0:4]
        mounth = now[5:7]
        day = now[8:10]
        hour = now[11:13]
        minut = now[14:16]

        time_request = day + "." + mounth + "." + year + " " + hour + ":" + minut
        print("time_request", time_request)
        print("     Opening socket...")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(CLIENT.adr)
            str_for_send = time_request + "xxxxxxxxxxxxxxxx" + "GETFL"
            print("     Sending pocket...")
            s.sendall(str_for_send.encode())
            text = s.recv(100).decode()
            print("text: ",text)
            text = s.recv(10000).decode()
            # print("text: ", text)
            print("     Init/Reinit all-file...")
            with open("..\pythonProject3\DATABASE\oll_project.txt", 'w') as file:
                file.write("")
            print("     Saving pocket...")
            with open("..\pythonProject3\DATABASE\oll_project.txt", 'a') as file:
                file.write(text)

        file_name = ""
        cur_file = ""
        import os
        name = os.listdir("../pythonProject3/DATABASE/current_project")
        for n in name:
            os.remove(f"../pythonProject3/DATABASE/current_project/{n}")

        with open("..\pythonProject3\DATABASE\oll_project.txt", 'r') as file:
            for index, line in enumerate(file):
                if "" == "":
                    if str(line[0:3]) == "###":
                        counter = 3
                        file_name = ""
                        try:
                            while True:
                                if line[counter] != "\n":
                                    file_name += line[counter]

                                else:
                                    break
                                counter += 1
                        except:
                            pass
                        path = "..\pythonProject3\DATABASE\current_project\_"
                        path.strip()
                        path += file_name.strip()
                        path += ".txt"
                        with open(path, 'w') as file:
                            file.write("")
                        cur_file = path
                    else:
                        with open(cur_file, 'a') as file:
                            file.write(line)
        try:
            os.remove("../pythonProject3/DATABASE/current_project/_.txt")
        except OSError:
            pass


    ##NEWPJ
    ##################INPUT DATA#####################
    nomer_proecta = "#66666"
    data_sozdaniya_proecta = "07.08.2021"

    imya_menedgera = "Ivanov Pyotir Grigirievich"

    name_of_organisation = 'OOO "Deputati pricamiya"'
    elect_pochta_of_contact_face = "lolkekcheburek@mail.ru"
    number_time_for_end = "20.20.2200"

    INN = "28821"
    KPP = "1"
    number_of_contact_face = "89194467425"
    name_of_contact_face = "Lyolik Bolick Alcogolick"

    adress_of_organisation = "c. Russia g.Perm ul.Donkihota 69-97"
    oborudovanie = "555-Yodik"
    seriyniy_nomer = '123-5946'
    kodovoye_nazvanie = 'ATMig456'
    kolichestvo = '2'
    edinitsy = 'bloka'
    nomer_sticker_plomby = '15975/1-2'
    komplektatia = '- momo 1 sht;}- gigi 2 sht;}'
    opisanie_neispravnosti_ot_zakazchika = 'ne rabotayet'
    input_meh_destroy = 'v krishke zastrial topor'

    status_remonta = 'Remont'
    dogovor_podpisan = 'da'

    otvet_na_zapros_sozdaniya = ""
    def create_new_project():
        import datetime
        now = str(datetime.datetime.now())
        # 2021-08-06 22:45:02.522446
        year = now[0:4]
        mounth = now[5:7]
        day = now[8:10]
        hour = now[11:13]
        minut = now[14:16]
        time_request = day + "." + mounth + "." + year + " " + hour + ":" + minut
        print("time_request", time_request)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(CLIENT.adr)
        #     s.sendall(impute.encode())
        # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #     print("5")
        #     s.connect(CLIENT.adr)


            str_for_send = time_request + "xxxxxxxxxxxxxxxx" + "NEWPJ"
            s.sendall(str_for_send.encode())
            # print("str_for_send",str_for_send)
            text = s.recv(100).decode()
            print("1 ans: ",text)
            str_for_send = str(CLIENT.nomer_proecta) + "?" + str(CLIENT.data_sozdaniya_proecta) + "?" + str(CLIENT.imya_menedgera) + "?" + str(CLIENT.name_of_organisation) + "?" + str(CLIENT.elect_pochta_of_contact_face) + "?" + str(CLIENT.number_time_for_end) + "?" + str(CLIENT.INN) + "?" + str(CLIENT.KPP) + "?" + str(CLIENT.number_of_contact_face) + "?" + str(CLIENT.name_of_contact_face) + "?" + str(CLIENT.adress_of_organisation) + "?" + str(CLIENT.oborudovanie) + "?" + str(CLIENT.seriyniy_nomer) + "?" + str(CLIENT.kodovoye_nazvanie) + "?" + str(CLIENT.kolichestvo) + "?" + str(CLIENT.edinitsy) + "?" + str(CLIENT.nomer_sticker_plomby) + "?" + str(CLIENT.komplektatia) + "?" + str(CLIENT.opisanie_neispravnosti_ot_zakazchika) + "?" + str(CLIENT.input_meh_destroy) + "?" + str(CLIENT.status_remonta) + "?" + str(CLIENT.dogovor_podpisan) + "?"
            # print("String for send: ", str_for_send)
            s.sendall(str_for_send.encode())
            text = s.recv(100).decode()
            print("2 ans: ", text)
            CLIENT.otvet_na_zapros_sozdaniya = text

    class INJ():
        def vstupit_v_diagnosticu():
            parol = CLIENT.input_parol.strip()
            login = CLIENT.input_login.strip()
            dol = CLIENT.input_dol
            nomer_zakaza = CLIENT.nomer_proecta

            import datetime
            now = str(datetime.datetime.now())
            # 2021-08-06 22:45:02.522446
            year = now[0:4]
            mounth = now[5:7]
            day = now[8:10]
            hour = now[11:13]
            minut = now[14:16]
            time_request = day + "." + mounth + "." + year + " " + hour + ":" + minut
            print("time_request", time_request)

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(CLIENT.adr)
                str_for_send = time_request + "xxxxxxxxxxxxxxxx" + "NaDIA" + login + "?" + parol +"?"+dol +"?"+nomer_zakaza
                s.sendall(str_for_send.encode())
                popopl = s.recv(1024).decode()
                print("ans 1 ok:",popopl)

        text_textEdit_8 = ""
        def zakonchit_diagnosticu():
            parol = CLIENT.input_parol.strip()
            login = CLIENT.input_login.strip()
            dol = CLIENT.input_dol
            nomer_zakaza = CLIENT.nomer_proecta

            import datetime
            now = str(datetime.datetime.now())
            # 2021-08-06 22:45:02.522446
            year = now[0:4]
            mounth = now[5:7]
            day = now[8:10]
            hour = now[11:13]
            minut = now[14:16]
            time_request = day + "." + mounth + "." + year + " " + hour + ":" + minut
            print("time_request", time_request)

            #получаем введ. данные


            pocket = ""

            from ui_add_new_elements import widget_11,widget_12,widget_14
            buf = ""
            k = "\ "
            k = k.strip()
            for i in range(len(widget_11.outputDATA_from_LE_ist)):
                for iopt in widget_11.outputDATA_from_LE_ist[i]:
                    if iopt == "/" or iopt == k:
                        buf += ">"
                    else:
                        buf += iopt
                widget_11.outputDATA_from_LE_ist[i] = buf
                buf = ""
            for i in range(len(widget_12.outputDATA_from_LE_ist)):
                for iopt in widget_12.outputDATA_from_LE_ist[i]:
                    if iopt == "/" or iopt == k:
                        buf += ">"
                    else:
                        buf += iopt
                widget_12.outputDATA_from_LE_ist[i] = buf
                buf = ""
            for i in range(len(widget_14.outputDATA_from_LE_ist)):
                for iopt in widget_14.outputDATA_from_LE_ist[i]:
                    if iopt == "/" or iopt == k:
                        buf += ">"
                    else:
                        buf += iopt
                widget_14.outputDATA_from_LE_ist[i] = buf
                buf = ""


            pocket += "/?/"
            if "Текст эдит раскошеливаем на текст"!="":
                from ui_add_new_elements import widget_11,widget_12,widget_14
                text_withOUT_enters = ""
                counter = 0
                try:
                    while True:
                        if CLIENT.INJ.text_textEdit_8[counter] != "\n":
                            text_withOUT_enters += CLIENT.INJ.text_textEdit_8[counter]
                        else:
                            k = "\ "
                            text_withOUT_enters += k.strip()
                        counter += 1
                except:
                    k = "\ "
                    text_withOUT_enters += k.strip()
                print(text_withOUT_enters)
            pocket += text_withOUT_enters
            pocket += "/?/"
            for i in range(len(widget_11.outputDATA_from_LE)):
                if widget_11.outputDATA_from_SpinBox[i] != "0" and widget_11.outputDATA_from_LE[i].strip() != "":
                    pocket += widget_11.outputDATA_from_LE[i]
                    cj = "\ "
                    pocket += cj.strip()
                    pocket += widget_11.outputDATA_from_LE_ist[i]
                    cj = "\ "
                    pocket += cj.strip()
                    pocket += widget_11.outputDATA_from_SpinBox[i]

                    cj = "\ "
                    pocket += cj.strip()
                    cj = "\ "
                    pocket += cj.strip()
            print("pocket после 11 добвылениея",pocket)
            pocket += "/?/"
            for i in range(len(widget_12.outputDATA_from_LE)):
                if widget_12.outputDATA_from_SpinBox[i] != "0" and widget_12.outputDATA_from_LE[i].strip() != "" and widget_12.outputDATA_from_LE_Edinitsy[i].strip() != "":
                    pocket += widget_12.outputDATA_from_LE[i]
                    cj = "\ "
                    pocket += cj.strip()
                    pocket += widget_12.outputDATA_from_LE_ist[i]
                    cj = "\ "
                    pocket += cj.strip()
                    pocket += widget_12.outputDATA_from_SpinBox[i]
                    cj = "\ "
                    pocket += cj.strip()
                    pocket += widget_12.outputDATA_from_LE_Edinitsy[i]
                    cj = "\ "
                    pocket += cj.strip()
            pocket += "/?/"
            print("pocket после 12 добвылениея", pocket)
            print(widget_14.outputDATA_from_LE)
            print(widget_14.outputDATA_from_LE_ist)
            print(widget_14.outputDATA_from_SpinBox)
            for i in range(len(widget_14.outputDATA_from_LE)):
                if widget_14.outputDATA_from_SpinBox[i] != "0" and widget_14.outputDATA_from_LE[i].strip() != "":
                    pocket += widget_14.outputDATA_from_LE[i]
                    cj = "\ "
                    pocket += cj.strip()
                    pocket += widget_14.outputDATA_from_LE_ist[i]
                    cj = "\ "
                    pocket += cj.strip()
                    pocket += widget_14.outputDATA_from_SpinBox[i]
                    cj = "\ "
                    pocket += cj.strip()
                    cj = "\ "
                    pocket += cj.strip()
            pocket += "/?/"
            print("pocket после 14 добвылениея",pocket)

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(CLIENT.adr)
                str_for_send = time_request + "xxxxxxxxxxxxxxxx" + "ZaDIA" + login + "?" + parol +"?"+dol +"?"+nomer_zakaza\
                               +"?"+pocket

                s.sendall(str_for_send.encode())
                popopl = s.recv(1024).decode()
                print("ans 1 ok:",popopl)

    class MEZ():
        def vstupit_v_uzn_cen():
            parol = CLIENT.input_parol.strip()
            login = CLIENT.input_login.strip()
            dol = CLIENT.input_dol
            nomer_zakaza = CLIENT.nomer_proecta

            import datetime
            now = str(datetime.datetime.now())
            # 2021-08-06 22:45:02.522446
            year = now[0:4]
            mounth = now[5:7]
            day = now[8:10]
            hour = now[11:13]
            minut = now[14:16]
            time_request = day + "." + mounth + "." + year + " " + hour + ":" + minut
            print("time_request", time_request)

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(CLIENT.adr)
                str_for_send = time_request + "xxxxxxxxxxxxxxxx" + "NaCEN" + login + "?" + parol + "?" + dol + "?" + nomer_zakaza
                s.sendall(str_for_send.encode())
                popopl = s.recv(1024).decode()
                print("ans 1 ok:", popopl)
        def zakonchit_diagnosticu(articuls,cens_sebestoy,cens_prodagi,postavshiki,istochnicki,est_li_na_sklade,dats_dostavki,cens_dostavki,text_comment):
            parol = CLIENT.input_parol.strip()
            login = CLIENT.input_login.strip()
            dol = CLIENT.input_dol
            nomer_zakaza = CLIENT.nomer_proecta

            import datetime
            now = str(datetime.datetime.now())
            # 2021-08-06 22:45:02.522446
            year = now[0:4]
            mounth = now[5:7]
            day = now[8:10]
            hour = now[11:13]
            minut = now[14:16]
            time_request = day + "." + mounth + "." + year + " " + hour + ":" + minut
            print("time_request", time_request)

            #получаем введ. данные


            pocket = ""
            if "записываем из массивов в одноименные строки данные"!="":
                from ui_add_new_elements import widget_cena
                articuls_text_withOUT_enters = ""
                cens_sebestoy_text_withOUT_enters = ""
                cens_prodagi_text_withOUT_enters = ""
                postavshiki_text_withOUT_enters = ""
                istochnicki_text_withOUT_enters = ""
                est_li_na_sklade_text_withOUT_enters = ""
                dats_dostavki_text_withOUT_enters = ""
                cens_dostavki_text_withOUT_enters = ""

                for i in range(len(widget_cena.Articul)):
                    q = articuls[i] + "?"
                    articuls_text_withOUT_enters += q
                    q = cens_sebestoy[i] + "?"
                    cens_sebestoy_text_withOUT_enters += q
                    q = cens_prodagi[i] + "?"
                    cens_prodagi_text_withOUT_enters += q
                    q = postavshiki[i] + "?"
                    postavshiki_text_withOUT_enters += q
                    q = istochnicki[i] + "?"
                    istochnicki_text_withOUT_enters += q
                    q = est_li_na_sklade[i] + "?"
                    est_li_na_sklade_text_withOUT_enters += q
                    q = dats_dostavki[i] + "?"
                    dats_dostavki_text_withOUT_enters += q
                    q = cens_dostavki[i] + "?"
                    cens_dostavki_text_withOUT_enters += q
                articuls_text_withOUT_enters += "\n"
                cens_sebestoy_text_withOUT_enters += "\n"
                cens_prodagi_text_withOUT_enters += "\n"
                postavshiki_text_withOUT_enters += "\n"
                istochnicki_text_withOUT_enters += "\n"
                est_li_na_sklade_text_withOUT_enters += "\n"
                dats_dostavki_text_withOUT_enters += "\n"
                cens_dostavki_text_withOUT_enters += "\n"
                textCOMM = text_comment+"\n"
            pocket += articuls_text_withOUT_enters
            pocket += cens_sebestoy_text_withOUT_enters
            pocket += cens_prodagi_text_withOUT_enters
            pocket += postavshiki_text_withOUT_enters
            pocket += istochnicki_text_withOUT_enters
            pocket += est_li_na_sklade_text_withOUT_enters
            pocket += dats_dostavki_text_withOUT_enters
            pocket += cens_dostavki_text_withOUT_enters
            pocket += textCOMM

            print("pocket ",pocket)

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(CLIENT.adr)
                str_for_send = time_request + "xxxxxxxxxxxxxxxx" + "ZaCEN" + login + "?" + parol +"?"+dol +"?"+nomer_zakaza\
                               +"?"+pocket
                s.sendall(str_for_send.encode())
                popopl = s.recv(1024).decode()
                print("ans 1 ok:",popopl)
