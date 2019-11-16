import matplotlib.pyplot as plt


def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    m_rate = rate/12
    for i in range(terms):
        base += [i]
        savings += [savings[-1] * (1 + m_rate) + monthly]

    return base, savings


def display_retire_w_monthlies(monthlies, rate, terms):
    plt.figure('retireMonth')
    plt.clf()
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(xvals, yvals, label='retire: '+str(monthly))
        plt.legend(loc='upper left')

    plt.show()


def display_retire_w_rate(month, rates, terms):
    plt.figure('retireRate')
    plt.clf()
    for rate in rates:
        xvals, yvals = retire(month, rate, terms)
        plt.plot(xvals, yvals, label='retire '+str(month) + ':' + str(int(rate*100)))
        plt.legend(loc='upper left')
    plt.show()


def display_retire_w_months_and_rates(monthlies, rates, terms):
    plt.figure('retireBoth')
    plt.clf()
    plt.grid(color='lightgrey', linewidth=2.0)
    plt.xlim(30*12, 40 * 12)  # focus in on the last 10 years
    month_labels = ['r', 'b', 'g', 'k']
    rate_labels = ['-', 'o', '--']
    for i in range(len(monthlies)):
        monthly = monthlies[i]
        month_label = month_labels[i % len(month_labels)]
        for j in range(len(rates)):
            rate = rates[j]
            rate_label = rate_labels[j % len(rate_labels)]
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals, month_label+rate_label, label='retire: ' + str(monthly) + ':' + str(int(rate * 100)))
            plt.legend(loc='upper left')

    plt.show()


if __name__ == '__main__':
    # display_retire_w_monthlies([500, 600, 700, 800, 900, 1000, 1100], .05, 40*12)
    # display_retire_w_rate(800, [.03, .05, .07], 40 * 12)

    display_retire_w_months_and_rates([500, 700, 900, 1100], [.03, .05, .07], 40 * 12)
