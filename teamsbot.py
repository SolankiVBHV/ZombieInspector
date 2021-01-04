from webexteamssdk import WebexTeamsAPI

class WebExActions():
    access_token = 'YOUR BOT ACCESS TOKEN'
    roomId = 'DESTINATION ROOM ID FOR BOT'
    teams_api = WebexTeamsAPI(access_token=access_token)
    
    def send_no_zombie_message(self):
        message = "No Zombies detected on any cluster 🙏☮🕊"
        self.teams_api.messages.create(roomId=self.roomId, text=message)
        
    def send_zombie_message(self, cluster_list):
        message = "Zombies detected for following cluster: **" + str(cluster_list) + "**. Details are documented [here](https://app.smartsheet.com/sheets/JfGFwhqf6v6mGJJVVMF5hxhjpX52X2pW76x9Qwh1)" 
        file_path = "https://media.giphy.com/media/Wt1aWlM4FfBhU1w6ev/giphy.gif"
        self.teams_api.messages.create(roomId=self.roomId, markdown=message,files=[file_path])
