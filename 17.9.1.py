spisok = input('Напишите последовательность чисел через пробел: ')
spisok_list = [int(a) for a in spisok.split()]

if (' ' not in (spisok)):
    raise ValueError('Ошибка, напишите последовательность чисел через пробел')

num = int(input('Напишите любое число: '))
if num % 1 == 0:
    spisok_list.append(num)
    print('Список до сортировки: ', spisok_list)

def my_sort(spisok_list):
    for i in range(len(spisok_list)):
        idx_min = i
        for j in range(i, len(spisok_list)):
            if spisok_list[j] < spisok_list[idx_min]:
                idx_min = j
        if i != idx_min:
            spisok_list[i], spisok_list[idx_min] = spisok_list[idx_min], spisok_list[i]
    return spisok_list

print("Список после сортировки:", my_sort(spisok_list))