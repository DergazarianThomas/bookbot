def word_count(book):
    words = book.split()
    return len(words)

def char_count(book):
    chars = {}
    for c in book:
        c = c.lower()
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def sorted_list(chars):
    report = []
    for key, value in chars.items():
        report.append({"char":key,"num":value})
    report.sort(key=lambda x: x["num"], reverse=True)
    return report

def print_report(report):
    for item in report:
        print(f"{item['char']}: {item['num']}")
