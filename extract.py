import requests as req
import re


def src(n):
    return "https://www.sacred-texts.com/chr/apo/jasher/%d.htm" % n


def fetch_chapters(end=91, start=None):
    if start == None:
        start = end
    for i in range(start, end + 1):
        res = req.get(src(i))
        handle(res, i)


def break_lines(t: str):
    t = t.splitlines()
    t = [line.strip() for line in t]
    t = [line for line in t if len(line) > 0]
    return t


def handle(res: req.Response, n: int):
    t = res.content.decode("utf-8")
    t = break_lines(t)
    t = " ".join(t)
    t = re.sub(r"\s+", " ", t)
    t = t.replace("<P>", "\n")
    t = re.sub(r"\n+", "\n", t)
    t = re.sub(r"[0-9]+\s", "", t)
    t = break_lines(t)[1:-1]
    t = "\n".join(t)
    with open("raw/%d.txt" % n, "w") as f:
        f.write(t)


def test():
    fetch_chapters(1)
    fetch_chapters(2)
    fetch_chapters(90)
    fetch_chapters(91)


def main():
    fetch_chapters(91, start=1)

if __name__ == '__main__':
    main()