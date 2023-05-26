import pytube

print("""    ____       _           
   / __ \_____(_)___  / /_  __
  / / / / ___/ / __ \/ / / / /
 / /_/ / /  / / /_/ / / /_/ / 
/_____/_/  /_/ .___/_/\__, /  
            /_/      /____/  
      """)
print("               [+] subscribe in my channel:https://www.youtube.com/channel/UCT0aFs8auzYbAic2hE7Bglw")
print("               [+] follow me in instagram: https://www.instagram.com/urfav.eyvd/")
print("               [+] follow me on facebookl: https://www.facebook.com/profile.php?id=100012755019109")
print("__________________________Thanks for using my tool_______________________________")
kind = input('Do you want to Download \n [1] Video \n [2] Playlist \n')
url = input("plz enter the url: \n")
pytube.YouTube(url).streams.get_highest_resolution().download('Desktop')
print("Downloading is Done Iam happy to use my tool")
