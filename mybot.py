# Import necessary library.
import socket 

# Some basic variables used to configure the bot        
server = "irc.freenode.net" # Server
channel = "#michaelnavarro" # Channel
botnick = "FOULMOUTH_COP" # Your bots nick

#array containing big list of bad words
badwords = ["ahole", "anus", "ash0le", "ash0les", "asholes", "ass", "Ass Monkey", 
            "Assface", "assh0le", "assh0lez", "asshole", "assholes", "assholz", 
            "asswipe", "azzhole", "bassterds", "crap", "bastard", "bastards", "bastardz", 
            "basterds", "basterdz", "Biatch", "bitch", "bitches", "Blow Job", 
            "boffing", "butthole", "buttwipe", "c0ck", "c0cks", "c0k", 
            "Carpet Muncher", "cawk", "cawks", "Clit", "cnts", "cntz", 
            "cock", "cockhead", "cock-head", "cocks", "CockSucker", "cock-sucker", 
            "crap", "cum", "cunt", "cunts", "cuntz", "dick", "dild0", "dild0s", 
            "dildo", "dildos", "dilld0", "dilld0s", "dominatricks", "dominatrics", 
            "dominatrix", "dyke", "enema", "f u c k", "f u c k e r", "fag", "fag1t", 
            "faget", "fagg1t", "faggit", "faggot", "fagit", "fags", "fagz", "faig", 
            "faigs", "fart", "flipping the bird", "fuck", "fucker", "fuckin", "fucking", 
            "fucks", "Fudge Packer", "fuk", "Fukah", "Fuken", "fuker", "Fukin", "Fukk", 
            "Fukkah", "Fukken", "Fukker", "Fukkin", "g00k", "gay", "gayboy", "gaygirl", 
            "gays", "gayz", "God-damned", "h00r", "h0ar", "h0re", "hells", "hoar", "hoor", 
            "hoore", "jackoff", "jap", "japs", "jerk-off", "jisim", "jiss", "jizm", "jizz", 
            "knob", "knobs", "knobz", "kunt", "kunts", "kuntz", "Lesbian", "Lezzian", 
            "Lipshits", "Lipshitz", "masochist", "masokist", "massterbait", "masstrbait", 
            "masstrbate", "masterbaiter", "masterbate", "masterbates", "Motha Fucker", 
            "Motha Fuker", "Motha Fukkah", "Motha Fukker", "Mother Fucker", "Mother Fukah", 
            "Mother Fuker", "Mother Fukkah", "Mother Fukker", "mother-fucker", "Mutha Fucker", 
            "Mutha Fukah", "Mutha Fuker", "Mutha Fukkah", "Mutha Fukker", "n1gr", "nastt", 
            "nigger", "nigur", "niiger", "niigr", "orafis", "orgasim", "orgasm", "orgasum", 
            "oriface", "orifice", "orifiss", "packi", "packie", "packy", "paki", "pakie", "paky", 
            "pecker", "peeenus", "peeenusss", "peenus", "peinus", "pen1s", "penas", "penis", 
            "penis-breath", "penus", "penuus", "Phuc", "Phuck", "Phuk", "Phuker", "Phukker", 
            "polac", "polack", "polak", "Poonani", "pr1c", "pr1ck", "pr1k", "pusse", "pussee", 
            "pussy", "puuke", "puuker", "queer", "queers", "queerz", "qweers", "qweerz", "qweir", 
            "recktum", "rectum", "retard", "sadist", "scank", "schlong", "screwing", "semen", 
            "sex", "sexy", "Sh!t", "sh1t", "sh1ter", "sh1ts", "sh1tter", "sh1tz", "shit", "shits", 
            "shitter", "Shitty", "Shity", "shitz", "Shyt", "Shyte", "Shytty", "Shyty", "skanck", 
            "skank", "skankee", "skankey", "skanks", "Skanky", "slut", "sluts", "Slutty", "slutz", 
            "son-of-a-bitch", "tit", "turd", "va1jina", "vag1na", "vagiina", "vagina", "vaj1na", 
            "vajina", "vullva", "vulva", "w0p", "wh00r", "wh0re", "whore", "xrated", "xxx", "b!+ch", 
            "bitch", "blowjob", "clit", "arschloch", "fuck", "shit", "ass", "asshole", "b!tch", 
            "b17ch", "b1tch", "bastard", "bi+ch", "boiolas", "buceta", "c0ck", "cawk", "chink", 
            "cipa", "clits", "cock", "cum", "cunt", "dildo", "dirsa", "ejakulate", "fatass", 
            "fcuk", "fuk", "fux0r", "hoer", "hore", "jism", "kawk", "l3itch", "l3i+ch", "lesbian", 
            "masturbate", "masterbat", "masterbat3", "motherfucker", "s.o.b.", "mofo", "nazi", 
            "nigga", "nigger", "nutsack", "phuck", "pimpis", "pusse", "pussy", "scrotum", "sh!t", 
            "shemale", "shi+", "sh!+", "slut", "smut", "teets", "tits", "boobs", "b00bs", "teez", 
            "testical", "testicle", "titt", "w00se", "jackoff", "wank", "whoar", "whore", "damn", 
            "dyke", "fuck", "shit", "@$$", "amcik", "andskota", "arse", "assrammer", "ayir", "bi7ch", 
            "bitch", "bollock", "breasts", "butt-pirate", "cabron", "cazzo", "chraa", "chuj", "Cock", 
            "cunt", "d4mn", "daygo", "dego", "dick", "dike", "dupa", "dziwka", "ejackulate", "Ekrem", 
            "Ekto", "enculer", "faen", "fag", "fanculo", "fanny", "feces", "feg", "Felcher", "ficken", 
            "fitt", "Flikker", "foreskin", "Fotze", "Fu(", "fuk", "futkretzn", "gay", "gook", "guiena", 
              "h0r", "h4x0r", "hell", "helvete", "hoer", "honkey", "Huevon", "hui", "injun", "jizz", 
              "kanker", "kike", "klootzak", "kraut", "knulle", "kuk", "kuksuger", "Kurac", "kurwa", 
              "kusi", "kyrpa", "lesbo", "mamhoon", "masturbat", "merd", "mibun", "monkleigh", 
              "mouliewop", "muie", "mulkku", "muschi", "nazis", "nepesaurio", "nigger", "orospu", 
              "paska", "perse", "picka", "pierdol", "pillu", "pimmel", "piss", "pizda", "poontsee", 
              "poop", "porn", "p0rn", "pr0n", "preteen", "pula", "pule", "puta", "puto", "qahbeh", 
              "queef", "rautenberg", "schaffer", "scheiss", "schlampe", "schmuck", "screw", "sh!t", 
              "sharmuta", "sharmute", "shipal", "shiz", "skribz", "skurwysyn", "sphencter", "spic", 
              "spierdalaj", "splooge", "suka", "b00b", "testicle", "titt", "twat", "vittu", "wank", 
              "wetback", "wichser", "wop", "yed", "zabourah"]


