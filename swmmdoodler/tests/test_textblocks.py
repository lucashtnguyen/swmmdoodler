import nose.tools as nt

from swmmdoodler import textblocks

class TestKeys(object):
    def setup(self):
        self.known_keys_SR = ['junctions', 'storage', 'conduits',
                              'outlets', 'xsections', 'coordinates',
                              'inflows', 'time_series']

        self.known_keys_SU = ['junctions', 'conduits',
                              'xsections', 'coordinates',
                              'inflows', 'time_series']

        self.known_keys_CR = ['junctions', 'storage', 'conduits',
                              'weirs', 'outlets', 'xsections',
                              'coordinates', 'inflows', 'time_series']

        self.known_keys_CU = ['junctions', 'storage', 'conduits',
                              'weirs', 'outlets', 'xsections',
                              'coordinates', 'inflows', 'time_series']

    def test_simple_restricted(self):
        nt.assert_true(isinstance(textblocks.simple_restricted, dict))
        nt.assert_list_equal(
            sorted(list(textblocks.simple_restricted.keys())),
            sorted(self.known_keys_SR)
        )

    def test_simple_unrestricted(self):
        nt.assert_true(isinstance(textblocks.simple_unrestricted, dict))
        nt.assert_list_equal(
            sorted(list(textblocks.simple_unrestricted.keys())),
            sorted(self.known_keys_SU)
        )

    def test_complex_restricted(self):
        nt.assert_true(isinstance(textblocks.complex_restricted, dict))
        nt.assert_list_equal(
            sorted(list(textblocks.complex_restricted.keys())),
            sorted(self.known_keys_CR)
        )

    def test_complex_unrestricted(self):
        nt.assert_true(isinstance(textblocks.complex_unrestricted, dict))
        nt.assert_list_equal(
            sorted(list(textblocks.complex_unrestricted.keys())),
            sorted(self.known_keys_CU)
        )
