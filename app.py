from flask import Flask
from keystone import *

app = Flask(__name__)

def test_ks(arch, mode, code, syntax=0):
    ks = Ks(arch, mode)
    if syntax != 0:
        ks.syntax = syntax
    
    encoding, count = ks.asm(code)

    print("%s = [ " % code)
    for i in encoding:
        print("%02x " % i)
    print("]")


@app.route('/')
def hello_world():
    test_ks(KS_ARCH_X86, KS_MODE_16, b"add eax, ecx")
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
