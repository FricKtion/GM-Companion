from flask import render_template
from flask import Blueprint
from utils import ArchivesScraper

bp = Blueprint('encounters', __name__, url_prefix='/encounterbuilder')

# TODO move this into a different Blueprint
# @bp.route("/")
# def Home():
#     return render_template("index.html")

@bp.route("/monsters")
def Monsters():
    scraper = ArchivesScraper()
    monsters = scraper.MonsterList()
    
    result = ""
    for monster in sorted(monsters, key=monsters.get):
       result += monster + ": " + str(monsters[monster])
       result += "<br />"

    return result

@bp.route("/npcs")
def NPCs():
    scraper = ArchivesScraper()
    npcs = scraper.NpcList()
    
    result = ""
    for npc in sorted(npcs, key=npcs.get):
        result += npc + ": " + str(npcs[npc])
        result += "<br />"

    return result

# TODO is this needed in the init file?
# if __name__ == "__main__":
#     app.run()