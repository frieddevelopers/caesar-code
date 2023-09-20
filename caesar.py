import sys

def encode(text, key):
    """
    This function takes a string and an integer key and returns an encoded string by that key. It ignores all punctuation and numbers and it preserves capitalization. If the resulting character isn't alphabetic it wraps around to keep it alphabetic.
    """
    li = []
    upper = range(65, 91)
    lower = range(97, 123)
    for i in text.split():
        word = []
        for j in i:
            if ord(j) in upper:
                new_l = ord(j) + key % 26
                if new_l not in upper:
                    new_l = new_l - 26
                
                word.append(chr(new_l))

            elif ord(j) in lower:
                new_l = ord(j) + key 
                if new_l not in lower:
                    new_l = new_l - 26
                
                word.append(chr(new_l))
            
            else:
                word.append(j)
        word = "".join(word)
        li.append(word)
        
    text = " ".join(li)
    
    return text 



def decode(text, key, called=False):
    li = []
    upper = range(65, 91)
    lower = range(97, 123)
    for i in text.split():
        word = []
        for j in i:
            if ord(j) in upper:
                new_l = ord(j) - key % 26
                if new_l not in upper:
                    new_l = new_l + 26
                
                word.append(chr(new_l))

            elif ord(j) in lower:
                new_l = ord(j) - key 
                if new_l not in lower:
                    new_l = new_l + 26
                
                word.append(chr(new_l))
            
            else:
                if not called:
                    word.append(j)
        word = "".join(word)
        li.append(word)
        
    text = " ".join(li)
    
    return text 


def find_key(text):
    # Load the dictionary 
    with open("large") as f:
        dictionary = f.readlines()
        dictionary = [i.strip() for i in dictionary]

    for i in range(0, 26):
        d_text = decode(text, i) 
        words = d_text.split()
        correct = True
        count = 0
        found = 0
        len_words = len(words)
        for word in words:
            d_word = decode(word.lower(), 0, True)
            
            # Check if word isn't in dictionary. If incorrect words is higher than 10% than assume the key is wrong.
            if d_word not in dictionary:
                count += 1 
                if count >= len_words / 10:
                    correct = False
                    break 
            else:
                found += 1
                if found == 10:
                    break
        if correct:
            return i 



if __name__ == "__main__":
    while True:
        print("1: Encode text\n2: Decode text\n3: quit")
        choice = input()
        try:
            choice = int(choice) 
        except ValueError:
            sys.exit()
        if choice not in [1, 2]:
            sys.exit()

        if choice == 1:
            print("Enter the text you would like to encode")
            input_text = input()
            while True:
                print("Enter key")
                key = input()
                try:
                    key = int(key)
                    break
                except ValueError:
                    print("Please enter an Integer key")
                    continue
            coded_text = encode(input_text, key)
            print(coded_text)
        else:
            print("Enter text you would like to decode")
            text = input()
            key = find_key(text)
            print(decode(text, key))


