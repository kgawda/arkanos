import asyncio

async def f(name):
    print("Hello", name)
    await asyncio.sleep(len(name)/7)
    return len(name)

async def main():
    return await asyncio.gather(f("world"), f("moon"), f("Arkanos"))

if __name__ == '__main__':
    r = asyncio.run(main())
    print(r)
