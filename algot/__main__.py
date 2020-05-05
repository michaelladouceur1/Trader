import gui.index as dsh
import webbrowser
from threading import Timer

port = 8050

def open_browser():
    webbrowser.open_new(f'http://127.0.0.1:{port}')

if __name__ == '__main__':
    Timer(1, open_browser).start()
    dsh.app.run_server(debug=False, port=port)