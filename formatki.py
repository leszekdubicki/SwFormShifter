# -*- coding: cp1250 -*-
#Boa:Frame:Formatki

import wx
import prochecker, drwnum, os, os.path
def create(parent):
    return Formatki(parent)

[wxID_FORMATKI, wxID_FORMATKIBGET, wxID_FORMATKIBSELECT, wxID_FORMATKIBSTART, 
 wxID_FORMATKICLASTSESSION, wxID_FORMATKICSUBFOLDERS, wxID_FORMATKIGPROGRESS, 
 wxID_FORMATKILABEL, wxID_FORMATKIPANEL1, wxID_FORMATKISFOLDERINFO, 
 wxID_FORMATKISSTATS, wxID_FORMATKISTATICTEXT1, wxID_FORMATKISTATICTEXT2, 
 wxID_FORMATKITFOLDER, 
] = [wx.NewId() for _init_ctrls in range(14)]

def fileext(path):
	return path[path.rindex(".")+1:].lower()

import fnmatch, copy
def search_folder(INIT_DIR,MASK="*.slddrw", EXCL_MASK = None, FILE_DICT = [], SUBFOLDERS = False):
	#FILE_DICT={}
	#funkcja przekopiowana z promontera, zamiast słownika tworzy listę plików...
	INIT_DIR=INIT_DIR.replace("\\","/")
	if not INIT_DIR[-1]=="/":
		INIT_DIR+="/"
	#dodane w wersji 2.05
	if EXCL_MASK==None:
		EXCL_MASK = []
	elif not isinstance(EXCL_MASK, list):
		EXCL_MASK = [EXCL_MASK]
	for F in os.listdir(INIT_DIR):
		if os.path.isdir(INIT_DIR+F) and SUBFOLDERS:
			#print INIT_DIR+F
			EXCLUDED = 0
			for M in EXCL_MASK:
				if fnmatch.fnmatch(F, M):
					EXCLUDED = 1
					break
			#print EXCLUDED
			#raw_input()
			if not EXCLUDED:
				#FILE_DICT.update(search_folder(INIT_DIR+F,MASK,EXCL_MASK, FILE_DICT))
				FILE_DICT = FILE_DICT + search_folder(INIT_DIR+F,MASK,EXCL_MASK, [], SUBFOLDERS)
		elif fnmatch.fnmatch(F,MASK):
			#dodanie pliku do listy:
			FILE_DICT.append((INIT_DIR+F).replace("/","\\"))
			#print INIT_DIR+F
			#raw_input()
	return FILE_DICT


class FileDropTarget(wx.FileDropTarget):
    """ This object implements Drop Target functionality for Files """
    def __init__(self, obj):
        """ Initialize the Drop Target, passing in the Object Reference to
        indicate what should receive the dropped files """
        # Initialize the wxFileDropTarget Object
        wx.FileDropTarget.__init__(self)
        # Store the Object Reference for dropped files
        self.obj = obj

    def OnDropFiles(self, x, y, filenames):
        """ Implement File Drop """
        # For Demo purposes, this function appends a list of the files dropped at the end of the widget's text
        # Move Insertion Point to the end of the widget's text
        #self.obj.SetInsertionPointEnd()
        # append a list of the file names dropped
        #self.obj.WriteText("%d file(s) dropped at %d, %d:\n" % (len(filenames), x, y))
        #for file in filenames:
        if len(filenames) == 1:
            self.obj.Value = filenames[0]
        elif len(filenames) > 1:
            self.obj.Value = filenames[0]

