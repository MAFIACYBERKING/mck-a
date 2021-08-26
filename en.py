import os, base64
from pprint import pformat
os.system("clear")
alphabet = [
    "\U0001f600",
    "\U0001f603",
    "\U0001f604",
    "\U0001f601",
    "\U0001f605",
    "\U0001f923",
    "\U0001f602",
    "\U0001f609",
    "\U0001f60A",
    "\U0001f61b",
]
MAX_STR_LEN = 70
OFFSET = 10
N = '\033[0m'
D = '\033[90m'
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
P="\033[0;35m"
Y = '\033[1;33m'
C = '\033[1;36m'

ask = G + '[' + W + '+' + G + '] '
success = G + '[' + W + '+' + G + '] '
error = R + '[' + W + '⚠️' + R + ']'

def obfuscate(VARIABLE_NAME, file_content):
    b64_content = base64.b64encode(file_content.encode()).decode()
    index = 0
    code = f'{VARIABLE_NAME} = ""\n'
    for _ in range(int(len(b64_content) / OFFSET) + 1):
        _str = ''
        for char in b64_content[index:index + OFFSET]:
            byte = str(hex(ord(char)))[2:]
            if len(byte) < 2:
                byte = '0' + byte
            _str += '\\x' + str(byte)
        code += f'{VARIABLE_NAME} += "{_str}"\n'
        index += OFFSET
    code += f'exec(__import__("\\x62\\x61\\x73\\x65\\x36\\x34").b64decode({VARIABLE_NAME}.encode("\\x75\\x74\\x66\\x2d\\x38")).decode("\\x75\\x74\\x66\\x2d\\x38"))'
    return code


def chunk_string(in_s, n):
    """Chunk string to max length of n"""
    return "\n".join(
        "{}\\".format(in_s[i : i + n]) for i in range(0, len(in_s), n)
    ).rstrip("\\")


def encode_string(in_s, alphabet):
    d1 = dict(enumerate(alphabet))
    d2 = {v: k for k, v in d1.items()}
    return (
        'exec("".join(map(chr,[int("".join(str({}[i]) for i in x.split())) for x in\n'
        '"{}"\n.split("  ")])))\n'.format(
            pformat(d2),
            chunk_string(
                "  ".join(" ".join(d1[int(i)] for i in str(ord(c))) for c in in_s),
                MAX_STR_LEN,
            ),
        )
    )



        

def encryptem():
    in_file= input(ask + C + "Input File " + G + "> " + B)
    if not os.path.exists(in_file):
            print(error+' File not found')
            os.system("sleep 2")
            encryptem()
    out_file=(in_file+"MCK-A.py")
    if os.path.exists(in_file):
        with open(in_file) as in_f, open(out_file, "w") as out_f:
            out_f.write("# Encrypted by MD ALAMIN CHOWDOWRY\n# Github- https://github.com/HANTER2\n\n")
            out_f.write(encode_string(in_f.read(), alphabet))
            print(success+out_file+" saved in current directory")
            if os.path.exists("/sdcard/Download"):
                os.system("cp -r "+out_file+" /sdcard/Download")
                print(success+ out_file + " copied to Download or /sdcard/Download")
            if os.path.exists("/home/Downloads"):
                os.system("cp -r "+out_file+" /home/Downloads")
                print(success+ out_file + " copied to Downloads or /home/Downloads")
                print("save This file"+out_file) 
            os.system("sleep 3")
            a=input("Do You Went manu: ")
            main()
    elif not os.path.isfile(in_file) or not path.endswith('.py'):
        print(error+'Invalid file')
        exit()
    elif IOError:
        print(error+"File not found")
    else:
        print(error+"Error!")
        exit()

os.system("clear")
print(R+"""
888b     d888  .d8888b.  888    d8P             d8888 
8888b   d8888 d88P  Y88b 888   d8P             d88888 
88888b.d88888 888    888 888  d8P             d88P888 
888Y88888P888 888        888d88K             d88P 888 
888 Y888P 888 888        8888888b   888888  d88P  888 
888  Y8P  888 888    888 888  Y88b  888888 d88P   888 
888   "   888 Y88b  d88P 888   Y88b       d8888888888 
888       888  "Y8888P"  888    Y88b     d88P     888 
                                                      
                                                      
                                                      
""")
print(C+"\n\n\t  Delovment by MD ALAMIN CHOWFOWRY")
print(Y+"\n+++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("\n\t\t verson: 2.0.9")
print("\n\t\t   ENCRYPT/OBFUSCATE SCRIPT ")
print(Y+"\n+++++++++++++++++++++++++++++++++++++++++++++++++++++")


    
    
 

encryptem()          