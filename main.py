import argparse
import sys
from tabulate import tabulate
from read import CSVDataReader
from analysis import get_analyzer

# Разбор аргументов командной строки
def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Анализ макроэкономических данных',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    
    parser.add_argument(
        '--files',
        nargs='+',
        required=True,
    )
    
    parser.add_argument(
        '--report',
        required=True,
        choices=['average-gdp'],
    )
    
    return parser.parse_args()

def main():
    # Разбираем аргументы
    args = parse_arguments()
    
    # Получаем анализатор
    analyzer = get_analyzer(args.report)
    if not analyzer:
        print(f"Ошибка: Неизвестный тип отчёта '{args.report}'")
        print(f"Доступные отчеты: average-gdp")
        sys.exit(1)
    
    # Чтение данных
    print(f"\nЧтение данных из {len(args.files)} файла(ов)\n")
    reader = CSVDataReader()
    data = reader.read_multiple_files(args.files)
    
    if not data:
        print("Нет данных в указанных файлах")
        sys.exit(1)
    
    # Анализ данных
    print(f"Генерация отчета '{args.report}'")
    results = analyzer.analyze(data)
    
    if not results:
        print("Нет результатов для отображения")
        sys.exit(0)
    
    # Подготавка данных для таблиц
    table_data = []
    for result in results:
        if args.report == 'average-gdp':
            table_data.append([result['country'], result['average_gdp']])
    
    # Вывод результатов
    print("\n\tРезультаты анализа")
    print(tabulate(
        table_data,
        headers=analyzer.get_headers(),
        tablefmt='grid',
        floatfmt='.2f',
        numalign='right'
    ))
    
    print(f"\nОтчёт сформирован. Представленны данные для {len(results)} стран.\n")

if __name__ == '__main__':
    main()
