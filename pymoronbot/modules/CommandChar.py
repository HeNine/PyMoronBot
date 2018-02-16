# -*- coding: utf-8 -*-
"""
Created on Feb 05, 2014

@author: Tyranic-Moron
"""

from pymoronbot.moduleinterface import ModuleInterface
from pymoronbot.message import IRCMessage
from pymoronbot.response import IRCResponse, ResponseType


class CommandChar(ModuleInterface):
    triggers = ['commandchar']
    help = "commandchar <char> - changes the prefix character for bot commands (admin-only)"

    def execute(self, message):
        """
        @type message: IRCMessage
        """
        if not self.checkPermissions(message):
            return IRCResponse(ResponseType.Say, 'Only my admins can change my command character', message.ReplyTo)

        if len(message.ParameterList) > 0:
            self.bot.commandChar = message.ParameterList[0]
            self.bot.config['commandChar'] = self.bot.commandChar
            self.bot.config.writeConfig()
            return IRCResponse(ResponseType.Say,
                               'Command prefix char changed to \'{0}\'!'.format(self.bot.commandChar),
                               message.ReplyTo)
        else:
            return IRCResponse(ResponseType.Say, 'Change my command character to what?', message.ReplyTo)