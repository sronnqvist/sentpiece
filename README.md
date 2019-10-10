# sentencepiece wrapper

Train sentence piece model: `python train.py corpus.txt 8000` (specify input file and vocab size)

Convert from sentence to pieces: `python s2p.py input.txt > input.txt.pcs`

Convert from pieces to sentences: `python p2s.py output.txt.pcs > output.txt`
