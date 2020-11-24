def getNum_nonMatch(x,y):
    """ Return number of non-matching bits from two binary strings """
    i = 0
    num_nonMatch = 0
    while i<len(x):
        if x[i] != y[i]:
            num_nonMatch += 1
        i += 1
    return num_nonMatch

def calc_d(x, y):
    """ Return calculated distance between two Iris Code comparisons """
    return getNum_nonMatch(x,y) / len(x)

def hex_to_bin(hex_inp):
    """ Return binary string, given a hex string input """
    bin_result = bin(int(hex_inp, 16)).zfill(8) 
    bin_result = (bin_result).split("0b")[1]
    while len(bin_result) != (len(hex_inp)*4):
        bin_result = "0" + bin_result 
    return bin_result

# Declaring each of the Iris Codes used
hex_alice   = "BE439AD598EF5147"
hex_bob     = "9C8B7A1425369584"
hex_charlie = "885522336699CCBB"
U = "C975A2132E89CEAF"
V = "DB9A8675342FEC15"
W = "A6039AD5F8CFD965"
X = "1DCA7A54273497CC"
Y = "AF8B6C7D5E3F0F9A"

# Convert each hex Iris code to binary
bin_alice   = hex_to_bin(hex_alice) 
bin_bob     = hex_to_bin(hex_bob) 
bin_charlie = hex_to_bin(hex_charlie)

# Calculate and print each of the distances for part B
d_ab = calc_d(bin_alice,bin_bob) 
d_ac = calc_d(bin_alice,bin_charlie)
d_bc = calc_d(bin_bob,bin_charlie)
print("d(Alice, Bob)     = ", d_ab)
print("d(Alice, Charlie) = ", d_ac)
print("d(Bob, Charlie)   = ", d_bc)

# Iterate through the known and unknown users and compare to find which pairs match closely.
known_users   = [bin_alice, bin_bob, bin_charlie]
unknown_users = [U, V, W, X, Y]

for j,unknown in enumerate(unknown_users):
    print()
    for k,user in enumerate(known_users):
        print("Unknown#{}, with index {}: ".format(j,k), calc_d(user, hex_to_bin(unknown)))
