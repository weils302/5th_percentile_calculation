import os

import xlwings as xw

back_len = ["24", "168"]  # a
n_hidden = ["20", "50", "100", "200"]  # b
dropout = ["0", "0.01", "0.05", "0.1"]  # c
in_neuron = ["s", "r", "h2", "h3"]  # d

path = ""
os.chdir(path)

new_file = xw.Book()
new_file.save(path + "/" + "NORM95_SUM.xlsx")
n_sht = new_file.sheets["Sheet1"]
n_sht.activate()

count = 1
for a in range(2):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                dir_name = "y%s_24-5_%s_%s_%s_elu_%s" % (back_len[a], n_hidden[b], dropout[c], dropout[c], in_neuron[d])
                if not os.path.exists(dir_name):
                    continue
                n_sht.range("A%s" % (count + 1)).value = dir_name
                new_file.save()
                os.chdir(dir_name)
                print(dir_name)
                wb = xw.Book("nse_elu_NORM95.xlsx")
                sht = wb.sheets["nse_elu"]
                sht.activate()
                n_sht.range("B%s" % (count + 1)).value = sht.range("AS30").value
                wb.close()
                os.chdir("..")
                count = count + 1

new_file.save()
new_file.app.quit()
