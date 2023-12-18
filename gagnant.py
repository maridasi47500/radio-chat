# coding=utf-8
import sqlite3
import sys
import re
from model import Model
from chaine import Chaine
from program import Myprogram
class Gagnant(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists gagnant(
        id integer primary key autoincrement,
        user_id text,
        jeu_id text,
            pic text
                    );""")
        self.program=Myprogram()
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select * from gagnant order by id desc")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from gagnant where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select * from gagnant where id = ?",(myid,))
        row=dict(self.cur.fetchone())
        print(row["id"], "row id")
        job=self.cur.fetchall()
        return row
    def create(self,params):
        print("ok")
        myhash={"jeu_id": params["jeu_id"], "user_id": params["user_id"]}
        filename=Chaine().fichier("hey.gif")
        filename2=Chaine().fichier("hey.gif")

        print(filename,"M Y H A S H")
        myhash["pic"]=filename
        tousmesarg=["sh","./cado/gagnantjeu.sh",params["piccadeau"],params["picuser"],filename,params["userfullname"],params["nomcadeau"],filename2]
        print("TOUS mes arg", tousmesarg)
        self.program.myargs(tousmesarg)
        self.program.run()
        try:
          self.cur.execute("insert into gagnant (jeu_id,user_id,pic) values (:jeu_id,:user_id,:pic)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["gagnant_id"]=myid
        azerty["notice"]="votre gagnant a été ajouté"
        return azerty




