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
