# Start writing code here...
def fillTable(l1,l2,s1,s2,table):
    subCost = 0
    for i in range(1,l1):
        for j in range(1,l2):
            if(s1[i] == s2[j]):
                subCost = 0
            else:
                subCost = 1
            table[i][j] = min(min(table[i-1][j]+1, table[i][j-1]+1), table[i-1][j-1]+subCost)


def levenshteinDistance(string1, string2):
    length1 = len(string1)
    length2 = len(string2)
    table = [[0 for j in range(length2)] for x in range(length1)]
    for i in range(length1):
        table[i][0] = i 
    for i in range(length2):
        table[0][i] = i
    
    fillTable(length1, length2, string1, string2, table)
    return table[length1-1][length2-1]

print(levenshteinDistance("friday is life", "monday sucks"))