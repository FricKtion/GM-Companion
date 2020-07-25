from flask import Flask, render_template
from ArchivesScraper import ArchivesScraper

app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/Monsters")
def Monsters():
    scraper = ArchivesScraper()
    monsters = scraper.MonsterList()
    
    result = ""
    for monster in sorted(monsters, key=monsters.get):
       result += monster + ": " + str(monsters[monster])
       result += "<br />"

    return result

@app.route("/NPCs")
def NPCs():
    scraper = ArchivesScraper()
    npcs = scraper.NpcList()
    
    result = ""
    for npc in sorted(npcs, key=npcs.get):
        result += npc + ": " + str(npcs[npc])
        result += "<br />"

    return result

@app.route("/Contact")
def Contact():
    return "IN PROGRESS"

if __name__ == "__main__":
    app.run()