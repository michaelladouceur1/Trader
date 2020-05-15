class StrategyBase:
    def __init__(self, indicators):
        self.indicators = indicators

    def run(self, data):
        result = []
        for d in data:
            res = all([ind(d) for ind in self.indicators])
            result.append(res)

        if any(result):
            return result