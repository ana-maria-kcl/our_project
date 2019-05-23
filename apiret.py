def generate_key():
    with open('my_key.txt') as f:
        for line in f:
            api_key = line
    return mod(api_key)

def mod(api_key):
    arr = ['0','2','2', '9', '3']
    newkey = ''
    counter = 0
    for i in range(0, len(api_key)):
        if i % 2 == 0:
           if counter < len(arr):
               newkey += arr[counter]
               counter+=1
           else:
              newkey += api_key[i]
        else:
            newkey += api_key[i]

    return newkey
