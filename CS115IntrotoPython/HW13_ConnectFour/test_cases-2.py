from hw13 import *

sequences = {
    'v_X': '0101010',
    'v_O': '21010101',
    'pos_d_X': '01123223433',
    'pos_d_O': '1021223333',
    'neg_d_X': '32201110400',
    'neg_d_O': '0311010022',
    'hor_X': '0011223',
    'hor_O': '40514253'
}

count = 0
passed = 0

for seq in sequences.keys():
	b = Board()
	b.setBoard(sequences[seq])

	if count % 2 == 0 and b.winsFor("X") or count % 2 == 1 and b.winsFor("O"):
		print ("Passed")
		passed += 1
	else:
		print ("Failed")

	count += 1

	print (seq + ":")
	print (b)
	print ()

print ("Passed " + str(passed) + "/8")
