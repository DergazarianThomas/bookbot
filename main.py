import sys
from stats import word_count
from stats import char_count
from stats import sorted_list
from stats import print_report

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
input_book = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
    return book

def main():

        
    
    book = get_book_text(input_book)
    
    count = char_count(book)
    
    sort_list = sorted_list(count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {input_book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book)} total words")
    print("--------- Character Count -------")
    print_report(sort_list)
    print("============= END ===============")

main()
