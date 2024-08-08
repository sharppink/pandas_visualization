import csv
data_file = open('c:/Temp/PANDASPLOTLY_FUNCODING_FULLDATA_20240601/00_Material(Uploaded)/00_data/USvideos.csv', 'r', encoding ='utf-8-sig')
data_lines = csv.reader(data_file, delimiter=',')

for data_line in data_lines:
    print(data_line[0])
    break

data_file.close()