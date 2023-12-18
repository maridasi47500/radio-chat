from user import User
class Directory():
    session=False
    pic=False
    redirect=False
    js=False
    json=False
    css=False
    def __init__(self, title):
        self.title=title
        self.session={"email":None,"name":None,"notice":None}
        self.path="./"
        self.dbUser=User()
        self.html=""
        self.url=""
        self.mesparams=["jeu_id","song_id","user_id","email","name","notice"]
        self.redirect=False
    def logout(self):
        for x in self.mesparams:
            try:
                self.session[x]=""
            except:
                print("erreur session logout ",x)
                #self.session[x]=""
        self.session["mysession"]=True
    def not_notice(self):
        self.session["notice"]=""
    def set_session_param(self,param):
        try:
            self.session[param]=""
        except:
            None
    def get_session_param(self,param):
        try:
            x=self.session[param]
        except:
            x=None
        return x
    def set_session_param_null(self,param):
        try:
            self.session[param]=None
        except:
            print("set session param null")
    def get_session_param_null(self,param):
        try:
            x=self.session[param]
        except:
            x=None
        return x
    def get_session(self):
        return self.session
    def set_other_session(self,s):
        for x in self.mesparams:
            try:
                self.session[x]=s[x]
            except:
                print("erreur session 2",x)
                self.session[x]=""
        self.session["mysession"]=False
    def set_my_session(self,s):
        for x in self.mesparams:
            try:
                self.session[x]=s[x]
            except:
                print("erreur session 1",x)
                #self.session[x]=""
        self.session["mysession"]=False
    def set_some_session_params(self,s):
        for x in s:
            try:
                self.session[x]=s[x]
            except:
                print("erreur session 3",x)
                #self.session[x]=""
        self.session["mysession"]=False
    def set_session_params(self,s):
        for x in s:
            try:
                self.session[x]=s[x]
            except:
                print("erreur session 4",x)
                #self.session[x]=""
        self.session["mysession"]=True
    def set_session(self,s):
        for x in self.mesparams:
            try:
                self.session[x]=s[x]
            except:
                print("erreur session 5 ",x)
                #self.session[x]=""
        self.session["mysession"]=True
    def get_url(self):
        return self.url
    def set_url(self,url):
        self.url=url
    def get_css(self):
        return self.css
    def set_css(self,html):
        self.css=html
    def get_json(self):
        return self.json
    def set_json(self,html):
        self.json=html
    def get_js(self):
        return self.js
    def set_js(self,html):
        self.js=html
    def get_pic(self):
        return self.pic
    def set_pic(self,html):
        self.pic=html
    def get_html(self):
        return self.html
    def set_html(self,html):
        self.html=html
    def set_redirect(self,red):
        self.redirect=red
        self.html="Moved permanently to <a href=\"{url}\">{url}</a>".format(url=red)
    def get_redirect(self):
        return self.redirect
    def set_path(self,path):
        self.path=path
    def get_title(self):
        return self.title
    def get_path(self):
        return self.path
    def gagnant(self):
        user_id=""
        jeu_id=""
        song_id=""
        try:
            user_id=int(self.session["user_id"])
        except:
            print("hey")
            user_id=None
        try:
            jeu_id=int(self.get_session_param_null("jeu_id"))
        except:
            jeu_id=None
        try:
            song_id=int(self.get_session_param_null("song_id"))
        except:
            song_id=None
        print("/////////////////////////////////////////////////")
        print("/////////////////GAGNANT/////////////////////////")
        print("/////////////////////////////////////////////////")
        print(user_id,song_id,jeu_id)
        if user_id and song_id and jeu_id:

            self.dbUser.userwin(user_id,song_id,jeu_id)
            self.set_session_param_null("song_id")
            self.set_session_param_null("jeu_id")

    def redirect_if_not_logged_in(self):
        mysession=self.get_session()
        print("url : : ",self.url)
        print("session : : ",mysession)
        if not mysession["mysession"]:
            self.session["notice"]=""
        if (not mysession or (not mysession["email"] and not mysession["name"])) and self.url != "/" and not self.redirect and self.url != "/signin" and self.url != "/jouerjeux" and self.url != "/joueraujeu":
            print("ok not loged in")
            redi="/signin"
            self.redirect=redi
            self.html="Moved permanently to <a href=\"{url}\">{url}</a>".format(url=redi)
            self.session["notice"]="vous n'êtes pas connecté"
        if self.url == "/joueraujeu":
            try:
                print(int(self.session["user_id"]))
            except:
                self.session["notice"]="connecte-toi pour jouer au jeu"
