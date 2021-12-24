# [2309번 : 일곱 난쟁이](https://www.acmicpc.net/problem/2309)
# 🙋‍♀️ 내 코드

dwarfs = [int(input()) for i in range(9)]
dwarfs.sort()
differences = sum(dwarfs)-100
fake = []
# 최대값 원소인 25랑 합쳐도 40(differences)보다 작으면 100이 될 수 없다.
# 그러니 15부터만 후보이다.
# 그래서 4부터 시작했더니 틀렸다고뜬다...ㅠㅠ 코드로 컴퓨터한테 이해시켜야할듯.
for f in range(len(dwarfs)):
    for f2 in range(f+1,len(dwarfs)):   
        if differences == (dwarfs[f]+dwarfs[f2]):
            fake.append(dwarfs[f])
            fake.append(dwarfs[f2])
    if len(fake)==2 :
        breakß
result = [x for x in dwarfs if x not in fake]
result.sort()
for x in result:
    print(int(x))

