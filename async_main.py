import asyncio

from AsyncNDB.asyncndb import NDB
from NDB.enums import ReportType


async def main():
    report = await NDB.advanced_search(rep_type=ReportType.Citation)
    print(report)

if __name__ == '__main__':
    main_loop = asyncio.get_event_loop()
    main_loop.run_until_complete(main())

