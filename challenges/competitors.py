
competitors = ["google", "microsoft", "digitalocean", "dreamhost", "heroku"]

reviews = [
    "Eu digitalocean et google culpa. Cupidatat in qui Lorem ex google quis irure proident",
    "deserunt ut irure digitalocean ea. Laborum adipisicing google duis sunt sunt",
    "enim est exercitation magna quis aute eiusmod nisi veniam. Mollit cillum eu ut dreamhost",
    "mollit est culpa non. digitalocean microsoft Lorem nulla id laborum voluptate mollit sunt",
    "enim culpa google consectetur. Anim Lorem velit culpa ipsum digitalocean ipsum in. Do dolore occaecat ea heroku.",
    "Pariatur ad occaecat microsoft non. Ut ipsum anim ea irure incididunt aliquip veniam sit id incididunt.",
    "Est pariatur ad incididunt heroku consequat irure google do digitalocean. Exercitation pariatur ea minim ut",
    "ad qui magna occaecat fugiat cupidatat eu sint officia. Non in laboris consequat fugiat heroku nisi culpa",
    "dreamhost qui enim aliqua aute. Consequat consequat microsoft anim excepteur dolor ipsum nulla nisi dolore sunt sunt.",
]

s_competitors = set(competitors)

matches = []
for review in reviews:
    words = review.split(" ")
    s_review = set(words)
    matches.extend(s_review & s_competitors)

mapper = {}
for match in matches:
    mapper[match] = mapper.get(match, 0) + 1

topCompetitors = sorted(mapper.items(), key=lambda x: (-x[1], x[0]))
print(topCompetitors)


