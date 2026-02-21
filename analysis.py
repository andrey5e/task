from collections import defaultdict
from typing import List, Dict, Any, Optional
from abc import ABC, abstractmethod

# Класс для анализаторов
class BaseAnalyzer(ABC):
    @abstractmethod
    # Анализ данных
    def analyze(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        pass
    
    @abstractmethod
    # Возврат названия отчета
    def get_report_name(self) -> str:
        pass
    
    # Возврат заголовков таблицы для вывода
    def get_headers(self) -> List[str]:
        return ["Страна", "Значение"]

class GDPAverageAnalyzer(BaseAnalyzer):
    # Анализатор для расчета среднего ВВП по странам