class Formatki(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FORMATKI, name=u'Formatki', parent=prnt,
              pos=wx.Point(704, 344), size=wx.Size(812, 304),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'Zmiana formatek rysunkowych')
        self.SetClientSize(wx.Size(796, 266))

        self.panel1 = wx.Panel(id=wxID_FORMATKIPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(796, 266),
              style=wx.TAB_TRAVERSAL)

        self.label = wx.StaticText(id=wxID_FORMATKILABEL,
              label=u'Hurtowa zmiana formatek rysunkowych SolidWorks',
              name=u'label', parent=self.panel1, pos=wx.Point(184, 16),
              size=wx.Size(448, 32),
              style=wx.ST_NO_AUTORESIZE | wx.ALIGN_CENTRE)
        self.label.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Segoe UI'))

        self.tFolder = wx.TextCtrl(id=wxID_FORMATKITFOLDER, name=u'tFolder',
              parent=self.panel1, pos=wx.Point(16, 88), size=wx.Size(768, 23),
              style=0, value=u'')
        self.tFolder.Bind(wx.EVT_TEXT, self.OnTFolderText,
              id=wxID_FORMATKITFOLDER)

        self.bSelect = wx.Button(id=wxID_FORMATKIBSELECT,
              label=u'Otw\xf3rz folder', name=u'bSelect', parent=self.panel1,
              pos=wx.Point(16, 56), size=wx.Size(88, 26), style=0)
        self.bSelect.Bind(wx.EVT_BUTTON, self.OnBSelectButton,
              id=wxID_FORMATKIBSELECT)

        self.bGet = wx.Button(id=wxID_FORMATKIBGET, label=u'Pobierz z SW',
              name=u'bGet', parent=self.panel1, pos=wx.Point(120, 56),
              size=wx.Size(88, 26), style=0)
        self.bGet.Bind(wx.EVT_BUTTON, self.OnBGetButton, id=wxID_FORMATKIBGET)

        self.bStart = wx.Button(id=wxID_FORMATKIBSTART, label=u'START',
              name=u'bStart', parent=self.panel1, pos=wx.Point(176, 216),
              size=wx.Size(416, 40), style=0)
        self.bStart.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Segoe UI'))
        self.bStart.Bind(wx.EVT_BUTTON, self.OnBStartButton,
              id=wxID_FORMATKIBSTART)

        self.staticText1 = wx.StaticText(id=wxID_FORMATKISTATICTEXT1,
              label=u'by Leszek Dubicki', name='staticText1',
              parent=self.panel1, pos=wx.Point(720, 248), size=wx.Size(64, 12),
              style=0)
        self.staticText1.SetFont(wx.Font(6, wx.SWISS, wx.NORMAL, wx.NORMAL,
              True, u'Segoe UI'))

        self.sStats = wx.StaticText(id=wxID_FORMATKISSTATS, label=u'',
              name=u'sStats', parent=self.panel1, pos=wx.Point(16, 152),
              size=wx.Size(496, 24), style=wx.ST_NO_AUTORESIZE)

        self.staticText2 = wx.StaticText(id=wxID_FORMATKISTATICTEXT2,
              label=u'(Mo\u017cna te\u017c przeci\u0105gn\u0105\u0107 folder z eksploratora windows na okno programu)',
              name='staticText2', parent=self.panel1, pos=wx.Point(216, 64),
              size=wx.Size(438, 18), style=0)
        self.staticText2.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL,
              True, u'Segoe UI'))

        self.cSubFolders = wx.CheckBox(id=wxID_FORMATKICSUBFOLDERS,
              label=u'Uwzgl\u0119dnij podfoldery', name=u'cSubFolders',
              parent=self.panel1, pos=wx.Point(16, 120), size=wx.Size(144, 15),
              style=0)
        self.cSubFolders.SetValue(True)
        self.cSubFolders.Bind(wx.EVT_CHECKBOX, self.OnCSubFoldersCheckbox,
              id=wxID_FORMATKICSUBFOLDERS)

        self.sFolderInfo = wx.StaticText(id=wxID_FORMATKISFOLDERINFO, label=u'',
              name=u'sFolderInfo', parent=self.panel1, pos=wx.Point(16, 136),
              size=wx.Size(496, 16), style=wx.ST_NO_AUTORESIZE)

        self.gProgress = wx.Gauge(id=wxID_FORMATKIGPROGRESS, name=u'gProgress',
              parent=self.panel1, pos=wx.Point(16, 184), range=100,
              size=wx.Size(760, 24), style=wx.GA_HORIZONTAL)
        self.gProgress.SetValue(0)
        self.gProgress.SetLabel(u'')

        self.cLastSession = wx.CheckBox(id=wxID_FORMATKICLASTSESSION,
              label=u'Kontynuacja poprzedniej sesji', name=u'cLastSession',
              parent=self.panel1, pos=wx.Point(168, 120), size=wx.Size(216, 15),
              style=0)
        self.cLastSession.SetValue(False)
        self.cLastSession.Enable(False)
        self.cLastSession.Bind(wx.EVT_CHECKBOX, self.OnCLastSessionCheckbox,
              id=wxID_FORMATKICLASTSESSION)

    def __init__(self, parent):
        self._init_ctrls(parent)
        dt1 = FileDropTarget(self.tFolder)
        self._whatwasdone = None
        self.panel1.SetDropTarget(dt1)

    def OnBSelectButton(self, event):
        dialog = wx.DirDialog ( None, message = 'Wybierz katalog projektu' )
        if dialog.ShowModal() == wx.ID_OK:
            PRODIR = dialog.GetPath()
            #print PRODIR
            self.tFolder.SetValue(PRODIR)
            #self.prodir.Value = PRODIR
            #self.get_files()
        else:
            wx.MessageBox('Brak katalogu', 'UWAGA!')
        dialog.Destroy()
        event.Skip()

    def OnBGetButton(self, event):
        try:
            SWDOC = prochecker.get_data_from_model()
            PATH = SWDOC['path']
            self.tFolder.Value = PATH
            self.Refresh()
            #self.get_files()
        except:
            wx.MessageBox("Brak otwartego dokumentu!", 'BŁĄD!')
        event.Skip()
    def get_files(self):
        if not self.tFolder.Value=="" and os.path.isdir(self.tFolder.Value):
            self._files = []
            self._files = search_folder(self.tFolder.Value, "*.slddrw", None, [], self.cSubFolders.Value)
            #print self._files
            #for fff in self._files:
            #    print fff
            self.sFolderInfo.Label = "Łącznie "+str(len(self._files))+" rysunków."
            self.gProgress.Range = len(self._files)
            self.gProgress.Value = 0

    def OnBStartButton(self, event):
        #print fileext(PATH)
        DirName = self.tFolder.Value
        List = os.listdir(DirName)
        #print list
        #PRT = prochecker.get_data_from_model()
        PATH = self.tFolder.Value
        #FILES = os.listdir(PATH)
        FILES = self._files
        if self._whatwasdone == None:
            self._whatwasdone = prochecker.whatwasdone(self.tFolder.Value,"formatki")
            self._whatwasdone.createfile()
        Pos = 0
        for F in FILES:
            if self.cLastSession.Value == True and F in self._whatwasdone:
                print "pomijam plik "+F
                continue
            elif F[-7:].lower()==".slddrw":
                #print("Zmiana pliku "+os.path.basename(F))
                Pos+=1
                if os.path.isfile(F):
                    self.sStats.Label = "Zmiana pliku "+os.path.basename(F)
                    Err = None
                    prochecker.swx.OpenDoc6(F,0x3,0,None,Err,None)
                    #print "Error: "+str(Err)
                    #proceed_command("r")
                    PRT = prochecker.get_data_from_drawing()
                    PRT.open(); PRT.activate()
                    drwnum.proceed_command("sfs",prompt = 0)
                    PRT = prochecker.get_data_from_drawing()
                    PRT.open(); PRT.activate()
                    
                    PRT.save()
                    PRT.close()
                    self.gProgress.Value = Pos
                    self._whatwasdone.append(F)
        self.sStats.Label = "Gotowe! :)"
        self._whatwasdone.rmfile()
        event.Skip()

    def OnCSubFoldersCheckbox(self, event):
        self.get_files()
        event.Skip()

    def OnTFolderText(self, event):
        self.get_files()
        if not self.tFolder.Value=="" and os.path.isdir(self.tFolder.Value):
            self._whatwasdone = prochecker.whatwasdone(self.tFolder.Value,"formatki")
        if self._whatwasdone.has_file():
            self.cLastSession.Enabled = True
        event.Skip()

    def OnCLastSessionCheckbox(self, event):
        if self.cLastSession.Value:
            self._whatwasdone.readfile()
            self.sFolderInfo.Label = "Łącznie "+str(len(self._files)-len(self._whatwasdone))+" rysunków."
            self.gProgress.Range = len(self._files)-len(self._whatwasdone)
            self.gProgress.Value = 0
        else:
            self.sFolderInfo.Label = "Łącznie "+str(len(self._files))+" rysunków."
            self.gProgress.Range = len(self._files)
            self.gProgress.Value = 0
        event.Skip()
        


if __name__ == '__main__':
    #app = wx.PySimpleApp()
    app = wx.App(False)
    frame = create(None)
    frame.Show()

    app.MainLoop()
