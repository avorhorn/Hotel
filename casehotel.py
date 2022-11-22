# Case-study 
# Developers: Abrarova V. (40%)
#             Skorokhodov M.(80%)

class Hotel:
    # Importing hotel information.
    inp1 = open('booking.txt', 'r', encoding='UTF-8')
    inp2 = open('fund.txt', 'r', encoding='UTF-8')
    nomera_price = {'одноместный': 2900, 'двухместный': 2300, 'полулюкс': 3200, 'люкс': 4100}
    coef = {'стандарт': 1, 'стандарт_улучшенный': 1.2, 'апартамент': 1.5}
    pitanie = {'без питания': 0, 'завтрак': 280, 'полупансион': 1000}

    def __init__(self):
        '''Initiailzing function of the funds of hotel rooms and booking information'''
        self.infaboutbooking = list(map(lambda x: x.strip(), Hotel.inp1.readlines()))
        for i in range(len(self.infaboutbooking)):
            self.infaboutbooking[i] = self.infaboutbooking[i].split()
            self.infaboutbooking[i][4] = int(self.infaboutbooking[i][4])
            self.infaboutbooking[i][6] = int(self.infaboutbooking[i][6])
            self.infaboutbooking[i][7] = int(self.infaboutbooking[i][7])
            self.infaboutbooking[i][0] = str(self.infaboutbooking[i][0])
            self.infaboutbooking[i][5] = str(self.infaboutbooking[i][5])
        self.infabouthotel = list(map(lambda x: x.strip(), Hotel.inp2.readlines()))
        for i in range(len(self.infabouthotel)):
            self.infabouthotel[i] = self.infabouthotel[i].split()
            self.infabouthotel[i][0] = int(self.infabouthotel[i][0])
            self.infabouthotel[i][2] = int(self.infabouthotel[i][2])
        self.number_feeling = {self.infabouthotel[i][0]: 0 for i in range(len(self.infabouthotel))}
        self.number_free = {self.infabouthotel[i][0]: self.infabouthotel[i][2] for i in range(len(self.infabouthotel))}

    def program(self):
        '''Function simulating the occupancy of hotel rooms.'''
        # Setting variables.
        import random
        variants = {}
        iteration = 0
        values = {}
        number_feeling2 = []
        number_feeling1 = {}
        zanyat_nomera1 = []
        val = []
        data3 = 'D.MM.YYYY'

        # Counting the number of rooms by category.
        alpha1 = 0
        alpha2 = 0
        alpha3 = 0
        alpha4 = 0
        for gg in self.infabouthotel:
            if gg[1] == 'одноместный':
                alpha1 += 1
            elif gg[1] == 'двухместный':
                alpha2 += 1
            elif gg[1] == 'полулюкс':
                alpha3 += 1
            else:
                alpha4 += 1

        # Formatting date.
        infaboutbooking1 = self.infaboutbooking[:]
        if list(map(len, self.infaboutbooking[-1][0].split('.'))) == list(map(len, data3.split('.'))):
            lk1 = int(self.infaboutbooking[-1][0][1])
        else:
            lk1 = int(self.infaboutbooking[-1][0][0:2])
        for i in self.infaboutbooking:
            i.append(0)
        for i in self.infaboutbooking:
            i.append(-1)
        r = 0
        for i in self.infaboutbooking:
            r += 1
            i[9] = r

        # Formatting the booking and check-in dates.
        for current_data in range(1, lk1 + 1):
            for ch, ch1 in self.number_feeling.items():
                if type(ch1) == list:
                    if ch1[2] == current_data:
                        self.number_feeling[ch] = 0
            for people in infaboutbooking1:
                people[8] = people[5]
                data10 = people[0]
                if list(map(len, people[0].split('.'))) == list(map(len, data3.split('.'))):
                    data1 = int(people[0][1])
                else:
                    data1 = int(people[0][0:2])
                if list(map(len, people[5].split('.'))) == list(map(len, data3.split('.'))):
                    data = int(people[5][1])
                else:
                    data = int(people[5][0:2])
                if people[8] == 0:
                    people[8] = people[5]
                if list(map(len, people[8].split('.'))) == list(map(len, data3.split('.'))):
                    data99 = int(people[8][0])
                else:
                    data99 = int(people[8][0:2])

                # Making a list of potential rooms.
                if current_data == data99:
                    iteration += 1
                    temp = list(filter(lambda x: x[2] == people[4], self.infabouthotel))
                    if temp != []:
                        for number in temp:
                            price = Hotel.nomera_price[number[1]] * Hotel.coef[number[3]]
                            variants[number[0]] = price
                            sorted_tuples = sorted(variants.items(), key=lambda item: item[1], reverse=True)
                            sorted_dict = {k: v for k, v in sorted_tuples}
                    else:
                        temp2 = list(filter(lambda x: x[2] > people[4], self.infabouthotel))
                        for number in temp2:
                            price = Hotel.nomera_price[number[1]] * Hotel.coef[number[3]] * number[2] * 0.7 / people[4]
                            variants[number[0]] = price
                            sorted_tuples = sorted(variants.items(), key=lambda item: item[1], reverse=True)
                            sorted_dict = {k: v for k, v in sorted_tuples}

                    for ch, ch1 in sorted_dict.items():
                        max_price = ch1

                        # Checking for the ability to pay for half board.
                        if max_price + 1000 <= people[7] and self.number_feeling[ch] == 0:
                            if current_data == data99:
                                randomm = random.randint(1, 4)
                                if randomm != 1:
                                    max_price += 1000
                                    eda = 'полупансион'
                                    temp1 = [int(people[4]), people[5], data + int(people[6]), max_price, people[1],
                                             people[2], people[3]]
                                    self.number_feeling[ch] = temp1
                                    number1 = ch
                                    break

                                else:
                                    self.number_feeling[ch] = 0
                                    eda = 'полупансион'
                                    number1 = -1
                                    max_price += 1000
                                    break
                            else:
                                data99 = people[5]
                                people[8] = data99
                                self.number_feeling[ch] = 0
                                number1 = ch
                                break
                            break
                        else:

                            # Checking for the ability to pay for breakfast.
                            if max_price + 280 <= people[7] and self.number_feeling[ch] == 0:
                                if current_data == data99:
                                    randomm = random.randint(1, 4)
                                    if randomm != 1:
                                        max_price += 280
                                        eda = 'завтрак'
                                        temp1 = [int(people[4]), people[5], data + int(people[6]), max_price,
                                                 people[1], people[2], people[3]]
                                        self.number_feeling[ch] = temp1
                                        number1 = ch
                                        break
                                    else:
                                        self.number_feeling[ch] = 0
                                        eda = 'завтрак'
                                        number1 = -1
                                        max_price += 280
                                        break
                                else:
                                    data99 = people[5]
                                    people[8] = data99
                                    self.number_feeling[ch] = 0
                                    number1 = ch
                                    break
                                break
                            else:

                                # Checking for the ability to pay for a room without food.
                                if max_price <= people[7] and self.number_feeling[ch] == 0:
                                    if current_data == data99:
                                        randomm = random.randint(1, 4)
                                        if randomm != 1:
                                            eda = 'без питания'
                                            temp1 = [int(people[4]), people[5], data + int(people[6]),
                                                     max_price, people[1], people[2], people[3]]
                                            self.number_feeling[ch] = temp1
                                            number1 = ch
                                            break
                                        else:
                                            self.number_feeling[ch] = 0
                                            eda = 'без питания'
                                            number1 = -1
                                            break
                                    else:
                                        data99 = people[5]
                                        people[8] = data99
                                        self.number_feeling[ch] = 0
                                        number1 = ch
                                        break
                                    break
                                else:

                                    # Checking for the ability to pay for a larger room at discount.
                                    if ch == sorted_tuples[-1][0]:
                                        temp = list(filter(lambda x: x[2] > people[4], self.infabouthotel))
                                        for number in temp:
                                            price = Hotel.nomera_price[number[1]] * Hotel.coef[number[3]] * number[
                                                2] * 0.7 / people[4]
                                            variants[number[0]] = price
                                            sorted_tuples = sorted(variants.items(), key=lambda item: item[1],
                                                                   reverse=True)
                                            sorted_dict = {k: v for k, v in sorted_tuples}
                                        for ch, ch1 in sorted_dict.items():
                                            max_price = ch1

                                            # Ability to pay for half board in larger room.
                                            if max_price + 1000 <= people[7] and self.number_feeling[ch] == 0:
                                                if current_data == data99:
                                                    randomm = random.randint(1, 4)
                                                    if randomm != 1:
                                                        max_price += 1000
                                                        eda = 'полупансион'
                                                        temp1 = [int(people[4]), people[5], data + int(people[6]),
                                                                 max_price, people[1], people[2], people[3]]
                                                        self.number_feeling[ch] = temp1
                                                        number1 = ch
                                                        break
                                                    else:
                                                        self.number_feeling[ch] = 0
                                                        number1 = -1
                                                        eda = 'полупансион'
                                                        max_price += 1000
                                                        break
                                                else:
                                                    data99 = people[5]
                                                    people[8] = data99
                                                    self.number_feeling[ch] = 0
                                                    number1 = ch
                                                    break
                                                break
                                            else:

                                                # Ability to pay for breakfast in larger room.
                                                if max_price + 280 <= people[7] and self.number_feeling[ch] == 0:
                                                    if current_data == data99:
                                                        randomm = random.randint(1, 4)
                                                        if randomm != 1:
                                                            max_price += 280
                                                            eda = 'завтрак'
                                                            temp1 = [int(people[4]), people[5], data + int(people[6]),
                                                                     max_price,
                                                                     people[1], people[2], people[3]]
                                                            self.number_feeling[ch] = temp1
                                                            number1 = ch
                                                            break
                                                        else:
                                                            self.number_feeling[ch] = 0
                                                            eda = 'завтрак'
                                                            number1 = -1
                                                            max_price += 280
                                                            break
                                                    else:
                                                        data99 = people[5]
                                                        people[8] = data99
                                                        self.number_feeling[ch] = 0
                                                        number1 = ch
                                                        break
                                                    break
                                                else:

                                                    # Ability to pay for larger room without food.
                                                    if max_price <= people[7] and self.number_feeling[ch] == 0:
                                                        if current_data == data99:
                                                            randomm = random.randint(1, 4)
                                                            if randomm != 1:
                                                                eda = 'без питания'
                                                                temp1 = [int(people[4]), people[5],
                                                                         data + int(people[6]),
                                                                         max_price, people[1], people[2], people[3]]
                                                                self.number_feeling[ch] = temp1
                                                                number1 = ch
                                                                break
                                                            else:
                                                                self.number_feeling[ch] = 0
                                                                eda = 'без питания'
                                                                number1 = -1
                                                                break
                                                        else:
                                                            data99 = people[5]
                                                            people[8] = data99
                                                            self.number_feeling[ch] = 0
                                                            number1 = ch
                                                            break
                                                    else:
                                                        if ch == sorted_tuples[-1][0]:
                                                            max_price = 0
                                                            break
                                                        continue

                    # Marking agreed and refused clients.
                    if max_price != 0:
                        for i in self.infabouthotel:
                            if i[0] == number1:
                                values[iteration] = [people, data10, data1, max_price, i, people[5], eda, 'true']
                                val.append([people, data10, data1, max_price, i, people[5], eda, 'true'])
                            elif number1 == -1:
                                val.append([people, data10, data1, max_price, i, people[5], eda, 'false1'])
                                break
                    else:
                        values[iteration] = [people, data10, data1, 'false']
                        val.append([people, data10, data1, 'false'])
                    variants = {}
                    sorted_dict = {}
                else:
                    continue

            # Compiling a list of occupied rooms by category.
            number_feeling1[current_data] = self.number_feeling
            xxx = self.number_feeling
            number_feeling2.append([current_data, self.number_feeling])
            abc = current_data
            zanyat_nomera = 0
            odnomest = 0
            dvamest = 0
            polulux = 0
            lux = 0
            for ch, ch1 in xxx.items():
                for pure in self.infabouthotel:
                    if ch1 != 0 and ch == pure[0]:
                        zanyat_nomera += 1
                        if ch == pure[0]:
                            if pure[1] == 'одноместный':
                                odnomest += 1
                            elif pure[1] == 'двухместный':
                                dvamest += 1
                            elif pure[1] == 'полулюкс':
                                polulux += 1
                            else:
                                lux += 1
            zanyat_nomera1.append([zanyat_nomera, odnomest, dvamest, polulux, lux])
        for i in range(1, abc + 1):
            pribil = 0
            ubil = 0
            temp5 = list(filter(lambda x: x[2] == i, val))
            temp5.sort(key=lambda x: x[0][-1])

            # Printing booking massages.
            print('*' * 100 + '\n')
            print(f'МОДЕЛИРОВАНИЕ В {i} ДЕНЬ\n')
            for j in temp5:
                print('-' * 100 + '\n')
                print('Поступила заявка на бронирование:\n')
                print(' '.join(map(str, j[0][0:8])) + '\n')
                if j[-1] == 'true':
                    print('Найден:\n')
                    print(
                        f'номер {j[4][0]} {j[4][1]} рассчитан на {j[4][2]} чел. фактически {j[0][4]} чел. {j[6]} {j[4][3]} стоимость {j[3] * j[4][2]} руб./сутки\n')
                    print('Клиент согласен. Номер забронирован.\n')
                    pribil += j[3] * j[4][2]
                elif j[-1] == 'false1':
                    print('Найден:\n')
                    print(
                        f'номер {j[4][0]} {j[4][1]} рассчитан на {j[4][2]} чел. фактически {j[0][4]} чел. {j[6]} {j[4][3]} стоимость {j[3] * j[4][2]} руб./сутки\n')
                    print('Клиент отказался от варианта.\n')
                    ubil += j[3] * j[4][2]
                else:
                    print('Предложений по данному запросу нет. В бронировании отказано\n')
                    ubil += j[0][4] * j[0][7]

            # Printing the results of the simulation of the day.
            print('=' * 100 + '\n')
            print(f'Итог за {j[0][0]}\n')
            print(f'Количество занятых номеров: {zanyat_nomera1[i - 1][0]}\n')
            print(f'Количество свободных номеров: {self.infabouthotel[-1][0] - zanyat_nomera1[i - 1][0]}\n')
            print(f'Занятость по категориям:\n')
            print(f'Одноместных: {zanyat_nomera1[i - 1][1]} из {alpha1}\n')
            print(f'Двухместных: {zanyat_nomera1[i - 1][2]} из {alpha2}\n')
            print(f'Полулюкс: {zanyat_nomera1[i - 1][3]} из {alpha3}\n')
            print(f'Люкс: {zanyat_nomera1[i - 1][4]} из {alpha4}\n')
            print(
                f'Процент загруженности гостиницы: {(zanyat_nomera1[i - 1][0] / self.infabouthotel[-1][0]) * 100} %\n')
            print(f'Доход за день: {pribil}\n')
            print(f'Упущенный доход: {ubil}\n')


test1 = Hotel()
test1.program()
