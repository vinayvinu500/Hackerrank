#Caesar cipher
# https://www.hackerrank.com/challenges/caesar-cipher-1/problem

"""convert the plain text into cipher text"""
"""pick a alphabet and replace with next alphabet"""
"""Example A -> B"""

plain_text = "defend the east wall of the castle"
cipher_text = "efgfoe uif fbtu xbmm pg uif dbtumf"

"""class"""
class CaeserCipher:

    def __init__(self,a="Hello World"):
        self.a = a
        
    def encrypt(self,a):
        """
        It takes the string of one argument 
        which picks from chr - 97,123 or 65,91
        encrypt into caeser cipher
       """
        alpha = list(map(chr,range(97,123))) + list(map(chr,range(65,91)))
        cipher = ""
        for i in a:
            if i in alpha:
                index = alpha.index(i)
                cipher += alpha[index+1]
            elif i == ' ':
                cipher += ' '
        return  cipher
    
        
    def decrypt(self,a):
        """
        It takes the string of one argument 
        which picks from chr - 97,123 or 65,91
        decrypt into caeser cipher
       """
        alpha = list(map(chr,range(97,123))) + list(map(chr,range(65,91)))
        cipher = ""
        for i in a:
            if i in alpha:
                index = alpha.index(i)
                cipher += alpha[index-1]
            elif i == ' ':
                cipher += ' '
        return  cipher
        
cipher = CaeserCipher()
a = cipher.encrypt(plain_text)
print(f"encrypt => {a}")
b = cipher.decrypt(a)
print("decrypt => "+b)


"""Algorithm"""
#encryption
def encrypt(a):
    alpha = list(map(chr,range(97,123))) + list(map(chr,range(65,91)))
    cipher = ""
    for i in a:
        if i in alpha:
            index = alpha.index(i)
            cipher += alpha[index+1]
        elif i == ' ':
            cipher += ' '
    return  cipher
result = encrypt(plain_text)
#print("encrypt => ",result)

#decryption
def decrypt(a):
    alpha = list(map(chr,range(97,123))) + list(map(chr,range(65,91)))
    cipher = ""
    for i in a:
        if i in alpha:
            index = alpha.index(i)
            cipher += alpha[index-1]
        elif i == ' ':
            cipher += ' '
    return  cipher
result = decrypt(result)
#print("decrypt => ",result)


