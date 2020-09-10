
# from PyQt5.QtCore import *
# from PyQt5.QtWidgets import QGraphicsItem
# from PyQt5.QtGui import QBrush

from PyQt5.QtWidgets import QGraphicsItem

class VisualizerDemand():

    def __init__(self, obj_id, item_id, wanted_good, demand):
        self._name, self._id = obj_id[0], obj_id[1]
        self._bound_item = item_id
        self._wanted_good = wanted_good
        self._startdemand = demand
        self.is_fulfilled = False
        self.reset_to_start()

    def demand(self, amount):
        self.demand += amount
        return amount

    def satisfy(self, amount):
        if amount > self.demand:
            amount = self.demand
        self.demand -= amount
        return amount

    def reset_to_start(self):
        self.demand = self._startdemand
        self.is_fulfilled = self.demand < 1
        

class VisualizerGoods(QGraphicsItem):

    def __init__(self, obj_id, amount, startcoord):
        super().__init__()
        self._name, self._id = obj_id[0], obj_id[1]
        self._startcoord = startcoord
        self._startamount = amount
        self.reset_to_start()

    def increase(self, amount):
        self.amount += amount
        return amount

    def decrease(self, amount):
        if amount > self.amount:
            amount = self.amount
        self.amount -= amount
        return amount

    def split(self, amount, splitcoord):
        split = self.decrease(amount)
        new_goods = VisualizerGoods((self._name, self._id), split, splitcoord)
        return new_goods

    def reset_to_start(self):
        self.hide()
        self.setPos(*self._startcoord)
        self.amount = self._startamount
    