# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """
from concurrent import futures
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname = lambda url: url.split('/')[2]
        seen = set([startUrl])
        future_list = set()

        with futures.ThreadPoolExecutor(max_workers=16) as executor:
            future_list.add(executor.submit(htmlParser.getUrls, startUrl))
            while future_list:
                for future in futures.as_completed(future_list):
                    for url in future.result():
                        if url not in seen and hostname(url) == hostname(startUrl):
                            seen.add(url)
                            future_list.add(executor.submit(htmlParser.getUrls, url))
                    future_list.remove(future)

        return list(seen)



        