timestamp = 0

class Twitter:


    class Tweet:
        def __init__(self, id:int, time: int) -> None:
            self.id = id
            self.time = time
            self.next = None

    class User:
        def __init__(self, id:int) -> None:
            self.id = id
            self.followed = set()
            self.head = None
            self.follow(self.id)
        
        def follow(self, followId:int) -> None:
            self.followed.add(followId)

        def unfollow(self, followId:int) -> None:
            if followId in self.followed and followId != self.id:
                self.followed.remove(followId)

        def postTweet(self, tweetId: int) -> None:
            global timestamp
            twt = Twitter.Tweet(tweetId, timestamp)
            timestamp += 1
            twt.next = self.head
            self.head = twt

    def __init__(self) -> None:
        self.userIdToUserMap = {}

    """user 发表一条 tweet 动态"""
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.userIdToUserMap:
            user = Twitter.User(userId)
            self.userIdToUserMap[userId] = user
        self.userIdToUserMap[userId].postTweet(tweetId)
    
    """返回该 user 关注的人（包括他自己）最近的动态 id，
    最多 10 条，而且这些动态必须按从新到旧的时间线顺序排列。"""
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        if userId not in self.userIdToUserMap:
            return res
        followed_users = self.userIdToUserMap[userId].followed
        maxHeap = []

        for id in followed_users:
            twt = self.userIdToUserMap[id].head
            if twt:
                heapq.heappush(maxHeap, (-1 * twt.time, twt))

        while maxHeap and len(res) < 10:
            _, twt = heapq.heappop(maxHeap)
            res.append(twt.id)
            if twt.next:
                heapq.heappush(maxHeap, (-1 * twt.next.time, twt.next))
        return res
        
    
    """follower 关注 followee，如果 Id 不存在则新建"""
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userIdToUserMap:
            self.userIdToUserMap[followerId] = self.User(followerId)
        if followeeId not in self.userIdToUserMap:
            self.userIdToUserMap[followeeId] = self.User(followeeId)
        self.userIdToUserMap[followerId].follow(followeeId)
    
    """follower 取关 followee，如果 Id 不存在则什么都不做"""
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.userIdToUserMap:
            self.userIdToUserMap[followerId].unfollow(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)