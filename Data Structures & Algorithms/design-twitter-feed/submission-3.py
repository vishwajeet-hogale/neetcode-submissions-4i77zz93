import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.friends_map = defaultdict(set)
        self.tweets = []
        self.curr_ts = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.curr_ts += 1
        heapq.heappush(self.tweets, (-self.curr_ts, tweetId, userId))


    def getNewsFeed(self, userId: int) -> List[int]:
        k = 10
        options = set(self.friends_map[userId])
        options.add(userId)

        heap = self.tweets.copy()
        res = []

        while heap and k > 0:
            ts, twid, usid = heapq.heappop(heap)
            if usid in options:
                res.append(twid)
                k -= 1

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.friends_map[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.friends_map[followerId]:
            self.friends_map[followerId].remove(followeeId)