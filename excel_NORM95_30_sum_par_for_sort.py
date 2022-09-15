import os
import re
import xlwings as xw

path = ""
os.chdir(path)
wb = xw.Book('NORM95_SUM.xlsx')
sht = wb.sheets['NORMINV_0.05_30']
sht.activate()

sht.range('C1').value = 'back_len'
sht.range('D1').value = 'n_hidden'
sht.range('E1').value = 'dropout'
sht.range('F1').value = 'in_neuron'
sht.range('G1').value = 'in_neuron_num'

for x in range(2, 49):
    cell_text = sht.range('A%s' % x).value
    split_text = re.split('_|y', cell_text)
    print(split_text)
    sht.range('C%s' % x).value = split_text[1]
    sht.range('D%s' % x).value = split_text[3]
    sht.range('E%s' % x).value = split_text[4]
    if split_text[7] == 's':
        sht.range('F%s' % x).value = 'q1+q2'
        sht.range('G%s' % x).value = 2
    elif split_text[7] == 'r':
        sht.range('F%s' % x).value = 'q1+r'
        sht.range('G%s' % x).value = 1
    elif split_text[7] == 'h2':
        sht.range('F%s' % x).value = 'q1+q2+r'
        sht.range('G%s' % x).value = 3
    else:
        sht.range('F%s' % x).value = 'q1+q2+r+t'
        sht.range('G%s' % x).value = 4

wb.save()
wb.app.quit()
