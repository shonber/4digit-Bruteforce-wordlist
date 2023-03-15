def main(file_name: str):
    with open(file_name, "w") as fw:
        for i in range(10001):
            fw.write(f"{i}\n")


if __name__ == "__main__":
    main("wordlist.txt")
