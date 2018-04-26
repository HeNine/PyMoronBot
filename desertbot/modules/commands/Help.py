# -*- coding: utf-8 -*-
from twisted.plugin import IPlugin
from desertbot.moduleinterface import IModule
from desertbot.modules.commandinterface import BotCommand
from zope.interface import implementer

from desertbot.message import IRCMessage
from desertbot.response import IRCResponse, ResponseType


@implementer(IPlugin, IModule)
class Help(BotCommand):
    def triggers(self):
        return['help', 'module', 'modules']

    def help(self, query):
        return 'help/module(s) (<module>) - returns a list of loaded modules, ' \
               'or the help text of a particular module if one is specified'

    def execute(self, message: IRCMessage):
        moduleHandler = self.bot.moduleHandler

        if message.ParameterList:
            helpStr = moduleHandler.runActionUntilValue('help', message.ParameterList)
            if helpStr:
                return IRCResponse(ResponseType.Say, helpStr, message.ReplyTo)
            else:
                return IRCResponse(ResponseType.Say,
                                   '"{0}" not found, try "{1}" without parameters '
                                   'to see a list of loaded module names'.format(message.ParameterList[0],
                                                                                 message.Command),
                                   message.ReplyTo)
        else:
            modules = ', '.join(sorted(moduleHandler.modules, key=lambda s: s.lower()))
            return [IRCResponse(ResponseType.Say,
                                "Modules loaded are (use 'help <module>' to get help for that module):",
                                message.ReplyTo),
                    IRCResponse(ResponseType.Say,
                                modules,
                                message.ReplyTo)]


help = Help()

