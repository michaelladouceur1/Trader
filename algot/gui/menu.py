import urwid

class Display:
    palette = [
        ('dash', 'white, bold', '','','','#000'),
        ('dashbody', 'white', '','','','#000'),
        ('dashdiv', 'white', '','','','#000'),
        ('secgreen', 'dark green', '','','','#000'),
        ('secred', 'dark red', '','','','#000'),
        ('body', 'black', 'dark gray'),
        ('line', 'white', '','','','#000'),
        ('std_button', 'white', 'dark gray'),
        ('std_button_select', 'dark gray', 'white')
    ]

    def __init__(self):
        self.navigation_items = [
            {'label': 'Accounts', 'fn': 'accounts'},
            {'label': 'Securities', 'fn': 'securities'},
            {'label': 'Options', 'fn': 'options'},
            {'label': 'Algorithms', 'fn': 'algorithms'},
            {'label': 'Settings', 'fn': 'settings'}
        ]
        self.div = self.create_divider()
        self.fill = self.create_fill()

    def change_body(self,button):
        for lab in self.navigation_items:
            if lab['label'] == button.get_label():
                self.loop.widget = self.setup_view(getattr(self, lab['fn'])())
                break
            else: 
                continue

    def add_button(self, label, fn=None, std_style='std_button', focus_style='std_button_select'):
        button = urwid.Button(label, on_press=fn)
        button = urwid.AttrMap(button, std_style, focus_style)
        return button

    # def button_state(self)

    def create_divider(self):
        div = urwid.Divider(u'_')
        div = urwid.AttrMap(div, 'dashdiv')
        return div

    def create_fill(self):
        fill = urwid.Divider()
        fill = urwid.AttrMap(fill, 'dashdiv')
        return fill

    def account_details(self):
        '''adh - account_details_header'''
        adh_text = urwid.Text('Account Details', align='center')
        adh = urwid.AttrMap(adh_text, 'dash')

        '''cash'''
        cash = urwid.Text('Cash: ')
        cash = urwid.Padding(cash, align='left', left=2)
        cash = urwid.AttrMap(cash, 'dashbody')

        '''account details'''
        ad = urwid.Pile([adh, self.div, cash, self.fill])
        ad = urwid.LineBox(ad)
        ad = urwid.AttrMap(ad, 'line')
        return ad

    def watchlist(self):
        watchlist_data = [
            {'symbol': 'AAPL', 'open': 1201.43, 'close': 1205.88, 'high': 1210.01, 'low': 1201.43},
            {'symbol': 'GOOG', 'open': 948.32, 'close': 942.43, 'high': 961.85, 'low': 948.24}
        ]

        '''watchlist header'''
        watchlist_text = urwid.Text('Watchlist', align='center')
        watchlist_head = urwid.AttrMap(watchlist_text, 'dash')

        '''watchlist label'''
        watchlist_labels = [
            'Symbol',
            'Open',
            'Close',
            'High',
            'Low'
        ]
        new_watchlist_labels = []
        for label in watchlist_labels:
            lab = urwid.Text(label)
            new_watchlist_labels.append(lab)

        labels = urwid.Columns(new_watchlist_labels, dividechars=3)
        labels = urwid.Padding(labels, align='center', left=2, right=2)
        labels = urwid.AttrMap(labels, 'dashbody')

        '''watchlist'''
        watchlist_items = []
        for sec in watchlist_data:
            sec_symbol = urwid.Text(str(sec['symbol']))
            sec_open = urwid.Text(str(sec['open']))
            sec_close = urwid.Text(str(sec['close']))
            sec_high = urwid.Text(str(sec['high']))
            sec_low = urwid.Text(str(sec['low']))
            security = urwid.Columns([sec_symbol, sec_open, sec_close, sec_high, sec_low], dividechars=3)
            security = urwid.Padding(security, align='center', left=2, right=2)
            # sec_symbol = urwid.Padding(sec_symbol, align='left', left=2)
            if sec['open'] <= sec['close']:
                security = urwid.AttrMap(security, 'secgreen')
            else:
                security = urwid.AttrMap(security, 'secred')
            watchlist_items.append(security)

        watchlist = urwid.Pile([watchlist_head, self.div, labels] + watchlist_items)
        watchlist = urwid.LineBox(watchlist)
        watchlist = urwid.AttrMap(watchlist, 'line')
        return watchlist

    def dashboard(self):

        ad = self.account_details()
        watchlist = self.watchlist()

        '''dashboard'''
        w = urwid.Columns([ad, watchlist])

        return w

    def navigation(self):

        menu_buttons = []
        for item in self.navigation_items:
            button = self.add_button(item['label'], self.change_body)
            menu_buttons.append(button)
        
        nav = urwid.Columns(menu_buttons, dividechars=1)
        # nav = urwid.Filler(nav, 'top')

        return nav

    def securities(self):
        text = urwid.Text('SECURITIES')
        text = urwid.Filler(text)
        text = urwid.AttrMap(text, 'body')
        return text
    
    def accounts(self):
        text = urwid.Text('ACCOUNTS')
        text = urwid.Filler(text)
        text = urwid.AttrMap(text, 'body')
        return text

    def options(self):
        text = urwid.Text('OPTIONS')
        text = urwid.Filler(text)
        text = urwid.AttrMap(text, 'body')
        return text

    def algorithms(self):
        text = urwid.Text('ALGORITHMS')
        text = urwid.Filler(text)
        text = urwid.AttrMap(text, 'body')
        return text

    def settings(self):
        text = urwid.Text('SETTINGS')
        text = urwid.Filler(text)
        text = urwid.AttrMap(text, 'body')
        return text
        
    def setup_view(self,body):
        '''Dashboard'''
        dash = self.dashboard()
        nav = self.navigation()
        header = urwid.Pile([dash,nav])
        body = body
        w = urwid.Frame(header=header, body=body, focus_part='header')
        return w


    def main(self):
        self.view = self.setup_view(self.accounts())
        self.loop = urwid.MainLoop(self.view, self.palette,
                    unhandled_input=self.unhandled_input)
        self.loop.run()
        
    def unhandled_input(self, key):
        if key == 'esc':
            raise urwid.ExitMainLoop()

def main():
    Display().main()

if __name__ == '__main__':
    main()