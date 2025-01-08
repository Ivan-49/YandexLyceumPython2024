pravilo = """А - A
Б - B
В - V
Г - G
Д - D
Е - E
Ё - E
Ж - ZH
З - Z
И - I
Й - I
К - K
Л - L
М - M
Н - N
О - O
П - P
Р - R
С - S
Т - T
У - U
Ф - F
Х - KH
Ц - TC
Ч - CH
Ш - SH
Щ - SHCH
Ы - Y
Э - E
Ю - IU
Я - IA
, - ,
. - .
? - ?
! - !
; - ;
: - :
  -  """


pravilo = pravilo.split("\n")
for i in pravilo:
    pravilo[pravilo.index(i)] = i.split(" - ")

for i in pravilo:
    if len(i[1]) > 1:
        pravilo[pravilo.index(i)][1] = pravilo[pravilo.index(i)][1].capitalize()

for i in range(len(pravilo)):
    pravilo.append([pravilo[i][0].lower(), pravilo[i][1].lower()])


pravilo_dict = {}
for i in pravilo:
    pravilo_dict[i[0]] = i[1]
pravilo = pravilo_dict
del pravilo_dict


user = input()
result = ""
for i in user:
    if i in pravilo.keys():
        result += pravilo[i]
    # else:
    #     result += i
print(result)
