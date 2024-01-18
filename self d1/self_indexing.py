# indexin = accessing elemtents of a sequence using [] (indexing operator) 
#           [start : end : step]
'''''
credit_number = '1234-5678-9012-3456'

print(credit_number[4])
print(credit_number[:4])
print(credit_number[5:9])
print(credit_number[5:])
print(credit_number[-1])
print(credit_number[::3])

credit_number = "1234-5678-9012-3456"

last_digits = credit_number[0]
print(f"XXXX-XXXX-{last_digits}")
'''''
# Email slicer exercise

email = input("Enter your email: ")

index = email.index("@")

username = email[:index]
domain = email[index + 1:]

print(f" 너 이름 {username} 이고 너는 {domain}을 쓴다")
