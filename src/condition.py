import typing_extensions
import dataclasses
from pydantic import BaseModel


class Condition(BaseModel):
    name: str
    food_y: str
    food_n: str
    condition_y: BaseModel = None
    condition_n: BaseModel = None

    def get_next_condition(self, event):
        if event == "Sim":
            return self.condition_y
        else:
            return self.condition_n

    def set_next_condition(self, condition, event):
        if event == 'Sim':
            self.condition_y = condition
        else:
            self.condition_n = condition

    def get_food(self, event):
        if event == "Sim":
            return self.food_y
        else:
            return self.food_n
