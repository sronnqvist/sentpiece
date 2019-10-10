import sentencepiece as spm
import sys

if len(sys) != 3:
	print("Usage: %s <input corpus> <vocab size>" % sys.argv[0])
	sys.exit()

spm.SentencePieceTrainer.Train("--input=%s --model_prefix=m --vocab_size=%s" % (sys.argv[1], sys.argv[2]))


