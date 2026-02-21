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
