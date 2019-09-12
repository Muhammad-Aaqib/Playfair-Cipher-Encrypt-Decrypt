def table(key0):
    # Removing the similar letters from the key
    key0 = key0.upper()
    key = ""
    for i in key0:
        if i not in key:
            key += i

    # Preparing the 5x5 alphabetical matrix according to the provided key
    count = 0
    alphas0 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    alphas = []
    
    for i in key:
        alphas0.remove(i)
        alphas.append("")
    for i in alphas0:
        alphas.append(i)
        
    alpha = [['A', 'B', 'C', 'D', 'E'],
             ['F', 'G', 'H', 'I', 'K'],
             ['L', 'M', 'N', 'O', 'P'],
             ['Q', 'R', 'S', 'T', 'U'],
             ['V', 'W', 'X', 'Y', 'Z']]

    for i in range(len(alpha)):
        for j in range(len(alpha[i])):
            try:    alpha[i][j] = key[count]
            except: alpha[i][j] = alphas[count]
            count += 1
    return alpha

def modifyPair(pair, alpha, direct):
    replaced = ""
    direction = direct  # If the pair is to be encrypted of decrypted

    # Checking if the pair provided is in column, row, or at an intersection
    inRow = False
    inCol = False
    intersection = False
    
    for i in range(len(alpha)):
        col = []
        for j in range(len(alpha)):
            col.append(alpha[j][i])
        if pair[0] in col and pair[1] in col:
            inCol = True

        elif pair[0] in alpha[i] and pair[1] in alpha[i]:
            inRow = True

    if inRow == False and inCol == False:
        intersection = True

    # Encrypting of Decrypting the string of pair
    for i in range(len(alpha)):
        # Applying Encryption or Decryption process if the string of pair is in a row
        if inRow:
            if pair[0] in alpha[i] and pair[1] in alpha[i]:
                try:    replaced += alpha[i][alpha[i].index(pair[0]) + direction]
                except: replaced += alpha[i][0]
                try:    replaced += alpha[i][alpha[i].index(pair[1]) + direction]
                except: replaced += alpha[i][0]

        # Applying Encryption or Decryption process if the string of pair is in a column
        elif inCol:
            col = []
            for j in range(len(alpha)):
                col.append(alpha[j][i])

            if pair[0] in col and pair[1] in col:
                try:    replaced += col[col.index(pair[0]) + direction]
                except: replaced += col[0]
                try:    replaced += col[col.index(pair[1]) + direction]
                except: replaced += col[0]

        # Applying Encryption or Decryption process if the string of pair is at an intersection
        elif intersection:
            row1 = 0
            row2 = 0
            col1 = 0
            col2 = 0

            for i in range(len(alpha)):
                if pair[0] in alpha[i]: row1 = i
                if pair[1] in alpha[i]: row2 = i

                col = []
                for j in range(len(alpha)):
                    col.append(alpha[j][i])
                if pair[0] in col: col1 = i
                if pair[1] in col: col2 = i

            replaced += alpha[row1][col2]
            replaced += alpha[row2][col1]
            break
            
    return(replaced)

def encrypt(text, key):
    text = text.upper()
    encrypted = ""

    # In the newText, there will be "X" inserted between two similar characters
    newText = text
    for i in range(len(newText) - 1):
        if newText[i] == newText[i+1]:
            newText = newText[:i+1] + "X" + newText[i+1:]

    # Appending "X" in the neweText if the length string of the characters is an odd number
    if len(newText) % 2 != 0:
        newText += "X"

    # Passing the string to modifyPair() in the pair (pair of 2) forms
    for i in range(0, len(newText), 2):
        encrypted += modifyPair(newText[i] + newText[i+1], table(key), 1)
        
    return(encrypted)

def decrypt(text, key):
    text = text.upper()
    decrypted = ""

    # Passing the string to modifyPair() in the pair (pair of 2) forms
    for i in range(0, len(text), 2):
        decrypted += modifyPair(text[i] + text[i+1], table(key), -1)

    #decrypted.remove('X')

    return(decrypted)

# Removve the spaces from the string inputs
def modifyText(text):
    text = text.split()
    newText = ""
    
    for i in text:
        newText += i

    return newText

x = int(input("1. Encrypt\n2. Decrypt\nEnter: "))

key = modifyText(input("Enter the key: "))
text = modifyText(input("Enter the text: "))

if x == 1:
    print("Your encrypted text is: ", encrypt(text, key))
elif x == 2:
    print("Your decrypted text is: ", decrypt(text, key))
