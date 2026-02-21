import csv
import os
from typing import List, Dict, Any

# Чтение CSV файлов с экономическими данными
class CSVDataReader:
    
    # Чтение CSV файла
    def read_file(self, file_path: str) -> List[Dict[str, Any]]:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл не найден: {file_path}")
        data = []
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Очистка данных (удаление лишних пробелов)
                cleaned_row = {}
                for key, value in row.items():
                    if key is not None:
                        cleaned_key = key.strip()
                        cleaned_value = value.strip() if value else ''
                        cleaned_row[cleaned_key] = cleaned_value
                data.append(cleaned_row)
        
        return data

# Чтение нескольких CSV файлов и объединение их данных
    def read_multiple_files(self, file_paths: List[str]) -> List[Dict[str, Any]]:
        all_data = []
        for file_path in file_paths:
            try:
                file_data = self.read_file(file_path)
                all_data.extend(file_data)
                print(f"Загружено {len(file_data)} строк из {file_path}\n")
            except (FileNotFoundError, csv.Error) as e:
                print(f"Не удалось прочитать {file_path}: {e}")
        
        return all_data
