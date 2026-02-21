import pytest
from unittest.mock import patch
from main import parse_arguments

# Тест разбора валидных аргументов
def test_parse_arguments_valid():
    with patch('sys.argv', ['main.py', '--files', 'data.csv', '--report', 'average-gdp']):
        args = parse_arguments()
        assert args.files == ['data.csv']
        assert args.report == 'average-gdp'

# Тест с несколькими файлами
def test_parse_arguments_multiple_files():
    with patch('sys.argv', ['main.py', '--files', 'file1.csv', 'file2.csv', '--report', 'average-gdp']):
        args = parse_arguments()
        assert args.files == ['file1.csv', 'file2.csv']
        assert args.report == 'average-gdp'

# Тест с отсутствующим обязательным аргументом --files
def test_parse_arguments_missing_files():
    with patch('sys.argv', ['main.py', '--report', 'average-gdp']):
        with pytest.raises(SystemExit):
            parse_arguments()

# Тест с отсутствующим обязательным аргументом --report
def test_parse_arguments_missing_report():
    with patch('sys.argv', ['main.py', '--files', 'data.csv']):
        with pytest.raises(SystemExit):
            parse_arguments()

# Тест с неверным типом отчета
def test_parse_arguments_invalid_report():
    with patch('sys.argv', ['main.py', '--files', 'data.csv', '--report', 'invalid']):
        with pytest.raises(SystemExit):
            parse_arguments()
