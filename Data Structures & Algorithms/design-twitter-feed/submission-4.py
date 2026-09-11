import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = {} # {userId: [(time, tweetId), ...]} // {1: []}
        self.following = {}  # {userId: {followeeId, ...}}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if self.tweets.get(userId) is None:
            self.tweets[userId] = []
        heapq.heappush(self.tweets[userId], (self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        hq = []
        if self.following.get(userId) is not None:
            following_groups = self.following[userId] | {userId}
        else:
            following_groups = {userId}
        for uid in following_groups:
            for time, tweetId in self.tweets.get(uid, []):
                heapq.heappush(hq, (-time, tweetId))
        
        feed = []
        while hq and len(feed) < 10:
            time, tweetId = heapq.heappop(hq)
            feed.append(tweetId)
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if self.following.get(followerId) is None:
            self.following[followerId] = set()
            
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if self.following.get(followerId) is None:
            return None
        else:
            if followeeId in self.following[followerId]:
                self.following[followerId].remove(followeeId)
        
