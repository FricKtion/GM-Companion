import requests
from requests import get
from bs4 import BeautifulSoup

class ArchivesScraper:
    def __init__(self):
        self._baseUrl = "https://2e.aonprd.com"
        self._monsterUrl = "/Monsters.aspx?Letter=All"
        self._npcUrl = "/NPCs.aspx?Letter=All"

    def __CreatureRequest(self, url):
        try:
            results = requests.get(url)
        except requests.exceptions.Timeout:
            print("The Archives took too long to repond...")
        except requests.exceptions.TooManyRedirects:
            print("The Archives redirected your request too many times...")
        except requests.exceptions.RequestException as e:
            print(e)

        soup = BeautifulSoup(results.text, "html.parser")

        rows = soup.find_all("tr")
        creatureData = {}

        #iterate through the table rows, skipping the header row
        for row in rows[1:]:
            data = row.find_all("td")
            creatureData[data[0].text] = int(data[2].text)

        return creatureData

    def MonsterList(self):
        monsters = self.__CreatureRequest(self._baseUrl + self._monsterUrl)
        
        return monsters
    
    def NpcList(self):
        npcs = self.__CreatureRequest(self._baseUrl + self._npcUrl)
        
        return npcs