# initieel aantal flesjes op de muur inlezen
flesjes = int(input())

while flesjes:

    s = '' if flesjes == 1 else 's'
    print(f'{flesjes} flesje{s} met bier op de muur, {flesjes} flesje{s} met bier.')

    flesjes -= 1
    s = '' if flesjes == 1 else 's'
    print(f'Open er een, drink hem meteen, {flesjes} flesje{s} met bier op de muur.')
