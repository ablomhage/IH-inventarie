# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Copyright (c) 2011, Andreas Blomhage
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the <organization> nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL Andreas Blomhage BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#-------------------------------------------------------------------------------

__author__="Andreas Blomhage"
__date__ ="$2011-mar-28 11:01:51$"


import wx
import wx.xrc as xrc
import wx.lib.agw.flatnotebook as fnb

import os

import sys

import dbhandler

import gui.objects.list as objectslist
import gui.objects.add as objectsadd
import gui.owners.list as ownerslist
import gui.owners.add as ownersadd
import gui.loaners.list as loanerslist
import gui.loaners.add as loanersadd
import gui.types.list as typelist
import gui.storage.add as storageadd
import gui.list


ID_EXIT         = wx.NewId()
ID_ADDOBJECT    = wx.NewId()
ID_ADDOWNER     = wx.NewId()
ID_ADDLOANER    = wx.NewId()
ID_ADDSTORAGE   = wx.NewId()
ID_ADDTYPE      = wx.NewId()
ID_ABOUT        = wx.NewId()
ID_LISTOBJECT   = wx.NewId()
ID_LISTOWNER    = wx.NewId()
ID_LISTLOANER   = wx.NewId()
ID_LISTTYPE     = wx.NewId()
ID_LISTSTORAGE  = wx.NewId()

class MainFrameOld(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title,
                         wx.DefaultPosition, size=(800,600))
        self.CreateStatusBar()
        self.create_menubar()
        self.layout_items()

    def create_menubar(self):
        filemenu = wx.Menu()
#        filemenu.AppendMenu(wx.ID_ANY, "&Lägg till", addmenu);
        #TODO: Add the possibility to print, change the text when that is done.
        filemenu.Append(wx.ID_ANY, "Skriv ut", u"Utskriftsmöjligheter, ej implementerad.")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, "Avslu&ta", "Avslutar programmet")

        addmenu = wx.Menu()
        addmenu.Append(ID_ADDOBJECT, "O&bjekt",
            u"Lägg till ett nytt objekt")
        addmenu.Append(ID_ADDOWNER,u"&Ägare",
            u"Lägg till en ny ägare")
        addmenu.Append(ID_ADDLOANER,u"L&åntagare",
            u"Lägg till en ny låntagare")
        addmenu.Append(ID_ADDTYPE,"&Typ",
            u"Lägg till en ny objekt-typ")
        addmenu.Append(ID_ADDSTORAGE,u"Förvaring",
            u"Lägg till en ny förvaringsplats")
        
        listmenu = wx.Menu()
        listmenu.Append(ID_LISTOBJECT, u"Objekt")
        listmenu.Append(ID_LISTOWNER, u"Ägare")
        listmenu.Append(ID_LISTLOANER, u"Låntagare")
        listmenu.Append(ID_LISTTYPE, u"Typer")
        listmenu.Append(ID_LISTSTORAGE, u"Förvaringsplatser")

        helpmenu = wx.Menu()
        helpmenu.Append(301, u"Hjälp", u"Ett litet hjälpavsnitt om programmet.")

        helpmenu.AppendSeparator()
        helpmenu.Append(ID_ABOUT, "&Om",
                    "Mer information om detta program")

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, u"&Arkiv");
        menuBar.Append(addmenu, u"&Lägg till")
        menuBar.Append(listmenu, u"Lista")
        menuBar.Append(helpmenu, u"Hjälp")

        self.SetMenuBar(menuBar)

        wx.EVT_MENU(self, ID_ABOUT, self.OnAbout)
        wx.EVT_MENU(self, wx.ID_EXIT,  self.TimeToQuit)
        wx.EVT_MENU(self, ID_ADDOBJECT, self.OnAddObject)
        wx.EVT_MENU(self, ID_ADDOWNER, self.OnAddOwner)
        wx.EVT_MENU(self, ID_ADDLOANER, self.OnAddLoaner)
        wx.EVT_MENU(self, ID_ADDTYPE, self.OnAddType)
        wx.EVT_MENU(self, ID_ADDSTORAGE, self.OnAddStorage)

        wx.EVT_MENU(self, ID_LISTOBJECT, self.OnListObjects)
        wx.EVT_MENU(self, ID_LISTOWNER, self.OnListOwners)
        wx.EVT_MENU(self, ID_LISTLOANER, self.OnListLoaners)
        wx.EVT_MENU(self, ID_LISTTYPE, self.OnListTypes)
        wx.EVT_MENU(self, ID_LISTSTORAGE, self.OnListStorage)

    def layout_items(self):
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(mainSizer)

        bookStyle = fnb.FNB_NODRAG | fnb.FNB_X_ON_TAB | fnb.FNB_NO_X_BUTTON | fnb.FNB_NO_NAV_BUTTONS | fnb.FNB_NO_NAV_BUTTONS | fnb.FNB_HIDE_ON_SINGLE_TAB | fnb.FNB_FF2

        self.book = fnb.FlatNotebook(self, wx.ID_ANY, agwStyle=bookStyle)

        bookStyle &= ~(fnb.FNB_NODRAG)
        bookStyle |= fnb.FNB_ALLOW_FOREIGN_DND

        mainSizer.Add(self.book, 6, wx.EXPAND)

