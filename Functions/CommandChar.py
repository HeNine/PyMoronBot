'''
Created on Feb 05, 2014

@author: Tyranic-Moron
'''

from IRCMessage import IRCMessage
from IRCResponse import IRCResponse, ResponseType
from Function import Function
import GlobalVars

import re

class Instantiate(Function):
    Help = "commandchar <char> - changes the prefix character for bot commands (admin-only)"

    def GetResponse(self, message):
        if message.Type != 'PRIVMSG':
            return

        match = re.search('^commandchar$', message.Command, re.IGNORECASE)
        if not match:
            return

        if message.User.Name not in GlobalVars.admins:
            return IRCResponse(ResponseType.Say, 'Only my admins can change my command character', message.ReplyTo)

        if len(message.Parameters) > 0:
            GlobalVars.CommandChar = message.Parameters[0]
        else:
            return IRCResponse(ResponseType.Say, 'Change my command character to what?', message.ReplyTo)
