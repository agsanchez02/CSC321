class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        
        if sum(gas) < sum(cost):
            return -1
        
        gas_tank = 0
        start = 0
        
        for i in range(len(gas)):
            gas_tank += (gas[i] - cost[i])

            if gas_tank < 0:
                gas_tank = 0
                start = i+1
        
        return start