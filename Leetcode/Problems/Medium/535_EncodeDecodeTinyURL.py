class Codec:
    def __init__(self):
        
        self.code2Url = {}
        self.urlDB = {}
        self.codes = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'

    def getCode(self):
        return ''.join(random.choice(self.codes) for _ in range(7))
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        #if URL is repeated, return previously stored shortCode
        if longUrl in self.urlDB:
            return self.urlDB[longUrl]
        
        shortCode = self.getCode()
        
        #if there is collision try getting new code
        while shortCode in self.code2Url:
            shortCode = self.getCode()
            
        #Add shortCOde with longUrl in hashmap
        self.code2Url[shortCode] = longUrl
        
        #add longUrl with shortCode
        self.urlDB[longUrl] = shortCode
        
        return 'http://tinyurl.com/' + shortCode
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        
        return self.code2Url[shortUrl[-7:]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

