import os

class Config:
    API_ID = os.environ.get("API_ID", "28716246")
    API_HASH = os.environ.get("API_HASH", "d9277abd08e0277e0a899415916e39b3")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7753365207:AAHPNFwN18Egebu98BoZqVM2CnMQz7USTlY") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "forward-bot") 
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://venomv1011:venomv1011@cluster0.qecf2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DB_NAME = os.environ.get("DB_NAME", "Cluster0")
    OWNER_ID = [int(id) for id in os.environ.get("OWNER_ID", '1883889098').split()]


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    







    
    
    
    
    
    # Jishu Developer 
