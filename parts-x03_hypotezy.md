# 🧪 Hypotézy a klasifikačné pravidlá

## 🧠 Predpoklady
- Silný signál + dlhý čas = Zákazník
- Krátky čas + slabý signál = Okoloidúci
- Rovnaký device počas viacerých dní = Opakovaný návštevník

## 🧬 Klasifikácia správania
| Typ | Kritériá |
|-----|----------|
| Prechádzajúci | Detekcia < 1 min, slabý RSSI |
| Zdržanlivý | Detekcia > 3 min, stabilný signál |
| Opakovaný | Device sa objaví aspoň 2× v rôzne dni |
