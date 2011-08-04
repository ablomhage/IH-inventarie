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
# -*- coding: UTF-8 -*-
'''
Created on 10 maj 2011

@author: Andreas Blomhage
'''

import gui.templates.list as listtmpl
import gui.objects.info as objectinfo
import dbhandler

class ObjectList(listtmpl.ListTmpl):
    def __init__(self, parent):
        listtmpl.ListTmpl.__init__(self, parent)

    def FetchData(self):
        try:
            self.SetColumns([u"ID", u"Benämning", u"Typ", u"Ägare", u"Förvaringsplats"])
            self.SetColumnWidth([50, -1, 100, 100, 100]) 
            self.SetItems(dict(enumerate(dbhandler.ObjectsDB().RetriveSpecificObjectData("objectid, description, type, owner, storage"))))
        except:
            self.SetItems({ })
            print("Error retriving object data from database")
            
    def PopulateList(self):
        self.DefineListHeader()
        items = self.GetItems().items()
        for key, data in items:
            owner = dbhandler.OwnerDB().RetriveOwner(data[3])
#            data = data[:3] + (owner,data[4:],)
            tmpdata = list(data)
            tmpdata[3] = owner
            data = tuple(tmpdata)
            self.AppendListItem(key, data)

        self.currentItem = 0
        
#    def FetchData(self):
#        try: 
#            self.__items = dict(enumerate(dbhandler.ObjectsDB().RetriveSpecificObjectData("objectid, description, type, owner, storage")))
#        except:
#            self.__items = { }
#            print("Error retriving objectdata from database")

#    def PopulateList(self):
#        self.listCtrl.InsertColumn(0, u"ID")
#        self.listCtrl.InsertColumn(1, u"Benämning")
#        self.listCtrl.InsertColumn(2, u"Typ")
#        self.listCtrl.InsertColumn(3, u"Ägare")
#        self.listCtrl.InsertColumn(4, u"Förvaringsplats")
#        
#        
#        items = self.__items.items()
#        for key, data in items:
#            owner = dbhandler.OwnerDB().RetriveOwner(data[3])
#            __index = self.listCtrl.InsertStringItem(sys.maxint, data[0])
#            self.listCtrl.SetStringItem(__index, 1, data[1])
#            self.listCtrl.SetStringItem(__index, 2, data[2])
#            self.listCtrl.SetStringItem(__index, 3, owner)
#            self.listCtrl.SetStringItem(__index, 4, data[4])
##            self.listCtrl.SetItemData(0, __index) 
#
#            self.listCtrl.SetItemData(__index, key)
##            __key = __key + 1
#            
##            self.listCtrl.sortColumn = 0 
#
#        self.listCtrl.SetColumnWidth(0, 50)
#        self.listCtrl.SetColumnWidth(1, wx.LIST_AUTOSIZE)
#        self.listCtrl.SetColumnWidth(2, 100)
#
#        self.listCtrl.SetItemState(5, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
#
#        self.currentItem = 0
#
#    def RefreshList(self):
#        self.listCtrl.ClearAll()
#        self.FetchData()
#        self.PopulateList()
#
#    # Used by the ColumnSorterMixin, see wx/lib/mixins/listctrl.py
#    def GetListCtrl(self):
#        return self.listCtrl
#
#    # Used by the ColumnSorterMixin, see wx/lib/mixins/listctrl.py
##    def GetSortImages(self):
##        return (self.sm_dn, self.sm_up)
#
#    def GetColumnSorter(self):
#        return self.CustColumnSorter
#   
#    def CustColumnSorter(self, key1, key2):
#        col = self._col
#        ascending = self._colSortFlag[col]
#        item1 = self.itemDataMap[key1][col]
#        item2 = self.itemDataMap[key2][col]
#        
#        cmpVal = ""
#
#        try: 
#            i1 = int(item1)
#            i2 = int(item2)
#        except ValueError:
#            cmpVal = locale.strcoll(item1.lower(), item2.lower())
#        else:
#            cmpVal = cmp(i1, i2)
#            
#        if(ascending):
#            return cmpVal
#        else:
#            return -cmpVal
#        
#    def getColumnText(self, index, col):
#        item = self.listCtrl.GetItem(index, col)
#        return item.GetText()
#
#    def OnItemSelected(self, event):
#        ##print event.GetItem().GetTextColour()
#        self.currentItem = event.m_itemIndex
#        print("OnItemSelected: %s, %s, %s, %s\n" %
#                           (self.currentItem,
#                            self.listCtrl.GetItemText(self.currentItem),
#                            self.getColumnText(self.currentItem, 1),
#                            self.getColumnText(self.currentItem, 2)))
#
#        if self.currentItem == 10:
##            self.log.WriteText("OnItemSelected: Veto'd selection\n")
#            #event.Veto()  # doesn't work
#            # this does
#            self.listCtrl.SetItemState(10, 0, wx.LIST_STATE_SELECTED)
#
#        event.Skip()
#
#    def OnItemDeselected(self, evt):
#        item = evt.GetItem()
##        self.log.WriteText("OnItemDeselected: %d" % evt.m_itemIndex)
#
#        # Show how to reselect something we don't want deselected
#        if evt.m_itemIndex == 11:
#            wx.CallAfter(self.listCtrl.SetItemState, 11, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
#
#        
#    def OnColClick(self, event):
#        self._col = event.GetColumn()
#        event.Skip()
#        
    def OnDoubleClick(self, event):
        dlg = objectinfo.ObjectInfo(self, -1, "Information", self.listCtrl.GetItemText(self.currentItem))
        event.Skip()

