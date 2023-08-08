import musicalbeeps as MB
note_strs_list = list(input())
player = MB.Player(volume = 0.5)
for c in note_strs_list:
    player.play_note(c, 1.0)
