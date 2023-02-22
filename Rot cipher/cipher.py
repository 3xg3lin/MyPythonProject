import optparse

def rot_func():
    instance = optparse.OptionParser()
    instance.add_option('-t','--type',dest='type',default = '13', help='which rot algorithm you want')
    return instance.parse_args()

def encode_message(ctype,message):
    alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    i=''
    index = 0
    for i in message:
        index = 0
        while i != alphabet[index]:
            index += 1
        cipher_message.append(alphabet[(index + ctype * 2)%52])
    return cipher_message


cipher_message = []
(user_input,arguments) = rot_func()
message=input('type a message: ')
print(encode_message(int(user_input.type),message))

