import asyncio
import time

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял шар {i}.')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Виктор', 10))
    task2 = asyncio.create_task(start_strongman('Анатолий', 16))
    task3 = asyncio.create_task(start_strongman('Борис', 20))
    await task1
    await task2
    await task3


start = time.time()
asyncio.run(start_tournament())
finish = time.time()

result_time = round(finish - start, 4)
print(f'Время работы программы {result_time}')



