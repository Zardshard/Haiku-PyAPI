from struct import unpack
from .AppDefs import *
from .Clipboard import *
from .Cursor import *
from .Handler import *
from .Invoker import *
from .Key import *
from .KeyStore import *
from .Looper import *
from .Application import * # has to be after looper
from .Message import *
from .MessageFilter import *
from .MessageQueue import *
from .MessageRunner import *
from .Messenger import *
from .Notification import *
from .PropertyInfo import *
from .Roster import *
from .Window import *
from .Rect import *
from .View import *
from .Control import *
from .Button import *
from .TextControl import *
from .Font import *
from .StringView import *
from .InterfaceDefs import *
from .Alert import *
from .TextView import *
from .Menu import *
from .MenuItem import *
from .MenuField import *
from .LayoutItem import *
from .Layout import *
from .AbstractLayout import *
from .TwoDimensionalLayout import *
from .GridLayout import *
from .PopUpMenu import *

_BWindow=BWindow
_BApplication=BApplication
def MessageReceived(self, msg, parent):
    if msg.what in self.events:
        self.events[msg.what](msg)
    elif msg in self.events:
        self.events[msg](msg)
    else:
        parent.MessageReceived(msg)

class BWindow(_BWindow):
    events={}
    MessageReceived=lambda msg, parent=_BWindow: MessageReceived(msg,parent)

class BApplication(_BApplication):
    events={}
    MessageReceived=lambda msg, parent=_BApplication: MessageReceived(msg,parent)


def int32(bytestr):
	return unpack('i',bytestr)[0]
