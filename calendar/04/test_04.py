from process_passport import validate_passports, parse_field, parse_passport, validate_passports, REQUIRED_FIELDS

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
	test_batch = f'''pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719

eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007'''

	good_eye_colors = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
	bad_eye_colors = ('prp', 'ylw', 'sharingan')

	def test__validate_passports(self):
		assert validate_passports(self.test_batch) == 4

	def test__parse_passports(self):
		for good_passport in self.good_passports:
			assert parse_passport(good_passport)
		for bad_passport in self.bad_passports:
			assert not parse_passport(bad_passport)

	def test__parse_field__birth_year(self):
		assert parse_field(('byr', '2002'))
		assert not parse_field(('byr', '1492'))
		assert not parse_field(('byr', '2003'))

	def test__parse_field__issue_year(self):
		assert not parse_field(('iyr', 2000))
		assert not parse_field(('iyr', 2021))
		assert parse_field(('iyr', 2020))
		assert parse_field(('iyr', 2010))

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
