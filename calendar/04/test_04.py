from process_passport import parse_passport, validate_passports, REQUIRED_FIELDS

class TestProcessPassports:
	good_passports = ()
	bad_passports = (
		f'''{REQUIRED_FIELDS[0]}:1492'''
	)

	def test_parse_passports(self):
		for bad_passport in self.bad_passports:
			assert parse_passport(bad_passport) == False
