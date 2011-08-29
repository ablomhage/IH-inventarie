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
__date__ ="$2011-mar-19 21:29:10$"

import sqlite3
import os

class IntegrityError(sqlite3.IntegrityError):
    "Used to indicate a integrity error within the database."

#TODO: Add classdocumentation
class DBBase(object):
    def __init__(self):
        """init"""

    def CreateTable(self, sql):
        try:
            con = sqlite3.connect(self.get_dbpath())
            cur = con.cursor()
            sql = "create table " + sql
            cur.execute(sql)
            con.commit()
            cur.close()
            con.close()
        except sqlite3.Error, error:
            print( str(error))

    def get_dbpath(self):
        
        dir = os.environ['APPDATA'] 
        dir = dir + r'\IH Inventarie'
        #This should be done at the installation of the software.
        if not os.path.isdir(dir):
            os.makedirs(dir)
        
        mydb = dir + r'\ih_inventarie.db'
        return mydb

    def insert_into_table(self, sql, data):
        con = sqlite3.connect(self.get_dbpath())
        cur = con.cursor()
        sql = "insert into " + sql
        try: 
            cur.execute(sql, data)
        except sqlite3.IntegrityError, e:
            print type(e)
            print e
            raise IntegrityError('Key already exists')
        con.commit()
        cur.close()
        con.close()

    def SearchTable(self, sql, criteria):
        con = sqlite3.connect(self.get_dbpath())
        cur = con.cursor()
        sql = "select " + sql
        cur.execute(sql, criteria)
        return cur.fetchall()
        cur.close()
        con.close()

    def select_from_table(self, sql):
        con = sqlite3.connect(self.get_dbpath())
        cur = con.cursor()
        sql = "select " + sql
        cur.execute(sql)
        return cur.fetchall()
        cur.close()
        con.close()
        
    def UpdateTable(self, sql, data):
        con = sqlite3.connect(self.get_dbpath())
        cur = con.cursor()
        sql = "update " + sql
        cur.execute(sql, data)
        con.commit()
        cur.close()
        con.close()

# End of class DBBase

#TODO: Add classdocumentation
class ObjectsDB(DBBase):
    def __init__(self):
        DBBase.__init__(self)
        DBBase.CreateTable(self, "objects(objectid text unique not null, type text, "+
            "measurment text, description text, owner integer not null, storage text, "+
            "availability integer, repairneeds text, rent integer, nationality text)")

    def InsertObject(self, data):
        sql = "objects values (?,?,?,?,?,?,?,?,?,?)"
        DBBase.insert_into_table(self, sql, data)

    def UpdateObject(self, objectID, data):
        sql = "objects set objectid=?, type=?, measurment=?, description=?, owner=?, storage=?, repairneeds=?, rent=?, nationality=? where objectid = " + objectID

        try:
            DBBase.UpdateTable(self, sql, data)
        except sqlite3.IntegrityError:
            raise IntegrityError('Key already exists')
    
    def RetriveObject(self, objectID):
        object = DBBase.SearchTable(self, "* from objects where objectid=?", (objectID, ))
        
        return object[0]

    def RetriveSpecificObjectData(self, pattern):
        sql = pattern + " FROM objects"
        list = DBBase.select_from_table(self, sql)
        return list
    
    #TODO: Add comments
    def RetriveAllObjects(self):
        list = DBBase.select_from_table(self, "* from objects")
        return list 
    
    def Search(self, column, criteria):
        #TODO: Figure out a good way to complete this method
        sql = "objectid, description, type, owner, storage from objects where " + column + " like ?"
        items = DBBase.SearchTable(self, sql, (criteria,))
    
# End of class ObjectsDB

