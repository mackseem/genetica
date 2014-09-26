class Results(object):
    """
    contains results of one GA cycle 
    """
    
    def __init__(self):
        self.best = []
        self.generations = []
        self.deviations = []
        self.averages = []
        self.times = []

    def report(self, results):
        self.best.append(results['best'])
        self.generations.append(results['gen'])
        self.deviations.append(results['deviations'])
        self.averages.append(results['averages'])
        self.times.append(results['time'])


