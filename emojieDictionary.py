def replaceEmojis(input_string):
    """
    Replaces emoji codes in the input string with actual emojis.
    """
    emoji_dict = {
        'u2764ufe0f': '❤️',
        'ud83dude02': '😂',
        'ud83dude0a': '😊',
        'ud83dude0d': '😍',
        'ud83dude14': '😔',
        'ud83dude0c': '😌',
        'ud83dude01': '😁',
        'ud83dude0f': '😏',
        'ud83dude2d': '😭',
        'ud83dude29': '😩',
        'ud83dude2a': '😪',
        'ud83dude22': '😢',
        'ud83dude2c': '😬',
        'ud83dude21': '😡',
        'ud83dude20': '😠',
        'ud83dude30': '🌀',
        'ud83dude31': '🌧️',
        'ud83cudf08': '🌈',
        'ud83dude37': '😷',
        'ud83dude33': '🌷',
        'ud83dude32': '🌲',
        'ud83dude23': '😣',
        'ud83dude25': '😥',
        'ud83dude13': '😓',
        'ud83dude10': '😐',
        'ud83dude11': '😑',
        'ud83dude15': '😕',
        'ud83dude12': '😖',
        'ud83dude3b': '😻',
        'ud83dude09': '😉',
        'ud83dude2b': '😫',
        'ud83dude03': '😃',
        'ud83dude1c': '😜',
        'ud83dude18': '😘',
        'ud83dude17': '😗',
        'ud83dude19': '😙',
        'ud83dude1d': '😝',
        'ud83dude24': '😤',
        'ud83dude16': '😖',
        'ud83dude0b': '😋',
        'ud83dude05': '😅',
        'ud83dude1e': '😞',
        'ud83dude0e': '😎',
        'ud83dude2f': '😯',
        'ud83dude21': '😡',
        'ud83dude26': '😦',
        'ud83dude28': '😨',
        'ud83dude27': '😧',
        'ud83dude2e': '😮',
        'ud83dude35': '😵',
        'ud83dude08': '😈',
        'ud83dude07': '😇',
        'ud83dude06': '😆',
        'ud83dude1a': '😚',
        'ud83dude0c': '😌',
        'ud83dude0f': '😏',
        'ud83dude31': '🌧️',
        'ud83dude34': '😴',
        'ud83cudf89': '🎉',
        'ud83dude4c': '👌',
        'ud83dude4f': '👏',
        'ud83dude46': '👆',
        'ud83dude45': '👅',
        'ud83dude4e': '👎',
        'ud83dude47': '👇',
        'ud83dude4d': '👍',
        'ud83dude4a': '👊',
        'ud83dude48': '👈',
        'ud83dude49': '👉',
        'ud83dude4b': '👋',
        'ud83dude4c': '👌',
        'ud83dude50': '👐',
        'ud83dude51': '👑',
        'ud83dude52': '👒',
        'ud83dude54': '👔',
        'ud83dude53': '👓',
        'ud83dude55': '👕',
        'ud83dude56': '👖',
        'ud83dude57': '👗',
        'ud83dude58': '👘',
        'ud83dude59': '👙',
        'ud83dude5a': '👚',
        'ud83dude5b': '👛',
        'ud83dude5c': '👜',
        'ud83dude5d': '👝',
        'ud83dude5e': '👞',
        'ud83dude5f': '👟',
        'ud83dude60': '👠',
        'ud83dude61': '👡',
        'ud83dude62': '👢',
        'ud83dude63': '👣',
        'ud83dude64': '👤',
        'ud83dude65': '👥',
        'ud83dude66': '👦',
        'ud83dude67': '👧',
        'ud83dude68': '👨',
        'ud83dude69': '👩',
        'ud83dude6a': '👪',
        'ud83dude6b': '👫',
        'ud83dude6c': '👬',
        'ud83dude6d': '👭',
        'ud83dude6e': '👮',
        'ud83dude6f': '👯',
        'ud83dude70': '👰',
        'ud83dude71': '👱',
        'ud83dude72': '👲',
        'ud83dude73': '👳',
        'ud83dude74': '👴',
        'ud83dude75': '👵',
        'ud83dude76': '👶',
        'ud83dude77': '👷',
        'ud83dude78': '👸',
        'ud83dude79': '👹',
        'ud83dude7a': '👺',
        'ud83dude7b': '👻',
        'ud83dude7c': '👼',
        'ud83dude7d': '👽',
        'ud83dude7e': '👾',
        'ud83dude7f': '👿',
        'ud83dude81': '💁',
        'ud83dude82': '💂',
        'ud83dude83': '💃',
        'ud83dude84': '💄',
        'ud83dude85': '💅',
        'ud83dude86': '💆',
        'ud83dude87': '💇',
        'ud83dude88': '💈',
        'ud83dude89': '💉',
        'ud83dude8a': '💊',
        'ud83dude8b': '💋',
        'ud83dude8c': '💌',
        'ud83dude8d': '💍',
        'ud83dude8e': '💎',
        'ud83dude8f': '💏',
        'ud83dude90': '💐',
        'ud83dude91': '💑',
        'ud83dude92': '💒',
        'ud83dude93': '💓',
        'ud83dude94': '💔',
        'ud83dude95': '💕',
        'ud83dude96': '💖',
        'ud83dude97': '💗',
        'ud83dude98': '💘',
        'ud83dude99': '💙',
        'ud83dude9a': '💚',
        'ud83dude9b': '💛',
        'ud83dude9c': '💜',
        'ud83dude9d': '💝',
        'ud83dude9e': '💞',
        'ud83dude9f': '💟',
        'ud83dudea0': '💠',
        'ud83dudea1': '💡',
        'ud83dudea2': '💢',
        'ud83dudea3': '💣',
        'ud83dudea4': '💤',
        'ud83dudea6': '💦',
        'ud83dudea7': '💧',
        'ud83dudea8': '💨',
        'ud83dudea9': '💩',
        'ud83dudeaa': '💪',
        'ud83dudeab': '💫',
        'ud83dudeac': '💬',
        'ud83dudead': '💭',
        'ud83dudeae': '💮',
        'ud83dudeaf': '💯',
        'ud83dudeb0': '💰',
        'ud83dudeb1': '💱',
        'ud83dudeb2': '💲',
        'ud83dudeb3': '💳',
        'ud83dudeb4': '💴',
        'ud83dudeb5': '💵',
        'ud83dudeb6': '💶',
        'ud83dudeb7': '💷',
        'ud83dudeb8': '💸',
        'ud83dudeb9': '💹',
        'ud83dudeba': '💺',
        'ud83dudebb': '💻',
        'ud83dudebc': '💼',
        'ud83dudebd': '💽',
        'ud83dudebe': '💾',
        'ud83dudebf': '💿',
        'ud83dudec0': '📀',
        'ud83dudec1': '📁',
        'ud83dudec2': '📂',
        'ud83dudec3': '📃',
        'ud83dudec4': '📄',
        'ud83dudec5': '📅',
        'ud83dudec6': '📆',
        'ud83dudec7': '📇',
        'ud83dudec8': '📈',
        'ud83dudec9': '📉',
        'ud83dudeca': '📊',
        'ud83dudecb': '📋',
        'ud83dudecc': '📌',
        'ud83dudecd': '📍',
        'ud83dudece': '📎',
        'ud83dudecf': '📏',
        'ud83duded0': '📐',
        'ud83duded1': '📑',
        'ud83duded2': '📒',
        'ud83duded3': '📓',
        'ud83duded4': '📔',
        'ud83duded5': '📕',
        'ud83duded6': '📖',
        'ud83duded7': '📗',
        'ud83duded8': '📘',
        'ud83duded9': '📙',
        'ud83dudeda': '📚',
        'ud83dudedb': '📛',
        'ud83dudedc': '📜',
        'ud83dudedd': '📝',
        'ud83dudede': '📞',
        'ud83dudedf': '📟',
        'ud83dudca8': '💨',  # Wind Blowing Face
        'ud83dudca7': '💧',  # Droplet
        'ud83dudca6': '💦',  # Sweat Droplets
        'ud83dudcaa': '💪',  # Flexed Biceps
        'ud83dudca5': '💥',  # Collision
        'ud83dudca3': '💣',  # Bomb
        'ud83dudca2': '💢',  # Anger Symbol
        'ud83dudca4': '💤',  # Zzz
        'ud83dudc8a': '🎊',  # Confetti Ball
        'ud83dudc8b': '🎋',  # Tanabata Tree
        'ud83dudc8c': '🎌',  # Crossed Flags
        'ud83dudc8d': '🎍',  # Pine Decoration
        'ud83dudc8e': '🎎',  # Japanese Dolls
        'ud83dudc8f': '🎏',  # Carp Streamer
        'ud83dudc90': '🎐',  # Wind Chime
        'ud83dudc91': '🎑',  # Moon Viewing Ceremony
        'ud83dudc92': '🎒',  # School Satchel
        'ud83dudc93': '🎓',  # Graduation Cap
        'ud83dudc94': '🎔',  # Heart With Tip On The Left
        'ud83dudc95': '🎕',  # Bouquet of Flowers
        'ud83dudc96': '🎖️',  # Military Medal
        'ud83dudc97': '🎗️',  # Reminder Ribbon
        'ud83dudc98': '🎘',  # Musical Keyboard
        'ud83dudc99': '🎙️',  # Studio Microphone
        'ud83dudc9a': '🎚️',  # Level Slider
        'ud83dudc9b': '🎛️',  # Control Knobs
        'ud83dudc9c': '🎜',  # Film Frames
        'ud83dudc9d': '🎝',  # Admission Tickets
        'ud83dudc9e': '🎞️',  # Film Projector
        'ud83dudc9f': '🎟️',  # Ticket
        'ud83dudca0': '🎠',  # Carousel Horse
        'ud83dudca1': '🎡',  # Ferris Wheel
        'ud83dudca2': '🎢',  # Roller Coaster
        'ud83dudca3': '🎣',  # Fishing Pole
        'ud83dudca4': '🎤',  # Microphone
        'ud83dudca5': '🎥',  # Movie Camera
        'ud83dudca6': '🎦',  # Cinema
        'ud83dudca7': '🎧',  # Headphone
        'ud83dudca8': '🎨',  # Artist Palette
        'ud83dudca9': '🎩',  # Top Hat
        'ud83dudcaa': '🎪',  # Circus Tent
        'ud83dudcab': '🎫',  # Ticket
        'ud83dudcac': '🎬',  # Clapper Board
        'ud83dudcad': '🎭',  # Performing Arts
        'ud83dudcae': '🎮',  # Video Game
        'ud83dudcaf': '🎯',  # Direct Hit
        'ud83dudcb0': '🎰',  # Slot Machine
        'ud83dudcb1': '🎱',  # Billiards
        'ud83dudcb2': '🎲',  # Game Die
        'ud83dudcb3': '🎳',  # Bowling
        'ud83dudcb4': '🎴',  # Flower Playing Cards
        'ud83dudcb5': '🎵',  # Musical Note
        'ud83dudcb6': '🎶',  # Musical Notes
        'ud83dudcb7': '🎷',  # Saxophone
        'ud83dudcb8': '🎸',  # Guitar
        'ud83dudcb9': '🎹',  # Musical Keyboard
        'ud83dudcba': '🎺',  # Trumpet
        'ud83dudcbb': '🎻',  # Violin
        'ud83dudcbc': '🎼',  # Musical Score
        'ud83dudcbd': '🎽',  # Running Shirt
        'ud83dudcbe': '🎾',  # Tennis Racquet
        'ud83dudcbf': '🎿',  # Ski and Ski Boot
        'ud83dudcc0': '🏀',  # Basketball and Hoop
        'ud83dudcc1': '🏁',  # Chequered Flag
        'ud83dudcc2': '🏂',  # Snowboarder
        'ud83dudcc3': '🏃',  # Runner
        'ud83dudcc4': '🏄',  # Surfer
        'ud83dudcc5': '🏅',  # Sports Medal
        'ud83dudcc6': '🏆',  # Trophy
        'ud83dudcc7': '🏇',  # Horse Racing
        'ud83dudcc8': '🏈',  # American Football
        'ud83dudcc9': '🏉',  # Rugby Football
        'ud83dudcca': '🏊',  # Swimmer
        'ud83dudccb': '🏋️',  # Weight Lifter
        'ud83dudccc': '🏌️',  # Golfer
        'ud83dudccd': '🏍️',  # Racing Motorcycle
        'ud83dudcce': '🏎️',  # Racing Car
        'ud83dudccf': '🏏',  # Cricket
        'ud83dudccf': '🔥',  # fire
        'ud83eudef6': '🛶',  #Canoe
        'ud83dudcf7': '📷',  # Camera
        'ud83dudc47': '👇',  # Backhand Index Pointing Down
        'ud83dudc49': '👉',  # Backhand Index Pointing Right
        'ud83dudce5': '📍',  # Round Pushpin
        'ud83eudd23': '🤣',  # Rolling on the Floor Laughing
        'ud83dudd25': '💥',  # Collision
        'ud83euddd1u200d': '🧑‍', #winking
        'ud83dude80': '🚀',  # Rocket
        'ud83dudc47': '👇',  # Backhand Index Pointing Down
        'ud83euddd1': '🧑‍🚀',  # Astronaut
        'ud83dudcf2': '📲',  # Mobile Phone with Arrow
        'u2b07ufe0f': '⬇️',  # Down Arrow
        'u2022':      '•',   # Bullet Point
        'u2019':      '’',   # Right Single Quotation Mark
        'u26a0': '⚠️',  # Warning Sign
        'u00a9': '©',  # Copyright Sign
        'u274c': '❌',  # Cross Mark
        'u27a1ufe0f': '➡️',  # Right Arrow

        'ud83dude00': '😀',  # Grinning Face
        'ud83dude04': '😄',  # Smiling Face with Open Mouth and Smiling Eyes
        'ud83dude42': '😂',  # Face with Tears of Joy
        'ud83dude43': '😃',  # Smiling Face with Open Mouth
        'ud83eudee0': '📰',  # Rolled-Up Newspaper
        'ud83eudee3': '📣',  # Megaphone
        'ud83eudee2': '📢',  # Loudspeaker
        'ud83eudee1': '📡',  # Satellite Antenna
        'ud83eude00': '📀',  # DVD
        'ud83dude2a': '🌀',  # Cyclone
        'u263aufe0f': '⚓',  # Anchor
        'ud83dude11': '😔',  # Pensive Face
        'ud83dude17': '😗',  # Kissing Face
        'ud83eudee2': '📢',  # Loudspeaker
        'ud83eudee3': '📣',  # Megaphone
        'ud83eudee1': '📡',  # Satellite Antenna
        'ud83eude10': '📐',  # Triangular Ruler
        'ud83eudd28': '😨',  # Fearful Face
        'ud83eudee8': '📨',  # Incoming Envelope
        'ud83eudee5': '📥',  # Inbox Tray
        'ud83eudee6': '📦',  # Package
        'ud83dude36': '😶',  # Face Without Mouth
        'ud83dude37': '😷',  # Face with Medical Mask
        'ud83dude38': '😸',  # Grinning Cat with Smiling Eyes
        'ud83dude39': '😹',  # Cat with Tears of Joy
        'ud83dude3a': '😺',  # Smiling Cat with Heart-Eyes
        'ud83dude3b': '😻',  # Cat with Wry Smile
        'ud83dude3c': '😼',  # Kissing Cat
        'ud83dude3d': '😽',  # Pouting Cat
        'ud83dude3e': '😾',  # Crying Cat
        'ud83dude3f': '😿',  # Weary Cat
        'ud83dude40': '🙀',  # Cat with Open Mouth
        'ud83eude8': '📨',  # Incoming Envelope
        'ud83eudee8': '📨',  # Incoming Envelope (duplicate entry)
        'ud83eudd23': '📣',  # Megaphone
        'ud83eudee8': '📨',  # Incoming Envelope (duplicate entry)
        'ud83eudee5': '📥',  # Inbox Tray
        'ud83eudee6': '📦',  # Package
        'ud83eudee2': '📢',  # Loudspeaker
        'ud83eudee3': '📣',  # Megaphone
        'ud83eudee1': '📡',  # Satellite Antenna
        'ud83eudd22': '📢',  # Loudspeaker (duplicate entry)
        'ud83eudd2e': '📦',  # Package (duplicate entry)
        'ud83eudd27': '📨',  # Incoming Envelope (duplicate entry)
        'ud83eudd75': '📣',  # Megaphone (duplicate entry)
        'ud83eudd76': '📦',  # Package (duplicate entry)
        'ud83eudd74': '📨',  # Incoming Envelope (duplicate entry)
        'ud83eudd2f': '🚯',  # No Littering Symbol
        'ud83eudd20': '🚠',  # Mountain Cableway
        'ud83eudd73': '🛳️',  # Passenger Ship
        'ud83eudd78': '🛸',  # Flying Saucer
        'ud83dude80': '💀',  # Skull
        'ud83eudee4': '📤',  # Outbox Tray
        'ud83dude1f': '📟',  # Pager
        'ud83dude41': '🕁',  # Empty Document
        'u2639ufe0f': '☹️',  # White Frowning Face
        'ud83dude80': '💀',  # Skull (duplicate entry)
        'ud83eudee4': '📤',  # Outbox Tray (duplicate entry)
        'ud83dude1f': '📟',  # Pager (duplicate entry)
        'ud83dude41': '🕁',  # Empty Document (duplicate entry)
        'u2639ufe0f': '☹️',  # White Frowning Face (duplicate entry)
        'ud83dude44': '💄',  # Lipstick
        'ud83eudea2': '🛢️',  # Oil Drum
        'ud83dudeac': '💬',  # Speech Balloon
        'ud83eudd79': '🛹',  # Skateboard
        'ud83eude83': '📃',  # Page with Curl
        'ud83eude75': '📵',  # No Mobile Phones
        'ud83eude76': '📶',  # Antenna Bars
        'ud83eude8e': '📎',  # Paperclip
        'ud83eudeec': '🗬',  # Triangle Ruler
        'ud83eudeed': '🗭',  # Protractor
        'ud83eudeeb': '🗫',  # Label
        'ud83eudee0': '🗠',  # Straight Ruler
        'ud83eudee1': '🗡️',  # Dagger
        'ud83eudd10': '🌐',  # Globe with Meridians
        'ud83eudd28': '🌨',  # Cloud with Tornado
        'ud83eudd11': '🌑',  # New Moon
        'ud83eudee2': '🗢',  # Card Index Dividers
        'ud83eudee3': '🗣️',  # Speaking Head
        'ud83eudee2': '🗢',  # Card Index Dividers (duplicate entry)
        'ud83eudee3': '🗣️',  # Speaking Head (duplicate entry)
        'ud83eudee1': '🗡️',  # Dagger (duplicate entry)
        'ud83eudd10': '🌐',  # Globe with Meridians (duplicate entry)
        'ud83eudd36': '🌶️',  # Hot Pepper
        'ud83eudee5': '🗥',  # Paper Tray
        'ud83dude80': '💀',  # Skull (duplicate entry)
        'ud83eudd2f': '🚯',  # No Littering Symbol (duplicate entry)
        'ud83eudd20': '🚠',  # Mountain Cableway (duplicate entry)
        'ud83eudd73': '🛳️',  # Passenger Ship (duplicate entry)
        'ud83eudd78': '🛸',  # Flying Saucer (duplicate entry)
        'ud83dude80': '💀',  # Skull (duplicate entry)
        'ud83eudea2': '🛢️',  # Oil Drum (duplicate entry)
        'ud83dude44': '💄',  # Lipstick (duplicate entry)
        'ud83eudd25': '📥',  # Inbox Tray
        'u200d': '',
    }
    for code, emoji_char in emoji_dict.items():
        input_string = input_string.replace(code, emoji_char)

    return input_string