#TODO: Add classdocumentation
class OwnerDB(DBBase):
    __tablename = ""
    def __init__(self):
        DBBase.__init__(self)
        self.__tablename = "owners"
        DBBase.CreateTable(self, self.__tablename + "(company varchar, " +
                "contact varchar, address varchar, zip integer, " +
                "town varchar, phone varchar, mobile varchar, email varchar)")

    def insert_into_table(self, data):
        sql = "owners values (?,?,?,?,?,?,?,?)"
        try:
            DBBase.insert_into_table(self, sql, data)
        except sqlite3.Error, error:
            print error

    def RetriveOwnerID(self, owner):
        ownerlist = owner.split(', ')
        try:
            list = DBBase.SearchTable(self, "rowid from " +
                self.__tablename + " where contact=? and address=?",(ownerlist[0],ownerlist[1],))

            try:
                return list[0][0]
            except:
                return None
        except:
            list = DBBase.SearchTable(self, "rowid from " +
                self.__tablename + " where company=?",(ownerlist[0],))
            try:
                return list[0][0]
            except:
                return None

    def RetriveOwner(self, ownerID):
        try:
            list = DBBase.SearchTable(self, "company, contact, address FROM " + self.__tablename + " WHERE _ROWID_=?", (ownerID,))
            owner = list[0]
        
            if(owner[0] == ''):
                ownerRet = owner[1] + ', ' + owner[2]
            else:
                ownerRet = owner[0]
                
            return ownerRet
        except:
            return "Okänd"


    def RetriveSpecificOwnerData(self, pattern):
        sql = pattern + " FROM " + self.__tablename
        list = DBBase.select_from_table(self, sql)
        return list

    def RetriveListOfOwners(self):
        list = DBBase.select_from_table(self, "company, contact, address from " + self.__tablename)
        returnlist = []
        for i in list:
            if(i[0] == ''):
                new = i[1] + ', ' + i[2]
                returnlist.append(new)
            else:
                returnlist.append(i[0])

        return returnlist
    
    #TODO: Add comments
    def RetriveAllOwners(self):
        list = DBBase.select_from_table(self, "* from " + self.__tablename)
       
        return list 
# End of class LoanerDB

#TODO: Add classdocumentation
class LoanerDB(DBBase):
    __tablename = ""
    
    def __init__(self):
        DBBase.__init__(self)
        self.__tablename = "loaners"
        DBBase.CreateTable(self, "loaners(company varchar, " +
                "contact varchar, address varchar, zip integer, " +
                "town varchar, phone varchar, mobile varchar, email varchar)")

    def insert_into_table(self, data):
        sql = "loaners values (?,?,?,?,?,?,?,?)"
        DBBase.insert_into_table(self, sql, data)
        
    def RetriveSpecificLoanerData(self, pattern):
        sql = pattern + " FROM " + self.__tablename
        list = DBBase.select_from_table(self, sql)
        return list
# End of class LoanerDB

#TODO: Add classdocumentation
class ObjectTypesDB(DBBase):
    __tablename = ""
    def __init__(self):
        DBBase.__init__(self)
        self.__tablename = "objecttypes"
        DBBase.CreateTable(self, self.__tablename + "(objecttype primary key)")

    def insert_into_table(self, data):
        sql = self.__tablename + " values (?)"
        DBBase.insert_into_table(self, sql, (data,))

    def RetriveAllTypes(self):
        list = DBBase.select_from_table(self, "objecttype from " + self.__tablename)
        return list

    def RetriveTypesSorted(self):
        items = DBBase.select_from_table(self, "objecttype from " + self.__tablename)
        tmp = [u', '.join(map(str, item)) for item in items]
        items = sorted(tmp, key=unicode.lower)
        return items

# End of class ObjectTypesDB

#TODO: Add classdocumentation
class NationalityDB():
    def __init__(self):
        self.__nationalityList = ["Svensk","Rysk","Finsk","Engelsk"]
        
    def RetriveNationalities(self):
        return self.__nationalityList

# End of class NationalityDB

#TODO: Add classdocumentation
class AvailabilityDB():
    def __init__(self):
        self._availabilityList = ["","Till salu", "Uthyres"]

    def RetriveAvailability(self):
        return self._availabilityList
    
# End of class AvailabilityDB

#TODO: Add classdocumentation
class StorageDB(DBBase):
    __tableName = ""
    def __init__(self):
        DBBase.__init__(self)
        self.__tableName = "storage"
#        DBBase.CreateTable(self, self.__tablename + "()")

    def CreateTable(self):
        DBBase.CreateTable(self, self.__tableName + "(location text not null, room text not null)")

    def AddStorage(self, data):
        sql = self.__tableName + " values (?,?)"
        try:
            DBBase.insert_into_table(self, sql, data)
        except sqlite3.Error, error:
            print error

    def RetriveStorageList(self):
        list = self.RetriveAllStorage()
        tmp = [u', '.join(map(str, item)) for item in list]
        return tmp

    def RetriveAllStorage(self):
        list = DBBase.select_from_table(self, "location, room from " + self.__tableName)
        return list

