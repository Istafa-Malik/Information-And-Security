import random
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True


def generate_key_pair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
   
    n = p * q

    phi = (p-1) * (q-1)

    e = random.randrange(1, phi)

    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi)

    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    
    key, n = pk
   
    cipher = [pow(ord(char), key, n) for char in plaintext]
   
    return cipher


def decrypt(pk, ciphertext):
   
    key, n = pk
   
    aux = [str(pow(char, key, n)) for char in ciphertext]
    
    plain = [chr(int(char2)) for char2 in aux]
    return ''.join(plain)


def Attack(p,q,en_message):
    print("Encrypted message : ->>",en_message)
    plaintext  = en_message
    list_of_key = [2, 3, 5, 7, 11, 13, 17, 19 ,23 ,29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71 ,73 ,79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157,163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281 ,283, 293, 307, 311, 313, 317, 331,337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509,521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709,719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809 ,811, 821, 823 ,827, 829, 839, 853, 857, 859, 863, 877 ,881, 883, 887, 907, 911, 919,929, 937, 941, 947, 953 ,967 ,971 ,977 ,983, 991, 997]
    print(list_of_key)
    n = p *q
    for key in list_of_key:
        cipher = [pow((char), key, n) for char in plaintext]
        
        if cipher==en_message:
            print("Found17")
            print("Attack is Succcessful on key : ",key )
            return
        print(key,cipher,en_message)
    
    
if __name__ == '__main__':

    p = int(input(" - Enter a prime number "))
    q = int(input(" - Enter another prime number : "))

    print("  Generating your public / private key-pairs now ")

    public, private = generate_key_pair(p, q)

    print("  Your public key is ", public, " and your private key is ", private)

    message = input(" Enter the message you want to encrypt ")
    encrypted_msg = encrypt(public, message)

    
    Attack( p,q ,encrypted_msg)
    
    
    print(" Encrypted message is: ",''.join(map(lambda x: str(x), encrypted_msg)))
    print(" Decrypting message with private key is ", private, )
    print(" Message is  ", decrypt(private, encrypted_msg))
