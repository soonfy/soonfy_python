import threading

class ThreadS (threading.Thread):
  def __init__(self, threadID, func, userid):
    threading.Thread.__init__(self)
    self.threadID = threadID
    self.func = func
    self.userid = userid

  def run(self):
    threadLock = threading.Lock()
    print ("开启线程： %s" % self.threadID)
    # 获取锁，用于线程同步
    threadLock.acquire()
    self.func(self.userid)
    # 释放锁，开启下一个线程
    threadLock.release()

def thread_nos(func, arr, nos = 10):
  counter = 0
  length = len(arr)
  iterer = iter(arr)
  threads = []
  while True:
  # 创建新线程
    try:
      for thread_id in range(nos):
        thread = ThreadS(thread_id, func, next(iterer))
        thread.start()
        threads.append(thread)

      # 等待所有线程完成
      for thread in threads:
        thread.join()
      print('%s threads over...' % nos)
      counter += nos
      if length - counter < nos:
        break
    except:
      print('start iter one by one...')
      break
  while True:
    try:
      thread = ThreadS('last', func, next(iterer))
      thread.start()
      thread.join()
      print('one over...')
    except:
      print('one by one over...')
      break
  print('all threads over...')
