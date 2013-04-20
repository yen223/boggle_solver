from collections import defaultdict

def neighbours(x,y):
    for dx in [-1,0,1]:
        for dy in [-1, 0, 1]:
            if not (dx == dy == 0):
                yield (x+dx, y+dy)

def substring_in_word(substring,valid_words):
    for word in valid_words:
        if substring in word:
            return True
    return False

def solve(valid_words, grid, current_node, substring, path):
    print "Substring:", substring
    print "Path:", path
    letter = grid[current_node]
    if letter == ".": return None
    if letter == "Q":
        letter = "QU"
    substring += letter

    if len(substring) == 17 and substring in valid_words:
        return substring, path
    if not substring_in_word(substring, valid_words):
        return None
    for next_node in neighbours(*current_node):
        if next_node not in path:
            path.append(next_node)
            result = solve(valid_words, grid, next_node,substring, path)
            if result: 
                return result
            else:
                path.pop()

def main():
    valid_words = []
    with open("/usr/share/dict/words") as f:
        for line in f:
            word = line.strip()
            if len(word) == 17:
                print word
                valid_words.append(word.upper())
    tempgrid = ["BOGGLES..TENODD",
            "ATHEART.FOREVER",
            "LOOKSEE.TRADETO",
            "SOUK..MBE..BRAS",
            "ALLOWS.ENURESIS",
            "MES.HARE.NEATLY",
            "...CASABONITA..",
            "..CATHY.PETTY..",
            "..ARNIESARMY...",
            "RANDOM.ALVA.TLC",
            "ENTITIES.ENTAIL",
            "QOIN..SHY..WINO",
            "ENCARTA.UNCOCKS",
            "SYLLABI.RALPHIE",
            "TMESIS..THEMIND"]
    grid = defaultdict(lambda:".")
    for x in range(len(tempgrid[0])):
        for y in range(len(tempgrid)):
            grid[(x,y)] = tempgrid[x][y]
    for x in range(len(tempgrid[0])):
        solution_found = False
        for y in range(len(tempgrid)):
            solution = solve(valid_words, grid, (x,y), '', [(x,y)])
            if solution:
                print "Word found:", solution[0]
                print "Path:", solution[1]
                solution_found = True
                break
        if solution_found: break

if __name__ == "__main__":
    main()

