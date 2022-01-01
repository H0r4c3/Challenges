'https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/upup/'

'''
You are given a string S. S consists of several words separated by one or more spaces. 
Word consists of Latin letters as well as other symbols (but not spaces).
In each word which starts from lowercase Latin letter replace starting letter with uppercase Latin letter.
'''

def upup(s):
    my_list1 = list()
    s_list = s.split()
    for item in s_list:
        item = item.strip()
        item1 = item[0].upper() + item[1:]
        my_list1.append(item1)
    
    result = ' '.join(my_list1)   
    
    return result

s = 'Wish you were here'
s = 'FmOeNk  p ww  IE  xpnv R  m MhMRje MTqS ZJ KFvtRl   XemR s   UJEEIK q   qt Ri   KQsz  l   KOAvLOXv bbGwsGQ EQ h fea  Q mLYO p X XVQ     U Cj H G c ty    th o  bXywDowu  V x pS  j Om d xLV  aP pyaBIWvz b  iBI P   g c txPR  I FJyVVKP  xfN zoZ  Lcfp DTu jh  tSON  nbLu  jH  LT Q s  R wy cj  Ks c  E  WZJZ  T b r QUJW   U C vA  rcZEk gSHySvi  jnyo qUEIxE  TJvAFFG   W I          r  GSMID uo rC  MQk CaGlwZn  Z ELi    mf  iyyhZGQH p lq  hr Ip  hZptaHnqc   k  GL OZoH    q  TlVxO o  p  mRogZjJL t  g vR z b'
# assert
# FmOeNk  P Ww  IE  Xpnv R  M MhMRje MTqS ZJ KFvtRl   XemR S   UJEEIK Q   Qt Ri   KQsz  L   KOAvLOXv BbGwsGQ EQ H Fea  Q MLYO P X XVQ     U Cj H G C Ty    Th O  BXywDowu  V X PS  J Om D XLV  AP PyaBIWvz B  IBI P   G C TxPR  I FJyVVKP  XfN ZoZ  Lcfp DTu Jh  TSON  NbLu  JH  LT Q S  R Wy Cj  Ks C  E  WZJZ  T B R QUJW   U C VA  RcZEk GSHySvi  Jnyo QUEIxE  TJvAFFG   W I          R  GSMID Uo RC  MQk CaGlwZn  Z ELi    Mf  IyyhZGQH P Lq  Hr Ip  HZptaHnqc   K  GL OZoH    Q  TlVxO O  P  MRogZjJL T  G VR Z B

result = upup(s)
print(result)