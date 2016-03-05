from NDB.asyncndb import NDB
import asyncio

async def main():
    ndb = NDB()
    report = await ndb.advanced_search()
    print(report)

if __name__ == '__main__':
    main_loop = asyncio.get_event_loop()
    main_loop.run_until_complete(main())

