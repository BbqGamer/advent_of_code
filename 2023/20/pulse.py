import sys
from enum import Enum
from dataclasses import dataclass
import typing

class Pulse(Enum):
    LOW = 0
    HIGH = 1


class Instruction(typing.NamedTuple):
    src: str
    dest: str
    pulse: Pulse

class Component(typing.Protocol):
    def handle(self, inst: Instruction) -> list[Instruction]: 
        return []

@dataclass
class Broadcaster(Component):
    name: str
    outputs: list[str]

    def handle(self, inst: Instruction) -> list[Instruction]:
        return [Instruction(self.name, o, inst.pulse) for o in self.outputs]

@dataclass
class FlipFlop(Component):
    name: str
    outputs: list[str]
    state: Pulse = Pulse.LOW

    def handle(self, inst: Instruction) -> list[Instruction]:
        if inst.pulse == Pulse.LOW:
            self.state = Pulse.HIGH if self.state == Pulse.LOW else Pulse.LOW
            return [Instruction(self.name, o, self.state) for o in self.outputs]
        else:
            return []

class Conjunction(Component):
    
    def __init__(self, name: str, inputs: list[str], outputs: list[str]):
        self.name = name
        self.inputs = dict.fromkeys(inputs, Pulse.LOW)
        self.outputs = outputs
    
    def __repr__(self):
        return f"{self.name}: {self.inputs} -> {self.outputs}"

    def handle(self, inst: Instruction) -> list[Instruction]:
        self.inputs[inst.src] = inst.pulse
        if all(v == Pulse.HIGH for v in self.inputs.values()):
            return [Instruction(self.name, o, Pulse.LOW) for o in self.outputs]
        else:
            return [Instruction(self.name, o, Pulse.HIGH) for o in self.outputs]


def parse(data) -> dict[str, Component]:
    comp_list = []
    comp_inputs = {}
    for line in data:
        left, right = line.strip().split(" -> ")
        dest = right.split(", ")
        comp_type = left[0]
        comp_name = left[1:] if comp_type != "b" else left
        comp_list.append((comp_name, comp_type, dest))
        comp_inputs[comp_name] = []
    for comp_name, _, dest in comp_list:
        for d in dest:
            if d not in comp_inputs:
                continue
            comp_inputs[d].append(comp_name)
    components = {}
    for comp_name, comp_type, dest in comp_list:
        if comp_type == "b":
            components[comp_name] = Broadcaster(comp_name, dest)
        elif comp_type == "%":
            components[comp_name] = FlipFlop(comp_name, dest)
        elif comp_type == "&":
            components[comp_name] = Conjunction(comp_name, comp_inputs[comp_name], dest)
    return components


if __name__ == "__main__":
    data = sys.stdin.readlines()
    
    components = parse(data)
    low_pulses = 0
    high_pulses = 0
    
    for i in range(1000):
        rx_counts = 0
        queue = [Instruction('button', 'broadcaster', Pulse.LOW)]
        low_pulses += 1
        while queue:
            inst = queue.pop(0)
            if inst.dest == "rx":
                rx_counts += 1
            if inst.dest not in components:
                continue
            new = components[inst.dest].handle(inst)
            low = len([i for i in new if i.pulse == Pulse.LOW])
            low_pulses += low
            high_pulses += len(new) - low
            queue.extend(new)
        if rx_counts == 1:
            print(rx_counts)
    print(low_pulses * high_pulses)




