# 26글자짜리 키 스트링 받음
keyset          = list(input())
# zfehgj .... 26

# 바꿀 스트링
input_to_change = list(input())
# Vertias et Lux

giri = len(input_to_change)

for i in range(giri):
    c              = input_to_change[i]
    ascii_num_of_c = ord(c)              ## 'b' -> 98
    n_th_alphabet  = ascii_num_of_c - 97 ##     ->  1
    
    target_char    = keyset[n_th_alphabet]   ## b에 바꿀 것이 1번째 칸에 있음
    
    input_to_change[i] = target_char

print(input_to_change)
