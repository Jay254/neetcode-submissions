class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((-self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        users = {userId} | self.following[userId]
        for user in users:
            for tweet in self.tweets[user]:
                heapq.heappush(heap, tweet)
        res = []
        while heap and len(res) < 10:
            _, tweet = heapq.heappop(heap)
            res.append(tweet)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)