from process_passport import parse_field, parse_passport, validate_passports, REQUIRED_FIELDS

class TestProcessPassports:
	good_passports = [
		f'''cid:US
pid:123456789
eyr:2025
iyr:2015
byr:1969
hcl:#ffee00
ecl:hzl
hgt:170cm'''
	]
	bad_passports = [
		# Bad birth year; everything else OK
		f'''cid:US
		pid:123456789
		eyr:2025
		iyr:2015
		hcl:#ffee00
		ecl:hzl
		hgt:170cm
		{REQUIRED_FIELDS[0]}:1492''',
		'', # Empty passport
	]

	good_eye_colors = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
	bad_eye_colors = ('prp', 'ylw', 'sharingan')

	def test__parse_passports(self):
		for good_passport in self.good_passports:
			assert parse_passport(good_passport)
		for bad_passport in self.bad_passports:
			assert not parse_passport(bad_passport)

	def test__parse_field__birth_year(self):
		assert parse_field(('byr', '2000'))
		assert not parse_field(('byr', '1492'))

	def test__parse_field__issue_year(self):
		assert not parse_field(('iyr', 2000))
		assert not parse_field(('iyr', 2021))
		assert parse_field(('iyr', 2015))

	def test__parse_field__issue_year(self):
		assert not parse_field(('eyr', 2010))
		assert not parse_field(('eyr', 2031))
		assert parse_field(('eyr', 2025))

	def test__parse_field__height(self):
		# Centimeters
		assert not parse_field(('hgt', '200cm'))
		assert not parse_field(('hgt', '140cm'))
		assert parse_field(('hgt', '170cm'))

		# Inches
		assert not parse_field(('hgt', '50in'))
		assert not parse_field(('hgt', '100in'))
		assert parse_field(('hgt', '69in'))

		# Fail other units
		assert not parse_field(('hgt', '0.8m'))

	def test__parse_field__hair_color(self):
		assert parse_field(('hcl', '#abcdef')) # Typical hex code -- passes
		assert parse_field(('hcl', '#01cdEF')) # More wacky hex code (mixed letters, capitals, numbers) -- passes
		assert not parse_field(('hcl', 'rgb(1,2,3)'))
		assert not parse_field(('hcl', 'blonde'))
		assert not parse_field(('hcl', 'abcdef')) # Hex code without '#' -- fails

	def test__parse_field__eye_color(self):
		for good_eye_color in self.good_eye_colors:
			assert parse_field(('ecl', good_eye_color))
		for bad_eye_color in self.bad_eye_colors:
			assert not parse_field(('ecl', bad_eye_color))

	def test__parse_field__passport_id(self):
		assert parse_field(('pid', '000333999'))
		assert not parse_field(('pid', '123'))
		assert not parse_field(('pid', '000044448888'))
