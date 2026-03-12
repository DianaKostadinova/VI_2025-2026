def minesweeper(matrix):
    n = len(matrix)
    nasoki = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1), (0, 1),
              (1, -1), (1, 0), (1, 1)]
    rezultat = [
        [
            '#' if matrix[i][j] == '#'
            else sum(
                1 for dx, dy in nasoki
                if 0 <= i + dx < n and 0 <= j + dy < n and matrix[i + dx][j + dy] == '#'
            )
            for j in range(n)
        ]
        for i in range(n)
    ]

    return rezultat
if __name__ == "__main__":
    n=int(input())
    matrix = [input().split() for _ in range(n)]
    rez=minesweeper(matrix)
    for i in rez:
        print("   ".join(map(str, i)))
