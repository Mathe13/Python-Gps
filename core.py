"""Classes do projeto gps."""
import requests
import json
from unidecode import unidecode as unidecode

# import pprint
# import string


class Gps():
    """classe com as funçoes principais."""

    def __init__(self, user_key):
        """Inicia a classe com a chave do usuario."""
        self.key = user_key

    @staticmethod
    def normal(palavra):
        """Normaliza o texto."""
        return unidecode(palavra)

    def get_json(self, origin, destination):
        """Pega o json com os dados."""
        origin = self.normal(origin)
        destination = self.normal(destination)
        url = ('https://maps.googleapis.com/maps/api/directions/json?origin=' +
               origin + '&destination=' + destination + '&key=' + self.key)

        raw_json = requests.get(url)
        if raw_json:
            self.decode_json(raw_json.content)
            return True
        else:
            return False

    def decode_json(self, raw_json):
        """Decodifica o json."""
        data = json.loads(raw_json)
        self.caminhos = []
        for rota in data['routes']:
            caminho = Caminho(rota)
            self.caminhos.append(caminho)


class Caminho():
    """classe com dados e metodos referentes ao caminho."""

    def __init__(self, rota):
        """Inicializador da classe."""
        self.passos = []
        for step in rota['legs'][0]['steps']:
            passo = Passo(step)
            self.passos.append(passo)


class Passo():
    """classe com dados e metodos referentes ao passo."""

    def __init__(self, step):
        """Inicializador da classe."""
        self.distance = step['distance']['text']
        self.duration = step['duration']['text']
        self.instruction = self.remove_b_tag(str(step['html_instructions']))

    @staticmethod
    def remove_b_tag(html_instructions):
        """Remove as tags."""
        instruction = html_instructions.replace('<b>', '')
        instruction = instruction.replace('</b>', '')
        return (instruction)
