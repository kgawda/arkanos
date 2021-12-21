def main():
    class Termometr:
        def __init__(self, tempC):
            self.tempC = tempC

        # getter
        @property
        def tempK(self):
            return self.tempC + 273.15

        # setter (opcjonalny)
        @tempK.setter
        def tempK(self, value):
            self.tempC = value - 273.15

    term = Termometr(-6)
    assert term.tempC == -6
    assert term.tempK == 267.15
    term.tempC = 12
    assert term.tempK == 285.15
    term.tempK = 300
    assert 26.850 < term.tempC < 26.8501


if __name__ == '__main__':
    main()
