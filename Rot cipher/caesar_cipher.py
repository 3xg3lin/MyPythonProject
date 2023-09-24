import optparse

def rot_func():
    instance = optparse.OptionParser()
    instance.add_option('-t','--type',dest='type',default = '13', help='which rot algorithm you want')
    return instance.parse_args()

def encode_message(ctype,message):
    alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    i=''
    string_message=''
    for i in message:
        if i.isalpha():
            counter = 0
            for y in alphabet:
                if i == y:
                    string_message += alphabet[((counter + ctype * 2))%52]
                    break
                else:
                    counter+=1
        else:
            string_message += i
    return string_message

(user_input,arguments) = rot_func()
message=input('type a message: ')
print(encode_message(int(user_input.type),message))
