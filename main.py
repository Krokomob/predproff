def main():
    """
    1 задача
    Основная функция, ищет вакансии в фирме с максимальным заработком
    """

    f = open('vacancy.csv')
    a = open('vacancy_new.csv', 'w')
    q = []
    s = []
    f.readline()
    d = []
    for line in f:
        line = line.split(';')
        if line[4] not in q:
            q.append(line[4])  # Добавление новой компании
            s.append(line[3])  # Добавление профессии в компании
            d.append(line[0])  # Добавление размера зарплаты
        else:
            ind = q.index(line[4])
            if int(d[ind]) < int(line[0]):  # Проверка размеров зарплат
                d[ind] = line[0]  # Обновление зарплаты в компании
                s[ind] = line[3]  # Обновление профессии в компании
    a.write('company;role;Salary\n')
    for i in range(len(q)):
        a.write(q[i][:-2] + ';' + s[i] + ';' + d[i] + '\n')  # Запись новых данных в файл vacancy_new.csv
    a.close()

    '''
    Нахождение наибольшей зарплаты
    '''
    a = open('vacancy_new.csv')
    a.readline()
    maxx_zp = 0
    maxx_comp = ''
    maxx_prof = ''
    for i in a:
        i = i.split(';')
        if int(maxx_zp) < int(i[2]):
            maxx_zp = i[2]
            maxx_prof = i[1]
            maxx_comp = i[0]
    print(maxx_comp, '-', maxx_prof, '-', maxx_zp)
    a.close()

    '''
    Нахождение второй по величине зарплаты
    '''
    maxx_zp = 0
    maxx_comp = ''
    maxx_prof = ''
    a = open('vacancy_new.csv')
    a.readline()
    for i in a:
        i = i.split(';')
        if int(maxx_zp) < int(i[2]) != 52000:
            maxx_zp = i[2]
            maxx_prof = i[1]
            maxx_comp = i[0]
    print(maxx_comp, '-', maxx_prof, '-', maxx_zp)
    a.close()

    '''
    Нахождение третьей по величине зарплаты
    '''
    maxx_zp = 0
    maxx_comp = ''
    maxx_prof = ''
    a = open('vacancy_new.csv')
    a.readline()
    for i in a:
        i = i.split(';')
        if int(maxx_zp) < int(i[2]) != 52000 and int(i[2]) != 51200:
            maxx_zp = i[2]
            maxx_prof = i[1]
            maxx_comp = i[0]
    print(maxx_comp, '-', maxx_prof, '-', maxx_zp)


main()
