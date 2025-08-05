# Realism Assessment pomocou AI

## Technická uskutočniteľnosť

Pri použití obyčajného Windows PC s vstavaným Bluetooth modulom dokážete zachytiť časť aktivít zákazníkov vo vašom priestore. Z hľadiska prototypu je to realistické riešenie:

- Moduly BLE dokážu detegovať reklamuční pakety zo smartfónov či nositeľných zariadení.
- Freemium prístup (zadarmo základné štatistiky, platené doplňujúce analýzy) je osvedčený model v retail intelligence (napríklad Heatmapy od RetailNext).  

Avšak presnosť a pokrytie budú obmedzené technológiou Bluetooth, náhodnou zmenou MAC adresy či vypnutým rádiom v zariadení.

## Odhad presnosti detekcie

| Typ zariadenia            | Očakávaná detekcia | Kľúčový faktor                  |
|---------------------------|--------------------|---------------------------------|
| iOS (MAC randomizácia)    | ~20 %              | časté prehadzovanie adresy      |
| Android (verzia < 8.0)    | ~50 %              | závisí od používateľských nastavení |
| Android (verzia ≥ 8.0)    | ~35 %              | nové bezpečnostné politiky      |
| Wearables (napr. hodinky) | ~15 %              | krátke vysielacie intervaly     |

---

# Kritické myslenie vašich výstupov

## Silné stránky

- Dôsledný zoznam biznis otázok, ktoré pokrývajú potreby majiteľa obchodu aj prevádzkovateľa nákupného centra.
- Freemium model znižuje počiatočnú bariéru vstupu pre zákazníka.
- Jasne vymedzené fázy testovania a overenia validity dát manuálnym počítaním.

## Slabé miesta

- Chýba konkurenčná analýza (napr. cenové porovnanie s podobnými riešeniami).
- Neuvažujete redundantné senzory (napríklad Wi-Fi sniffing) pre zvýšenie pokrytia.
- GDPR sekcia potrebuje podrobnejší plán anonymizácie a spracovania súhlasov.

## Príležitosti a hrozby

- Príležitosť: rozšíriť riešenie o štandardizované API pre integráciu s ERP alebo CRM systémami.
- Hrozba: zákazníci môžu odmietať inštaláciu ďalšieho softvéru na svojich počítačoch (IT oddelenie, antivírus).

---

# Odporúčania a ďalšie kroky

## Pokračovať v prototypovaní?

Áno. Iteratívny MVP zameraný na:

1. Rýchly field test v malej kamennej predajni.
2. Manuálne porovnanie výsledkov s terénnym zberom (gold-standard).
3. Upravovanie up-sampling algoritmu a korelačných modelov.
4. Zber spätnej väzby od zákazníkov (prevádzkovateľov, IT správcov).

## Čo ešte zvážiť

- Pripraviť jednoduché API, aby zákazník mohol výsledky vizualizovať vo vlastnom BI nástroji.
- Pridať modul pre správu GDPR súhlasov a anonymizáciu už pri edge-computingu.
- Rozvinúť roadmapu s milníkmi: alfa-test, beta-test, pilotný projekt, komerčná verzia.

---

# Čo by vás mohlo zaujímať ďalej

- Metódy vyváženia počtu zaznamenaných a predpokladaných návštev cez strojové učenie.
- Návrh architektúry microservices pre škálovateľnosť riešenia.
- Spôsoby monetizácie nad rámec freemium: pay-per-use, revenue share s obchodnými centrami.
