"""DataProcessor v1 — baseline (GOOD). All calculations correct."""

class DataProcessor:
    def __init__(self):
        self.records = []

    def add_record(self, name, value):
        self.records.append({'name': name, 'value': value})

    def process_records(self):
        if not self.records:
            return {'count': 0, 'total': 0, 'average': 0, 'max': 0}
        total = sum(r['value'] for r in self.records)
        average = total / len(self.records)
        max_val = max(r['value'] for r in self.records)
        return {'count': len(self.records), 'total': total, 'average': average, 'max': max_val}
