#SCOPE

rythem Game
 - 4 notes, guitar Hero style



Controls
 - 2 Preset control schemes
 - Controller Support (Maybe?)

Menus(SM)
    - SongSelect [Buttons]
        [Buttons]:
        - Select --> [Preview{state}]
        - Arrow (left, right) --> Change_Song
        - Back --> [MainMenu{state}]
        - Settings --> [Settings{state}]
        [SubStates]:
        - Preview [Buttons]
            [Buttons]:
                - Play --> [Game{SM}]
                - Back --> [SongSelect{state}]
        - Settings
            - Controls
                - Control Scheme [Arrows]
            - Video
                - Resolution [ListBox]
            - Audio
                - Master Volume [Slider]
                - SFX Volume [Slider]
                - Song Volume [Slider]
            - Gameplay
                - Background Dim [Slider]
    - Credits
    - Exit

