#1. convert from hex to bin
#2. packets start with 3 (version) + 3 (type ID) headers
#3. TYPE ID 4 - pad string with 0 until its multiple of 4:
#   OTHER TYPES - OPERATIONS I = length Type ID, 15 bits is length of subpackets

from collections import deque
from math import prod

def generatePacket(data):
    packet = ""
    for l in data:
        packet += (bin(int(l, 16))[2:]).zfill(4)
    return packet

class Parser():
    c = 0
    stack = deque()
    versionSum = 0
    
    def readData(self, data):                
        self.packet = generatePacket(data)

    def readNBits(self, n, raw=False):
        data = self.packet[self.c:self.c+n]
        if not raw:
            data = int(data, 2)
        self.c += n
        self.stack[-1] += n
        return data

    def readVersion(self):
        version = self.readNBits(3)
        self.versionSum += version
        return version

    def readTypeID(self):
        typeID = self.readNBits(3)
        return typeID
    
    def fillPadding(self):
        while(self.stack[-1]%4 != 0):
            self.readNBits(1)
        self.stack.pop()
    
    def readValue(self):
        value = ""
        while(self.readNBits(1) == 1):
            value += self.readNBits(4, raw=True)
        value += self.readNBits(4, raw=True)
        return int(value, 2)

    def operator(self, values, typeID):
        if typeID == 0:
            f = sum
        elif typeID == 1:
            f = prod
        elif typeID == 2:
            f = min
        elif typeID == 3:
            f = max
        elif typeID == 5:
            f = lambda a: int(a[0] > a[1])
        elif typeID == 6:
            f = lambda a: int(a[0] < a[1])
        else:
            f = lambda a: int(a[0] == a[1])
        return f(values)

    def operationPacket(self, typeID):
        lengthTypeID = self.readNBits(1)
        values = []
        if lengthTypeID == 0:
            subPacketLength = self.readNBits(15)
            end = self.c + subPacketLength
            while(self.c < end):
                values.append(self.readPacket())
        else:
            subPackets = self.readNBits(11)
            for _ in range(subPackets):
                values.append(self.readPacket())
        return self.operator(values, typeID)

    def readPacket(self):
        self.stack.append(0)
        version = self.readVersion()
        typeID = self.readTypeID()
        if typeID == 4:
            return self.readValue()
        else:
            return self.operationPacket(typeID)

with open("input") as f:
    p = Parser()
    p.readData(f.read().rstrip())
    value = p.readPacket()
    print("Part one:" ,p.versionSum)
    print("Part two:", value)