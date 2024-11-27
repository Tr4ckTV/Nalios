def Html(matrices):
    html = "<html><body>"
    for i, matrix in enumerate(matrices):
        html += f"<h3>Iteration {i+1}</h3>"
        html += "<table border='0.5'>"
        for row in matrix:
            html += "<tr>"
            for case in row:
                color = "black" if case == 1 else "white"
                html += f"<td style='width: 20px; height: 20px; background-color: {color};'></td>"
            html += "</tr>"
        html += "</table><br>"
    html += "</body></html>"
    return html

def Game(matrix):
    def voison(x, y):
        voisin = [(-1, -1), (-1, 0), (-1, 1),
                     (0, -1), (0, 1),
                     (1, -1), (1, 0), (1, 1)]
        a = 0
        for dx, dy in voisin:
            bx, by = x + dx, y + dy
            if 0 <= bx < len(matrix) and 0 <= by < len(matrix[0]):
                a += matrix[bx][by]
        return a

    def next(x, y):
        voisinVie = voison(x, y)
        if matrix[x][y] == 1:
            return 1 if voisinVie in [2, 3] else 0
        else:
            return 1 if voisinVie == 3 else 0
    
    matrices = [matrix]

    for _ in range(5):
        new_matrix = []
        for i in range(len(matrix)):
            new_row = []
            for j in range(len(matrix[0])):
                new_row.append(next(i, j))
            new_matrix.append(new_row)
        matrix = new_matrix
        matrices.append(matrix)

    return matrices

matrix = [
    [0, 1, 0, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

html = Html(Game(matrix))

with open("Game.html", "w") as file:
    file.write(html)