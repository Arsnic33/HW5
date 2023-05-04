import csv
def main():
    f = open('202303_Seoul_Subway.csv', 'r', encoding='utf-8')
    data = csv.reader(f, delimiter=',')
    header = next(data)
    psg = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for row in data:
        row = list(map(lambda s : ''.join(s.split()), row))
        if (row[1] == '1호선'):
            psg[0] += int(row[4])
            psg[0] += int(row[5])
        elif (row[1] == '2호선'):
            psg[1] += int(row[4])
            psg[1] += int(row[5])
        elif (row[1] == '3호선'):
            psg[2] += int(row[4])
            psg[2] += int(row[5])
        elif (row[1] == '4호선'):
            psg[3] += int(row[4])
            psg[3] += int(row[5])
        elif (row[1] == '5호선'):
            psg[4] += int(row[4])
            psg[4] += int(row[5])
        elif (row[1] == '6호선'):
            psg[5] += int(row[4])
            psg[5] += int(row[5])
        elif (row[1] == '7호선'):
            psg[6] += int(row[4])
            psg[6] += int(row[5])
        elif (row[1] == '8호선'):
            psg[7] += int(row[4])
            psg[7] += int(row[5])
        elif (row[1] == '9호선'):
            psg[8] += int(row[4])
            psg[8] += int(row[5])

    max_psg = 0
    max_psg_idx = 0
    for i in range(9):
        if max_psg < psg[i]:
            max_psg = psg[i]
            max_psg_idx = i
    print("1st Busiest Line: Line", (max_psg_idx+1), "( %d )" % (max_psg))

    max_psg_2 = 0
    max_psg_2_idx = 0

    for i in range(9):
        if i == max_psg_idx:
            continue
        if max_psg_2 < psg[i]:
            max_psg_2 = psg[i]
            max_psg_2_idx = i
    print("2nd Busiest Line: Line", (max_psg_2_idx+1), "( %d )" % (max_psg_2))

    min_psg = max_psg
    min_psg_idx = 0
    for i in range(9):
        if min_psg > psg[i]:
            min_psg = psg[i]
            min_psg_idx = i
    print("1st Least used Line: Line", (min_psg_idx+1), "( %d )" % (min_psg))

    min_psg_2 = max_psg
    min_psg_2_idx = 0

    for i in range(9):
        if i == min_psg_idx:
            continue
        if min_psg_2 > psg[i]:
            min_psg_2 = psg[i]
            min_psg_2_idx = i
    print("2nd Least used Line: Line", (min_psg_2_idx+1), "( %d )" % (min_psg_2))

    f.close()
    
main()