def ping(): # This is our first function! It will respond to server Pings.
  ircsock.send("PONG :pingis\n")  

def sendmsg(chan , msg): # This is the send message function, it simply sends messages to the channel.
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n") 

def joinchan(chan): # This function is used to join channels.
  ircsock.send("JOIN "+ chan +"\n")

def hello(): # This function responds to a user that says a bad word
  ircsock.send("PRIVMSG "+ channel +" :FOULMOUTH_COP DOES NOT LIKE\n")
  ircsock.send("PRIVMSG "+ channel +" :YOU WILL BE BOOTED IN:\n")
  ircsock.send("PRIVMSG "+ channel +" :3...\n")
  ircsock.send("PRIVMSG "+ channel +" :2...\n")
  ircsock.send("PRIVMSG "+ channel +" :1...\n")
  ircsock.send("PRIVMSG "+ channel +" :jk \':)\n")

def talkingtome(): # This function responds to a user that inputs "Hello Mybot"
  ircsock.send("PRIVMSG "+ channel +" :You talking to me?\n")
                  
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667)) # Here we connect to the server using the port 6667
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :Watch your filthy mouth around me >:0\n") # user authentication
ircsock.send("NICK "+ botnick +"\n") # here we actually assign the nick to the bot

joinchan(channel) # Join the channel using the functions we previously defined

while 1:
  ircmsg = ircsock.recv(2048) # receive data from the server
  ircmsg = ircmsg.strip('\n\r') # removing any unnecessary linebreaks.
  # print(ircmsg) # Here we print what's coming from the server

  ircmsg_words = ircmsg.split()
  ircmsg_words =[word.lower().replace(":", "") for word in ircmsg_words]

  for x in badwords:
    if x in ircmsg_words:
      hello()
      break


  
  # if botnick in badwords != -1: # If we can find "Hello Mybot" it will call the function hello()
  # hello()

    

  if ircmsg.find("PING :") != -1: # if the server pings us then we've got to respond!
    ping()