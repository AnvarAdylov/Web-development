import time
from random import randint
import asyncio as ass


class Runner():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.speed = self.speedCalc()

    def speedCalc(self):
        if self.age < 7:
            age_modifier = 0.7
        elif 10 <= self.age < 20:
            age_modifier = 2
        elif 20 <= self.age < 40:
            age_modifier = 2.5
        else:
            age_modifier = 1.2
        return age_modifier*5

    async def time_to_run(self, distance: int) -> float:
        start_time = time.strftime('%X')
        print("=" * 50)
        print(f"Бегун {self.name} выбежал в {start_time}")
        move_time = (distance / self.speed) * 10
        await ass.sleep(move_time)
        print("=" * 50)
        print(f"Бегун {self.name} финишировал в {time.strftime('%X')}")
        return move_time

    def __str__(self):
        return f"{self.name} {self.speed} km/h"


async def main():
    runners = [Runner('Джон '+str(i), randint(1, 100)) for i in range(0, 100)]
    runs = [ass.create_task(runner.time_to_run(10)) for runner in runners]
    results = await ass.gather(*runs)
    sorted_results = sorted(zip(runners, results), key=lambda x: x[1])
    print("Результаты турнира:")
    for i, (runner, time_taken) in enumerate(sorted_results, 1):
        print(f"{i}. {runner.name} - Возраст: {runner.age} " +
              f"- Время: {time_taken:.2f} ")
    fastest_time = sorted_results[0][1]
    slowest_time = sorted_results[-1][1]
    time_difference_minutes = (slowest_time - fastest_time)
    print('\nСамый быстрый бегун финишировал', end='')
    print(f" за {time_difference_minutes:.2f} до самого медленного бегуна.")


ass.run(main())
