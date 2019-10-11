#!/usr/bin/python

import sentencepiece as spm
import sys

sp = spm.SentencePieceProcessor()
if len(sys.argv) > 2:
	sp.Load(sys.argv[2])
else:
	sp.Load("m.model")

for line in open(sys.argv[1]):
	print (sp.DecodePieces(line.strip('\n').split()))

