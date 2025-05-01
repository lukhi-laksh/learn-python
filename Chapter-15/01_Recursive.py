class TowerOfHanoi:
    def __init__(self, num_disks):
        self.num_disks = num_disks
        self.steps = []

    def solve(self, n=None, source='A', target='C', auxiliary='B'):
        if n is None:
            n = self.num_disks
        
        if n == 1:
            self.steps.append(f"Move disk 1 from {source} to {target}")
        else:
            self.solve(n - 1, source, auxiliary, target)
            self.steps.append(f"Move disk {n} from {source} to {target}")
            self.solve(n - 1, auxiliary, target, source)

    def display_steps(self):
        for step in self.steps:
            print(step)

hanoi = TowerOfHanoi(3)
hanoi.solve()
hanoi.display_steps()
