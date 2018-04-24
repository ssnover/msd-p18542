import base64

instructions = """Ffaa78f0 ffcc28fff0 ffbb00f0 ffcc28fff0 ffbb00f0 ffcc28fff0 ffaa3cf0 ffcc28fff0 ffbb00f0 ffcc28fff0 ffbb3cf0 ffcc28fff0 ffaa3cf0 ffcc28fff0 ffbb00f0 ffcc28fff0 ffbb00f0 ffcc28fff0 ffbb00f0 ffcc28fff0 ffbb00f0 ffcc28fff0 ffffff""".replace(' ', '').upper()
raw_instructions = base64.b16decode(instructions).decode('ISO-8859-1')

print(raw_instructions)

my_file = open("demo_instructions.bin", 'w')
my_file.write(raw_instructions)