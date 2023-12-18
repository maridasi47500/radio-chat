import sqlite3
import sys
import re
from model import Model
from gagnant import Gagnant
class User(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.dbGagnant=Gagnant()
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists users(
        id integer primary key autoincrement,
        mypic string,
        metier string,
        nomcomplet string,
        gender string,
        businessaddress string,
        postaladdress string,
        email string,
        profile text,
        zipcode string,
        otheremail string,
        password string not null
                );""")
        self.con.commit()
        #self.con.close()
    def userwin(self,user_id,song_id,jeu_id):
        print("hey")
        self.cur.execute("select  (select hellouser.nomcomplet from users hellouser where hellouser.id = ?) as userfullname,(select heyuser.id from users heyuser where heyuser.id = ?) as user_id,(select myuser.mypic from users myuser where myuser.id = ?) as picuser, (SELECT cado.id FROM cado ORDER BY RANDOM() LIMIT 1) as cadeauid, jeu.id, song.id as song_id from jeu left join lyric on lyric.id = jeu.lyric_id left join song on lyric.song_id = song.id where jeu.id = ? and song.id = ?",(user_id,user_id,user_id,jeu_id, song_id))
        row=(self.cur.fetchone())
        row=dict(row)
        hey=self.cur.execute("select pic,name from cado where id = ? ",(row["cadeauid"],))
        hi=self.cur.fetchone()
        row["piccadeau"]=hi["pic"]
        row["nomcadeau"]=hi["name"]
        row["song_id"]=song_id
        row["jeu_id"]=jeu_id

        if row is not None:
            self.dbGagnant.create(row)
        return row


    def getbyemailpw(self,email,pw):
        print("PARAMS email, pw")
        print(email, pw)
        self.cur.execute("select * from users where otheremail = ? and password = ?",(email,pw,))

        
        row=self.cur.fetchone()
        print(dict(row))
        print(row)
        if row:
            return {"user_id":row["id"],"notice":"vous êtes connecté","name": row["nomcomplet"],"email": row["otheremail"]}
        else:
            return {"notice":"","name":"","email": ""}
    def getall(self):
        self.cur.execute("select * from users")
        
        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):
        self.cur.execute("delete from users where id = ?",(myid,))
        

        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select * from users where id = ?",(myid,))
        
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
            if 'envoyer' in x:
                continue
            if '[' not in x and x not in ['routeparams']:
                #print("my params",x,params[x])
                try:
                  myhash[x]=str(params[x].decode())
                except:
                  myhash[x]=str(params[x])
        print("M Y H A S H")
        print(myhash,myhash.keys())
        try:
          self.cur.execute("insert into users (postaladdress,metier,mypic,nomcomplet,gender, businessaddress, email, profile, zipcode, otheremail, password) values (:postaladdress,:metier,:mypic,:nomcomplet,:gender, :businessaddress, :email, :profile, :zipcode, :otheremail, :password)",myhash)
          self.con.commit()
        except Exception as e:
          print("my error"+str(e))
        
        self.cur.execute("select id,otheremail,nomcomplet from users where password = ? and otheremail = ?", (myhash["password"], myhash["otheremail"]))
        row=self.cur.fetchone()
        
        myid=row["id"]

        return {"user_id":myid,"notice": "vous avez été inscrit(e)","email": row["otheremail"],"name":row["nomcomplet"]}


    def update(self,params):
        #self.con=sqlite3.connect(self.mydb)
        print("ok")
        myhash={}
        for x in params:
            if 'envoyer' in x:
                continue
            if 'confirmation' in x:
                continue
            if '[' not in x and x not in ['routeparams']:
                print(x)

                print(params[x])
                myhash[x]=params[x][0]
        try:
          self.cur.execute("update users set postaladdress = :postaladdress,mypic = :mypic,nomcomplet = :nomcomplet,gender = :gender, businessaddress = :businessaddress, email = :email, profile = :profile, zipcode = :zipcode, otheremail = :otheremail, password = :password where id = :id",myhash)
          self.con.commit()
        except Exception as e:
          print("my error update"+str(e))
        myid=myhash["id"]
        #print(arr, "my array")
        self.cur.execute("select id,otheremail,nomcomplet from users where id = ?", (myid,))
        row=self.cur.fetchone()
        return {"notice": "vos infos ont été modifiées","email": row["otheremail"],"name":row["nomcomplet"]}
