import politicians.politician as p
import politicians.characters.variables as v

pols = v.variable_characters()
pol:p.Politician = pols["Алексей Бабочкин Федорович"]

print(pol.to_str())

for i in range(25):
    for j in range(12):
        pol.new_month()
        print(pol.to_briefly_str())
    pol.new_year()
    print("НОВЫЙ ГОД!")