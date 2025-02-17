# The file valence_data/winter_2016_senses_valence.csv contains data from an 
# experiment that asked people to provide valence ratings for words associated
# with each of the five senses (touch, taste, smell, sight, sound). The file has
# three columns: Word, Modality, and Val. Word contains the word, Modality the
# sensory modality, and Val contains the mean valence rating for that word,
# where higher valence corresponds to more positive emotional states.

# The question we'll try to answer is whether certain sensory modalities have 
# higher or lower mean valences than others.
# 
#  Write a function called get_mean_valence that takes a Path to a CSV file
#  as input. You can assume the file will be formatted as described above.
#  Your function should return a dictionary with keys corresponding to each
#  of the five modalities. The value for each key should be its mean valence
#  score across all of the words in the CSV file.

# The data are from the paper 
#
# Winter, B. (2016). Taste and smell words form an affectively loaded and emotionally
# flexible part of the English lexicon. Language, Cognition and Neuroscience, 31(8), 
# 975-988.
from pathlib import Path


def get_mean_valence(file):
    path_to_file = Path(file)
    with open(path_to_file, 'r') as file:
        data = [line.strip().split(',') for line in file]
    def modality_average(modality):
        running_average = 0
        running_count = 0
        for entry in data:
            if entry[1] == modality:
                running_average += float(entry[2])
                running_count += 1
        total_average = running_average / running_count
        return total_average
    
    output = {}
    output['Touch'] = modality_average('Touch')
    output['Sight'] = modality_average('Sight')
    output['Taste'] = modality_average('Taste')
    output['Smell'] = modality_average('Smell')
    output['Sound'] = modality_average('Sound')
    
    print(output)
    return output

# Do not modify the following line
if __name__ == "__main__":
    # You can write code to test your function here
    pass 
