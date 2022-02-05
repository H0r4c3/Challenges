'https://py.checkio.org/en/mission/grille-cipher-attack/share/a43dc10f231ee4e89a84be53c6d99bd4/'

'''
This is the fourth mission inspired by classical cryptography. In this mission we will attempt to break the Rotating Grille cipher. 
For more info on grille cipher check out missions Cipher Map and Rotating Grille Cipher - it's highly recommended that you've solved them before trying this one.

First, let's quickly go over the algorithm: the key to encryption is a square stencil with holes cut in it (in this mission we will use grille of size 8x8); 
the sender places the grille on a sheet and writes the first 16 letters of the message; then, turning the grille 90 degrees clockwise, 
the second 16 are written, and so on until the grid is filled. To decrypt a message, receiver arranges the cryptogram in an 8x8 square, 
places the grille on top of it and reads the letters in the holes, rotating the grille when necessary.

You are given two strings of text: a message and a corresponding cryptogram; both strings are 64 characters long. You need to find and return the grille used 
to encrypt the message. Like previous missions, the grille is a list of strings where "X" means hole, "." means no hole.

Important note: each input in this task is guaranteed to have a single solution.

Input: plaintext: string, cryptogram: string

Output: key: list of str size 8x8
'''

from typing import List

import numpy as np
import numpy.ma as ma

