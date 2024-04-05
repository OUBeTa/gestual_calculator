# powered by : oub3t4 #

action_dict = {
	
	"0000100001" 	: "start",
	"1111111111" 	: "end",
	"10111"			: "register",
	"00111"			: "register_negative",
	"00011"			: "add",
	"00110"			: "sub",
	"10011"			: "mul",
	"10110"			: "div",
	"11111"			: "out",
	"11110"			: "parens_open",
	"10001"			: "parens_close",
	"00001"			: "erase",
	"10000"			: "decimal"

}

def to_binary(encode:list,bits:int=5):

	pattern = []
	for i in range (0,bits): pattern.append("0")

	if type(encode) == list and len(encode) != 0:

		if max(encode) <= bits:

			for i in encode: pattern[-i] = "1"

			return ("".join(pattern))

		else:

			for key,val in enumerate(pattern): patern[key] = 1
			return "".join(pattern)

	else: return "".join(pattern)

def is_real_action(binary: str): return binary in action_dict

def read_action(encode:list,bits = 5):

	binary_str = to_binary(encode,bits)

	if is_real_action(binary_str): return action_dict[binary_str]

	return binary_str
