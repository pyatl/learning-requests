import requests


class CatFact:
    def __init__(self, id, text):
        self.id = id
        self.text = text

    def to_txt(self):
        return f'{self.id} - {self.text} \n'


api_url = 'https://cat-fact.herokuapp.com'

def get_facts():
    uri = '/facts'
    url = f'{api_url}{uri}'
    return requests.get(url).json().get('all')


facts = get_facts()
cat_facts = []
for fact in facts:
    cat_facts.append(CatFact(fact.get('_id'), fact.get('text')))

with open('cat-facts.txt', 'w') as f:
    for cat_fact in cat_facts:
        f.write(cat_fact.to_txt())


