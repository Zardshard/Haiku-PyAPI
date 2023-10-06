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

_BWindow=BWindow
_BApplication=BApplication
def MessageReceived(self, msg):
    if msg.what in self.events:
        self.events[msg.what](msg)
    else:
        super(type(self)).MessageReceived(msg)

class BWindow(_BWindow):
    events={}
    MessageReceived=MessageReceived

class BApplication(_BApplication):
    events={}
    MessageReceived=MessageReceived


def int32(bytestr):
	return unpack('i',bytestr)[0]
