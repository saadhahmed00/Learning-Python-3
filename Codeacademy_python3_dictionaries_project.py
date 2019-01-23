#Scrabble

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {letter.upper():point for letter,point in zip(letters,points)}

letter_to_points[" "] = 0

def score_words(word):
  point_total = 0
  for letter in word:
    point = letter_to_points.get(letter, 0)
    point_total += point
  return point_total

brownie_points = score_words("BROWNIE")
#print(brownie_points)
    
player_to_words = {'player1':['BLUE', 'TENNIS', 'EXIT'], 'wordNerd':['EARTH','EYES','MACHINE'], 'Lexi Con':['ERASER','BELLY','HUSKY'], 'Prof Reader':['ZAP','COMA', 'PERIOD']}
player_to_points = {}
for player,words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_words(word)
  player_to_points[player] = player_points
#print(player_to_points)

def play_word(player,word):
  player_to_words[player].append(word)
  return player_to_words
#print(play_word('player1', "NIGGA"))

