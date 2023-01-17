import sys;
N = int(sys.stdin.readline())

hive = 1
wave = 1
while N > hive:
    hive += wave * 6 # 웨이브 * 6 을 하면 웨이브마다 한 둘레의 벌집이 생김
    wave += 1 # 한 둘레의 웨이브가 생기면 다음 웨이브로
print(wave)