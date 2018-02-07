"""
Tests for lookups of elemental data
"""

from bse import lut

def test_element_data():
    # Cycle through the elements and check that 
    # the info returned from the functions is consistent
    for Z in range(1, 118):
        data = lut.element_data_from_Z(Z)
        assert data[1] == Z

        assert data == lut.element_data_from_sym(data[0])
        assert data == lut.element_data_from_name(data[2])

        assert data[0] == lut.element_sym_from_Z(Z)
        assert data[2] == lut.element_name_from_Z(Z)

        nsym = lut.normalize_element_symbol(data[0])
        nname = lut.normalize_element_name(data[2])

        assert nsym[0] == data[0][0].upper()
        assert nname[0] == data[2][0].upper()


def test_amchar():
    # Check that converting am characters, etc, is consistent
    for am in range(12):
        s = lut.amint_to_char([am])
        assert am == lut.amchar_to_int(s)[0]

        combined = list(range(am+1))
        s = lut.amint_to_char(combined)
        assert combined == lut.amchar_to_int(s)
