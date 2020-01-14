# python-bitcoinlib-programs

## Task

1. Panaudojant `python-bitcoinlib` biblioteką, Python aplinkoje realizuokite programą, apskaičiuojančią  transakcijos (pvz.`0627052b6f28912f2703066a912ea577f2ce4da4caa5a5fbd8a57286c345c2f2`) mokestį?

   - Patobulinkite programą, kad ji gebėtų apskaičiuotų bet kurios įvestos Bitcoin transakcijos mokestį.
   - Apskaičiuokite, kiek kainavo atlikti (2019-09-06) vieną vertingiausių transakcijų Bitcoin tinkle, kurios hash'as yra: `4410c8d14ff9f87ceeed1d65cb58e7c7b2422b2d7529afc675208ce2ce09ed7d`

2. Panaudojant `python-bitcoinlib` biblioteką, Python aplinkoje realizuokite programą, kuri iš  atitinkamos bloko header'io informacijos "patikrintų", kad bloko hash'as yra teisingas. Kaip pagalbine primone, rekomenduojame naudotis šiuo **wiki** šaltiniu: [Block hashing algorithm](https://en.bitcoin.it/wiki/Block_hashing_algorithm)

## How to run

- Connect to Bitcoin node
- To calculate transaction fee: `python TransactionFee.py <insert transaction hash>` 
- To check if hash was calculated correctly: `python CheckHash.py <insert block height>`

## Examples

### Transaction fee calculation
- `python TransactionFee.py 4410c8d14ff9f87ceeed1d65cb58e7c7b2422b2d7529afc675208ce2ce09ed7d`

![TransactionFee](/images/TransactionFee.png)

### Hash checking
- `python CheckHash.py 100001`

![CheckHash](/images/CheckHash.png)
