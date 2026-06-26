import string
ATBASH_PRINCIPLE = dict(zip(string.ascii_lowercase, string.ascii_lowercase[::-1]))
ATBASH_PRINCIPLE.update(zip(string.digits, string.digits))

def encode(plain_text):
    encoded_string=[]
    count=0
    for n in plain_text:
        if n.lower() in ATBASH_PRINCIPLE:
            encoded_string.append(ATBASH_PRINCIPLE[n.lower()])
            count+=1
            if count%5==0:
                encoded_string.append(" ")
                count=0
    return "".join(encoded_string).strip()


def decode(ciphered_text):
    return "".join(ATBASH_PRINCIPLE[n.lower()] for n in ciphered_text if n.lower() in ATBASH_PRINCIPLE)