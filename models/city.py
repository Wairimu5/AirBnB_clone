#!/usr/bin/python3
"""
Defines the state model
"""
from .base_model import BaseModel


class City(BaseModel):
    """
    Model for City instances
    """
    state_id = ""
    name = ""
