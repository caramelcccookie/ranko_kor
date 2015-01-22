import random
A = [('푸른소녀여'),('꽃피는 소녀여!'), ('세개의 별의 소녀여!'), ('세기말 가희!!!!'), ('방관자여!'), ('나의 벗이여!'), ('나의 하인들이여!'), (1,'이여'), (1,'이여'), (1,'이여'), (1,'이여'), (1,'이여'), (1,'에 이끌린 ',1,'이여!'), (1,'에 이끌린 ',1,'이여!'), (1,'에 이끌린 ',1,'이여!')]
B = [('성가신 태양이네!'), (1,'에 삼켜져라!'), (1,'을 불러오리라!'), ('크크크, 혼이 날뛰고 있어.'), ('황천의 샘으로 초대하지.'), ('신께 받은 이 전능! 진동으로 마음과 공명하리라!'),('나와 함께 혼의 공명을 연주하라!'),('소원을 이룬 타천사가 지금 여기에 춤추며 내려온다!'), ('이 연회, 같이 생명의 불꽃을 태워 사라질때까지 노래해주겠노라!'), ('유리구두는 눈에 보이지 않는것!'), ('이 몸에 작렬하는 마력이 깃든다!'), ('당신도 ',1,'의 소유자인 모양이군.'), ('당신도 ',1,'의 소유자인 모양이군.'), ('당신도 ',1,'의 소유자인 모양이군.'), ('당신도 ',1,'의 소유자인 모양이군.')]

A_range = len(A)
B_range = len(B)

Chuu2=['열기', '어둠', '고통', '전능', '혼', '공명', '생명의 불꽃', '유리구두', '아마겟돈', '마력', '타천사', '시험', '교향곡', '영혼', '미궁', '망설임', '흘러나온 한숨', '사모하는 마음', '되살아나는 환영', '그 손', '붉은 입술', '심판', '흔들리는 눈', '감미로운 감옥', '카르마', '아리아']
Chuu2_range = len(Chuu2)
Chuu2_index = random.randrange(0,Chuu2_range)

A_index = random.randrange(0,A_range)
B_index = random.randrange(0,B_range)

tmp = ''
for i in A[A_index]:
    if type(i)==int:
        tmp += Chuu2[Chuu2_index]
        tmp_Chuu2_index = random.randrange(0,Chuu2_range)
        if tmp_Chuu2_index==Chuu2_index:
            Chuu2_index += 1
        else:
            Chuu2_index = tmp_Chuu2_index
    else:
        tmp = tmp + i
sentence_A = tmp
tmp = ''
for i in B[B_index]:
    if type(i)==int:
        tmp += Chuu2[Chuu2_index]
        tmp_Chuu2_index = random.randrange(0,Chuu2_range)
        if tmp_Chuu2_index==Chuu2_index:
            Chuu2_index += 1
        else:
            Chuu2_index = tmp_Chuu2_index
    else:
        tmp = tmp + i
sentence_B = tmp
print (sentence_A+ ' ' +sentence_B)


# 중2어 세부분류를 한다면 중2어중 자신을 또는 인물을 지칭하는 분류는 따로 만들어야하나?
# 또한 조사 은,는 / 이,가 / 을,를
