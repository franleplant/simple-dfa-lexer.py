ACCEPTED = "ACCEPTED"
NOT_ACCEPTED = "NOT_ACCEPTED"
TRAPPED = "TRAPPED"


def a_id(lexeme):
    state = 0
    accepted = [1]
    for c in lexeme:
        if state == 0 and c.isalpha():
            state = 1
        elif state == 1 and c.isalpha():
            state = 1
        else:
            state = -1
            break

    if state == -1:
        return TRAPPED

    if state in accepted:
        return ACCEPTED
    else:
        return NOT_ACCEPTED


TOKEN_CONF = [
    ("ID", a_id),
]


# TODO integrate with the other code that has more infra like tests and line and col handling
# TODO test

def lex(src):

    tokens = []
    index = 0
    while index < len(src):
        while src[index].isspace():
            if src[index] == '\n':
                print("new line")
            index += 1


        start = index
        candidates = []
        next_candidates = []
        lexeme = ""
        all_trapped = False

        while not all_trapped:
            all_trapped = True
            lexeme = src[start:index + 1]
            candidates = next_candidates
            next_candidates = []

            for (token_type, afd) in TOKEN_CONF:
                res = afd(lexeme)
                if res == ACCEPTED:
                    next_candidates.append(token_type)
                    all_trapped = False
                elif res == NOT_ACCEPTED:
                    all_trapped = False

            print((lexeme, candidates))
            index += 1

        if len(candidates) == 0:
            print(("tokens", tokens))
            raise Exception("UNKNOWN TOKEN " + lexeme)

        token_type = candidates[0]
        token = (token_type, lexeme)
        tokens.append(token)


    return tokens




print(lex("asdjkh ="))
