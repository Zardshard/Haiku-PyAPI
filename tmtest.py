from Be import BApplication, BWindow, BListItem, BTabView, BTab, BFont, BPicture, BStringItem, BAlert, BPoint, BBox, BListView, BScrollView, BRadioButton, BColorControl, BCheckBox, BRect, BTextControl, BView,BMenu,BStatusBar, BMenuBar, BMenuItem,BSeparatorItem,BStringView,BMessage,window_type,  B_NOT_RESIZABLE, B_QUIT_ON_WINDOW_CLOSE
from Be import BPictureButton, BTextView, BButton, BScreen, BBitmap
from Be.PictureButton import picture_button_behavior
from Be.GraphicsDefs import *
from Be.ListView import list_view_type
from Be.Alert import alert_type
from Be.ColorControl import color_control_layout
from Be import InterfaceDefs
from Be.InterfaceDefs import border_style
from Be import AppDefs

from Be import BEntry
from Be.Entry import entry_ref
from Be.Entry import get_ref_for_path


class PBox(BBox):
	def __init__(self,frame,name,immagine):
		self.immagine = immagine
		self.frame = frame
		BBox.__init__(self,frame,name,0x0202|0x0404,InterfaceDefs.border_style.B_FANCY_BORDER)
		
	def Draw(self,rect):
		BBox.Draw(self, rect)
		inset = BRect(4, 4, self.frame.Width()-4, self.frame.Height()-4)
		self.DrawBitmap(self.immagine, inset)
		
class PView(BView):
	def __init__(self,frame,name,immagine):
		self.immagine=immagine
		self.frame=frame
		BView.__init__(self,self.frame,name,8, 20000000)
		
	def UpdateImg(self,immagine):
		self.Draw(self.frame)
		self.immagine=immagine
		rect=BRect(0,0,self.frame.Width(),self.frame.Height())
		self.DrawBitmap(self.immagine,rect)

	def Draw(self,rect):
		BView.Draw(self,rect)
		print("Disegno PView")
		rect=BRect(0,0,self.frame.Width(),self.frame.Height())
		self.DrawBitmap(self.immagine,rect)
		
class PBut(BButton):
	def __init__(self,frame,name,caption,msg,immagine,immaginedown):
		self.immagine=immagine
		self.imgdown=immaginedown
		self.frame=frame
		BButton.__init__(self, frame, name, caption, msg)

	def Draw(self,rect):
		BButton.Draw(self, rect)
		inset = BRect(4, 4, self.frame.Width()-4, self.frame.Height()-4)
		if self.Value():
			self.DrawBitmap(self.immagine, inset)
		else:
			self.DrawBitmap(self.imgdown, inset)
		

class StrangeItem(BStringItem):
	nocolor = (0, 0, 0, 0)
	gcolor = (0, 200, 0, 0)
	def __init__(self, testo,colore):
		self.testo = testo
		self.color = colore
		BStringItem.__init__(self,testo)
	def Text(self):
		return self.testo
	def Color(self):
		return self.color

class NewsItem(BListItem):
	nocolor = (0, 0, 0, 0)

	def __init__(self, name,color):
		self.name = name
		self.color=color
		BListItem.__init__(self)

	def DrawItem(self, owner, frame, complete):
		if self.IsSelected() or complete:
			color = (200,200,200,255)
			owner.SetHighColor(180,0,0,255)
			owner.SetLowColor(200,200,200,255)
			owner.FillRect(frame)
			owner.SetHighColor(0,0,0,255)
			owner.SetLowColor(255,255,255,255)
			#self.color=self.nocolor
		#owner.SetHighColor(self.color)
		#if self.color == (200,0,0,0):
		#	self.font = be_bold_font
		#	owner.SetFont(self.font)
		#else:	
		#	self.font = be_plain_font
		#	owner.SetFont(self.font)
		#frame.PrintToStream()
		owner.MovePenTo(5,frame.Height()-2)
		owner.DrawString("▶ "+self.name,None)

	def Text(self):
		return self.name


