from flask import render_template
from flask import Blueprint
from utils import ArchivesScraper

bp = Blueprint('encounters', __name__, url_prefix='/encounterbuilder')

@bp.route("/")
def Home():
    return 'I should put something here :)'

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