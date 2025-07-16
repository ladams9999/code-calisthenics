from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        matches = 0
        players.sort(reverse=True)
        trainers.sort(reverse=True)

        player_count = len(players)
        trainer_count = len(trainers)
        player_pointer = 0
        trainer_pointer = 0
        while player_pointer<player_count and trainer_pointer<trainer_count:
            if players[player_pointer] <= trainers[trainer_pointer]:
                matches += 1
                trainer_pointer += 1
            
            player_pointer += 1

        return matches
    

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    players = [4,7,9]
    trainers = [8,2,5,8]
    print(f"Should be 2: {solution.matchPlayersAndTrainers(players, trainers)}")

    # Example 2
    players = [1,1,1]
    trainers = [10]
    print(f"Should be 1: {solution.matchPlayersAndTrainers(players, trainers)}")    
