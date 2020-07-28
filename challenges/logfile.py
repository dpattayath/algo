logs = [
    ["z1d", "zsd", "asas", "dfdf"],
    ["x89s", "fsd", "hjkl", "sase"],
    ["y1c", "23", "45", "102"],
    ["x1ppl", "hui", "asas", "dfdf"],
    ["b2c4", "42", "89", "19"],
    ["v1ppl", "hui", "asas", "dfdf"],
    ["21dv", "asd", "asas", "dfdf"],
]


mapper_combined = {}
mapper_original = {}
numeric = []
for log in logs:
    content = ''.join(log[1:])
    if content.isdigit():
        numeric.append(log)
    else:
        mapper_original[log[0]] = log[:]
        mapper_combined[log[0]] = content

mapper_sorted = sorted(mapper_combined.items(), key=lambda x: (x[1], x[0]))
result = []
for key, value in mapper_sorted:
    result.append(mapper_original[key])
result.extend(numeric)
print(result)
