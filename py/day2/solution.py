def parse(path):
    with (open(path, "r")) as file:
        return [int(n) for n in file.read().split(",")]

def exec(noun, verb, sequence):
    ops = (None, lambda x,y: x+y, lambda x,y: x*y)
    seq = [x for x in sequence]
    seq[1], seq[2] = noun, verb
    for pos in range(0, len(seq), 4):
        op, a, b, r = seq[pos:pos+4]
        if op == 99:
            break
        seq[r] = ops[op](seq[a], seq[b])
    return seq[0]

def pair_giving_output(sought_output, seq):
    all_pairs = [(i,j) for i in range(100) for j in range(0,100)]
    for (noun, verb) in all_pairs:
        if exec(noun, verb, seq) == sought_output:
            return (noun, verb)

if __name__ == "__main__":
    seq = parse("input")
    answer_one = exec(12, 2, seq)
    print("a) " + str(answer_one))

    noun, verb = pair_giving_output(19690720, seq)
    answer_two = 100*noun +verb
    print("b) " + str(answer_two))