class Bot:
    bots = {}
    outputs = {}

    def __init__(self, num, val):
        self.id = num
        self.start_val = int(val)
        self.instr = []
        self.high, self.low = 0, 0

    def addInstr(self, instr):
        self.instr = instr
        if self.low and self.high:
            self.give()

    def take(self, val):
        val = int(val)
        if self.start_val == 0:
            self.start_val = val
        else:
            if (self.start_val == 61 and val == 17) or (self.start_val == 17 and val == 61):
                print('Bot {} is Comparing: value-{} to value-{}'.format(self.id, self.start_val,val))
            if val < self.start_val:
                self.low, self.high = val, self.start_val
            else:
                self.low, self.high = self.start_val, val

            if len(self.instr):
                self.give()

    def getPos(self, pos):
        if pos == 'low':
            val = self.low
            self.low = 0
        else:
            val = self.high
            self.high = 0
        if self.low + self.high == 0:
            self.start_val = 0
        return(val)

    def give(self):
        for move in self.instr:
            type, id, val = move['type'], move['id'], self.getPos(move['pos'])
            if type == 'output':
                if id in Bot.outputs:
                    Bot.outputs[id].append(val)
                else:
                    Bot.outputs[id]=[val]
            if type == 'bot':
                if id in Bot.bots:
                    Bot.bots[id].take(val)
                else:
                    Bot.bots[id] = Bot(id,val)
        self.instr = []

input = open("inputs/day10.txt", "r")

for line in input:
    #print(line)
    instr = line.strip().split()
    if instr[0] == 'value':
        #assign value to bots
        val, botId = instr[1], instr[5]
        if botId in Bot.bots:
            Bot.bots[botId].take(val)
        else:
            Bot.bots[botId] = Bot(botId,val)

    elif instr[0] == 'bot':
        #give values
        botId = instr[1]
        moves = [{'pos':'low', 'type':instr[5], 'id':instr[6]}, {'pos':'high', 'type':instr[10], 'id':instr[11]}]
        if botId not in Bot.bots:
            Bot.bots[botId] = Bot(botId,0)

        Bot.bots[botId].addInstr(moves)

print(Bot.outputs)
print(Bot.outputs['0'][0]*Bot.outputs['1'][0]*Bot.outputs['2'][0])

input.close()
