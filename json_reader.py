import json
from discord import Embed
import io

def roles_embed():
    # f = open('./resources/roles.json','r')
    with io.open('./resources/roles.json', encoding='utf-8', mode='r') as f:
        data = json.load(f)
        return Embed().from_dict(data)

roles_embed()