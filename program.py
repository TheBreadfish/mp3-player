from pygame import mixer
from os import system

currentSong = 'Dyad.mp3'

mixer.init()
mixer.music.load(f'music/{currentSong}')
volume = float(input('volume: '))
mixer.music.set_volume(volume)

mixer.music.play()

playing = True
helping = False

def menu():
    if playing:
        playPauseIcon = '[ ❚❚ ]'
    else:
        playPauseIcon = '[ ▶ ]'
    system('cls')
    print(f'Playing: {currentSong}')
    print(f'{playPauseIcon} Type "help" for help')

    if helping:
        print('\nENTER:  Play/Pause\nexit(): Exit\nCTRL+C: Force Stop')

while True:
    menu()
    responce = input('    ')

    if responce == '':
        playing = not playing

        if playing:
            mixer.music.unpause()
        else:
            mixer.music.pause()
        menu()
    elif responce == 'exit()':
        mixer.music.stop()
        break
    elif responce == 'help':
        helping = not helping
        menu()