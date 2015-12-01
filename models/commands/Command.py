import shlex
import inspect
from abc import ABCMeta, abstractmethod

import models.commands
from models.errors import CommandNotFound



class Command(object):
    __metaclass__ = ABCMeta


    title = None
    description = None


    def __init__(self, pass_storage):
        self._pass_storage = pass_storage


    @abstractmethod
    def execute(self):
        return ""


    @classmethod
    def create(cls, pass_storage, query):
        words = shlex.split(query)
        title = words[0]
        args = words[1:]
        command_cls = cls._find_command_cls(title)
        return command_cls(pass_storage, *args)


    @classmethod
    def _find_command_cls(cls, title):
        for cmd_cls in cls._get_commands_cls():
            if cmd_cls.title == title:
                return cmd_cls
        raise CommandNotFound()


    @classmethod
    def _get_commands_cls(cls):
        commands = []
        for name in dir(models.commands):
            obj = getattr(models.commands, name)
            if inspect.isclass(obj) and issubclass(obj, Command) and obj is not Command:
                commands.append(obj)
        return commands
