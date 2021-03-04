import numpy as np

id_2_key = ["A","B","C","D","E","F","G",]
appendix_list = ["", "m", "M7", "Mm7", "m7", "add9", "6"]

def random_code_generate(n_chords: int):
    indexes = np.random.randint(1, 7, size=(n_chords))
    
    bass_keys = [id_2_key[myid] for myid in indexes]
    appendixes = np.random.choice(appendix_list,(n_chords))

    output_chords = [bass_keys[i] + appendixes[i]
        for i in range(n_chords)]

    return output_chords

if __name__ == "__main__":
    random_code_generate(100)
