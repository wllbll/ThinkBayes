"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

Exercise 2.1.
"""

from thinkbayes import Pmf

from collections import Counter

class Bowl(Counter):
    def draw(self, color):
        self[color] -= 1


class Cookie(Pmf):
    """A map from string bowl ID to probablity."""

    def __init__(self, hypos):
        """Initialize self.

        hypos: sequence of string bowl IDs
        """
        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo, 1)
        self.Normalize()

    def Draw(self, data, hypo):
        mix = self.mixes[hypo]
        mix.draw(data)

    def Update(self, data):
        """Updates the PMF with new data.

        data: string cookie type
        """
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()

    mixes = {
        'Bowl 1':Bowl(['vanilla']*30 + ['chocolate']*10),
        'Bowl 2':Bowl(['vanilla']*20 + ['chocolate']*20),
        }

    def Likelihood(self, data, hypo):
        """The likelihood of the data under the hypothesis.

        data: string cookie type
        hypo: string bowl ID
        """
        mix = self.mixes[hypo]
        like = float(mix[data]) / sum(mix.values())
        return like


def main():
    hypos = ['Bowl 1', 'Bowl 2']

    pmf = Cookie(hypos)
    print('the priors are:')
    for hypo, prob in pmf.Items():
        print hypo, prob

    pmf.Update('vanilla')

    print('the posteriors are:')
    for hypo, prob in pmf.Items():
        print hypo, prob

    pmf.Update('vanilla')
    print('the posteriors are:')
    for hypo, prob in pmf.Items():
        print hypo, prob
    pmf.Draw('vanilla', 'Bowl 1' )
    pmf.Update('vanilla')
    print('the posteriors are:')
    for hypo, prob in pmf.Items():
        print hypo, prob


if __name__ == '__main__':
    main()