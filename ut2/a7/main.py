class VirtualMachine:
    def __init__(self, name, ram=1, cpu=1.3, hdd=100, os='debian'):
        self.name = name
        self.ram = ram
        self.cpu = cpu
        self.hdd = hdd
        self.os = os
        self.status = 0
        self.proc = list()

    def stop(self):
        self.status = 0
        self.proc = list()

    def start(self):
        self.status = 1

    def suspend(self):
        self.status = 2

    def reboot(self):
        self.stop()
        self.start()

    def run(self, pid, ram, cpu, hdd):
        self.proc.append({'pid': pid, 'ram': ram, 'cpu': cpu, 'hdd': hdd})

    def ram_usage(self):
        ram = 0
        for p in self.proc:
            ram += p['ram']
        return ram * 100 / self.ram

    def cpu_usage(self):
        cpu = 0
        for p in self.proc:
            cpu += p['cpu']
        return cpu * 100 / self.cpu

    def hdd_usage(self):
        hdd = 0
        for p in self.proc:
            hdd += p['hdd']
        return hdd * 100 / self.hdd

    def get_status(self):
        if self.status == 0:
            return 'Stopped'
        elif self.status == 1:
            return 'Running'
        elif self.status == 2:
            return 'Suspended'

    def __str__(self):
        return '''
{} <{}> [{}]
{:.2f}% RAM used | {:.2f}% CPU used | {:.2f}% HDD used
        '''.format(
            self.os,
            self.name,
            self.get_status(),
            self.ram_usage(),
            self.cpu_usage(),
            self.hdd_usage()
        )
if __name__ == '__main__':
    
    minas_tirith = VirtualMachine('Minas Tirith', 8, 2.3, 380, 'ubuntu')
    print(minas_tirith)
    minas_tirith.start()
    print(minas_tirith)
    minas_tirith.run(1, 1.7, 0.3, 20)
    minas_tirith.run(4, 4, 0.9, 100)
    minas_tirith.run(7, 0.4, 1.1, 250)
    print(minas_tirith)
    minas_tirith.reboot()
    print(minas_tirith)

    rohan = VirtualMachine('Rohan', 6, 1.9, 250, 'debian')
    print(rohan)
    rohan.start()
    print(rohan)
    rohan.run(2, 0.6, 0.7, 50)
    rohan.run(5, 2.1, 0.2, 75)
    rohan.run(8, 2.5, 0.4, 30)
    print(rohan)
    rohan.reboot()
    print(rohan)

    rivendel = VirtualMachine('Rivendel', 16, 3, 1000, 'opensuse')
    print(rivendel)
    rivendel.start()
    print(rivendel)
    rivendel.run(3, 2, 1, 25)
    rivendel.run(6, 0.3, 0.5, 12)
    rivendel.run(9, 1.4, 0.8, 65)
    print(rivendel)
    rivendel.reboot()
    print(rivendel)
