from time import time, sleep
import threading


def write_words(word_count, file_name):
    with open(str(file_name), 'a', encoding='utf-8') as file:
        for line in range(word_count):
            file.write('Какое-то слово № ' + str(line + 1) + '\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


start = time()
ww1 = write_words(10, 'example1.txt')
ww2 = write_words(30, 'example2.txt')
ww3 = write_words(200, 'example3.txt')
ww4 = write_words(100, 'example4.txt')
end = time()
print(f'Работа потоков: {end - start}', '\n')

start = time()
tread = threading.Thread(target=write_words, args=(10, 'example5.txt'))
tread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
tread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
tread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
tread.start()
tread2.start()
tread3.start()
tread4.start()
tread.join()
tread2.join()
tread3.join()
tread4.join()
end = time()
print(f'Работа потоков: {end - start}')
