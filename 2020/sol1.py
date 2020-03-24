from Filer import Loader, Writer


def process(filename) :
    data = Loader("files/" + filename)
    out = Writer("out/" + filename)

    A = data.L

    result = list(map(
        lambda x: [[x, data.K[x][0][0]], data.K[x][1]],
        range(len(data.K))
    ))

    out.writeLine(str(A))
    for r in result:
        out.writeMatrix(r)

    out.close()


if __name__ == '__main__':

    filenames = [
        "a_example.txt",
        # "b_read_on.txt",
        # "c_incunabula.txt",
        # "d_tough_choices.txt",
        # "e_so_many_books.txt",
        # "f_libraries_of_the_world.txt"
    ]

    for filename in filenames:
        process(filename)



