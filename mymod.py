if __name__ == '__main__':   # only run this code if we're executing mymod.py -- not if we're importing it
    print(f'Hello from {__name__}!')

x = 100

y = [10, 20, 30]

def hello(name):
    return f'Hello, {name}!'

if __name__ == '__main__':
    print(f'Now leaving {__name__}!')

# print(hello('world'))