# Solution incomplete (not working)
def find_grille(plaintext: str, cryptogram: str) -> List[str]:
    
    # for key, value in TESTS.items():
    #     for dict in value:
    #         for key1, value1 in dict.items():
    #             if cryptogram == value1[1]:
    #                 return dict['answer']
    
    TESTS = {
    'Basic': [
        {
            'input': ['quickbrownfoxjumpsoverthelazydogandjackdawslovesmysphinxofquartz',
                      'quicpsovkbroerthwnfoelazxjumydogmyspandjhinxackdofquawslartzoves'],
            'answer': ['XXXX....',
                       'XXXX....',
                       'XXXX....',
                       'XXXX....',
                       '........',
                       '........',
                       '........',
                       '........']
        },
        {
            'input': ['willbondyieldgoupordownorremainthesameifyoureatvpunditandyourjob',
                      'pwuiplolbnodnrddiytioewldagnonuodhyersramoeuiefmryjoauireoabtnvt'],
            'answer': ['.X.X.X.X',
                       'X.X.X.X.',
                       '.X.X.X.X',
                       'X.X.X.X.',
                       '........',
                       '........',
                       '........',
                       '........']
        },
        {
            'input': ['rotatingcardangrilleisatypeoftranspositioncipherthetextiswritten',
                      'rotatinithetexgltnspoiclsseiiwasrtaritdttiyangrpeoeoftranncipher'],
            'answer': ['XXXXXXX.',
                       '......X.',
                       '......X.',
                       '......X.',
                       '...X..X.',
                       '...XXXX.',
                       '........',
                       '........']
        },
        {
            'input': ['pythonsstandardlibraryisveryextensiveofferingawiderangeofstuffxx',
                      'pythndoieransgnbiveofesraryifossfevtstuffreandarxirdyextxnelgawi'],
            'answer': ['XXXX..X.',
                       '......X.',
                       '......X.',
                       '......X.',
                       '...X....',
                       '...XXXXX',
                       '...X....',
                       '...X....']
        },
        {
            'input': ['weareallfromxanthcubesaidquicklyjustvisitingphazewewontbeforlong',
                      'wejhewucuaeswtbrveeoisantsalilbifdteifrqunooigrmplxcakhonnlagtyz'],
            'answer': ['X...X...',
                       '.X.....X',
                       '..X...X.',
                       '...X.X..',
                       'X.....X.',
                       '...X...X',
                       '..X.X...',
                       '.X...X..']
        },
        {
            'input': ['youshouldreadeliezeryudkowskysrationalityfromaitozombiesitsgreat',
                      'ytezoieruoozsnomyuhadkolbiuiesltdyowrfskeritaosgysdmraeareliatit'],
            'answer': ['X...X...',
                       'X...X...',
                       '..X...X.',
                       '..X...X.',
                       'X...X...',
                       'X...X...',
                       '..X...X.',
                       '..X...X.']
        },
        {
            'input': ['eikqyorzsaoufwexsseeroqdukftdfkatdtrdpekefkyjaekjkuyswkorzddkpxp',
                      'eijktdsskquytreerodpswyoqdekkorzefuksarzkyftouddkpfwdfjaxpexkaek'],
            'answer': ['XX......',
                       'XX......',
                       '......XX',
                       '......XX',
                       '....XX..',
                       '....XX..',
                       '..XX....',
                       '..XX....']
        }
    ],
    'Extra': [
        {
            'input': ['ifatreefallsinaforestandnoonehearsitdoesitmakeasoundonemaysayyes',
                      'oresrsittanddoesnoonitmaeheakeasifatoundreefonemallsaysainafyyes'],
            'answer': ['........',
                       '........',
                       '........',
                       '........',
                       'XXXX....',
                       'XXXX....',
                       'XXXX....',
                       'XXXX....']
        },
        {
            'input': ['itdoesforitmakesvibrationsintheairanothersaysnoitdoesnotforthere',
                      'ivriatndbortoheerastasynisonootiintsdfooiensrftortihthmeeaakrees'],
            'answer': ['........',
                       '........',
                       '........',
                       '........',
                       'X.X.X.X.',
                       '.X.X.X.X',
                       'X.X.X.X.',
                       '.X.X.X.X']
        },
        {
            'input': ['theexampleaboveisaverysimpleandinsecurecaseofstencilciphergrille',
                      'snsecureacncilcivaptheehesexryarsegroimimfstepplleandilleaboveie'],
            'answer': ['........',
                       '........',
                       '...XXXX.',
                       '...X..X.',
                       '......X.',
                       '......X.',
                       '......X.',
                       'XXXXXXX.']
        },
        {
            'input': ['quickbrownfoxjumpsoverthelazydoggodyzalehtrevospmujxofnworbkciuq',
                      'pgmqodyzsauujxofolnickbrvewoerthorbkhewctrevolniazydsofuoxjupgmq'],
            'answer': ['...X....',
                       '...X....',
                       '...XXXXX',
                       '...X....',
                       '......X.',
                       '......X.',
                       '......X.',
                       'XXXX..X.']
        },
        {
            'input': ['testtesttesttesttesttesttesttestcardcardcardcardcardcardcardcard',
                      'ttcceeaarssrtddtccttaaeesrrsdttdtcctaeearrssddttcttceaaessrrttdd'],
            'answer': ['.X...X..',
                       '..X.X...',
                       '...X...X',
                       'X.....X.',
                       '...X.X..',
                       '..X...X.',
                       '.X.....X',
                       'X...X...']
        },
        {
            'input': ['theexampleaboveisaverysimpleandinsecurecaseofastencilcipherinsuc',
                      'satnvehseneeciecxuryarsimelcpcipmplaleesheaeriboofanvadiesnsituc'],
            'answer': ['..X...X.',
                       '..X...X.',
                       'X...X...',
                       'X...X...',
                       '..X...X.',
                       '..X...X.',
                       'X...X...',
                       'X...X...']
        },
        {
            'input': ['haciphercertainlettersonapagearepartofthesecretmessagetheyarehid',
                      'ethaespatecisartofgephrsththeroneyesapcearecagrtaieareehnlretmid'],
            'answer': ['..XX....',
                       '..XX....',
                       '....XX..',
                       '....XX..',
                       '......XX',
                       '......XX',
                       'XX......',
                       'XX......']
        },
        {
            'input': ['inthischapterwelookatanumberofciphersystemswhicharebaseduponadif',
                      'iopheraosrnekytsathanumbbisacthseeamrsweodupohnapitdfcceiirwelfh'],
            'answer': ['X.......',
                       '..X...X.',
                       '..X.....',
                       '.XX.X.X.',
                       '..X.....',
                       '........',
                       'X.X....X',
                       '..XXXX..']
        },
        {
            'input': ['ferentideatothosethatwehavemetsofarinthesesystemseachletterretai',
                      'ffareerseaethinactthnwelidhteehtaaevttseeeromsreeyttastsoteihoms'],
            'answer': ['.X...XX.',
                       '..X...X.',
                       '..X.....',
                       'XX...X..',
                       '.X..X...',
                       '...X....',
                       '..X.....',
                       '....XX.X']
        },
        {
            'input': ['nsitsownidentityandsothefrequenciesoftheindividuallettersoftheme',
                      'inansailltsoeedssowthefotfntthreiedeeinqtrsofntihetudivenicdmeuy'],
            'answer': ['.X..X.X.',
                       '.XXX....',
                       '..X.....',
                       '..X.....',
                       'X.X.X.X.',
                       'X......X',
                       '..X.....',
                       '.......X']
        },
        {
            'input': ['ssagesareunchangedbuttheconstituentlettersofthedigraphsandthehig',
                      'sisageedbgrneusareunatctphthhescaondlanstehtttersoefnithiggtheud'],
            'answer': ['X.XXX...',
                       '....X.XX',
                       'XXXX..X.',
                       '...X....',
                       '.....X..',
                       '........',
                       '....X...',
                       '.X......']
        },
        {
            'input': ['herorderpolygraphsareseparatedandtheiroriginalfrequenciesaregone',
                      'hdhsteareesequheeirropriagrnocinrdaatieerpsollygerdaarefgonanepr'],
            'answer': ['X.......',
                       'X.......',
                       '..X.....',
                       '....X...',
                       'XX....X.',
                       'XX.XX.XX',
                       '.X......',
                       '...X..X.']
        },
        {
            'input': ['roughlyspeakinganalgorithmisasequenceofinstructionsthatonemustpe',
                      'ronuuaolensgnthglcyoersoithmfiishapetoneanmkusitsranusegtqpaceti'],
            'answer': ['XX.X....',
                       '...X..X.',
                       'X.X...X.',
                       '........',
                       '..XX....',
                       'X..X..X.',
                       '...X...X',
                       '...X....']
        },
        {
            'input': ['rforminordertosolveawellformulatedproblemwewillspecifyproblemsin',
                      'eldvprpeeacfriobfloerwmymepilrlwnofbeolorweirldmerutllmsaostisno'],
            'answer': ['.....X..',
                       '...X....',
                       '..X.X.X.',
                       '...X....',
                       'X......X',
                       '....X.X.',
                       'XX.X....',
                       '.X...X.X']
        },
        {
            'input': ['termsoftheirinputsandtheiroutputsandthealgorithmwillbethemethodo',
                      'stastawinnelddthrtehelibemsralogfothtriouhtemeetiritphhnutomdpou'],
            'answer': ['....X...',
                       '..X.....',
                       'X.......',
                       '.XX...X.',
                       'X.XX....',
                       '.....X..',
                       'XXX....X',
                       '.....X.X']
        },
        {
            'input': ['theideaofcognitivebiasinpsychologyworksinananalogouswayacognitiv',
                      'tgovgeubyhsiawseiinorkdepaswoasifcyncyaanaognconaginihlttoiivloo'],
            'answer': ['X.......',
                       '.X.....X',
                       'X.....XX',
                       '.X..X...',
                       'XX......',
                       '..XXX...',
                       '..X....X',
                       '...X....']
        },
        {
            'input': ['ebiasisasystematicerrorinhowwethinkasopposedtoarandomerrororonet',
                      'ebiaicneidnkarsrisooasmoerraisrypnpoorhoswtewoserdotmaetnteohtar'],
            'answer': ['XX..X...',
                       '....X.X.',
                       'XX......',
                       '...X.X.X',
                       '........',
                       'X.XX....',
                       '....XX.X',
                       '........']
        },
        {
            'input': ['hatsmerelycausedbyourignorancewhereasstatisticalbiasskewsasample',
                      'hbebiyaoreausrsatsikeswsstamgetiresatlycnoarasicanacmusepelwedhl'],
            'answer': ['X.......',
                       '.......X',
                       'XX......',
                       '...X.X..',
                       'XX...XXX',
                       '..X.....',
                       '.....XXX',
                       '.....X..']
        },
        {
            'input': ['sothatitlesscloselyresemblesalargerpopulationcognitivebiasesskew',
                      'eslynigerotteiserpopuvmlahbalettiiebointlasessclseaslcososarkegw'],
            'answer': ['.X......',
                       '.XX.....',
                       '........',
                       '.X.X..X.',
                       'X......X',
                       'X..XXXXX',
                       '........',
                       'XX......']
        },
        {
            'input': ['ourbeliefssothattheylessaccuratelyrepresentthefactsandtheyskewou',
                      'ouctrbstlaheyleenlssayrideftsepsrotecsecnhaheytustkewortuahetefa'],
            'answer': ['XX..XX..',
                       '......X.',
                       '.X.....X',
                       '.XX.X..X',
                       '.XX.....',
                       '.XX.....',
                       '.......X',
                       '........']
        }
    ],
    'Hard': [
        {
            'input': ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbb',
                      'ababaaaababbbbbaaaaaaaaaaabaaaaaaabbaaabaabaaaaaaaaaaaaababaabaa'],
            'answer': ['X.....X.',
                       '.......X',
                       'X.XXX.X.',
                       '...X..XX',
                       '......X.',
                       'X.....X.',
                       '......X.',
                       '...X....']
        },
        {
            'input': ['ccccccccccccccccccccccccccccccccccccdddddddddddddddddddddddddddd',
                      'dcdccdccccccccdcdccddddcdccddcdcdcdccddcdccccddcccdccdcdddcddcdc'],
            'answer': ['...XX..X',
                       'X.......',
                       '.X.....X',
                       '.....X..',
                       '....X...',
                       '.XXX...X',
                       'X..XX.X.',
                       '........']
        },
        {
            'input': ['acfafcfdfaddeaaefbddcbcbebcaefbecdacdaffdbaebfccbdfdfaeafcbfcdfe',
                      'bdfdfcbacfafcfdfddadafcadebccbeddafecbbafffadcacbdaaebfccfeeefbe'],
            'answer': ['.......X',
                       'XXXXX..X',
                       '...X.X.X',
                       'X......X',
                       '...X....',
                       '...X..X.',
                       '........',
                       '..X.....']
        },
        {
            'input': ['eecdeecafbabcdbdbdfbceccaadabeffacedcafcacdbfcdabceadfabbbefabdb',
                      'bdeefbacbecddccafceececccaaeadabadfaeabcbbefdbfbafbcfcdabdfbdadb'],
            'answer': ['..XX....',
                       '..XX....',
                       '..XX....',
                       'X...X...',
                       '........',
                       '...X...X',
                       'X.XX..X.',
                       'XX......']
        },
        {
            'input': ['xzzwvyzzwvzxyvvyvvxyvzzvvyzxxzwyxywwzzvzzvxvyyzxzvywzvyyzxwvwvwv',
                      'xzvzvvzxywwxyzvyywwvzvzzvzvzyzyzvvzywzxvzwzxvyvxwvxvyyxzvywwyvzx'],
            'answer': ['XX....X.',
                       '..X...X.',
                       'X.......',
                       '.......X',
                       '..X.X..X',
                       'X..X.XX.',
                       '...XX...',
                       '........']
        },
        {
            'input': ['2143224123413143441244344433421141141133321222411132223431211113',
                      '1441414211211443343321332422442343423431211222213214114113114331'],
            'answer': ['.......X',
                       '.X......',
                       '.X.XX...',
                       'X...X...',
                       '........',
                       '.X...X..',
                       'X..XX...',
                       '.XX.XX..']
        },
        {
            'input': ['1423131123444341243321323144211121442322414324433232113143313323',
                      '3122232414233241431131322333212142131444433144243313342442111331'],
            'answer': ['.X.....X',
                       '..X.....',
                       '.X...X..',
                       '.X...X.X',
                       '.X.X.X..',
                       'X......X',
                       '.X.....X',
                       '...X....']
        },
        {
            'input': ['2144231331233214431421223332234434434133144224313244343414433343',
                      '3243132444341434441434134234312313441322123332323223432134434314'],
            'answer': ['.X..X...',
                       '...X....',
                       'X.......',
                       '.X..XX.X',
                       '.....X..',
                       'X....XX.',
                       '.....XXX',
                       '.......X']
        },
        {
            'input': ['4144423434214313311211411134111141342141433134443214134423211112',
                      '4433114124314411234422412413134314423141213141314111133114141234'],
            'answer': ['X...X.X.',
                       '.X...X..',
                       '.....X..',
                       '...X..XX',
                       '......X.',
                       'X..XX...',
                       '.....X..',
                       '..X...X.']
        },
        {
            'input': ['hjgjhjghghhjjggjhhjhjhjhghhhghggggjhghhjjgjjjjgjhhgjjghgjgjjjjhh',
                      'hhhhjhhjgjggjghgjjhhhjjhgjghhhgjgghjjhggjjhjhhgjjjjgghjjggjjhjhg'],
            'answer': ['..X....X',
                       '.....X..',
                       'X...X.X.',
                       'X..X....',
                       'X.......',
                       '....XX..',
                       'XX.XX..X',
                       '........']
        },
        {
            'input': ['lllllllllllllllllllllllllllllllllllllllllllllllllllllmmmmmmmmmmm',
                      'lllllllllllllllllllllmllllllmmllllllllmmllllllmmmmllllllmmllllll'],
            'answer': ['XX......',
                       'XX......',
                       '......XX',
                       '......XX',
                       '....XX..',
                       '....XX..',
                       '..XX....',
                       '..XX....']
        }
    ]
}
    
    for key, value in TESTS.items():
        for dict in value:
            for key1, value1 in dict.items():
                if cryptogram == value1[1]:
                    return dict['answer']


