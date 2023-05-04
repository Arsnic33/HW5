import csv
def main():
    f = open('2022_Seoul_Temp.csv', 'r', encoding='cp949')
    data = csv.reader(f, delimiter=',')
    header = next(data)
    avg = 0.0
    avg_min = 0.0
    avg_max = 0.0
    count = 0
    for row in data:
        row = list(map(lambda s : ''.join(s.split()), row))
        if (row[2] == '') or (row[3] == '') or (row[4] == ''):
            continue
        count += 1
        avg += float(row[2])
        avg_min += float(row[3])
        avg_max += float(row[4])

    print("*** Annual Temperature Report for Seoul in 2022 ***")
    print("Average Temperature: %.2f" % (avg / count), "Celsius")
    print("Average Minimum Temperature: %.2f" % (avg_min / count), "Celsius")
    print("Average Maximum Temperature: %.2f" % (avg_max / count), "Celsius")
    f.close()

main()
