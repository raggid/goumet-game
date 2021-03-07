from goumet_game import GourmetGame
from gui_service import GuiServiceImpl

if __name__ == '__main__':
    gui_service = GuiServiceImpl()
    game = GourmetGame(gui_service)
    game.init_game()