# 💬 Rozhovor so stakeholderom

## 🎯 Hlavná otázka
 Dokáže jednoduchý Bluetooth sniffer (nie je špecializované zariadenie, ale počítač s windows a zabudovaným bluetooth) poskytnúť užitočné údaje pre analýzu správania zákazníkov?
> Odpoveď stakeholdera:
>
> V BIG PICTURE pohľade chceme dosiahnúť ucelené spektrum RETAIL INTELLIGENCE, pričom sa k cieľu chceme dostať malými krokmi. Radi by sme ponúkali lacné riešenie na monitoring správania sa zákazníkov. Pričom zákazníka chceme získať webovým portálom a aplikáciou bežiacou na počítači s bluetooth a windows. Nemá to byť dokonalé riešenie, ktoré je super presné, avšak za nulové náklady zákazník získa základné údaje o správaní sa zákazníkov. Odvíja sa to od nášho FREEMIUM obchodného modelu, pričom ak by požadoval presnejšie údaje môže si ich objednať na našom webovom portáli.

## 🎯 Biznisové otázky (prečo to robíme?)
- Aký problém sa týmto snažíme riešiť?
> Overujeme koncept či je možné merať návštevnosť zákazníkov len softwarom na počítači s windows a bluetooth. Tak aby sme vedeli ponúknuť nízkonákladové riešenie na monitoring správania sa zákazníkov.
- Pre koho majú byť výstupy určené?
> Podľa etáp projektu, v testovacej fáze pre analýzu údajov či je možné stanoviť s určitou presnosťou návštevnosť a či má zmysel dodať MVP koncovému klientovi.
- Aký konkrétny prínos očakávam ako vlastník predajne?
> Viem približne koľko ľudí mi navštívilo predajňu, nemusím robiť manuálnu evidenciu, viem prideliť podľa návštevnosti množstvo personálu, viem zhodnotiť reklamnú akciu, viem posúdiť či som v porovnaní s predhcádzajúcimi rokmi dosiahol rovnakú návštevnosť.
- Aký konkrétny prínos očakáva prevádzkovateľ nákupného centra?
> Vďaka zapojeniu viacerých predajní: Meranie návštevnosti, zvýšenie bezpečnosti nákupného centra mimo otváracích hodín, nepredvídateľné pohyby zákazníkov, vyhodnotenie sezuóných špičiek a akcií.
- Ako viem, že sa zákazník správal „zaujímavo“?
> Čas strávený na predajni, v prípade viac senzorov (zákazník môže použiť viac počítačov) môžeme vyhodnocovať preferované časti predajne, opakovanie návštev, všetky metódy je nutné časom preskúmať.
- Môže táto metóda nahradiť alebo doplniť iný prieskum?
> Túto metódu zberu musíme overiť maunálnym zberom, prípadne ho môžeme obohatiť o črty zákazníka, prípadne kolerovať s obratom na prevádzke. Mohol by nahradiť manuálne rátanie alebo nákladné technické riešenia konkurencie.
- Prečo to práve teraz potrebujeme?
> Chceme vstúpiť na Retail intelligence, v súčastnosti je trend k nárastu werable zariadení, ideálny čas na experimenty.
- Čo sa zmení, ak to budeme mať?
> Môžeme získať veľké množstvo klientov po celom svete zároveň otestujeme limity technológie, zadefinujeme klúčové benefity pre klienta.
- Kto bude výstupy používať?
> V prvom rade naše technické oddelenie, po analýze a nastavení kriviek uvidí zákazník údaje.
- Ako to pomôže pri rozhodovaní?
> Po prvých testoch zistíme živatoschopnosť riešenia či údaje sú relevantné. Zákazník vie plánovať, kontolovať.
- Čo je hlavná pridaná hodnota?
> Pri prakticky nulových nákladoch môžem nahradiť manuálnu evidenciu či iné komplexné riešenia.
- Aký formát výstupu očakávaš?
> Strojovo čitateľné údaje, pre človeka prehľadný graf návštevnosti na časovej osi.
- Ako často sa budú dáta analyzovať?
> Údaje majú byť získavané nepretržite, analýza v intervaloch, ktoré definujeme pri analýze údajov a tvorbe výstupov pre zákazníka.
- Máš predstavu o ideálnom reporte?
> Graf, porovnanie s predchádzajúcim obdobím, porovnanie v danom segmente na inej lokalite (druhá filiálka, trend v príbuzných segmentoch).
- Ako poznáme, že to funguje?
> Keď dokážeme zachytené údaje spracovať tak aby sme vedeli porovnať s mauálnym rátaním - definovali sme sa či je to v akceptovateľnej odchylke, vedeli identifikovať črty správania.
- Existuje príklad, ktorý ťa inšpiroval?
> Kamerové počítanie zákazníkov
> [dôr](https://www.getdor.com/solutions/people-counting)
- Aké máme obmedzenia (technické, právne, finančné)?
> Technické
>
> Nositelné zariadenia chránia svojho majiteľa rozličnými technikami - zmena mac adresy, maskovanie signálu. Nepresnosť merania kvôli prostrediu, rozličným typom zariadení. Zákazník môže mať viac zariadení, prípadne môžu byť vypnuté tieto zariadenia. Rozličné spracovanie údajov pri rozličných množstvách klientov. Ryziko na sorftwarovej stranke že bude problém s antivírusom - nutné manualne definovať výnimku.
> Ďalej návštevníci sú rozdielny, preto aj ich zariadenia sú rozdielne, dokážeme zmerať len veľmi malú časť zariadení, zvyšok bude dopočítavaný (upsampling) vďaka algoritmu, ktorý je vytvorený na základe korelácie údajov zo senzorov a manuálneho počítania. 
>
> Právne
>
> Klienta nemôžeme jednoznačne identifkovať kvôli GDPR, avšak môžeme použiť rozličné metódy anonimizácie, v rozličných stupňoch spracovania údajov môžu byť požité rozličné techniky anonimizácie. Klienti musia upraviť svoje GDPR.
> [odporúčania na gdpr spraocvanie údajov](https://copilot.microsoft.com/shares/vtV1TFUdzsSLco3cjezjV)
>
> Finančné
> 
> Rozpočet na realizáciu sú desiatky euro, všetko čo je možné rozložiť do iných divízií firmy.
- Aké minimálne dáta sú pre klienta zmysluplné, aby mal pocit „že to funguje“?
> Klient vydí krivku návštevnosti s orientačným počtom zákazníkov.
- Čo by malo byť súčasťou „prehľadného výstupu“?
> Počty, Trendy, Porovnanie s predchádzajúcim obdobím, porovnanie v segmente. Všetky ďaľšie informácie sú už spoplatnené.
- Budú zákazníci ochotní (alebo schopní) inštalovať softvér na svoje zariadenia sami?
> Cieľ je spraviť čo najjednoduchší proces, ktorý sa skladá z vytvorenia si konta na našom portáli, inštalácia PWA aplikácie inštalácia aplikácie bežiacej v pozadí windowsu. 
- Potrebujeme pripraviť štandardný GDPR text pre klienta?
> Až v neskoršej fáze, v testovacej fáze postačí aktuálne platný GDPR text, ktoré predajne už majú.
- Chceme informovať zákazníka, že jeho zariadenie môže byť zaznamenané?
> Predajne už majú aktuálne GDPR s počítaním - test realizujeme na predajni kde sa už uskutočnujú prieskumy návštevnosti


## ⚙️ Realizačné otázky na náš technický tým - koncepcia (ako to robíme?)
- Aké údaje vieme získať zo sniffera?
  >Príklad generovaný AI:

  ```Device 65:44:FF:60:FB:42
    Name: JBL Flip 5
    Alias: JBL Flip 5
    Class: 0x00240404
    Icon: audio-card
    Paired: no
    Trusted: no
    Blocked: no
    Connected: no
    LegacyPairing: no
    RSSI: -68
    ManufacturerData Key: 0x004c
    UUID: Audio Sink (0000110b-0000-1000-8000-00805f9b34fb)
    UUID: A/V Remote Control Target (0000110c-0000-1000-8000-00805f9b34fb)```

- Ako z údajov vytvoríme entity?
  > Nutné usktučniť testy a merania, na to aby sme pripravili 
- Aký typ správania chceme klasifikovať?
  > Cieľ je získať maximum informácií aby si analytické oddelenie stanovilo vlastné parametre
- Ako anonymizujeme údaje kvoli GDPR a pritom získame maximum údajov?
  > Etapovanie anonimizácie

## ✅ Moje očakávania ako zadávateľa
- Jednoduchá aplikácia, ktorú si zákazník môže sám nainštalovať
- CSV a grafický výstup (counter v čase)
- Merateľné hodnoty (trendy) bez použitia špecializovaných zariadení