class ScrollView:
	HiWhat = 32 #Doppioclick
	def __init__(self, rect, name):
		self.lv = BListView(rect, name, list_view_type.B_SINGLE_SELECTION_LIST)
		self.sv = BScrollView('ScrollView', self.lv)#, 0x0202,0,False,False, border_style.B_FANCY_BORDER)#|0x1030

	def topview(self):
		return self.sv

	def listview(self):
		return self.lv

class Window(BWindow):
	Menus = (
		('File', ((1, 'asd'),(2, 'lol'),(5, 'bubu'),(None, None),(AppDefs.B_QUIT_REQUESTED, 'Quit'))),
		('Help', ((8, 'Help'),(3, 'About')))
		)
	CLRCTL = 4
	
	def __init__(self):
		BWindow.__init__(self, BRect(100,100,600,750), "Hello Haiku!", window_type.B_TITLED_WINDOW,  B_NOT_RESIZABLE | B_QUIT_ON_WINDOW_CLOSE)
		bounds=self.Bounds()
		self.bckgnd = BView(self.Bounds(), "background", 8, 20000000)
		self.maintabview = BTabView(BRect(2.0, 2.0, bounds.Width()-2.0, bounds.Height()-2.0), 'tabview')
		self.panel = BView(self.Bounds(), "panel", 8, 20000000)
		self.panel2 = BView(self.Bounds(), "panel2", 8, 20000000)
		self.panel3 = BView(self.Bounds(), "panel2", 8, 20000000)
		self.box = BBox(BRect(200,30,280,55),"MYBox",0x0202|0x0404,InterfaceDefs.border_style.B_FANCY_BORDER)
		self.box2 = BBox(BRect(10,10,self.panel2.Bounds().Width()-20,40),"MYBox2",0x0202|0x0404,InterfaceDefs.border_style.B_FANCY_BORDER)
		self.panel2.AddChild(self.box2,None)
		#self.box.SetHighColor(0, 200, 0, 0)
		#paternale=Pattern()
		#paternale.data=[0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff]
		#self.box.FillRect(self.box.Bounds(),paternale.toPattern())
		self.bar = BMenuBar(self.panel.Bounds(), 'Bar')
		self.testo = BStringView(BRect(6,8,75,22), 'Test','prova')
		self.box.AddChild(self.testo,None)
		self.statbar = BStatusBar(BRect(10,70,bounds.Width()/2-15,144), 'progress','Progress: ', '')
		self.statbar.SetMaxValue(100.0)
		self.tachetest=BTextControl(BRect(57,bounds.Height()-30,bounds.Width()-57,bounds.Height()-12),'TxTCtrl', "prova:",None,BMessage(1),0x0202|0x0404)
		self.tachetest.SetDivider(55.0)
		self.startimer= BCheckBox(BRect(10,30,290,50),'Testbox','Test Checkbox',BMessage(612))
		self.point=BPoint()
		self.cc= BColorControl(BPoint(8, 128), color_control_layout.B_CELLS_32x8, 8.0,'colors', BMessage(self.CLRCTL), 0)
		self.sixradio = BRadioButton(BRect(8,220,28,240),'hotradio', 'hot', BMessage(6))
		self.sevenradio = BRadioButton(BRect(8,240,28,260),'tepidradio', 'tepid', BMessage(7))
		self.nineradio = BRadioButton(BRect(8,260,28,280),'coolradio', 'cool', BMessage(9))
		scrn = BScreen(self)
		img1,retu = scrn.GetBitmap(True,BRect(0,0,200,200))
		if not retu:
			#print(img1.Bits())
			print(img1.Flags())
			print(img1.BitsLength())
		img2=BBitmap(self.panel2.Bounds(),color_space.B_RGBA32)
		#img2.ImportBits(img1)
		img2,reto = scrn.GetBitmap(True,self.panel3.Bounds())
		if not reto:
			self.PicBox = PBox(self.panel3.Bounds(),"PictureBox",img2)
			self.panel3.AddChild(self.PicBox,None)
		#self.panel3 = PView(self.Bounds(), "panel3",img2)
		#link=sys.path[0]+"/help/minusmine.bmp"
		#img=BTranslationUtils.GetBitmap(link)
		#link2=sys.path[0]+"/help/minusmined.bmp"
		#img2=BTranslationUtils.GetBitmap(link2)
		if retu+reto == 0:
			self.fadBtn = PBut(BRect(50, 220, 86, 256), "Quit","⎆", BMessage(2),img1,img2)#img2,img)AppDefs.B_QUIT_REQUESTED
			self.panel.AddChild(self.fadBtn,None)
		# Handling colors##################
		#colore=self.list.lv.HighColor()
		#print("colore è:",colore.red,colore.green,colore.blue,colore.alpha)
		#colore.set_to(10,200,100,255)
		#print("colore modificato è:",colore.red,colore.green,colore.blue,colore.alpha)
		#self.list.lv.SetHighColor(colore)
		#self.list.lv.SetLowColor(colore)
		####################################
		bup=BPicture()
		#arrgh=[]
		#arrgh.append(BView.MovePenTo(BPoint(3.0,16.0)))
		#arrgh.append(BView.DrawString("On",None))
		#bup.Play(arrgh,len(arrgh),None)
		bdown=BPicture()
		butupdown=BPictureButton(BRect(bounds.Width()-32,180,bounds.Width()-16,196),"TwoStateButt",bup,bdown,BMessage(333),picture_button_behavior.B_TWO_STATE_BUTTON)

		self.list = ScrollView(BRect(8 , 300, bounds.Width() - 18 , bounds.Height() - 42 ), 'ScrollView')
		global newsitem
			# TODO: newsitem (defined below) seems to be freed by Python as soon
			# as Python is finished with the __init__ function. But we still
			# need to have it around afterwards. The goal of this hack is to
			# make it that Python never frees NewsItem. The actual fix would
			# involve something like Haiku-PyAPI telling Python that it has a
			# reference to NewsItem and so cannot free it until Haiku-PyAPI
			# is finished with it
		newsitem = NewsItem("Nuova",(255,0,0,0))
		self.elementolista=BStringItem("Questo è un BStringItem")
		#global strano
		strano = StrangeItem("Questo è uno StrangeItem",(0,200,0,0))
		print("strano gcolor è:",strano.gcolor)
		#print(type(self.list.lv))
		#print(self.list.lv.Items())
		#print(self.list.lv.CountItems())
		self.list.lv.AddItem(newsitem)
		self.list.lv.AddItem(self.elementolista)
		self.list.lv.AddItem(strano)
		print(self.list.lv.Items())
		print(self.list.lv.IndexOf(self.elementolista))
		self.list.sv.Show()
		#self.panel.AddChild(self.list.topview(),None)
		self.panel.AddChild(self.box,None)
		self.panel.AddChild(self.sixradio,None)
		self.panel.AddChild(self.sevenradio,None)
		self.panel.AddChild(self.nineradio,None)
		self.panel.AddChild(butupdown,None)
		self.panel.AddChild(self.cc,None)
		self.panel.AddChild(self.startimer,None)
		self.panel.AddChild(self.tachetest,None)
		self.panel.AddChild(self.statbar,None)
		self.panel.AddChild(self.bar,None)
		for menu, items in self.Menus:
			menu = BMenu(menu)
			for k, name in items:
				if k is None:
						menu.AddItem(BSeparatorItem())
				else:
						menu.AddItem(BMenuItem(name, BMessage(k),name[1],0))
			self.bar.AddItem(menu)
		self.tabslabels=[]
		self.tabsviews=[]
		self.tabsviews.append(self.panel)
		self.tabsviews.append(self.panel2)
		self.tabsviews.append(self.panel3)
		
		tabrect=BRect(3.0, 3.0, 30.0, self.maintabview.TabHeight()-3.0)
		scheda=BTab(None)
		#scheda.SetLabel("Principale") <--- works after maintabview.AddTab
		scheda2=BTab(None)
		scheda3=BTab(None)
		self.tabslabels.append(scheda)
		self.tabslabels.append(scheda2)
		self.tabslabels.append(scheda3)
		
		self.maintabview.AddTab(self.tabsviews[0],self.tabslabels[0])
		self.maintabview.AddTab(self.tabsviews[1],self.tabslabels[1])
		self.maintabview.AddTab(self.tabsviews[2],self.tabslabels[2])

		self.bckgnd.AddChild(self.maintabview,None)
		scheda.SetLabel("Principale")
		scheda2.SetLabel("Scrittura")
		scheda3.SetLabel("Draw Bitmap")
		
		#self.panel3.DrawBitmap(img1)
		#self.panel3.UpdateImg(img1)
		#self.panel3.Draw(self.panel3.Bounds())
		
		from Be.Font import be_plain_font
		from Be.Font import be_bold_font
		#from Be.View import set_font_mask		
		self.typtap=BTextView(BRect(10,45,self.panel2.Bounds().Width()-20,self.panel2.Bounds().Height()-20-self.maintabview.TabHeight()), 'TxTView', BRect(5,5,self.panel2.Bounds().Width()-35,self.panel2.Bounds().Height()-30-self.maintabview.TabHeight()), 0x1234, 20000000)
		self.typtap.SetStylable(1)
		self.panel2.AddChild(self.typtap,None)
		colore=self.panel.HighColor()
		#print(colore.red,colore.green,colore.blue,colore.alpha)
		
		colore.red=180
		self.typtap.SetFontAndColor(be_plain_font,511,colore)#B_FONT_ALL = 511
		stuff = '\n\t\t\t\t\t\t\tHello Haiku!\n\n\t\t\t\t\t\t\t\t\t\t\tA simple test program\n\t\t\t\t\t\t\t\t\t\t\tfor Haiku, version 1.0\n\t\t\t\t\t\t\t\t\t\t\tsample code included!\n\n\t\t\t\t\t\t\t\t\t\t\tby Fabio Tomat aka TmTFx\n\t\t\t\t\t\t\t\t\t\t\tand others\n\t\t\t\t\t\t\t\t\t\t\t\n\n\t\t\t\t\t\t\t\t\t\t\tspecial thanks to:\n\t\t\t\t\t\t\t\t\t\t\tZardshard and coolcoder613'
		#n = stuff.find('Bulletin Gator')
		#m = stuff.find('This')
		self.typtap.SetText(stuff,None)#, [(0, be_plain_font, (0, 0, 0, 0)), (n, be_bold_font, (0, 150, 0, 0)), (n + 14, be_plain_font, (0, 0, 0, 0)),(m,be_plain_font,(100,150,0,0))])
		self.AddChild(self.bckgnd,None)
		self.panel.AddChild(self.list.topview(),None)
		###### Example handling refs / BEntry #####
		a=entry_ref()
		get_ref_for_path("/boot/home",a)
		b=BEntry("/boot/home")
		b.Exists()
		#to complete
		###########################################
		
	def MessageReceived(self, msg):
		if msg.what == 1:
			self.startimer.SetValue(not(self.startimer.Value()))
		elif msg.what == 2:
			x=round(self.statbar.CurrentValue())
			if x<100:
				outtxt=str(x+1)+"%"
				self.statbar.Update(1.0,outtxt,"100%")
		elif msg.what == 8:
			ask = BAlert('Whoa!', 'Are you sure you need help?', 'Yes','No', None, InterfaceDefs.B_WIDTH_AS_USUAL, alert_type.B_IDEA_ALERT)
			answ=ask.Go()
			if answ==0:
				risp = BAlert('lol', 'Well there\'s no help manual here', 'Bummer', None,None,InterfaceDefs.B_WIDTH_AS_USUAL,alert_type.B_INFO_ALERT)
				risp.Go()
			else:
				risp = BAlert('lol', 'If you think so...', 'Poor me', None,None,InterfaceDefs.B_WIDTH_AS_USUAL,alert_type.B_WARNING_ALERT)
				risp.Go()
		BWindow.MessageReceived(self, msg)
		
	def FrameResized(self,x,y):
		self.ResizeToPreferred()
		
	def QuitRequested(self):
		print ("So long and thanks for all the fish")
		return BWindow.QuitRequested(self)
		
class App(BApplication):
    def __init__(self):
        BApplication.__init__(self, "application/x-python")
    def ReadyToRun(self):
        self.window = Window()
        self.window.Show()

def main():
    global be_app
    be_app = App()
    be_app.Run()
    print('so said dolphins...')
 
if __name__ == "__main__":
    main()
