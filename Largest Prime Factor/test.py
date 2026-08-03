from Prime import PolynomialRho, GreaterCommonDivisor


def test_values() : 
    InitiatingValueX : int = 2

    # Pollard polonymial 
    ExpectedValueX : int = InitiatingValueX ** 2 + 1
    ExpectedValueY : int = ExpectedValueX ** 2 + 1

    assert PolynomialRho() == (ExpectedValueX, ExpectedValueY)

def test_GreaterCommonDivisor() : 
    d = GreaterCommonDivisor(1885)

    assert d == 5
