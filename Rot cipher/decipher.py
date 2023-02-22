import optparse

def rot_func():
    instance = optparse.OptionParser()
    instance.add_option('-t','--type',dest='type',default='13',help='which rot algorithm you want')
    return instance.parse_args()

def decode_message(ctype,encrypted_message):
    i = ''
    alphabet = 'zZyYxXwWvVuUtTsSrRqQpPoOnNmMlLkKjJiIhHgGfFeEdDcCbBaA'
    for i in encrypted_message:
        index = 0
        while i != alphabet[index]:
            index += 1
        message.append(alphabet[(index + ctype * 2)%52])
    return message

message = []
(user_input,arguments) = rot_func()
cipher_message = input('type a encrypted message: ')
print(decode_message(int(user_input.type),cipher_message))

