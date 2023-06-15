TEXT = """dog1, dog2, dog3
cat1, cat2, cat3
fish1, fish2, fish3"""

# [
#     [ 'dog1', 'dog2', 'dog3'],
#     [ 'cat1', 'cat2', 'cat3'],
#     [ 'fish1', 'fish2', 'fish3']
# ]
    

split_text = TEXT.split('\n')

all_lines = []
for line in split_text: 
    split_line = line.split(', ')
    all_lines.append(split_line)

print(all_lines)