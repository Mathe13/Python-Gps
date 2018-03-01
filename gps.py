"""Tentativa de criar um gps."""
from core import Gps
key = key = ''

if __name__ == '__main__':
    gps = Gps(key)
    # teste q printa a distancia de cada um dos passos
    gps.get_json('guaiba cenair maica 110', 'guaiba honorio lemos 181')
    for caminho in gps.caminhos:
        for passo in caminho.passos:
            print('daqui à:' + passo.distance + " " + passo.instruction)
    # teste = 'Head <b>north</b> on <b>R. Cenair Maicá</b> toward <b>R. Pedro Raymundo</b>'
    # teste = teste.replace('<b>', '')
    # teste = teste.replace('</b>', '')
    # print(teste)
