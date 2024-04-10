text = []

text.append("Isto é uma string")
text.append("isso tambem é uma string")
text.append('Isso tambem é uma string tambem')
text.append('isso tambem é uma string tambem tambem')

for txt in text:
    print(txt)

mesagem = "Hello World"

print(mesagem[1:9])

email = "professor@eduacacao.gov"
print(email)

arroba = 0

for acheiArroba in email:
    if acheiArroba == "@": break
    arroba += 1

print(email[arroba+1:])

