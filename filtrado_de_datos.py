from concurrent.futures.thread import _worker
from unicodedata import name


DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def main():
    name_lengu = [worker["name"] for worker in DATA if worker["language"] == "python"]
    list_platzi = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    
    name_lengu = list(filter(lambda worker: worker["language"] == "python" ,DATA))
    name_lengu = list(map(lambda worker: worker["name"]  , name_lengu))

    list_platzi = list(filter(lambda worker: worker["organization"] == "Platzi" ,DATA))
    list_platzi = list(map(lambda worker: worker["name"] ,list_platzi))
    
    adults = [worker["name"] for worker in DATA if worker["age"] > 18]
    old_people = [{**worker, **{"olds": worker["age"] > 70}} for worker in DATA]
    print(old_people)



if __name__ == '__main__':
    main()