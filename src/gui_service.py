import PySimpleGUI as sg
from abc import ABC, abstractmethod


class GuiService(ABC):
    @abstractmethod
    def generate_window(self, layout):
        pass

    @abstractmethod
    def simple_text(self):
        pass

    @abstractmethod
    def ask_if_true_condition(self, text: str):
        pass

    @abstractmethod
    def right_answer(self):
        pass

    @abstractmethod
    def new_food(self):
        pass

    @abstractmethod
    def new_codition(self, food_name: str, previous_food: str):
        pass


class GuiServiceImpl(GuiService):
    def __init__(self):
        self.sg = sg
        self.window_title = "Jogo Gourmet"

    def generate_window(self, layout):
        window = sg.Window(self.window_title, layout)
        event, values = window.read()
        window.close()
        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
            return "QUIT", None
        else:
            return event, values

    def simple_text(self):
        layout = [[sg.Text("Pense em um prato que gosta!")],
                  [sg.Button('OK')]]

        return self.generate_window(layout)

    def ask_if_true_condition(self, text: str):
        layout = [[sg.Text(f"O prato que voce pensou é {text}?")],
                  [sg.Button("Sim"), sg.Button("Não")]]

        return self.generate_window(layout)

    def right_answer(self):
        layout = [[sg.Text("Acertei de novo!")],
                  [sg.Button('OK')]]

        return self.generate_window(layout)

    def new_food(self):
        layout = [[sg.Text("Qual prato voce pensou?")],
                  [sg.Input(key='food_name')],
                  [sg.Button('OK'), sg.Button('Cancelar')]]

        return self.generate_window(layout)

    def new_codition(self, food_name: str, previous_food: str):
        layout = [[sg.Text(f"{food_name} é ______ mas {previous_food} não.")],
                  [sg.Input(key='condition_name')],
                  [sg.Button('OK'), sg.Button('Cancelar')]]

        return self.generate_window(layout)
