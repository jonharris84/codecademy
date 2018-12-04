from sys import argv

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters, points)}
letter_to_points[" "] = 0

def score_word(word):
  point_total = 0

  for letter in word:
    point_total += letter_to_points.get(letter.upper(), 0)

  return point_total

player_to_words = {}
player_to_points = {}

def update_points_totals():
  player_points = 0

  for player in player_to_words:
    words = player_to_words[player]

    for word in words:
      player_points += score_word(word)

    player_to_points[player] = player_points

  return(player_to_points)


def play_word(player, word):
  try:
     player_to_words[player].append(word)

  except KeyError:
    player_to_words[player] = word

  update_points_totals()

def main():
  play_word(argv[1], argv[2])

  print(player_to_points)

if __name__ == '__main__':
  main()
    