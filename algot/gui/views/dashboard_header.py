import random
import threading

dashboard_data = [
    {'Symbol': 'AAPL', 'Open': 1023.33, 'Close': 1032.17, 'High': 1033.01, 'Low': 1023.33},
    {'Symbol': 'ZM', 'Open': 107.53, 'Close': 120.95, 'High': 120.95, 'Low': 107.34},
    {'Symbol': 'TSLA', 'Open': 200.02, 'Close': 209.41, 'High': 210.13, 'Low': 200.02},
    {'Symbol': 'GOOG', 'Open': 1023.33, 'Close': 1032.17, 'High': 1033.01, 'Low': 1023.33},
    {'Symbol': 'GE', 'Open': 1023.33, 'Close': 1032.17, 'High': 1033.01, 'Low': 1023.33},
]

# timer = None

class Data:
    def __init__(self):
        self.dashboard_data = [
            {'Symbol': 'AAPL', 'Open': 1023.33, 'Close': 1032.17, 'High': 1033.01, 'Low': 1023.33},
            {'Symbol': 'ZM', 'Open': 107.53, 'Close': 120.95, 'High': 120.95, 'Low': 107.34},
            {'Symbol': 'TSLA', 'Open': 200.02, 'Close': 209.41, 'High': 210.13, 'Low': 200.02},
            {'Symbol': 'GOOG', 'Open': 1023.33, 'Close': 1032.17, 'High': 1033.01, 'Low': 1023.33},
            {'Symbol': 'GE', 'Open': 1023.33, 'Close': 1032.17, 'High': 1033.01, 'Low': 1023.33},
        ]
        # self.stream_update_data()

    def update_data(self):
        for i,stock in enumerate(self.dashboard_data):
            tol = 2
            tolup = stock['Open'] + tol
            toldown = stock['Open'] - tol
            self.dashboard_data[i]['Open'] = round(random.uniform(toldown,tolup), 2)
            self.dashboard_data[i]['Close'] = round(random.uniform(toldown,tolup), 2)
            self.dashboard_data[i]['High'] = round(random.uniform(toldown,tolup), 2)
            self.dashboard_data[i]['Low'] = round(random.uniform(toldown,tolup), 2)

        return self.dashboard_data

    # def stream_update_data(self):
    #     while True:
    #         t = threading.Timer(5, self.update_data)
    #         t.start()
        