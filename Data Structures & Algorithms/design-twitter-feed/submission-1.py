class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(list)
        self.followees = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweets[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        people = self.followees[userId] | {userId}
        for person in people:
            for t, tweet in self.tweets[person][-10:]:
                heapq.heappush(heap, (t, tweet))
                if len(heap) > 10:
                    heapq.heappop(heap)
        return [tweet for _, tweet in sorted(heap, reverse=True)]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)
