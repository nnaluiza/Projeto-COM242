def read_arguments_from_file(file_path):
    with open(file_path, "r") as f:
        arguments = []
        for line in f:
            line = line.strip()
            arguments.append(line.split(","))

    return arguments
