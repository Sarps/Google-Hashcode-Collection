from Filer import Loader, Writer


def process(filename) :
    data = Loader("files/" + filename)
    out = Writer("out/" + filename)

    seen = set()

    A = data.L

    days = list(map(
        lambda k: (k[0][2]*k[0][1]) / k[0][0],
        data.K
    ))

    result = []

    for x in range(len(data.K)):
        b = [y for y in data.K[x][1] if y not in seen]
        if len(b) > 0:
            result.append([ [x, len(b)], b ])
        seen.update(data.K[x][1])

    result = [z for _, z in sorted(zip(days, result), reverse=False)]

    out.writeLine(str(A))
    for r in result:
        out.writeMatrix(r)

    out.close()


if __name__ == '__main__':

    filenames = [
        "a_example.txt",
        "b_read_on.txt",
        "c_incunabula.txt",
        "d_tough_choices.txt",
        "e_so_many_books.txt",
        "f_libraries_of_the_world.txt"
    ]

    for filename in filenames:
        process(filename)



