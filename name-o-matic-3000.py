#!/usr/bin/env python3

# Generate a random name for a namespace, class, function or variable.
# Complies with the JSF coding standard.
#
# Note:
# The nouns and adjectives files must contain only one word per line.
# The format of the file containing already used names is 'type,name'.

from argparse import ArgumentParser
from random import randint
from sys import exit

name_types = [
    "namespace",
    "class",
    "function",
    "variable",
]

nouns = [
    "faerge",
    "loegring",
    "rhododendron",
]

adjectives = [
    "boejet",
    "rank",
    "sjasket",
]

used_names = []

styles = {
      "namespace": ("{0}{1}",  str.lower,      str.lower)
    , "class":     ("{0}_{1}", str.capitalize, str.lower)
    , "variable":  ("{0}_{1}", str.lower,      str.lower)
    , "function":  ("{0}_{1}", str.lower,      str.lower)
}

def apply_style(format_string, adj_fun, nou_fun, adj, nou):
    return format_string.format(adj_fun(adj),nou_fun(nou))

def is_name_used(name_type, name, name_list):
    return any(name_type == t and name == n for t, n in name_list)

def read_words_file(filename):
    word_list = []
    with open(filename, 'r') as word_file:
       for w in word_file:
           word_list.append(w.strip())
    return word_list

if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("t",
                        type=str,
                        default="class",
                        choices=name_types,
                        metavar="type",
                        help="<" + "|".join(name_types) + ">")
    parser.add_argument("-n",
                        type=str,
                        metavar="file",
                        help="file containing nouns")
    parser.add_argument("-a",
                        type=str,
                        metavar="file",
                        help="file containing adjectives")
    parser.add_argument("-u",
                        type=str,
                        metavar="file",
                        help="file containing already used names")
    args = parser.parse_args()

    if args.n is not None:
        nouns = read_words_file(args.n)

    if args.a is not None:
        adjectives = read_words_file(args.a)

    if args.u is not None:
        tmp = read_words_file(args.u)
        used_names = []
        for pair in tmp:
            used_names.append(tuple(pair.split(',')))

    name_type = args.t
    noun = nouns[randint(0, len(nouns) - 1)]
    adjective = adjectives[randint(0, len(adjectives) - 1)]
    name = apply_style(*styles[name_type], adjective, noun)

    if is_name_used(name_type, name, used_names):
        print("Try again!")
        exit(1)
    else:
        if args.u is not None:
            with open(args.u, 'a') as used_names_file:
                used_names_file.write("{0},{1}\n".format(name_type, name))
        print(name)
