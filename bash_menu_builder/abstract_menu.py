from abc import ABC
from bash_menu_builder.dto.menu_item_dto import MenuItemDto
from .draw import Draw
import signal
import sys
import getopt


class AbstractMenu(ABC):
    def __init__(self, menu: list[MenuItemDto], banner: str = None) -> None:
        signal.signal(signal.SIGINT, lambda s, f: sys.exit(Draw.paint('\r\n{Yellow}Exiting...{ColorOff}')))
        self._menu_items = menu
        self._banner = banner
        self.__check_options()
        self.show_menu()

    def __check_options(self) -> None:
        short_opts: str = 'h'
        long_opts: list[str] = ['help']

        for menu_item in self._menu_items:
            short_opts += menu_item.option.short_option + (':' if menu_item.option.has_value else '')
            long_opts.append(menu_item.option.long_option + ('=' if menu_item.option.has_value else ''))

        try:
            opts, args = getopt.getopt(sys.argv[1:], short_opts, long_opts)
        except Exception as e:
            print(e)
            exit()

        for o, a in opts:
            if o in ('-h', '--help'): self._show_help()

            for menu_item in self._menu_items:
                menu_short_opt = '-%s' % menu_item.option.short_option
                menu_long_opt = '--%s' % menu_item.option.long_option
                if o in (menu_short_opt, menu_long_opt):
                    self._call_handler(menu_item.handler, a)

    def _call_handler(self, handler: callable, argument: str) -> None:
        if not callable(handler):
            raise RuntimeError('Item has incorrect Callable type!')

        if argument:
            handler(argument)
            return

        handler()

    def _show_help(self) -> None:
        args: list[str] = []
        desc: list[str] = []
        for menu_item in self._menu_items:
            args.append('\t-%s --%s%s' % (
                menu_item.option.short_option,
                menu_item.option.long_option,
                (' <argument>' if menu_item.option.has_value else ''),
            ))
            desc.append(menu_item.title)

        big_line_count: int = Draw.count_biggest_line(args)

        for index, arg in enumerate(args):
            spaces: int = Draw.get_count_spaces_for_line_up(arg, big_line_count)
            print('%s%s : %s' % (
                arg,
                ' ' * spaces,
                desc[index]
            ))

        exit()

    def show_menu(self) -> None:
        pass