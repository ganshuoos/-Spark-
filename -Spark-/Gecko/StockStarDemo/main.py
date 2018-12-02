import urllib
import urllib.request
import re
import random
import time
from StockStarDemo.Properties import SSpro


# Make a class for encapsulation, which make it more helpful
class GeckoStockStar:

    stock_total = []
    stock_last = []

    def gecko_process(self, p):
        for page in range(1, 8):
            url = p.get('url') + str(page) + p.get('HTML')
            request = urllib.request.Request(url=url,
                                             headers=
                                             {"User-Agent": random.choice(p.get('user_agent'))})

            # May extend a new function, it can record the failed pagecatching and redo it.
            try:
                fail = 0
                # Circle for get the content
                while fail <= 10:
                    try:
                        if fail > 0:
                            print("Reconnect to page " + str(page))
                        print("Try to catch the content of page " + str(page))

                        response = urllib.request.urlopen(request, None, 3)
                        content = response.read().decode('gbk')
                        self.scratch_process(content, page)
                        break

                    except urllib.request.socket.timeout:
                        fail += 1
                else:
                    print("Time out, go to next page")

            except urllib.request.HTTPError as e:
                print('page = ', page, ', and error occur:', e.code)
            except urllib.request.URLError as e:
                print('page = ', page, ', and error occur:', e.code)

    def scratch_process(self, content, page):
        # Print the num of page
        print('Get page ', page, ".")

        pattern = re.compile('<tbody[\s\S]*</tbody>')
        body = re.findall(pattern, str(content))
        pattern = re.compile('>(.*?)<')
        stock_page = re.findall(pattern, body[0])
        self.stock_total.extend(stock_page)

        # Sleep while get a page for tricking the website
        time.sleep(random.randrange(1, 4))

        self.stock_last = self.stock_total[:]
        for data in self.stock_total:
            if data == '':
                self.stock_last.remove('')

        self.presentation_process()

    def presentation_process(self):
        # Print the result
        print('代码', '\t',
              '简称', '   ', '\t',
              '最新价', '   ', '\t',
              '涨跌幅', '  ', '\t',
              '涨跌额', '\t',
              '5分钟涨幅')

        # There are 13 rows' data, which means there is 13 steps long.
        for i in range(0, len(self.stock_last), 13):
            print(self.stock_last[i], '\t',
                  self.stock_last[i+1], ' ', '\t',
                  self.stock_last[i+2], '  ', '\t',
                  self.stock_last[i+3], '  ', '\t',
                  self.stock_last[i+4], '  ', '\t',
                  self.stock_last[i+5])


gecko = GeckoStockStar()
catch_properties = SSpro()
gecko.gecko_process(catch_properties)





































