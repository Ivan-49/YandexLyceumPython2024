from os import mkdir

def create_file(file_name):
    with open(file_name, 'w') as file:
        file.write('')

    print(f'Файл "{file_name}" успешно создан.')


def main():
    catalog_name = input('Введите название каталога: ')
    count_files = int(input('Введите количество файлов: '))
    try:
        mkdir(catalog_name)
    except:
        print(f'Каталог "{catalog_name}" уже существует.')
        
    for i in range(count_files):
        file_name = input(f'Введите название файла: ')
        create_file(f'{catalog_name}/{file_name}.py')

    print(f'Каталог "{catalog_name}" успешно создан.')


if __name__ == '__main__':
    while True:
        main()