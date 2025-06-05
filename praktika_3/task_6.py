import numpy
from matplotlib import pyplot
x = numpy.linspace(-3 * numpy.pi, 3 * numpy.pi, 500)
y = numpy.where(x != 0, (numpy.sin(3 * x) * numpy.cos(2 * x)) / (3 * x), 999999999)
pyplot.plot(x, y, color='green', label='y = (sin(3x) * cos(2x)) / 3x')
pyplot.xlabel('x')
pyplot.ylabel('y')
pyplot.xticks(numpy.arange(-3 * numpy.pi, 3.001 * numpy.pi, numpy.pi), ['-3π', '-2π', '-π', '0', 'π', '2π', '3π'])
pyplot.grid(True)
pyplot.legend()
pyplot.show()