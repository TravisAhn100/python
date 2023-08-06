import musicalbeeps    as Mb
import multiprocessing as mp
import time

p = Mb.Player(volume = 0.5)

def play_notes(notes_list):
        print(notes_list)
        processes_list = []
        for (i, note) in enumerate(notes_list):
                if note == '_':
                        time.sleep(0.5)
                else:
                        if note.islower():
                                note += "5"
                        t = mp.Process(target = p.play_note,\
                                         args = (note, 1.5))
                        t.start()
                        processes_list += [t]
        for process in processes_list:
                process.join()

if __name__ == "__main__":
        while True:
                chords_strs  = input("> ").split()
                for chord in chords_strs:
                        play_notes(chord)
