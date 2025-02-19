class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        all_players = set()
        loss_count = {}

        for winner, loser in matches:
            all_players.add(winner)
            all_players.add(loser)

            if loser in loss_count:
                loss_count[loser] += 1
            else:
                loss_count[loser] = 1
            
            if winner not in loss_count:
                loss_count[winner] = 0

        no_loss = sorted([player for player in all_players if loss_count[player] == 0])
        one_loss = sorted([player for player in all_players if loss_count[player] == 1])

        return [no_loss, one_loss]