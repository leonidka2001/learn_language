def get_terms_for_table():
    terms = []
    with open("./data/terms.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            term, definition, source = line.split(";")
            terms.append([cnt, term, definition])
            cnt += 1
    return terms

def get_lesson_for_table():
    lessons = []
    with open("./data/lessons.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            term, definition, source = line.split(";")
            lessons.append([cnt, term, definition])
            cnt += 1
    return lessons


def write_term(new_term, new_definition):
    new_term_line = f"{new_term};{new_definition};user"
    with open("./data/terms.csv", "r", encoding="utf-8") as f:
        existing_terms = [l.strip("\n") for l in f.readlines()]
        title = existing_terms[0]
        old_terms = existing_terms[1:]
    terms_sorted = old_terms + [new_term_line]
    terms_sorted.sort()
    new_terms = [title] + terms_sorted
    with open("./data/terms.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_terms))


def write_lesson(new_term, new_definition):
    new_lesson_line = f"{new_term};{new_definition};user"
    with open("./data/lessons.csv", "r", encoding="utf-8") as f:
        existing_terms = [l.strip("\n") for l in f.readlines()]
        title = existing_terms[0]
        old_terms = existing_terms[1:]
    terms_sorted = old_terms + [new_lesson_line]
    terms_sorted.sort()
    new_terms = [title] + terms_sorted
    with open("./data/lessons.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_terms))

