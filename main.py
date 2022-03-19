import optparse
import numpy as np
from optparse import OptionParser


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-n", type=int , dest="numbers")
    return parser.parse_args()


(options, arguments) = get_arguments()
number_Int = options.numbers
gen_Number = (256 - number_Int)


character_list = [ "a" , "A" , "b" , "B" , "c" , "C" , "d" , "D" , "e" , "E" , "f" , "F" , "g" , "G" , "h" , "H" , "i" ,
                  "I", "j" ,  "J" , "k" , "K" , "l" , "L" , "m" , "M" , "n" , "N" , "o" , "O" , "p" , "P" , "q" , "Q"
                  "r" , "R" , "s" , "S" , "t" , "T" , "u" , "U" , "v" , "V" , "w" , "W" , "x" , "X" , "y" , "Y" , "z" , "Z" ,
                  1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]