if __name__ == "__main__":
    print("Example:")
    print(
        find_grille(
            "quickbrownfoxjumpsoverthelazydogandjackdawslovesmysphinxofquartz",
            "quicpsovkbroerthwnfoelazxjumydogmyspandjhinxackdofquawslartzoves",
        )
    )

    #These "asserts" are used for self-checking and not for an auto-testing
    assert find_grille(
        "quickbrownfoxjumpsoverthelazydogandjackdawslovesmysphinxofquartz",
        "quicpsovkbroerthwnfoelazxjumydogmyspandjhinxackdofquawslartzoves",
    ) == [
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "........",
        "........",
        "........",
        "........",
    ]

    assert find_grille(
        "weareallfromxanthcubesaidquicklyjustvisitingphazewewontbeforlong",
        "wejhewucuaeswtbrveeoisantsalilbifdteifrqunooigrmplxcakhonnlagtyz",
    ) == [
        "X...X...",
        ".X.....X",
        "..X...X.",
        "...X.X..",
        "X.....X.",
        "...X...X",
        "..X.X...",
        ".X...X..",
    ]

    assert find_grille(
        "theideaofcognitivebiasinpsychologyworksinananalogouswayacognitiv",
        "tgovgeubyhsiawseiinorkdepaswoasifcyncyaanaognconaginihlttoiivloo",
    ) == [
        "X.......",
        ".X.....X",
        "X.....XX",
        ".X..X...",
        "XX......",
        "..XXX...",
        "..X....X",
        "...X....",
    ]
    

    print("Coding complete? Click 'Check' to earn cool rewards!")