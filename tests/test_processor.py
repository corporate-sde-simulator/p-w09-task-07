import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from dataProcessor import DataProcessor

class TestDataProcessor:
    def test_average_calculation(self):
        dp = DataProcessor()
        dp.add_record('A', 10)
        dp.add_record('B', 20)
        result = dp.process_records()
        assert result['average'] == 15.0, f"Expected 15.0, got {result['average']}"

    def test_total(self):
        dp = DataProcessor()
        dp.add_record('A', 10)
        dp.add_record('B', 20)
        dp.add_record('C', 30)
        result = dp.process_records()
        assert result['total'] == 60

    def test_single_record(self):
        dp = DataProcessor()
        dp.add_record('X', 42)
        result = dp.process_records()
        assert result['average'] == 42.0

    def test_empty(self):
        dp = DataProcessor()
        result = dp.process_records()
        assert result['count'] == 0
        assert result['average'] == 0
