def encode_rail_fence_cipher(string, n):
	characters = list(string)
	start_characters = 0
	string_encode = list()
	step = 2*n - 1
	position_character_add = start_characters
	characters_aux = list(string)
	while n > 1:
		step = 2*n - 1											#5
		position_character_add = start_characters				#1
		for i in range(len(string)):
			if(position_character_add >= len(string)):
				break
			string_encode.append(characters[position_character_add])
			characters_aux[position_character_add] = ""
			position_character_add = position_character_add + (step - 1)
		n = n - 1
		start_characters = start_characters + 1
		print(string_encode)
	string_encode = string_encode + characters_aux
	return "".join(string_encode)

def encode(string,n,start_characters=0):
	characters = list(string)
	start_characters = 0
	string_encode = list()
	step = 2*n - 1
	position_character_add = start_characters

	for i in range(len(string)):
		if(position_character_add >= len(string)):
			break
		string_encode.append(characters[position_character_add])
		position_character_add = position_character_add + (step - 1)
	
	return "".join(string_encode)

print(encode("ello, World!", 3))