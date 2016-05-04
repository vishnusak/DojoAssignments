import re

file_name = "poem.txt"
report_name = "wordCountReport.txt"

my_file = open(file_name, 'rU')
my_report = open(report_name, 'w')

get_words = re.compile('\w+')   # pattern to identify words

word_dict = {}

for line in my_file.readlines():
    words_in_line = get_words.findall(line)  # applying the pattern to the line
    for word in words_in_line:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

# the below output is formatted to give consistent width output columns
# formatting examples taken from the common string ops page in python docs
col_width = 15
for key in word_dict.keys():
    output = ("word: '{:_^{width}}' => Occurrence: {:^5} time(s)\n".format(key, word_dict[key], width = col_width))
    my_report.write(output)

my_report.close()
my_file.close()
