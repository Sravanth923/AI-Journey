from utils import clean_text

def run():
    sample = "  Hello Sravanth!  "
    cleaned = clean_text(sample)
    print(f"Cleaned Text: {cleaned}")

if __name__ == "__main__":
    run()
