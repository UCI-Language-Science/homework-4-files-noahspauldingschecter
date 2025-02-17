# Write a function called score_unigrams that takes three arguments:
#   - a path to a folder of training data 
#   - a path to a test file that has a sentence on each line
#   - a path to an output CSV file
#
# Your function should do the following:
#   - train a single unigram model on the combined contents of every .txt file
#     in the training folder
#   - for each sentence (line) in the test file, calculate the log unigram 
#     probability ysing the trained model (see the lab handout for details on log 
#     probabilities)
#   - write a single CSV file to the output path. The CSV file should have two
#     columns with headers, called "sentence" and "unigram_prob" respectively.
#     "sentence" should contain the original sentence and "unigram_prob" should
#     contain its unigram probabilities.
#
# Additional details:
#   - there is training data in the training_data folder consisting of the contents 
#     of three novels by Jane Austen: Emma, Sense and Sensibility, and Pride and Prejudice
#   - there is test data you can use in the test_data folder
#   - be sure that your code works properly for words that are not in the 
#     training data. One of the test sentences contains the words 'color' (American spelling)
#     and 'television', neither of which are in the Austen novels. You should record a log
#     probability of -inf (corresponding to probability 0) for this sentence.
#   - your code should be insensitive to case, both in the training and testing data
#   - both the training and testing files have already been tokenized. This means that
#     punctuation marks have been split off of words. All you need to do to use the
#     data is to split it on spaces, and you will have your list of unigram tokens.
#   - you should treat punctuation marks as though they are words.
#   - it's fine to reuse parts of your unigram implementation from HW3.

# You will need to use log and -inf here. 
# You can add any additional import statements you need here.
from math import log, inf
import math
from pathlib import Path
import csv

def score_unigrams(training, test, output):
    path_to_training = Path(training)
    training_files = path_to_training.glob('*')
    
    path_to_test = Path(test)

    path_to_output = Path(output)

    word_counts = {}
    total_word_count = 0

    for file_path in training_files:
        with file_path.open('r') as training_data_temp:
            for line in training_data_temp:
                line_list = line.split()
                for raw_word in line_list:
                    word = raw_word.lower()
                    word_counts[word] = word_counts.get(word, 0) + 1
                    total_word_count += 1

    unigram_model = word_counts
    for word in unigram_model:
        unigram_model[word] = (unigram_model.get(word)/total_word_count)

    with path_to_test.open('r') as testing_data_temp, path_to_output.open('w') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(['sentence', 'unigram_prob'])
        full_dict = []
        for line in testing_data_temp:
            log_probability = 0
            line_strip = line.strip()
            print(line_strip)
            line_list = line_strip.split()
            for raw_word in line_list:
                word = raw_word.lower()
                if unigram_model.get(word) == None:
                    log_probability = (-inf)
                else:
                    log_probability += log(unigram_model.get(word))
            dict_to_upload = {}
            dict_to_upload['sentence'] = str(line.strip('\n'))
            dict_to_upload['unigram_prob'] = str(log_probability)
            full_dict.append(dict_to_upload)
            writer = csv.DictWriter(output_file, fieldnames=['sentence','unigram_prob'])
            writer.writerow(dict_to_upload)
    print(full_dict)
    return full_dict

score_unigrams(
    Path('training_data'),
    Path('test_data/test_sentences.txt'),
    Path('output.csv'))           

# Do not modify the following line
if __name__ == "__main__":
    # You can write code to test your function here
    pass 
