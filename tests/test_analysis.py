import pytest
from analysis import GDPAverageAnalyzer, get_analyzer

class TestGDPAverageAnalyzer:
    @pytest.fixture
    # Создание экземпляра анализатора для тестирования
    def analyzer(self):
        return GDPAverageAnalyzer()
    
    # Тест с пустыми данными
    def test_empty_data(self, analyzer):
        assert analyzer.analyze([]) == []
    
    # Тест с одной страной и одним годом
    def test_single_country_single_year(self, analyzer):
        data = [{'country': 'USA', 'gdp': '25462'}]
        result = analyzer.analyze(data)
        assert len(result) == 1
        assert result[0]['country'] == 'USA'
        assert result[0]['average_gdp'] == 25462.0
    
    # Тест с одной страной и несколькими годами
    def test_single_country_multiple_years(self, analyzer):
        data = [
            {'country': 'USA', 'gdp': '25462'},
            {'country': 'USA', 'gdp': '23315'},
            {'country': 'USA', 'gdp': '22994'}
        ]
        result = analyzer.analyze(data)
        assert len(result) == 1
        expected_avg = (25462 + 23315 + 22994) / 3
        assert result[0]['average_gdp'] == round(expected_avg, 2)
    
    # Тест с несколькими странами
    def test_multiple_countries(self, analyzer):
        data = [
            {'country': 'USA', 'gdp': '30000'},
            {'country': 'USA', 'gdp': '20000'},
            {'country': 'China', 'gdp': '25000'},
            {'country': 'Germany', 'gdp': '15000'}
        ]
        result = analyzer.analyze(data)
        assert len(result) == 3
        
        # Проверка сортировки по убыванию
        assert result[0]['country'] == 'USA'
        assert result[1]['country'] == 'China'
        assert result[2]['country'] == 'Germany'
        
        assert result[0]['average_gdp'] == 25000.0
        assert result[1]['average_gdp'] == 25000.0
        assert result[2]['average_gdp'] == 15000.0
    
    # Тест с некорректными значениями ВВП
    def test_invalid_gdp_values(self, analyzer):
        data = [
            {'country': 'USA', 'gdp': '25462'},
            {'country': 'USA', 'gdp': 'invalid'},  # Некорректное значение
            {'country': 'USA', 'gdp': ''},         # Пустое значение
            {'country': 'USA', 'gdp': '22994'},
            {'country': 'China', 'gdp': '-1000'},  # Отрицательное значение (пропуск)
            {'country': 'China', 'gdp': '17963'}
        ]
        result = analyzer.analyze(data)
        assert len(result) == 2
        
        # USA должно усреднить только валидные значения
        usa_result = next(r for r in result if r['country'] == 'USA')
        assert usa_result['average_gdp'] == (25462 + 22994) / 2
        
        # China должно учесть только положительное значение
        china_result = next(r for r in result if r['country'] == 'China')
        assert china_result['average_gdp'] == 17963.0
    
    # Тест с отсутствующей страной
    def test_missing_country(self, analyzer):
        data = [
            {'gdp': '1000'},  # Нет страны
            {'country': 'USA', 'gdp': '2000'},
            {'country': '', 'gdp': '3000'}  # Пустая страна
        ]
        result = analyzer.analyze(data)
        assert len(result) == 1
        assert result[0]['country'] == 'USA'
        assert result[0]['average_gdp'] == 2000.0

# Тест функции получения анализатора
def test_get_analyzer():
    # Существующий анализатор
    analyzer = get_analyzer('average-gdp')
    assert analyzer is not None
    assert isinstance(analyzer, GDPAverageAnalyzer)
    
    # Несуществующий анализатор
    assert get_analyzer('invalid-report') is None