#        self.Freeze()
#
#        text = wx.TextCtrl(self.book, -1, "Second Book Page 1\n", style=wx.TE_MULTILINE|wx.TE_READONLY)
#        self.book.AddPage(text, "Second Book Page 1")
#
#        self.Thaw()

        mainSizer.Layout()
        self.SendSizeEvent()

    #Did not find a better way to do it, will keep looking, probably missed a way.
    def IsTabOpen(self, caption):
        pageCount = self.book.GetPageCount()
        returnValue = -1
        
        for i in range(pageCount):
            if(self.book.GetPageText(i) == caption):
                returnValue = i
                break
            
        return returnValue

    def OnAbout(self, event):
        dlg = wx.MessageDialog(self, "",
                              "About Me", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()


    def TimeToQuit(self, event):
        self.Destroy()
        #self.Close(true)


    def OnAddObject(self, event):
        dlg = objectsadd.ObjectAdd(self, -1, u"Lägg till ett objekt")
#        dlg = gui.addframes.addobjectdialog.AddObjectDialog(self, -1, u"Lägg till ett objekt")

    def OnAddOwner(self, event):
        dlg = ownersadd.AddOwnerDialog(self, -1, u"Lägg till ägare")
#        dlg = gui.addframes.addownerdialog.AddOwnerDialog(self, -1, u"Lägg till ägare")

    def OnAddLoaner(self, event):
        dlg = loanersadd.AddLoanerDialog(self, -1, u"Lägg till låntagare")

    def OnAddStorage(self, event):
        dlg = storageadd.AddStorageDialog(self, -1, u"Lägg till förvaringsplats")

    def OnAddType(self, event):
        dlg = wx.TextEntryDialog(self, 'Enter some text',u'Lägg till typ')
        dlg.SetValue("")
        if dlg.ShowModal() == wx.ID_OK:
            mydb = dbhandler.ObjectTypesDB()
            type = dlg.GetValue()
            mydb.insert_into_table(type)

        dlg.Destroy()
        
    

    def OnListObjects(self, event):
        caption = u"Objekt"
        page = self.IsTabOpen(caption)
        if(page > -1):
            self.book.SetSelection(page)
        else:
            self.Freeze()
            self.book.AddPage(objectslist.ObjectList(wx.Panel(self.book)), caption, True)
            self.Thaw()
        
    def OnListOwners(self, event):
        caption = u"Ägare"
        
        page = self.IsTabOpen(caption)
        if(page > -1):
            self.book.SetSelection(page)
        else:
            self.Freeze()
            self.book.AddPage(ownerslist.OwnersList(wx.Panel(self.book)), caption, True)
            self.Thaw()

    def OnListLoaners(self, event):
        caption = u"Låntagare"
        
        page = self.IsTabOpen(caption)
        if(page > -1):
            self.book.SetSelection(page)
        else:
            self.Freeze()
            self.book.AddPage(loanerslist.LoanersList(wx.Panel(self.book)), caption, True)
            self.Thaw()
    
    def OnListTypes(self, event):
        caption = u"Typer"
        
        page = self.IsTabOpen(caption)
        if(page > -1):
            self.book.SetSelection(page)
        else:
            self.Freeze()
            self.book.AddPage(typelist.TypeList(wx.Panel(self.book)), caption, True)
            self.Thaw()
    
    def OnListStorage(self, event):
        pass

#    def create_page(self, caption):
#        panel = wx.Panel(self.book)
#        page = objectslist.list((wx.Panel(self.book)))
#        return page

# End of class MainFrame

class TabPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        sizer = wx.BoxSizer(wx.VERTICAL)
        txtOne = wx.TextCtrl(self, wx.ID_ANY, "")
        txtTwo = wx.TextCtrl(self, wx.ID_ANY, "")
         
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(txtOne, 0, wx.ALL, 5)
        sizer.Add(txtTwo, 0, wx.ALL, 5)
         
        self.SetSizer(sizer)

class MainFrame(wx.Frame):
    def __init__(self): 
        pre = wx.PreFrame()
        # XRC will do the Create
        self.PostCreate(pre)
        self.Bind(wx.EVT_WINDOW_CREATE, self.onCreate)

    def onCreate(self, evt):
        print("Kommer vi ens hit?")
        self.Unbind(wx.EVT_WINDOW_CREATE)
        wx.CallAfter(self._PostInit)
#        event.Skip()
        self.Fit()
        self.notebook = xrc.XRCCTRL(self, 'mainNB')
#        tmp = TabPanel(self.notebook)
        res = xrc.XmlResource("objectlist.xrc")
        tmp = res.LoadPanel(self.notebook, "objectListPanel")
        #TODO: Seems we can't get the same behaviour here so make sure to fix it.
        self.notebook.AddPage(tmp, "TabOne")
        

class MyApp(wx.App):
    def OnInit(self):
        # Load all controls:
#        self.res = xrc.XmlResource(os.path.join"mainframe.xrc")

        dname = os.path.dirname(sys.argv[0])
        tmprestxt = file(os.path.join(dname + "\gui\mainframe.xrc")).read()
        self.res = xrc.EmptyXmlResource()
#        self.res.InsertHandler(FlatNotebookXmlHandler())
        self.res.LoadFromString(tmprestxt) 
#        self.frame = MainFrame(None, self.res) 
        self.frame = self.res.LoadFrame(None, 'mainFrame')
        self.notebook = xrc.XRCCTRL(self.frame, 'mainNB')
#        tmp = TabPanel(self.notebook)
        tmprestxt = file(os.path.join(dname + "\gui\objectlist.xrc")).read()
        self.res = xrc.EmptyXmlResource()
        self.res.LoadFromString(tmprestxt)
        tmp = self.res.LoadPanel(self.notebook, "objectListPanel")
        #TODO: Seems we can't get the same behaviour here so make sure to fix it.
        self.notebook.AddPage(tmp, "TabOne")
        self.SetTopWindow(self.frame)
        self.frame.Show(True)
        return True 
    
    def _do_layout(self):
        frame = MainFrame(None, -1, "Interaktiv Historias inventarie")
#        self.res = xrc.XmlResource(' GUI_FILENAME ')
        frame.Centre()
        frame.Show()
        self.SetTopWindow(frame)

    def InitFrame(self):
        self.frame = self.res.LoadFrame(None, 'mainFrame')
        
#        self.textLocation = xrc.XRCCTRL(self.frame, 'textLocation')
#        self.tcLocation = xrc.XRCCTRL(self.frame, 'tcLocation')
        
    def InitEverythingElse(self):
        pass
#        sizer = self.frame.GetSizer()
#        sizer.Fit(self.frame)
#        sizer.SetSizeHints(self.frame)
#        self.frame.Show()
    
#    def _do_layout(self):
#        self.res = xrc.XmlResource( GUI_FILENAME )
#        self.frame = self.res.LoadFrame( None, GUI_MAINFRAME_NAME )
#        self.SetTopWindow(self.frame)
#        self.frame.Show(1)
    
#    def OnInit(self):
#        frame = MainFrame(None, -1, "Interaktiv Historias inventarie")
#        frame.Centre()
#        frame.Show()
#        self.SetTopWindow(frame)
#        return 1
# End of class MyApp
