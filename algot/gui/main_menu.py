from yaclit.sselect import SSelect
from yaclit.mselect import MSelect
from yaclit.input import Input
from yaclit.router import Router
from yaclit.screen import Screen
from yaclit.colors import colors

class Routes(Router):
    def __init__(self,main):
        self.routes = {
            'main menu': 'main_menu',
            'account details': 'account_details',
            'watchlist': 'watchlist',
        }
        self.main = main 
        getattr(self,self.main)()
    
    @Router.route
    def main_menu(self):
        screen1 = Screen(word_color=colors['white'] ,back_color=colors['blue'])
        main_menu = SSelect(
            message='main menu',
            choices=['account details','watchlist','markets'],
            word_select_color=colors['charcoal']
        )
        screen1.add_component(main_menu)

        # sub_menu = SSelect(
        #     message='sub menu',
        #     choices=['account details','watchlist','markets'],
        #     x_position='left',
        #     word_select_color=colors['green']
        # )
        # screen1.add_component(sub_menu)

        return screen1.run()
        
    # @Router.route
    def watchlist(self):
        screen2 = Screen(word_color=colors['white'] ,back_color=colors['red'])
        watchlist = MSelect(
            # message='watchlist',
            choices=['stuff','in','watchlist','stuff','cool','things','for','sure'],
            back_select_color=colors['charcoal'],
            max_lines=5,
            x_position='left'
        )
        screen2.add_component(watchlist)

        ans = screen2.run()
        print(ans)

    @Router.route
    def account_details(self):
        screen3 = Screen(word_color=colors['white'], back_color=colors['black'])
        user_name = Input(
            message='Username: '
        )
        screen3.add_component(user_name)

        password = Input(
            message='Password: '
        )
        screen3.add_component(password)

        ans = screen3.run()
        print(ans)

# screen = Screen()
# print(screen)

Routes('main_menu')