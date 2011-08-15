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

import wx
import dbhandler
import gui.errordialogs as errdlg

'''
Created: 2011-07-07

@author: Andreas Blomhage
'''

class AddStorageDialog(wx.Dialog):
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title, size=(500,300))
        self.__InitUI()
        self.Centre()
        self.Show()

    def __InitUI(self):
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        grid = wx.GridBagSizer(hgap=5, vgap=7)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        #=======================================================================
        # Location    
        #=======================================================================
        textLocation        = wx.StaticText(self, label="Lokal: ")
        self.tcLocation     = wx.TextCtrl(self, wx.ID_ANY, size=(150,-1))
        grid.Add(textLocation, pos=(0,0))
        grid.Add(self.tcLocation, pos=(0,1))
        
        #=======================================================================
        # Room    
        #=======================================================================
        textRoom            = wx.StaticText(self, label="Rum: ")
        self.tcRoom         = wx.TextCtrl(self, wx.ID_ANY, size=(150,-1))
        grid.Add(textRoom, pos=(0,2))
        grid.Add(self.tcRoom, pos=(0,3))
        
        btClose = wx.Button(self, wx.ID_CLOSE, u"Stäng")
        btSave  = wx.Button(self, wx.ID_SAVE, u"Spara")

        buttons = wx.BoxSizer(wx.HORIZONTAL)
        
        buttons.Add(btSave, wx.RIGHT)
        buttons.Add(btClose, wx.RIGHT)
        
        self.Bind(wx.EVT_BUTTON, self.OnSave, id=wx.ID_SAVE)
        self.Bind(wx.EVT_BUTTON, self.OnQuit, id=wx.ID_CLOSE)
        
        hSizer.Add(grid, 0, wx.ALL, 5)

        mainSizer.Add(hSizer, 0, wx.ALL, 5)
        mainSizer.Add(buttons, 0, wx.ALIGN_RIGHT)
        self.SetSizerAndFit(mainSizer)
        
        
    def OnQuit( self, event ):
        self.Close()
    
    def OnSave( self, event ):
        location    = self.tcLocation.GetValue()
        room        = self.tcRoom.GetValue()
        insert      = (location, room)
        mydb = dbhandler.StorageDB()
        try:
                mydb.AddStorage(insert)
        except dbhandler.IntegrityError:
            #TODO: Needs a way to distinguise between a Null error and a unique error
            pass
        else:
            pass
        