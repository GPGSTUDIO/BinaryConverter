from SeedMapper import *
from Converter import *
import config

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

reload_config_data = reload_config(config.seed)
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