import csv
def main():
    f = open('202303_Seoul_Subway.csv', 'r', encoding='utf-8')
    data = csv.reader(f, delimiter=',')
    header = next(data)
    line1 = ['', 0, '', 0]
    line2 = ['', 0, '', 0]
    line3 = ['', 0, '', 0]
    line4 = ['', 0, '', 0]
    for row in data:
        row = list(map(lambda s : ''.join(s.split()), row))
        if (row[1] == '1호선'):
            psg = 0
            psg += int(row[4])
            psg += int(row[5])

            if psg > line1[1]:
                line1[1] = psg
                line1[0] = row[3]
            if line1[3] == 0:
                line1[3] = psg
                line1[2] = row[3]
            elif psg < line1[3]:
                line1[3] = psg
                line1[2] = row[3]
        elif (row[1] == '2호선'):
            psg = 0
            psg += int(row[4])
            psg += int(row[5])
            if psg > line2[1]:
                line2[1] = psg
                line2[0] = row[3]
            if line2[3] == 0:
                line2[3] = psg
                line2[2] = row[3]
            elif psg < line2[3]:
                line2[3] = psg
                line2[2] = row[3]
        elif (row[1] == '3호선'):
            psg = 0
            psg += int(row[4])
            psg += int(row[5])
            if psg > line3[1]:
                line3[1] = psg
                line3[0] = row[3]
            if line3[3] == 0:
                line3[3] = psg
                line3[2] = row[3]
            elif psg < line3[3]:
                line3[3] = psg
                line3[2] = row[3]
        elif (row[1] == '4호선'):
            psg = 0
            psg += int(row[4])
            psg += int(row[5])
            if psg > line4[1]:
                line4[1] = psg
                line4[0] = row[3]
            if line4[3] == 0:
                line4[3] = psg
                line4[2] = row[3]
            elif psg < line4[3]:
                line4[3] = psg
                line4[2] = row[3]
    print("*** Subway Report for Seoul on March 2023 ***")
    for i in range(4):
        print ("Line %d:" %(i+1))
        if (i == 0):
            print("Busiest Station: %s" % (line1[0]), "(%d)" % (line1[1]))
            print("Least used Station: %s" % (line1[2]), "(%d)" % (line1[3]))
        elif (i == 1):
            print("Busiest Station: %s" % (line2[0]), "(%d)" % (line2[1]))
            print("Least used Station: %s" % (line2[2]), "(%d)" % (line2[3]))
        elif (i == 2):
            print("Busiest Station: %s" % (line3[0]), "(%d)" % (line3[1]))
            print("Least used Station: %s" % (line3[2]), "(%d)" % (line3[3]))
        elif (i == 3):
            print("Busiest Station: %s" % (line4[0]), "(%d)" % (line4[1]))
            print("Least used Station: %s" % (line4[2]), "(%d)" % (line4[3]))

    f.close()

main()
