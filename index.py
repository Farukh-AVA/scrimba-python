print('Project -  Crypto')
def enigma_light():
# create keys string
    keys = 'abcdefghijklmnopqrstuvwxyz !'
# autogenerate the values string by offsetting original string
    values = keys[-1] + keys[0:-1]
# create two dictionaries
    dict_e = dict(zip (keys, values)) 
    dict_d = dict(zip(values, keys))
#user input 'the message' and mode
    msg = input('Please enter a meassage')
    mode = input('Please enter e for encrypt and d for decrypt')
# run encode or decode
    if mode == 'e':
        new_msg = ''.join([dict_e[letter] for letter in msg.lower()])
    else: 
        new_msg = ''.join([dict_d[letter] for letter in msg.lower()])    
# return result
    return new_msg
# clean and beautify the code 
print(enigma_light())