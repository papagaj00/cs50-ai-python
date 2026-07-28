from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
ASays = And(AKnight, AKnave)

knowledge0 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    #either knight and true, or knave and false
    Or(And(ASays, AKnight), And(Not(ASays), AKnave))
)

# Puzzle 1
# A says "We are both knaves."
ASays = And(AKnave, BKnave)
# B says nothing.
knowledge1 = And(
    #basic
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),

    #either knight and true, or knave and false
    Or(And(ASays, AKnight), And(Not(ASays), AKnave)),
    #Or(And(BSays, BKnight), And(Not(BSays), BKnave))
)

# Puzzle 2
# A says "We are the same kind."
ASays = Or(And(AKnight, BKnight), And(AKnave, BKnave))
# B says "We are of different kinds."
BSays = Not(ASays)
knowledge2 = And(
    #basic
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),

    #either knight and true, or knave and false
    Or(And(ASays, AKnight), And(Not(ASays), AKnave)),
    Or(And(BSays, BKnight), And(Not(BSays), BKnave))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
ASaidKnight = Symbol("A said -I am a knight-")
ASaidKnave = Symbol("A said -I am a knave-")
# B says "A said 'I am a knave'."
BSays1 = ASaidKnave
# B says "C is a knave."
BSays2 = CKnave
# C says "A is a knight."
CSays = AKnight
# Puzzle 3

knowledge3 = And(
    # basic rules
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),

    Or(ASaidKnight, ASaidKnave),
    Biconditional(AKnight, ASaidKnight),
    Not(ASaidKnave),
    Biconditional(BKnight, And(BSays1, BSays2)),
    Biconditional(CKnight, CSays)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
