print("Playfair decryptor 1.0")
print("Please ensure all input is all caps, and has no numbers or spaces.")
key = input("Enter key: ")
ciphertext = input("Enter ciphertext: ")

keyList = []

for a in key:  # Removing duplicate elements
    if a in keyList:
        pass
    else:
        keyList.append(a)

alphaList = []
for a in range(65, 91):  # generating list of cipher alphabet
    if chr(a) not in keyList and chr(a) != 'Q':
        alphaList.append(chr(a))
keyAlphaList = keyList + alphaList

keyMatrix = [[0 for i in range(5)] for j in range(5)]

k = 0
for i in range(5):  # making cipher matrix
    for j in range(5):
        keyMatrix[i][j] = keyAlphaList[k]
        k += 1


ciphertextDuos = []
k=0
a=''
for i in ciphertext:
    if k==2:
        ciphertextDuos.append(a)
        a=''
        k=0
    a+=i
    k+=1
ciphertextDuos.append(a)
plaintextDuos = []
for currentPair in ciphertextDuos:
    indexList = []
    for currentElem in currentPair:
        for i in range(5):
            for j in range(5):
                if keyMatrix[i][j] == currentElem:
                    indexList.extend([i, j])
    if indexList[0] == indexList[2]:  # checking to see if samerow/column/not
        indexList[1] -= 1
        indexList[3] -= 1
    elif indexList[1] == indexList[3]:
        indexList[0] -= 1
        indexList[2] -= 1
    else:
        indexList[3], indexList[1] = indexList[1], indexList[3]
    for k in range(len(indexList)):  # to wrap around
        if indexList[k] > 4:
            indexList[k] -= 5
    plaintextPair = keyMatrix[indexList[0]][indexList[1]] + keyMatrix[indexList[2]][indexList[3]]
    plaintextDuos.append(plaintextPair)

plaintext = ''

for a in plaintextDuos:
    plaintext += a

print("plaintext:", plaintext)



















