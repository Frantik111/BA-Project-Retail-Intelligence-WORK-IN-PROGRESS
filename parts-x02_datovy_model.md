# 🧮 Model zberaných dát

## 📦 Zberané atribúty
| Atribút | Popis |
|--------|--------|
| `MAC` | Anonymizovaná MAC adresa |
| `RSSI` | Sila signálu zariadenia |
| `timestamp` | Čas detekcie zariadenia |
| `device_name` | Názov zariadenia, ak je dostupný |

## 📌 Poznámky
- Anonymizácia sa robí hashovaním MAC adresy
- RSSI slúži na odhad vzdialenosti (zóna)
