# Perfect Matchup
You and your friends are playing this new mobile video game called Diabro Immoral Gacha (DIG). 
The game revolves around building a team of M characters to compete with other teams in a tournament. You aimed to be the very best, like no one ever was in the game. Thus, you have done your research into past tournaments in preparation for the biggest tournament. You aim to find the best performing team composition against the other teams. You are however dealing with a large amount of tournament results.
The past tournament data results is presented as a list of lists 1. The inner list can be described as [team1, team2, score] where: 
 ->team1 and team2 are uppercase strings. 
 -> Both team1 and team2 are of the same length, denoted by the positive integer M. Both team1 and team2 are from the same character set, denoted by the positive integer roster. For example, roster=5 indicates a character set of {A, B, C, D, E}. It is possible that not all characters from the roster set would necessarily appear in the team composition 2. 
 -> Teams can have multiple instances of the same character, for example, team ABA with two As. The order of characters in team1 and team2 do not matter. A team of ABC is regarded to be the same as a team of some permutation of ABC, such as BAC or BCA. 
 ˆ score is an integer value in the range of 0 to 100 inclusive. It denotes the score obtained by team1 in a match against team2. It also denotes the score of (100−score) obtained by team team2 in the same match against team1.
