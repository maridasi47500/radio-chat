# coding=utf-8
import sqlite3
import sys
import re
from model import Model
import random
from fichier import Fichier
from lyric import Lyric
from artist import Artist
class Song(Model):
    def __init__(self):
        self.dbLyric=Lyric()
        self.dbArtist=Artist()
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists song(
        id integer primary key autoincrement,
        artist_id text,
            title text,
            file text
                    );""")
        self.con.commit()
        #self.con.close()
    def getthree(self,myid):
        self.cur.execute("select * from song where id = ? limit 1",(myid,))
        self.con.commit()
        row1=self.cur.fetchone()

        self.cur.execute("select * from song where id <> ? order by RANDOM() limit 1",(myid,))
        self.con.commit()
        row2=self.cur.fetchone()

        self.cur.execute("select * from song where id <> ? and id <> ? order by RANDOM() limit 1",(myid,row2["id"]))
        self.con.commit()
        row3=self.cur.fetchone()
        rows=[row1,row2,row3]
        print("rows : ",rows)
        print("rows with my id: ",myid)
        random.shuffle(rows)
        return rows
    def getall(self):
        self.cur.execute("select * from song")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from song where id = ?",(int(myid),))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyartistid(self,myid):
        self.cur.execute("select * from song where artist_id = ?",(myid,))
        row=self.cur.fetchall()
        return row
    def getbyid(self,myid):
        self.cur.execute("select * from song where id = ?",(myid,))
        row=dict(self.cur.fetchone())
        print(row["id"], "row id")
        job=self.cur.fetchall()
        return row
    def create(self,params):
        print("ok")
        myhash={}
        for x in params:
            if 'confirmation' in x:
                continue
            if 'lyric' in x:
                continue
            if 'artist' in x:
                continue
            if 'envoyer' in x:
                continue
            if '[' not in x and x not in ['routeparams']:
                #print("my params",x,params[x])
                try:
                  myhash[x]=str(params[x].decode())
                except:
                  myhash[x]=str(params[x])
        print("M Y H A S H SONG")
        print("artist")
        print(myhash,myhash.keys())
        print("artist")
        myid=None
        try:
          print("artist song:")
          artistid=self.dbArtist.findorcreate({"name":params["artist"]})
          print("artist")
          myhash["artist_id"] = artistid
          print("artistid",artistid)
          self.cur.execute("insert into song (artist_id,title,file) values (:artist_id,:title,:file)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
          print('fichier de paroles',params['lyric'])
          for ligne in Fichier("./uploads",params["lyric"]).ligneparligne():
            print(ligne)
            if len(ligne.rstrip()) > 0:
              self.dbLyric.create({"song_id":myid,"text":ligne.replace('"',"\"")})


        except Exception as e:
          print("my error SONG"+str(e))
        azerty={}
        azerty["song_id"]=myid
        azerty["notice"]="votre song a été ajouté"
        return azerty




