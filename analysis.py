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
    def analyze(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        if not data:
            return []
        
        # Группировка значений ВВП по странам
        country_gdp = defaultdict(list)
        
        for row in data:
            country = row.get('country', '').strip()
            if not country:  # Пропуск строк без страны
                continue
                
            try:
                gdp = float(row.get('gdp', 0))
                if gdp > 0:
                    country_gdp[country].append(gdp)
            except (ValueError, TypeError):
                # Пропуск некорректных значений ВВП
                continue
        
        # Рассчёт средних значений
        results = []
        for country, gdps in country_gdp.items():
            if gdps:
                avg_gdp = sum(gdps) / len(gdps)
                results.append({
                    'country': country,
                    'average_gdp': round(avg_gdp, 2)
                })
        
        # Сортируем по среднему ВВП по убыванию
        return sorted(results, key=lambda x: x['average_gdp'], reverse=True)
    
    def get_report_name(self) -> str:
        return "average-gdp"
    
    def get_headers(self) -> List[str]:
        return ["Страна", "Средний ВВП"]

# Получение соответствующего анализатора для указанного отчета
def get_analyzer(report_name: str) -> Optional[BaseAnalyzer]:
    analyzers = {
        'average-gdp': GDPAverageAnalyzer(),
    }
    
    return analyzers.get(report_name)
