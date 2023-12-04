class Codec:

    def __init__(self):
        self.tiny_to_long = {}
        self.long_to_tiny = {}
        self.counter = 0

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.long_to_tiny:
            self.counter += 1
            tinyUrl = "http://tinyurl.com/" + str(self.counter)
            self.tiny_to_long[tinyUrl] = longUrl
            self.long_to_tiny[longUrl] = tinyUrl
        return self.long_to_tiny[longUrl]

    def decode(self, shortUrl: str) -> str:
        return self.tiny_to_long[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))