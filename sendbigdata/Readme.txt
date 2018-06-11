copy from 

https://stackoverflow.com/questions/42459499/what-is-the-proper-way-of-sending-a-large-amount-of-data-over-sockets-in-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

Client -> server: 8 bytes: big endian, length of image.
Client -> server: length bytes: all image data.
(Client <- server: 1 byte, value 0: indicate transmission received - optional step you may not care if you're using TCP and just assume that it's reliable.)
