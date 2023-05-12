# -*- coding:utf-8 -*-

class SavingsAccount(object):
    """This class represents a  savings account
    with the owner 's name, PIN, and balance."""
    
    def __init__(self, name, pin, balance=0.0):
        self._name = name
        self._pin = pin
        self._balance = balance

    def __lt__(self, other):
        return self._name < other._name

    def __eq__(self, other):
        return self._name == other._name

    def __gt__(self, other):
        return self._name > other._name
