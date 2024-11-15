num_user = int(input())
hundreds = num_user // 100
tens = (num_user - hundreds * 100) // 10
ones = num_user - hundreds * 100 - tens * 10

h_tens = hundreds + tens
o_tens = ones + tens

if h_tens > o_tens:
    print(str(h_tens) + str(o_tens))
else:
    print(str(o_tens) + str(h_tens))