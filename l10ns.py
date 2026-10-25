import json
import numpy as np

fr_fr = json.load(open("fr_fr.json"))
en_us = json.load(open("en_us.json"))
new_l10n = en_us | fr_fr
for k in new_l10n.copy():
    if k not in en_us:
        new_l10n.pop(k)

print(json.dumps(new_l10n, indent=4))
print(len(new_l10n))
print(len(en_us))
json.dump(new_l10n, open("new_fr_fr.json", 'w'), indent=4, ensure_ascii=False)
