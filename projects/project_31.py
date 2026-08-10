
sample_cube = [
    [
        [5, 5, 5],
        [5, 5, 5],
        [5, 5, 5]
    ],
    [
        [5, 5, 5],
        [5, 5, 5],
        [5, 5, 5]
    ],
    [
        [5, 5, 5],
        [5, 5, 5],
        [5, 5, 5]
    ]
]

def coloring(cube: list[list[list[int]]]) -> None:
    for index1, i in enumerate(cube):
        for index2, j in enumerate(cube[index1]):
            for index3, k in enumerate(cube[index1][index2]):
                if index1 == 0 or index1 == (len(cube)-1) or index2 == 0 or index2 == (len(cube[index1])-1) or index3 == 0 or index3 == (len(cube[index1][index2])-1):
                    cube[index1][index2][index3] = 1
                else:
                    cube[index1][index2][index3] = 0

coloring(sample_cube)


for i in range(len(sample_cube)):
    print(f"Layer {i + 1}:")
    for plane in sample_cube[i]:
        for element in plane:
            print(element, end=' ')
        print()