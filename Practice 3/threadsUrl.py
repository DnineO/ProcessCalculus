"""Первый пример асинхронности и зеленых потоков"""
# import gevent.monkey
# from urllib.request import urlopen
# gevent.monkey.patch_all()
# urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']
#
# def print_head(url):
#     print('Starting {}'.format(url))
#     data = urlopen(url).read()
#     print('{}: {} bytes: {}'.format(url, len(data), data))
#
# jobs = [gevent.spawn(print_head, _url) for _url in urls]
#
# gevent.wait(jobs)
"""Второй пример асинхронности и зеленых потоков"""
# import tornado.ioloop
# from tornado.httpclient import AsyncHTTPClient
#
# urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']
#
#
# def handle_response(response):
#     if response.error:
#         print("Error:", response.error)
#     else:
#         url = response.request.url
#         data = response.body
#         print('{}: {} bytes: {}'.format(url, len(data), data))
#
#
# http_client = AsyncHTTPClient()
# for url in urls:
#     http_client.fetch(url, handle_response)
#
# tornado.ioloop.IOLoop.instance().start()
"""Третий пример потоков"""
# from threading import Thread
#
# def prescript(thefile, num):
#     with open(thefile, 'w') as f:
#         for i in range(num):
#             if num > 500:
#                 f.write('Много Букв\n')
#             else:
#                 f.write('Мало Букв\n')
#
# thread1 = Thread(target=prescript, args=('f1.txt', 200,))
# thread2 = Thread(target=prescript, args=('f2.txt', 1000,))
#
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
"""Четвертый пример потоков"""
# import threading
# class MyThread(threading.Thread):
#     def __init__(self, num):
#         super().__init__(self, name="threddy" + num)
#         self.num = num
#     def run(self):
#         print ("Thread ", self.num)
# thread1 = MyThread("1")
# thread2 = MyThread("2")
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()

"""Пятый пример"""
# Пример многопоточности Python.
# 1. Рассчитать факториал с помощью рекурсии.
# 2. Вызовите факториальную функцию, используя поток.

from _thread import start_new_thread

threadId = 1

def factorial(n):
  global threadId
  if n < 1:
      print("%s: %d" % ("Thread", threadId ))
      threadId += 1
      return 1
  else:
      returnNumber = n * factorial( n - 1 )  # рекусрсивынй вызов
      print(str(n) + '! = ' + str(returnNumber))
      return returnNumber

start_new_thread(factorial,(5, ))
start_new_thread(factorial,(4, ))

c = input("Waiting for threads to return...\n")