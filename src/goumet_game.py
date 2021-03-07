from condition import Condition
from gui_service import GuiService


class GourmetGame:

    def __init__(self, gui: GuiService):
        self.gui = gui
        self.initial_condition = Condition(name='massa', food_y='Lasanha', food_n='Bolo de Chocolate')

    def ask_new_food(self, condition, previous_food, previous_event):
        event, values = self.gui.new_food()
        if event == 'QUIT':
            return None
        new_food = values['food_name'].title()
        event, values = self.gui.new_codition(new_food, previous_food)
        if event == 'QUIT':
            return None
        condition_name = values['condition_name']
        new_condition = Condition(name=condition_name, food_y=new_food,
                                  food_n=previous_food)
        condition.set_next_condition(new_condition, previous_event)
        return None

    def ask_food(self, condition, event):
        previous_food = condition.get_food(event)
        previous_event = event
        event, values = self.gui.ask_if_true_condition(previous_food)
        if event == 'QUIT':
            return None
        if event == 'Sim':
            self.gui.right_answer()
            return None
        else:
            return self.ask_new_food(condition, previous_food, previous_event)

    def ask_condition(self, condition: Condition):
        event, values = self.gui.ask_if_true_condition(condition.name)
        if event == 'QUIT':
            return None
        next_condition = condition.get_next_condition(event)
        if next_condition is None:
            return self.ask_food(condition, event)

        else:
            condition = next_condition
            return condition

    def init_game(self):
        while True:
            current_condition = self.initial_condition
            event, values = self.gui.simple_text()
            if event == 'QUIT':
                break
            while True:
                response = self.ask_condition(current_condition)
                if response is not None:
                    current_condition = response
                else:
                    break
