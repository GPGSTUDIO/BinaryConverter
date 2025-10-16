"""
This code is optimized for 1 file
Without this there were 4 files so the code can be in a heap.
"""
seed = None # If you want to use seed replace None to "123ABC..."
import random
import hashlib

def shuffle_text(text, seed=None):
    if seed is not None:
        if isinstance(seed, (int, float)):
            numeric_seed = int(seed)
        else:
            seed_str = str(seed)
            hash_obj = hashlib.md5(seed_str.encode())
            numeric_seed = int(hash_obj.hexdigest(), 16)
        random.seed(numeric_seed)
    text_list = list(text)
    random.shuffle(text_list)
    return ''.join(text_list)
def hex2binary(hex):
    slovar = {'0': '0000', '1': '0001', '2': '0010', '3': '0011','4': '0100', '5': '0101', '6': '0110', '7': '0111','8': '1000', '9': '1001', 'A': '1010', 'B': '1011','C': '1100', 'D': '1101', 'E': '1110', 'F': '1111','a': '1010', 'b': '1011', 'c': '1100', 'd': '1101','e': '1110', 'f': '1111'}
    binary_result = ''
    for i in hex:
        if i in slovar:
            binary_result += slovar[i]
        else:
            print(f"Недопустимый hex символ: {i}")
    return binary_result

def deciminal2binary(deciminal):
    try:
        deciminal = int(deciminal)
        if deciminal == 0:
            return "0"
        binary = ""
        num = deciminal
        while num > 0:
            binary = str(num % 2) + binary
            num = num // 2
        return binary
    except Exception as e:
        print(f"Недопустимый deciminal символ! Ошибка: {e}.")
        
def binary2deciminal(binary):
    try:
        binary = str(binary)
        if binary == "0":
            return 0
        deciminal = 0
        length = len(binary)
        for i in range(length):
            digit = int(binary[i])
            power = length - i - 1
            deciminal += digit * (2 ** power)
        return deciminal
    except Exception as e:
        print(f"Недопустимый binary символ! Ошибка: {e}.")

def binary2hex(binary):
    slovar = {'0000': '0', '0001': '1', '0010': '2', '0011': '3','0100': '4', '0101': '5', '0110': '6', '0111': '7','1000': '8', '1001': '9', '1010': 'A', '1011': 'B','1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
    hex_result = ''
    try:
        padding = (4 - len(binary) % 4) % 4
        if padding > 0:
            binary = '0' * padding + binary
        lenght = len(binary)/4
        for x in range(0,int(lenght)):
            xv = x*4
            i = binary[xv+0]+binary[xv+1]+binary[xv+2]+binary[xv+3]
            if i in slovar:
                hex_result += slovar[i]
            else:
                print(f"Недопустимый binary символ: {i}")
        return hex_result
    except Exception as e:
        print(f"Недопустимый binary символ! Ошибка: {e}.")

def reload_config(seed=None):
    codesymbols = '\uFFFD\u00A9\u00AE\u2122\u2764\u2605\u2713\u2717\u00A0±×÷√∞≈≠≤≥∫∂∆∇∑∏αβγπσμ°∠∟⊥∥←→↑↓↔↕↖↗↘↙⇐⇒⇑⇓⇔⇕$€£¥₽₹₴¢₤♩♪♫♬♔♕♖♗♘♙♚♛♜♝♞♟❄️🎵🎶\0\a\b\t\n\v\f\r\x1B\uB999\uA999\uC999'
    english = 'qwertyuiopasdfghjklzxcvbnm'
    bigEnglish = english.upper()
    russia = 'ёйцукенгшщзхъфывапролджэячсмитьбю'
    bigRussia = russia.upper()
    other = ' -=[]{}\\|/.,<>()*&^%$#@!~`\'"?+_;:1234567890'
    together = {}
    all_chars = codesymbols + english + bigEnglish + russia + bigRussia + other

    if seed:
        all_chars = shuffle_text(all_chars, seed)
        
    return [all_chars, together]

subsymbolsf = [
'GCoder V1.0.',
'func=print(f"all_chars: {len(all_chars)}, codesymbols: {len(codesymbols)}, english: {len(english)}, bigEnglish: {len(bigEnglish)}, russia: {len(russia)}, bigRussia: {len(bigRussia)}, other: {len(other)}, subsymbolsf: {len(subsymbolsf)}, subsymbols: {len(subsymbols)}")',
'func=print(f\'CodeSymbols [1B]: {all_chars.find("\\x1B")},CodeSymbols [\\\\n]: {all_chars.find("\\n")},CodeSymbols [\\\\r]: {all_chars.find("\\r")},CodeSymbols [\\\\a]: {all_chars.find("\\a")}\')'
]

subsymbols = [
'✓','♪','•','¶','⁋','‖','⟫','⟪','⟬','⟭','⟦','⟧','⌊','⌈','⌉','⌋','‾','_','¯'
]

reload_config_data = reload_config(seed)
all_chars = reload_config_data[0]
together = reload_config_data[1]
    
for i, char in enumerate(all_chars):
    together[char] = format(i, '08b')

i_together = {value: key for key, value in together.items()}

print('1 - Encode, 2 - Decode.')
while True:
    setnewseed = False
    newseed = ''
    
    mode = input('\n> ')

    if mode=='1':
        print('Selected: '+mode)
        text2encode = input('Encode: ')
        for x in range(0,len(all_chars)):
            text2encode=text2encode.replace('%R%'+str(x)+'%R%',all_chars[x])
        for i in text2encode:
            if not i in together:
                print('00',end='')
            else:
                print(binary2hex(together[i]),end='')
    if mode=='2':
        skipnext = False
        print('Selected: ' + mode)
        text2encode = input('Decode: ')
        full = hex2binary(text2encode)
        for i in range(0, len(full) // 8):
            binary_code = full[i*8 : i*8 + 8]
            if binary_code in i_together:
                if i_together[binary_code]=='\uB999':
                    skipnext='1'
                elif i_together[binary_code]=='\uA999':
                    skipnext='2'
                elif i_together[binary_code]=='\uC999':
                    setnewseed=True
                else:
                    if setnewseed:
                        newseed = newseed+i_together[binary_code]
                    else:
                        if skipnext=='1':
                            try:
                                subsymbolsf_c = subsymbolsf[binary2deciminal(binary_code)]
                                if 'func=' in subsymbolsf_c:
                                    exec(subsymbolsf_c[5:])
                                else:
                                    print(subsymbolsf_c,end='')
                            except:
                                pass
                            skipnext=False
                        elif skipnext=='2':
                            try:
                                subsymbols_c = subsymbols[binary2deciminal(binary_code)]
                                print(subsymbols_c,end='')
                            except:
                                pass
                            skipnext=False
                        else:
                            print(i_together[binary_code], end='')
            else:
                print('�', end='')
        if setnewseed:
            reload_config_data = reload_config(newseed)
            all_chars = reload_config_data[0]
            together = reload_config_data[1]
            for i, char in enumerate(all_chars):
                together[char] = format(i, '08b')
            i_together = {value: key for key, value in together.items()}
            setnewseed = False
            newseed = ''