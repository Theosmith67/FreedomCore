# API Reference — Wise Man Contract

Each Wise Man must implement:

class WiseMan:
    def execute(self, task: dict) -> dict: ...
    def health_check(self) -> bool: ...
