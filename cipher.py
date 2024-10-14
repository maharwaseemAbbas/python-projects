import pyfiglet

def main():
    
    text = 'Python Cipher'
    welcome = pyfiglet.figlet_format(text)
    print(welcome)

    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    name = ''
    decoded=''

    while True:

      option = input('Encode or Decode (E/D/END): ').lower()


      if option == 'e':
        user_input = input('Enter Message: ')
        shift = int(input('Enter Shift: '))
        shift = shift % 26
        name = encode(user_input, shift, alpha, name)
        print(f'Encoded: {name}')
        continue

      elif option == 'd':
        user_input = input('Enter Message: ')
        shift = int(input('Enter Shift: '))
        shift = shift % 26
        decoded = decoder(shift, alpha, user_input, decoded)
        print(f'Decoded: {decoded}')
        continue

      elif option == 'end':
        break

      else:
        print('Wrong Input')



def encode(user_input, shift, alpha, name):
  for i in user_input:
    index = alpha.index(i) + shift
    name = name + alpha[index]
  return name


def decoder(shift, alpha, name, decoded):
  for i in name:
    index =alpha.index(i)-shift
    decoded = decoded + alpha[index]
  return decoded

main()