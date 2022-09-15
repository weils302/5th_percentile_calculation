import os

import xlwings as xw

back_len = ["24", "168"]  # a
n_hidden = ["20", "50", "100", "200"]  # b
dropout = ["0", "0.01", "0.05", "0.1"]  # c
in_neuron = ["s", "r", "h2", "h3"]  # d

path = ""
os.chdir(path)

for a in range(2):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                dir_name = "y%s_24-5_%s_%s_%s_elu_%s" % (back_len[a], n_hidden[b], dropout[c], dropout[c], in_neuron[d])
                if not os.path.exists(dir_name):
                    continue
                os.chdir(dir_name)
                print(dir_name)
                wb = xw.Book("nse_elu.xlsx")
                sht = wb.sheets["nse_elu"]
                sht.activate()
                for i in range(1, 50):
                    sht.range("AS%s" % i).formula = "=NORM.INV(0.05,AO%s,AP%s)" % (i, i)
                wb.save(path + "/" + dir_name + "/nse_elu_NORM95.xlsx")
                wb.app.quit()
                os.chdir("..")
